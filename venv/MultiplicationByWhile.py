# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
乘法表 while实现
支持用户输入最大乘到几
'''
print("Which multiplication table would you like?")
number = int(raw_input())
i = 1
userInput = int(raw_input("Which number do you want to mutiply?"))
print("Here's your table:")
while i <= userInput:
    print(str(number) + " * " + str(i) + " = " + str(number * i))
    i += 1
