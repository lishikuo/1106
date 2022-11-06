#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:39
# @Author  : 李
# @File    : 乘法表.py

def chengfabiao(n):
    #for循环
    for i in range(1,n+1):
        for j in range(1,i+1):
            #print("%d*%d=%d"%(j,i,j*i),end="\t")  #占位符"%d"%(int) ; "%s"%(str) ; "%f"%(float)   "\t"制表符
            print(f"{j}*{i}={j*i}\t",end="")
        print("")

    print("----------------------------")
    #while循环
    i = 1
    while i <= n :
        j = 1
        while j <= i:
            print(f"{j}*{i}={j*i}\t",end="")
            j += 1
        print("")
        i+=1

    print("---------------------------------")
    #while + for 循环
    i = 1
    while i <= n:
        for j in range(1,i+1):
            print(f"{j}*{i}={j * i}\t", end="")
        print("")
        i += 1

    print("---------------------------------")
    # for + while 循环
    for i in range(1,n+1):
        j = 1
        while j <= i:
            print(f"{j}*{i}={j * i}\t", end="")
            j += 1
        print("")


    print("-----------------------------------")
    #倒乘法表
    i = 9
    while i > 0:
        j = 1
        while j <= i:
            print(f"{j}*{i}={j * i}\t", end="")
            j += 1
        print("")
        i -= 1

if __name__ == "__main__":
    chengfabiao(9)