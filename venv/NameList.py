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
print
newNameList = nameList[:]
newNameList.sort()
print "sort nameList:",
for k in newNameList:
    print k, " ",
print
print "The third name you entered is:", nameList[2]

replace = int(raw_input("Replae on name. Which one? (1-5):"))
newname = raw_input("New name:")
nameList[replace - 1] = newname
print "The nams are",
for l in nameList:
    print l, " ",
