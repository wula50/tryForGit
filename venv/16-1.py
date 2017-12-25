# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
画一个绿色的圆环

画100个长方形
'''
import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
# pygame.draw.circle(screen,[0,255,0],[100,100],100,50)
for i in range(50):
    top = random.randint(0, 250)
    left = random.randint(0, 400)
    wide = random.randint(0, 480)
    length = random.randint(0, 300)
    linewide = random.randint(0, 10)
    colorname = random.choice(pygame.color.THECOLORS.keys())
    pygame.draw.rect(screen, pygame.color.THECOLORS[colorname], [top, length, wide, length], 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
