#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 20:39
# @Author  : 李
# @File    : 冒泡.py

list1 = [3,2,5,7,1,9,0,6]
list2 = [64, 34, 25, 12, 22, 11, 90]

print(type(len(list1)))
#冒泡排序
def maopao(a):
    for i in range(len(a)):  #控制循环次数，遍历所有元素
        for j in range(len(a)-i-1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]


    print(a)



if __name__ == "__main__":
    maopao(list1)
    maopao(list2)