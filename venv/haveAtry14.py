# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
建立一个银行帐号类，用来存储户名，帐号，余额信息
再定义一些显示，存钱和取钱的方法
'''


class BankAccount:
    def __init__(self):
        self.accountName = ""
        self.accountNumber = ""
        self.accountChange = 0.0

    def __str__(self):
        msg = "My accountname is: " + self.accountName + " My accoutnumber is: " + self.accountNumber + " My changes is: " + str(
            self.accountChange)
        return msg

    def save(self, money):
        self.accountChange += money

    def draw(self, money):
        self.accountChange -= money


myAccount = BankAccount()
myAccount.accountName = "Ada"
myAccount.accountNumber = "0011"
print myAccount
myAccount.save(100)
print myAccount
