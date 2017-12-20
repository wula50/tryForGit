# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
长途旅行中，遇到一个加油站，编写一个程序确定是否要在这里加油
问题：
你的油箱有多大？
油箱有多满？（百分比）
汽车每升走多远？
包含一个5升缓冲区，以防油表不准
'''
volumeOfTank=int(raw_input("Size of tank:"))
percentOfTank=float(raw_input("percent full:"))*0.01
literPerKm=float(raw_input("km per liter:"))
buffer=5
distanceToNextStation=float(raw_input("How long is it to next station?"))
youCanGo=((volumeOfTank*percentOfTank)-5)*literPerKm
print("You can go another "+str(youCanGo)+" km\n"+
"The next gas station is "+str(distanceToNextStation)+" km away")
if youCanGo>distanceToNextStation:
    print("You can wait for the next sation.")
else:
    print("Get gas now!")

