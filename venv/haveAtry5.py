#!/usr/bin/python
# -*- coding: utf-8 -*-

#编写程序询问长方形房间的尺寸（单位是米），然后计算覆盖整个房间总共需要多少地毯，并显示出来
length=float(raw_input("请输入房间的长度："))
width=float(raw_input("请输入房间的宽度："))
area=length*width
print("总共需要"+str(area)+"平方米地毯。")

#询问每平方尺地毯的价格，并显示一下内容
#总共需要多少地毯，单位是平方米
#总共需要多少地毯，单位是平方尺
#地毯的总价格

print("总共需要"+str(area*9)+"平方尺地毯。")
priceOfCarpet=float(raw_input("请问每平方尺地毯的价格："))
print("地毯的总价是："+str(priceOfCarpet*area*9))