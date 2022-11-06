#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 17:50
# @Author  : 李
# @File    : test_01.py

from requests import request
from pytest import mark  #标签


class Test_user_reg():
    @mark.team("团队1")
    def testuserreg(self):
        url="http://shop-xo.hctestedu.com/index.php?s=/index/user/reg.html"
        headers={
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Type": "multipart/form-data"
                    }
        data={"accounts": "lsk3",
            "pwd": "lsk333",
            "type": "username"}

        req=request(method="post",url=url,headers=headers,data=data)
        print(req.json())
        assert req.json()["msg"] == "账号已存在"
