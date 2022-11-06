#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 16:54
# @Author  : 李
# @File    : 打印三角.py

#n= int(input("输入要打印的星星高度:"))
n=6
#打印左上三角

def zuoshangsanjiao(a):
    print("打印左上三角：")
    for i in range(1,1+a):
        for j in range(1,i+1):
            print("*",end="")
        print("")

    #第二种方法
    for i in range(1,a+1):
        print("*"*i)


#打印左下三角
def zuoxiasanjiao(a):
    print("打印左下三角：")
    for i in range(0,a):
        for j in range(1,a-i+1):
            print("*",end="")
        print("")

    # 第二种方法
    for i in range(0,a):
        print("*"*(a-i))

#打印右上三角
def youshangsanjiao(a):
    print("打印右上三角：")
    for i in range(0,a):
        for j in range(1,a-i):
            print(" ",end="")
        for k in range(a-i,a+1):
            print("*",end="")
        print("")

    #第二种方法
    for i in range(1,a+1):
        print(" "*(a-i)+"*"*i)


# 打印右下三角
def youxiasanjiao(a):
    print("打印右下三角：")
    for i in range(0, a):
        for j in range(a - i,a):
            print(" ", end="")
        for k in range(0, a-i ):
            print("*", end="")
        print("")

    # 第二种方法
    for i in range(0, a ):
        print(" " * i + "*" * (a-i))


#打印等腰三角
def dengyaosanjiao(a):
    print("打印等腰三角：")

    for i in range(a):
        for j in range(0, a - i):
            print(end=" ")
        for k in range(a - i, a):
            print("a", end=" ")
        print("")


    for i in range(a):
        for j in range(1, a - i):
            print(" ",end="")
        for k in range(a - i, a+i+1):
            print("*", end="")

        print("")


    #第二种方法
    for i in range(1, a+1 ):
        print(" " * (a - i) + "*" * i,end="")
        print("*"*(i-1))

#打印倒等腰三角
def daodengyaosanjiao(a):
    print("打印倒等腰三角：")
    for i in range(0,a):
        for j in range(0,i):
            print(" ",end="")
        for k in range(i,a-i+1):
            print("*",end="")
        print("")

    for i in range(a):
        for j in range(0, i):
            print(end=" ")
        for j in range(i, a):
            print("*", end=" ")
        print("")
     #?????????????????????
    for i in range(0,a):
        for j in range(0,i):
            print(" ",end="")
        for k in range(0,a-i):
            print("*",end="")
        for z in range(i+1,a):
            print("*",end="")
        print("")

    #第二种方法
    for i in range(0, a ):
        print(" " * i + "*" * (a-i),end="")
        print("*"*(a-i-1))


#打印菱形
def lingxing(a):
    print("打印菱形：")
    for i in range(0,a-1):
        print(" "*(a-i-1)+"*"*(i+1),end="")
        print("*"*i)
    for i in range(0, a ):
        print(" " * i + "*" * (a-i),end="")
        print("*"*(a-i-1))
    print("------------------")
    for i in range(0,a-1):
        for j in range(0,a-i-1):
            print(" ",end="")
        for k in range(0,i*2+1):
            print("*",end="")
        print("")
    for i in range(0, a):
        for j in range(0,i):
            print(" ",end="")
        for j in range(0,(a*2-1)-i*2):
            print("*",end="")
        print("")


# 打印平行四边形
def pingxingsibianxing(a):
    print("打印平行四边形：")
    for i in range(0, a):
        for j in range(a - i,a):
            print(" ", end="")
        for k in range(0, a ):
            print("*", end="")
        print("")

    # 第二种方法
    for i in range(0, a ):
        print(" " * i + "*" * a)


if __name__ == "__main__" :
    #zuoshangsanjiao(n)
    #zuoxiasanjiao(n)
    #youshangsanjiao(n)
    #youxiasanjiao(n)
    #dengyaosanjiao(n)
    #daodengyaosanjiao(n)
    lingxing(10)
    #pingxingsibianxing(n)

