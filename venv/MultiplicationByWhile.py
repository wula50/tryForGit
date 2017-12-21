# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
乘法表 while实现
'''
print("Which multiplication table would you like?")
number = int(raw_input())
print("Here's your table:")
i=1
while i<11:
    print(str(number) + " * " + str(i) + " = " + str(number * i))
    i+=1