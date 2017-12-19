#!/usr/bin/python
# -*- coding: utf-8 -*-

#创建一个变量，赋值并显示
var=5
print(var)

#改变这个变量，用新值替换原来的值，再增加一个量，再显示
var=6
print(var)
var+=2
print(var)

#创建另一个变量，赋给它一个字符串，再显示
str="lunch time"
print(str)

#用变量的方式计算一周多少天
daysPerWeek=7
hourPerDay=24
minutesPerHour=60
totalMinutes=daysPerWeek*hourPerDay*minutesPerHour
print(totalMinutes)

#改变hourPerDay的量
hourPerDay=26
totalMinutes=daysPerWeek*hourPerDay*minutesPerHour
print(totalMinutes)