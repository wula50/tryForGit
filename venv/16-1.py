# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
画一个绿色的圆环
'''
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[0,255,0],[100,100],100,50)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
