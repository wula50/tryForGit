#!/usr/bin/python
# -*- coding: utf-8 -*-

#3个人吃饭，分摊饭费，公共35.27美元，还想留15美分小费，每人该如何付钱？
total=35.27
tip=0.15
count=3
average=(total+tip)/count
print("每个人应付："+str(average))

#计算一个12.5m*16.7m的矩形房间的面积和周长
length=16.7
width=12.5
perimeter=2*(length+width)
area=length*width
print("长方形的周长是："+str(perimeter)+"长方形的面积是："+str(area))

#把温度从华氏度转换成摄氏度。转换公式C=5/9*(F-32)
f=input("请输入华氏度：")
c=float(5)/9*(f-32)
print(str(f)+"华氏度对应的摄氏度是："+str(c))

#计算坐车去某个地方需要花多长的时间，“旅行时间等于距离除以速度”
speed=80
distance=200
time=distance*1.0/speed
print("以"+str(speed)+"km/h的速度行驶"+str(distance)+"km需要花"+str(time)+"小时")























