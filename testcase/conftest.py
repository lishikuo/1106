#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 16:41
# @Author  : 李
# @File    : conftest.py

#公共调用文件

from requests import request
from pytest import fixture


#登录接口
@fixture()
def login():

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "multipart/form-data"
    }
    def _login(username,password):
        url = "http://shop-xo.hctestedu.com/index.php?s=/index/user/login.html"
        data = {"accounts": username,
                "pwd": password,
                "type": "username"}

        req = request(method="post", url=url, headers=headers, data=data)
        return req
    return _login

@fixture()
def requests():
    return requests

@fixture()
def method():
    class Method:
        post = "post"
        get = "get"
    return  Method

@fixture()
def headers():
    _headers={
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "multipart/form-data",

        }
    return _headers

@fixture()
def url():
    _url="http://shop-xo.hctestedu.com/"
    return _url







