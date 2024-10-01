import pygame, sys
from pygame import *
from consts import *
import initial


def grass_screen():
    screen = initial.creating_empty_board()
    screen.fill(GREEN)
    initial.random_bush_bomb('grass', screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG)


def mine_screen():
    screen = initial.creating_empty_board()
    screen.fill(BLACK)
    initial.drawGrid(screen)
    initial.random_bush_bomb('mine', screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG)
