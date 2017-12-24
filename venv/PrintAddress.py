# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
可以打印全世界的人名、地址、街道、城市、州或省、邮政编码和国家
'''


def printAddress(list=[]):
    print(list[0] + '\n' + list[1] + ' ' + list[2] + '\n' + list[3] + ', ' + list[4] + '\n' + list[5] + ', ' + list[6])


list = []
for i in range(7):
    list.append(raw_input())

printAddress(list)
