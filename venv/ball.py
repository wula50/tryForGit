# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
显示2个球

隐藏第一个球
'''
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.png")
screen.blit(my_ball, [50, 50])
pygame.display.flip()
pygame.time.delay(2000)
screen.blit(my_ball, [300, 50])
pygame.draw.rect(screen,[255,255,255],[50,50,255,255],0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
