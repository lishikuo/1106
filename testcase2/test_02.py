#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 18:03
# @Author  : 李
# @File    : test_02.py

def test02():
    assert 1==2


import pytest


# 首先， 在fixture函数上，加@pytest.fixture()

@pytest.fixture()
def my_method():
    print('This is testing fixture')


# 其次，把fixture函数的函数名作为参数，传入被测试用例

def test_use_fixtures(my_method):
    print('Please follow Testing from WL')


import pytest


@pytest.fixture()
def my_method():
    print('This is Testing fixture')
    yield
    print("用例后操作")


# 函数直接使用fixture
@pytest.mark.usefixtures('my_method')
def test_use_fixtures():
    print('Please follow Testing from WL')


class TestClass1:
    # 类方法使用fixture
    @pytest.mark.usefixtures('my_method')
    def test_class_method_usage(self):
        print('[classMethod]Please follow Testing from WL')


# 类直接使用fixture
@pytest.mark.usefixtures('my_method')
class TestClass2:
    def test_method_usage_01(self):
        pass

    def test_method_usage_02(self):
        pass
