# !/usr/bin/python
# -*- coding: utf-8 -*-

#商场降价促销，低于等于10元，会给10%折扣，大于10元，给20%折扣。
salePrice=float(raw_input("请输入购买价格："))
discountBelowsETen=0.1
discountAboveTen=0.2
if salePrice<=10:
    salePrice=salePrice*(1-discountBelowsETen)
    print("享受10%折扣，折后价为："+str(salePrice))
else:
    salePrice=salePrice*(1-discountAboveTen)
    print("享受20%折扣，折后价为："+str(salePrice))