# !/usr/bin/python
# -*- coding: utf-8 -*-

print("Which multiplication table would you like?")
number = int(raw_input())
print("Here's your table:")
for i in range(1, 11):
    print(str(number) + " * " + str(i) + " = " + str(number * i))
