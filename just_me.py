## import pygame, sys
# import os
#
# pygame.init()
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# green = (64, 200, 45)
# screen = pygame.display.set_mode((800, 600))
# soldier_pic = pygame.image.load(os.path.join('bin', 'soldier.png'))
#
#
# def draw_window():
#     screen.fill(green)
#     screen.blit(soldier_pic, (0,0))
#     pygame.display.update()
#
#
#
# running = True
#
# while running:
#     # screen.fill(green)
#     # pygame.display.flip()
#     for event in pygame.event.get():
#         if event.type == pygame.quit():
#             running = False
#
# sys.exit()
# quit()
#
import pygame, sys
from pygame import *
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
green = (64, 200, 45)
screen = display.set_mode((800, 600))
soldier_pic = pygame.image.load(os.path.join('bin', 'soldier.png'))

running = True

while running:
    screen.fill(green)
    screen.blit(soldier_pic, (0, 0))
    display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
#
# sys.exit()
quit()



#