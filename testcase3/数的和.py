#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/24 16:58
# @Author  : 李
# @File    : 奇数合.py


#for循环
sum1=0
for i in range(1,11,2):  #(1,11)是1-10的和：(0,11,2)是1-10的偶数和：(1,11,2)是1-10的奇数和：
    sum1+=i  #sum=sum+i
print(sum1)


#sum()  放可迭代数据
sum2=sum(range(1,11,2))#(1,11)是1-10的和：(0,11,2)是1-10的偶数和：(1,11,2)是1-10的奇数和：)
print(sum2)

#while循环
a=0
b=1
while b<11:

    a += b
    b += 2  # 控制循环次数  b=0偶数和：b=1是奇数和
print(a)

#添加if
a=0
b=0
for i in range(11):
    if i%2 == 0:
        a+=i
    else:
        b+=i
print(a)
print(b)