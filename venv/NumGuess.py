#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

key=random.randint(1,100)
guess=0
tries=0

print("来玩个游戏，试试运气")
print("从1到99选一个数字，你只有6次机会")
while guess!=key and tries<=6:
    guess=input("猜一猜")
    if guess<key:
        print("小了")
    elif guess>key:
        print("大了")
    tries+=1
if guess==key:
    print("猜对了，你赢了！")
else:
    print("没机会了，下次再来，正确答案是"+key)