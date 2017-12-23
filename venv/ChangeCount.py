# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
根据输入的各种分币的个数，计算总金额
'''


def changeCount(wufen, erfen, yifen):
    total = 5 * wufen + 2 * erfen + 1 * yifen
    print "五分：", wufen
    print "二分：", erfen
    print "一分：", yifen
    print "total is ￥", total, "分"


changeCount(int(raw_input("请输入五分的个数：")), int(raw_input("请输入二分的个数：")), int(raw_input("请输入一分的个数：")))
