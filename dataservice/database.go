package dataservice

import (
	"context"
	"database/sql"
	"github.com/ducc/kwɒnt/protos"
	"github.com/golang/protobuf/ptypes"
	_ "github.com/lib/pq"
	"time"
)

type database struct {
	db *sql.DB
}

func newDatabase(ctx context.Context, connectionString string) (*database, error) {
	db, err := sql.Open("postgres", connectionString)
	if err != nil {
		return nil, err
	}

	if err := db.Ping(); err != nil {
		return nil, err
	}

	return &database{
		db: db,
	}, nil
}

func (d *database) GetPartialCandlesticks(ctx context.Context, symbolName, symbolBroker string, start, end time.Time) ([]*protos.Candlestick, error) {
	const statement = `SELECT timestamp, high, low, current FROM candlesticks WHERE timestamp >= $1 AND timestamp < $2 ORDER BY timestamp ASC`

	iter, err := d.db.QueryContext(ctx, statement, start.Format(time.RFC3339), start.Format(time.RFC3339))
	if err != nil {
		return nil, err
	}
	defer iter.Close()

	output := make([]*protos.Candlestick, 0)

	for iter.Next() {
		var timestamp time.Time
		var high, low, current int64

		if err := iter.Scan(&timestamp, &high, &low, &current); err != nil {
			return nil, err
		}

		ts, err := ptypes.TimestampProto(timestamp)
		if err != nil {
			return nil, err
		}

		output = append(output, &protos.Candlestick{
			Timestamp: ts,
			High:      high,
			Low:       low,
			Current:   current,
		})
	}

	return output, nil
}

func (d *database) InsertCandlestick(ctx context.Context, symbolName, symbolBroker string, timestamp time.Time, open, close, high, low, current, spread, buyVolume, sellVolume int64) error {
	const statement = `INSERT INTO candlesticks (symbol_name, symbol_broker, timestamp, open, close, high, low, current, spread, buy_volume, sell_volume) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);`

	if _, err := d.db.ExecContext(ctx, statement, symbolName, symbolBroker, timestamp, open, close, high, low, current, spread, buyVolume, sellVolume); err != nil {
		return err
	}

	return nil
}
