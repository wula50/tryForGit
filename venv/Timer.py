# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
Countdown timer: How many seconds?4
4 * * * *
3 * * *
2 * *
1 *
BLAST OFF!
'''
import time
#import sys

seconds = int(raw_input("Countdown timer: How many seconds?"))
for i in range(seconds, 0, -1):
    print i,
    for j in range(0,i):
        print "*",  #sys.stdou.wirte("*")
    time.sleep(1)
    print
print("BLAST OFF!")
