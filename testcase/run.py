#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 17:52
# @Author  : 李
# @File    : main.py
#说明：用于执行用例的总文件

import pytest


#pytest.main()  #运行父级文件下所有测试用例
pytest.main(["D:/华测项目/testcase","--html=D:/华测项目/testcase/report/report.html","--self-contained-html"])    #运行指定父级文件下的所有测试用例,报告写绝对路径
#pytest.main(["-m","li"])  #运行父级文件下的所有"li"标签的测试用例