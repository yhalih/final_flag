from pygame import *
from consts import *
import pygame
import screen
import sys

pygame.init()
g_screen= display.set_mode((PIXEL_COLS, PIXEL_ROWS))

running=True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.grass_screen(g_screen)
    display.flip()


pygame.quit()



