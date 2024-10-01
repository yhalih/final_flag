import pygame, sys
from pygame import *
from consts import *
import initial


def grass_screen():
    screen= initial.creating_empty_board()
    screen.fill(GREEN)
    display.flip()
    initial.random_bush_bomb('grass', screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG)
#
