# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
显示2个球

隐藏第一个球

小球来回动
'''
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([800, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.png")
x = 50
y = 50
x_speed = 20
screen.blit(my_ball, [50, 50])
pygame.display.flip()
# for looper in range(1, 5):#使小球一直动

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(10)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 255, 255], 0)
    x += x_speed
    if x > screen.get_width() - 255 or x < 0:
        x_speed = -x_speed
    screen.blit(my_ball, [x, 50])
    pygame.display.flip()
