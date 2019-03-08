# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2019/3/8
# setup.py

from setuptools import setup,find_packages
setup(
    name = "grpc_base_models",
    version = "0.0.1",
    keywords = ("pip", "pygrpc", "company", "chenhuachao"),
    description = "python版本的grpc公用模块,个人项目专用,仅供参考",
    long_description="grpc server for python",
    license="MIT Licence",
    url="https://github.com/leizhu900516",
    author="chenhuachao",
    author_email="leizhu900516@163.com",
    packages = find_packages(),
    install_requires = [
        'grpcio==1.19.0',
        'grpcio-tools==1.19.0',
        'protobuf==3.7.0',
    ]
)