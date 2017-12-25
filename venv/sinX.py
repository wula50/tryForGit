# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
尝试画正弦曲线
'''
import pygame, sys
import math

pygame.init()
screean = pygame.display.set_mode([640, 480])

screean.fill([255, 255, 255])
for x in range(640):
    pygame.draw.rect(screean,[0,0,0],[x,100,1,1],1)
for y in range(640):
    pygame.draw.rect(screean,[0,0,0],[100,y,1,1],1)
for y in range(0, 10000):
    x =(math.sin(200*y))/1000000+200
    pygame.draw.rect(screean, [0, 0, 0], [x, y, 1, 1], 1)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
