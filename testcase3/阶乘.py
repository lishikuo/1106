#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/24 16:49
# @Author  : 李
# @File    : 阶乘.py


#输入一个数然后计算该数的阶乘
a=int(input())
def jiecheng(a):

    b=1
    for i in range(1,a+1):
        b*=i
    print(b)

#输入一个数然后计算该数的阶乘之和
def jiechenghe(a):
    e=0
    for i in range(1,a+1):
        d=1
        for j in range(1,i+1):
            d *= j
        e += d
    print(e)

#递归实现阶乘
def digui(n):
    if n == 1:
        return  1
    else:
        return n * digui(n-1)

def shuhe(n):
    if n == 1:
        return  1
    else:
        return n + shuhe(n-1)

if __name__=="__main__":
    jiecheng(a)
    jiechenghe(a)
    print(digui(a))
    print(shuhe(a))
