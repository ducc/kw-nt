package main

import (
	"context"
	"flag"
	"github.com/ducc/kwɒnt/brokers"
	"github.com/ducc/kwɒnt/brokers/xtb"
	"github.com/ducc/kwɒnt/protos"
	"github.com/sirupsen/logrus"
	"github.com/streadway/amqp"
	"google.golang.org/grpc"
	"net"
	"os"
)

var (
	level            string
	amqpAddress      string
	tickTopic        string
	tradeTopic       string
	tradeStatusTopic string
	serverAddress    string
	routerAddress    string
)

func init() {
	flag.StringVar(&level, "level", "debug", "logrus logging level")
	flag.StringVar(&amqpAddress, "amqp-address", "", "amqp server connection address")
	flag.StringVar(&tickTopic, "tick-topic", "ticks", "nats topic")
	flag.StringVar(&tradeTopic, "trade-topic", "xtb-trades", "nats topic")
	flag.StringVar(&tradeStatusTopic, "trade-status-topic", "xtb-trade-status", "nats topic")
	flag.StringVar(&serverAddress, "server-address", ":8080", "grpc server address")
	flag.StringVar(&routerAddress, "router-address", "", "router service address")
}

func main() {
	flag.Parse()
	if ll, err := logrus.ParseLevel(level); err != nil {
		logrus.WithError(err).Fatal("parsing log level")
	} else {
		logrus.SetLevel(ll)
	}

	logrus.WithField("POD_IP", os.Getenv("POD_IP")).Debug("starting xtb broker")

	amqpConn, err := amqp.Dial(amqpAddress)
	if err != nil {
		logrus.WithError(err).Fatal("connecting to amqp server")
	}
	defer func() {
		if err := amqpConn.Close(); err != nil {
			logrus.WithError(err).Error("closing amqp conn")
		}
	}()

	tickChan, err := amqpConn.Channel()
	if err != nil {
		logrus.WithError(err).Fatal("creating amqp channel")
	}
	defer func() {
		if err := tickChan.Close(); err != nil {
			logrus.WithError(err).Error("closing amqp chan")
		}
	}()

	tradeChan, err := amqpConn.Channel()
	if err != nil {
		logrus.WithError(err).Fatal("creating amqp channel")
	}
	defer func() {
		if err := tradeChan.Close(); err != nil {
			logrus.WithError(err).Error("closing amqp chan")
		}
	}()

	tradeStatusChan, err := amqpConn.Channel()
	if err != nil {
		logrus.WithError(err).Fatal("creating amqp channel")
	}
	defer func() {
		if err := tradeStatusChan.Close(); err != nil {
			logrus.WithError(err).Error("closing amqp chan")
		}
	}()

	tickQueue, err := tickChan.QueueDeclare(
		tickTopic,
		true,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		logrus.WithError(err).Fatal("declaring amqp queue")
	}

	tradeQueue, err := tradeChan.QueueDeclare(
		tradeTopic,
		true,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		logrus.WithError(err).Fatal("declaring amqp queue")
	}

	tradeStatusQueue, err := tradeStatusChan.QueueDeclare(
		tradeStatusTopic,
		true,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		logrus.WithError(err).Fatal("declaring amqp queue")
	}

	ctx := context.Background()

	routerConn, err := brokers.NewClient(ctx, routerAddress)
	if err != nil {
		logrus.WithError(err).Fatal("connecting to router")
	}

	server := xtb.New(tickChan, tradeChan, tradeStatusChan, tickQueue, tradeQueue, tradeStatusQueue, routerConn)
	grpcServer := grpc.NewServer()

	protos.RegisterBrokerServiceServer(grpcServer, server)

	listener, err := net.Listen("tcp", serverAddress)
	if err != nil {
		logrus.WithError(err).Fatal("tcp listen")
	}

	if err := grpcServer.Serve(listener); err != nil {
		logrus.WithError(err).Fatal("serving grpc")
	}
}
