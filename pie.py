#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/7 15:40
# @Author  : 李
# @File    : pie.py.py

from pyecharts.charts import Pie   #饼状图包

data = [["失败",10],["跳过",50],["通过",100]]

pie = (
    Pie()
    .add("",data)
    .render("D:/华测项目/可视图形.html")
)

from pyecharts.charts import Line  #折线图


