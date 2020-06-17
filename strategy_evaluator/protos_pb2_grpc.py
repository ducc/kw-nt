# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protos_pb2 as protos__pb2


class DataServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStrategy = channel.unary_unary(
                '/protos.DataService/CreateStrategy',
                request_serializer=protos__pb2.CreateStrategyRequest.SerializeToString,
                response_deserializer=protos__pb2.CreateStrategyResponse.FromString,
                )
        self.UpdateStrategy = channel.unary_unary(
                '/protos.DataService/UpdateStrategy',
                request_serializer=protos__pb2.UpdateStrategyRequest.SerializeToString,
                response_deserializer=protos__pb2.UpdateStrategyResponse.FromString,
                )
        self.DeleteStrategy = channel.unary_unary(
                '/protos.DataService/DeleteStrategy',
                request_serializer=protos__pb2.DeleteStrategyRequest.SerializeToString,
                response_deserializer=protos__pb2.DeleteStrategyResponse.FromString,
                )
        self.ListStrategies = channel.unary_unary(
                '/protos.DataService/ListStrategies',
                request_serializer=protos__pb2.ListStrategiesRequest.SerializeToString,
                response_deserializer=protos__pb2.ListStrategiesResponse.FromString,
                )
        self.GetPriceHistory = channel.unary_unary(
                '/protos.DataService/GetPriceHistory',
                request_serializer=protos__pb2.GetPriceHistoryRequest.SerializeToString,
                response_deserializer=protos__pb2.GetPriceHistoryResponse.FromString,
                )
        self.AddTick = channel.unary_unary(
                '/protos.DataService/AddTick',
                request_serializer=protos__pb2.AddTickRequest.SerializeToString,
                response_deserializer=protos__pb2.AddTickResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/protos.DataService/CreateUser',
                request_serializer=protos__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=protos__pb2.CreateUserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/protos.DataService/UpdateUser',
                request_serializer=protos__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=protos__pb2.UpdateUserResponse.FromString,
                )
        self.ListUsers = channel.unary_unary(
                '/protos.DataService/ListUsers',
                request_serializer=protos__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=protos__pb2.ListUsersResponse.FromString,
                )
        self.AddOrder = channel.unary_unary(
                '/protos.DataService/AddOrder',
                request_serializer=protos__pb2.AddOrderRequest.SerializeToString,
                response_deserializer=protos__pb2.AddOrderResponse.FromString,
                )
        self.AddXTBTrade = channel.unary_unary(
                '/protos.DataService/AddXTBTrade',
                request_serializer=protos__pb2.AddXTBTradeRequest.SerializeToString,
                response_deserializer=protos__pb2.AddXTBTradeResponse.FromString,
                )
        self.AddXTBTradeStatus = channel.unary_unary(
                '/protos.DataService/AddXTBTradeStatus',
                request_serializer=protos__pb2.AddXTBTradeStatusRequest.SerializeToString,
                response_deserializer=protos__pb2.AddXTBTradeStatusResponse.FromString,
                )


class DataServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def CreateStrategy(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStrategy(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStrategy(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListStrategies(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPriceHistory(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTick(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOrder(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddXTBTrade(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddXTBTradeStatus(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStrategy,
                    request_deserializer=protos__pb2.CreateStrategyRequest.FromString,
                    response_serializer=protos__pb2.CreateStrategyResponse.SerializeToString,
            ),
            'UpdateStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStrategy,
                    request_deserializer=protos__pb2.UpdateStrategyRequest.FromString,
                    response_serializer=protos__pb2.UpdateStrategyResponse.SerializeToString,
            ),
            'DeleteStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStrategy,
                    request_deserializer=protos__pb2.DeleteStrategyRequest.FromString,
                    response_serializer=protos__pb2.DeleteStrategyResponse.SerializeToString,
            ),
            'ListStrategies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListStrategies,
                    request_deserializer=protos__pb2.ListStrategiesRequest.FromString,
                    response_serializer=protos__pb2.ListStrategiesResponse.SerializeToString,
            ),
            'GetPriceHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPriceHistory,
                    request_deserializer=protos__pb2.GetPriceHistoryRequest.FromString,
                    response_serializer=protos__pb2.GetPriceHistoryResponse.SerializeToString,
            ),
            'AddTick': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTick,
                    request_deserializer=protos__pb2.AddTickRequest.FromString,
                    response_serializer=protos__pb2.AddTickResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=protos__pb2.CreateUserRequest.FromString,
                    response_serializer=protos__pb2.CreateUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=protos__pb2.UpdateUserRequest.FromString,
                    response_serializer=protos__pb2.UpdateUserResponse.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=protos__pb2.ListUsersRequest.FromString,
                    response_serializer=protos__pb2.ListUsersResponse.SerializeToString,
            ),
            'AddOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrder,
                    request_deserializer=protos__pb2.AddOrderRequest.FromString,
                    response_serializer=protos__pb2.AddOrderResponse.SerializeToString,
            ),
            'AddXTBTrade': grpc.unary_unary_rpc_method_handler(
                    servicer.AddXTBTrade,
                    request_deserializer=protos__pb2.AddXTBTradeRequest.FromString,
                    response_serializer=protos__pb2.AddXTBTradeResponse.SerializeToString,
            ),
            'AddXTBTradeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.AddXTBTradeStatus,
                    request_deserializer=protos__pb2.AddXTBTradeStatusRequest.FromString,
                    response_serializer=protos__pb2.AddXTBTradeStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def CreateStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/CreateStrategy',
            protos__pb2.CreateStrategyRequest.SerializeToString,
            protos__pb2.CreateStrategyResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/UpdateStrategy',
            protos__pb2.UpdateStrategyRequest.SerializeToString,
            protos__pb2.UpdateStrategyResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/DeleteStrategy',
            protos__pb2.DeleteStrategyRequest.SerializeToString,
            protos__pb2.DeleteStrategyResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListStrategies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/ListStrategies',
            protos__pb2.ListStrategiesRequest.SerializeToString,
            protos__pb2.ListStrategiesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPriceHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/GetPriceHistory',
            protos__pb2.GetPriceHistoryRequest.SerializeToString,
            protos__pb2.GetPriceHistoryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/AddTick',
            protos__pb2.AddTickRequest.SerializeToString,
            protos__pb2.AddTickResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/CreateUser',
            protos__pb2.CreateUserRequest.SerializeToString,
            protos__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/UpdateUser',
            protos__pb2.UpdateUserRequest.SerializeToString,
            protos__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/ListUsers',
            protos__pb2.ListUsersRequest.SerializeToString,
            protos__pb2.ListUsersResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/AddOrder',
            protos__pb2.AddOrderRequest.SerializeToString,
            protos__pb2.AddOrderResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddXTBTrade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/AddXTBTrade',
            protos__pb2.AddXTBTradeRequest.SerializeToString,
            protos__pb2.AddXTBTradeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddXTBTradeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.DataService/AddXTBTradeStatus',
            protos__pb2.AddXTBTradeStatusRequest.SerializeToString,
            protos__pb2.AddXTBTradeStatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class StrategyEvaluatorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Evaluate = channel.unary_unary(
                '/protos.StrategyEvaluator/Evaluate',
                request_serializer=protos__pb2.EvaulateStrategyRequest.SerializeToString,
                response_deserializer=protos__pb2.EvaluateStrategyResponse.FromString,
                )


class StrategyEvaluatorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Evaluate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StrategyEvaluatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Evaluate': grpc.unary_unary_rpc_method_handler(
                    servicer.Evaluate,
                    request_deserializer=protos__pb2.EvaulateStrategyRequest.FromString,
                    response_serializer=protos__pb2.EvaluateStrategyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.StrategyEvaluator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StrategyEvaluator(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Evaluate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.StrategyEvaluator/Evaluate',
            protos__pb2.EvaulateStrategyRequest.SerializeToString,
            protos__pb2.EvaluateStrategyResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class BrokerServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrentSessions = channel.unary_unary(
                '/protos.BrokerService/GetCurrentSessions',
                request_serializer=protos__pb2.GetCurrentSessionsRequest.SerializeToString,
                response_deserializer=protos__pb2.GetCurrentSessionsResponse.FromString,
                )
        self.OpenSession = channel.unary_unary(
                '/protos.BrokerService/OpenSession',
                request_serializer=protos__pb2.OpenSessionRequest.SerializeToString,
                response_deserializer=protos__pb2.OpenSessionResponse.FromString,
                )
        self.OpenPosition = channel.unary_unary(
                '/protos.BrokerService/OpenPosition',
                request_serializer=protos__pb2.OpenPositionRequest.SerializeToString,
                response_deserializer=protos__pb2.OpenPositionResponse.FromString,
                )
        self.ClosePosition = channel.unary_unary(
                '/protos.BrokerService/ClosePosition',
                request_serializer=protos__pb2.ClosePositionRequest.SerializeToString,
                response_deserializer=protos__pb2.ClosePositionResponse.FromString,
                )
        self.GetBrokerPriceHistory = channel.unary_unary(
                '/protos.BrokerService/GetBrokerPriceHistory',
                request_serializer=protos__pb2.GetBrokerPriceHistoryRequest.SerializeToString,
                response_deserializer=protos__pb2.GetBrokerPriceHistoryResponse.FromString,
                )
        self.SubscribeToPriceChanges = channel.unary_unary(
                '/protos.BrokerService/SubscribeToPriceChanges',
                request_serializer=protos__pb2.SubscribeToPriceChangesRequest.SerializeToString,
                response_deserializer=protos__pb2.SubscribeToPriceChangesResponse.FromString,
                )
        self.RegisterBroker = channel.unary_unary(
                '/protos.BrokerService/RegisterBroker',
                request_serializer=protos__pb2.RegisterBrokerRequest.SerializeToString,
                response_deserializer=protos__pb2.RegisterBrokerResponse.FromString,
                )


class BrokerServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetCurrentSessions(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenPosition(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosePosition(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrokerPriceHistory(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToPriceChanges(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterBroker(self, request, context):
        """used by the broker services to notify the router of their existence - maybe a service mesh is better
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BrokerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCurrentSessions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentSessions,
                    request_deserializer=protos__pb2.GetCurrentSessionsRequest.FromString,
                    response_serializer=protos__pb2.GetCurrentSessionsResponse.SerializeToString,
            ),
            'OpenSession': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenSession,
                    request_deserializer=protos__pb2.OpenSessionRequest.FromString,
                    response_serializer=protos__pb2.OpenSessionResponse.SerializeToString,
            ),
            'OpenPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenPosition,
                    request_deserializer=protos__pb2.OpenPositionRequest.FromString,
                    response_serializer=protos__pb2.OpenPositionResponse.SerializeToString,
            ),
            'ClosePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.ClosePosition,
                    request_deserializer=protos__pb2.ClosePositionRequest.FromString,
                    response_serializer=protos__pb2.ClosePositionResponse.SerializeToString,
            ),
            'GetBrokerPriceHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBrokerPriceHistory,
                    request_deserializer=protos__pb2.GetBrokerPriceHistoryRequest.FromString,
                    response_serializer=protos__pb2.GetBrokerPriceHistoryResponse.SerializeToString,
            ),
            'SubscribeToPriceChanges': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeToPriceChanges,
                    request_deserializer=protos__pb2.SubscribeToPriceChangesRequest.FromString,
                    response_serializer=protos__pb2.SubscribeToPriceChangesResponse.SerializeToString,
            ),
            'RegisterBroker': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterBroker,
                    request_deserializer=protos__pb2.RegisterBrokerRequest.FromString,
                    response_serializer=protos__pb2.RegisterBrokerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.BrokerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BrokerService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetCurrentSessions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/GetCurrentSessions',
            protos__pb2.GetCurrentSessionsRequest.SerializeToString,
            protos__pb2.GetCurrentSessionsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/OpenSession',
            protos__pb2.OpenSessionRequest.SerializeToString,
            protos__pb2.OpenSessionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/OpenPosition',
            protos__pb2.OpenPositionRequest.SerializeToString,
            protos__pb2.OpenPositionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/ClosePosition',
            protos__pb2.ClosePositionRequest.SerializeToString,
            protos__pb2.ClosePositionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBrokerPriceHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/GetBrokerPriceHistory',
            protos__pb2.GetBrokerPriceHistoryRequest.SerializeToString,
            protos__pb2.GetBrokerPriceHistoryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeToPriceChanges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/SubscribeToPriceChanges',
            protos__pb2.SubscribeToPriceChangesRequest.SerializeToString,
            protos__pb2.SubscribeToPriceChangesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterBroker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.BrokerService/RegisterBroker',
            protos__pb2.RegisterBrokerRequest.SerializeToString,
            protos__pb2.RegisterBrokerResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenPosition = channel.unary_unary(
                '/protos.OrderService/OpenPosition',
                request_serializer=protos__pb2.OpenPositionRequest.SerializeToString,
                response_deserializer=protos__pb2.OpenPositionResponse.FromString,
                )
        self.ClosePosition = channel.unary_unary(
                '/protos.OrderService/ClosePosition',
                request_serializer=protos__pb2.ClosePositionRequest.SerializeToString,
                response_deserializer=protos__pb2.ClosePositionResponse.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def OpenPosition(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosePosition(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OpenPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenPosition,
                    request_deserializer=protos__pb2.OpenPositionRequest.FromString,
                    response_serializer=protos__pb2.OpenPositionResponse.SerializeToString,
            ),
            'ClosePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.ClosePosition,
                    request_deserializer=protos__pb2.ClosePositionRequest.FromString,
                    response_serializer=protos__pb2.ClosePositionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def OpenPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.OrderService/OpenPosition',
            protos__pb2.OpenPositionRequest.SerializeToString,
            protos__pb2.OpenPositionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.OrderService/ClosePosition',
            protos__pb2.ClosePositionRequest.SerializeToString,
            protos__pb2.ClosePositionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
