# !/usr/bin/python
# -*- coding: utf-8 -*-

#询问你的姓名，房间号，街道和城市，省/直辖市，最后是邮编，使用对话框形式，最后显示一个寄信格式的完整地址
import easygui

name=easygui.enterbox("请输入你的姓名：",default='Bob')
roomNum=easygui.enterbox("请输入你的房间号：",default='202')
street=easygui.enterbox("请输入你的街道：",default='Hello')
city=easygui.enterbox("请输入你的城市：",default='Mianyang')
provice=easygui.enterbox("请输入你的省：",default='Sichuan')
code=easygui.enterbox("请输入你的邮编：",default='123456')
easygui.msgbox(name + '\n' + roomNum + ' ' + street + '\n' + city + ', '+ provice + '\n' + code)