# !/usr/bin/python
# -*- coding: utf-8 -*-

import easygui

# 把温度从华氏度转换成摄氏度。转换公式C=5/9*(F-32)
f = float(easygui.enterbox("请输入需要转化的华氏度："))
c = float(5) / 9 * (f - 32)
easygui.msgbox(str(f) + "华氏度对应的摄氏度是：" + str(c))
