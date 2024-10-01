import pygame, sys
from pygame import *
from consts import *
import initial


def grass_screen(screen):
    screen.fill(GREEN)
    initial.random_bush(screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG_LOCATION)


screen = display.set_mode((PIXEL_COLS, PIXEL_ROWS))
def mine_screen(screen):
    screen.fill(BLACK)
    initial.drawGrid(screen)
#     initial.random_bush_bomb('mine', screen)
#     initial.placement(screen, 'soldier', SOLDIER_START)
#     initial.placement(screen, 'flag', FLAG)

