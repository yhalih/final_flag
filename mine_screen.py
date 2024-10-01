from pygame import *
from consts import *
import pygame
import screen


def
    pygame.init()
    mine_screen= display.set_mode((PIXEL_COLS, PIXEL_ROWS))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.mine_screen(mine_screen)
        display.flip()


    pygame.quit()
