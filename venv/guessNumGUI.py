# !/usr/bin/python
# -*- coding: utf-8 -*-

import easygui
import random

key = random.randint(1, 100)
easygui.msgbox(key)
guess = 0
tries = 0

while guess != key and tries <= 6:
    guess = easygui.integerbox("请输入一个1到99的数:")
    if guess < key:
        easygui.msgbox("小了")
    elif guess > key:
        easygui.msgbox("大了")
    tries += 1
if guess == key:
    easygui.msgbox("猜对了")
else:
    easygui.msgbox("下次再来吧")
