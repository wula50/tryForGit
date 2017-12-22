# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
Enter 5 names:
Tomy
Ada
Bob
Nick
Jacky
The names are Tomy   Ada   Bob   Nick   Jacky
'''

print "Enter 5 names:"
nameList = []
for i in range(0, 5):
    nameList.append(raw_input())
# print nameList
print "The names are",
for j in nameList:
    print j, " ",
