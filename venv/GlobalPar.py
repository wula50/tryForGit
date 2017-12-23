# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
在函数中使用全局变量，改变他的值，并输出

在函数调用时是使用最近一次改变的值
或者说是在调用方法之前给定的值
如下方my_price=200若注释掉，程序会报错

参数传进的是值，不是名称
'''


def calculateTax(price, tax_rate):
    global my_price
    my_price = 10000
    total = price + (price * tax_rate)

    print "my_price (inside function)=", my_price
    return total


my_price = 200

totalPrice = calculateTax(my_price, 0.06)
print "print=", my_price, "Total price=", totalPrice
print "my_price (outside function)=", my_price
