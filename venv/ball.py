# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
显示一个球
'''
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.png")
screen.blit(my_ball, [50, 50])
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
