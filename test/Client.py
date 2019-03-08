# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2019/3/7
# Client.py
import sys
import grpc
sys.path.append('grpc_base_models')
# import grpcdatabase_pb2_grpc
# import grpcdatabase_pb2
from grpc_base_models import grpcdatabase_pb2_grpc
from grpc_base_models import grpcdatabase_pb2

# _HOST = '192.168.3.191'
_HOST = '127.0.0.1'
_PORT = '19999'



def RpcClient(funcname,content):
    '''
    rpc客户端程序
    :param funcname: 可用funcname为下面两个
        >>> GetContent  获取摘要， 参数：content='文本'
        *** 上面两个函数均返回message属性和code(1:failed 0:success)属性
        >>> 返回值：response.message   response.code
    :return:
    '''
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = grpcdatabase_pb2_grpc.GreeterStub(channel=channel)
        if hasattr(client,funcname):
            response = getattr(client,funcname)(grpcdatabase_pb2.Request(content=content))
        else:
            raise Exception(u"函数名错误")
    print("message=" , response.message)
    print( "code=",response.code)
if __name__ == '__main__':
    text = u'''
    测试的文本
    '''
    RpcClient('GetContent',text)
