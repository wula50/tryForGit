# !/usr/bin/python
# -*- coding: utf-8 -*-
import easygui
favor=easygui.choicebox("What do you like?",choices=['apple','banana','milk'])
easygui.msgbox("Your choice is "+favor)
favor=easygui.buttonbox("What do you like?",choices=['apple','banana','milk'])
easygui.msgbox("Your choice is "+favor)
favor=easygui.enterbox("What do you like?")
easygui.msgbox("Your enter "+favor)