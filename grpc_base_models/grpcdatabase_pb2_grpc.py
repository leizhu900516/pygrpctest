# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpcdatabase_pb2 as grpcdatabase__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetContent = channel.unary_unary(
        '/grpcServer.Greeter/GetContent',
        request_serializer=grpcdatabase__pb2.Request.SerializeToString,
        response_deserializer=grpcdatabase__pb2.Return.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetContent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetContent': grpc.unary_unary_rpc_method_handler(
          servicer.GetContent,
          request_deserializer=grpcdatabase__pb2.Request.FromString,
          response_serializer=grpcdatabase__pb2.Return.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcServer.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
