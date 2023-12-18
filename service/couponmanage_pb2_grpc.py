# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import couponmanage_pb2 as couponmanage__pb2


class CouponManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterCafe = channel.unary_unary(
                '/couponmanage.CouponManager/RegisterCafe',
                request_serializer=couponmanage__pb2.CafeDetail.SerializeToString,
                response_deserializer=couponmanage__pb2.CUDReply.FromString,
                )
        self.ReceiveAllCafes = channel.unary_unary(
                '/couponmanage.CouponManager/ReceiveAllCafes',
                request_serializer=couponmanage__pb2.EmptyRequest.SerializeToString,
                response_deserializer=couponmanage__pb2.AllCafeReply.FromString,
                )
        self.ReceiveCafeDetail = channel.unary_unary(
                '/couponmanage.CouponManager/ReceiveCafeDetail',
                request_serializer=couponmanage__pb2.CafeName.SerializeToString,
                response_deserializer=couponmanage__pb2.CafeDetail.FromString,
                )
        self.UpdateCafe = channel.unary_unary(
                '/couponmanage.CouponManager/UpdateCafe',
                request_serializer=couponmanage__pb2.CafeUpdateRequest.SerializeToString,
                response_deserializer=couponmanage__pb2.CUDReply.FromString,
                )
        self.DeleteCafe = channel.unary_unary(
                '/couponmanage.CouponManager/DeleteCafe',
                request_serializer=couponmanage__pb2.CafeName.SerializeToString,
                response_deserializer=couponmanage__pb2.CUDReply.FromString,
                )
        self.ReceiveAllCoupons = channel.unary_unary(
                '/couponmanage.CouponManager/ReceiveAllCoupons',
                request_serializer=couponmanage__pb2.UserId.SerializeToString,
                response_deserializer=couponmanage__pb2.AllCouponReply.FromString,
                )


class CouponManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterCafe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveAllCafes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveCafeDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCafe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCafe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveAllCoupons(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CouponManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterCafe': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterCafe,
                    request_deserializer=couponmanage__pb2.CafeDetail.FromString,
                    response_serializer=couponmanage__pb2.CUDReply.SerializeToString,
            ),
            'ReceiveAllCafes': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveAllCafes,
                    request_deserializer=couponmanage__pb2.EmptyRequest.FromString,
                    response_serializer=couponmanage__pb2.AllCafeReply.SerializeToString,
            ),
            'ReceiveCafeDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveCafeDetail,
                    request_deserializer=couponmanage__pb2.CafeName.FromString,
                    response_serializer=couponmanage__pb2.CafeDetail.SerializeToString,
            ),
            'UpdateCafe': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCafe,
                    request_deserializer=couponmanage__pb2.CafeUpdateRequest.FromString,
                    response_serializer=couponmanage__pb2.CUDReply.SerializeToString,
            ),
            'DeleteCafe': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCafe,
                    request_deserializer=couponmanage__pb2.CafeName.FromString,
                    response_serializer=couponmanage__pb2.CUDReply.SerializeToString,
            ),
            'ReceiveAllCoupons': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveAllCoupons,
                    request_deserializer=couponmanage__pb2.UserId.FromString,
                    response_serializer=couponmanage__pb2.AllCouponReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'couponmanage.CouponManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CouponManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterCafe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/RegisterCafe',
            couponmanage__pb2.CafeDetail.SerializeToString,
            couponmanage__pb2.CUDReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveAllCafes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/ReceiveAllCafes',
            couponmanage__pb2.EmptyRequest.SerializeToString,
            couponmanage__pb2.AllCafeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveCafeDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/ReceiveCafeDetail',
            couponmanage__pb2.CafeName.SerializeToString,
            couponmanage__pb2.CafeDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCafe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/UpdateCafe',
            couponmanage__pb2.CafeUpdateRequest.SerializeToString,
            couponmanage__pb2.CUDReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCafe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/DeleteCafe',
            couponmanage__pb2.CafeName.SerializeToString,
            couponmanage__pb2.CUDReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveAllCoupons(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/couponmanage.CouponManager/ReceiveAllCoupons',
            couponmanage__pb2.UserId.SerializeToString,
            couponmanage__pb2.AllCouponReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
