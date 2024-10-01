import time

import pygame, sys
from pygame import *
from consts import *
import initial



def create_grass_screen(screen):
    screen.fill(GREEN)
    initial.placing_bushes_list(screen)
    initial.placement(screen, SOLDIER_STR, SOLDIER_START)
    initial.placement(screen, FLAG_STR, FLAG_LOCATION_CORNER)


def create_mine_screen(screen, mine_list, soldier_location):
    initial.drawgrid(screen)
    for mine_location in mine_list:
        initial.placement(screen, MINE_STR, mine_location)

    initial.placement(screen, SOLDIER_STR, soldier_location)


def display_gridscreen(soldier_location, mine_list):
    pygame.init()

    mine_screen= display.set_mode((PIXEL_COLS, PIXEL_ROWS))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        create_mine_screen(mine_screen, mine_list, soldier_location)
        display.flip()
    time.sleep(1)

#