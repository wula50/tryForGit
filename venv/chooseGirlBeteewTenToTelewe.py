# !/usr/bin/python
# -*- coding: utf-8 -*-

gender=raw_input("请输入你的性别，男生请输入‘M’，女生请输入‘F’：")
if gender=='M':
    print("对不起，我们是女子足球队。")
else:
    age=int(raw_input("请输入你的年龄："))
    if 10<=age<=12:
        print ("欢迎你，你可以加入足球队！")
    else:
        print ("对不起，你的年龄不符合要求。")