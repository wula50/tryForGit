# !/usr/bin/python
# -*- coding: utf-8 -*-

import time

seconds = int(raw_input("Countdown timer: How many seconds?"))
for i in range(seconds, 0, -1):
    print i
    time.sleep(1)
print("BLAST OFF!")
