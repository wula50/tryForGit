#!/usr/bin/python
# -*- coding: utf-8 -*-

# 仅使用int()，实现四舍五入
f = input("请输入一个浮点数：")
af = int(f)
if f - af < 0.5:
    print(af)
else:
    print(af + 1)

# 使用float从字符串创建一个数，如‘12.34’,保证结果确实是一个数？
str = input("请输入一个需要转换成浮点数的字符串：")
strToFloat = float(str)
print(strToFloat)  # 直接输出数值可以，但是要和字符串一块输出就要转换成字符串
