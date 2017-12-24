# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
建立一个银行帐号BankAccount类，用来存储户名，帐号，余额信息
再定义一些显示，存钱和取钱的方法

再建立一个税率类InterestAccount，继承自BankAccount类
定义一个addInterest方法实现加利率
'''


class BankAccount:
    def __init__(self, accountName, accountNumber, accountChange):
        self.accountName = accountName
        self.accountNumber = accountNumber
        self.accountChange = accountChange

    def __str__(self):
        msg = "My accountname is: " + self.accountName + ", My accoutnumber is: " + self.accountNumber + ", My changes is: " + str(
            self.accountChange)
        return msg

    def save(self, money):
        self.accountChange += money

    def draw(self, money):
        self.accountChange -= money


class InterestAccount(BankAccount):
    def __init__(self, accountName, accountNumber, accountChange, rate):
        BankAccount.__init__(self, accountName, accountNumber, accountChange)  # 初始化时要和父类的初始方法一致
        self.rate = rate

    # def __str__(self):#该方法已继承，不需要再写
    # msg = "My accountname is: " + self.accountName + " My accoutnumber is: " + self.accountNumber + " My changes is: " + str(
    #     self.accountChange)
    # return msg

    def addInterest(self):
        self.accountChange = self.accountChange * (1 + self.rate)


myAccount = BankAccount("Ada", "0011", 0.2)
# myAccount.accountName = "Ada"
# myAccount.accountNumber = "0011"
print myAccount
myAccount.save(100)
print myAccount

myRate = InterestAccount("Ada", "0011", 10, 0.05)
print myRate
for i in range(3):  # 显示？年的本金和利息
    myRate.addInterest()
    print myRate
