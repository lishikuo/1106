#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 16:48
# @Author  : 李
# @File    : 应用.py

#消费满100后享8折，满150后享5折，累计200元后恢复原价，输入天数和票价，得出需要多少钱
def chepiao(d,p):
    a = 0
    for i in range(d):
        if a < 100:
            a += p
            if a > 100:
                a = (a-100)*0.8 + 100
                continue
        elif 100 <= a < 150:
            a += (p*0.8)
            if a > 150:
                a = (a-150)*0.5 + 150
                continue
        elif 150 <= a < 200:
            a += (p*0.5)
            if a > 200:
                a = (a-200)*2 +200
                continue
        elif a >= 200 :
            a += p
    return a


#兔子数列:一个兔子从第四年开始每年可以生一只兔子，20年后一共有多少只兔子？
def fib(n):
    if n <= 3:
        return 1
    else:
        return fib(n-1)+fib(n-4)







if __name__ == "__main__":
    print(chepiao(26,14))
    print(fib(30))

