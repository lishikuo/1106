#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 16:43
# @Author  : 李
# @File    : test_user_update.py

from requests import request
# from pytest import mark
import pytest




class Test_user_update():

    data =  [('姓名7', "编辑成功"),
             (0,"昵称 2~16 个字符之间"),
             ('姓名6', "编辑失败或数据未改变")]

    @pytest.mark.parametrize("name,ass",data)
    # @pytest.mark.parametrize("name",["kk",9])
    @pytest.mark.team("团就2")


    def testuserupdate(self,login,method,headers,url,name,ass):
        login=login("lsk2","lsk222")  #登录操作
        url =url+ "index.php?s=/index/personal/save.html"
        # headers={
        #         "X-Requested-With": "XMLHttpRequest",
        #         "Content-Type": "multipart/form-data",
        #
        # }
        data={
            "nickname": name,
            "gender":0,
            "birthday": "2022-10-02"}
        req=request(method=method.post,url=url,headers=headers,data=data,cookies=login.cookies)

        assert  req.json()["msg"] == ass
        print(req.json())

