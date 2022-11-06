#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/6 14:57
# @Author  : 李
# @File    : conftest.py.py

from pytest import fixture
from requests import request

@fixture()
def login():
    url = "http://shop-xo.hctestedu.com/index.php?s=/index/user/login.html"
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "multipart/form-data"
    }

    def _login(name="lsk1",paw="lsk111"):
        data = {"accounts":name,
                "pwd": paw,
                "type": "username"}

        req = request(method="post", url=url, headers=headers, data=data)
        print(req.json())
        return req
    return _login

if __name__ == "__main__":
    pass