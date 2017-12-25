# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
生成1-20之间的5个随机整数
每3秒打印一个随机小数
'''
import random
import time

for i in range(5):
    print random.randint(1, 21)

for i in range(10):
    print random.random()
    time.sleep(3)
