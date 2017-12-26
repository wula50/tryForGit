# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
实验各种draw方法
'''
import pygame, sys, math

pygame.init()
screen = pygame.display.set_mode([480, 600])
screen.fill([255, 255, 255])
# pygame.draw.arc(screen,[0,255,0],[50,50,200,100],0,math.pi,5)#?
# pygame.draw.ellipse(screen,[255,0,0],[50,50,100,80],0)
pygame.draw.aaline(screen, [0, 0, 255], [50, 50], [50, 100], 5)
pygame.draw.line(screen, [255, 0, 255], [100, 50], [100, 150], 5)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
