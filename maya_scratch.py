import initial
import random

import soldier
from consts import *
import pygame
from pygame import *
import initial


def find_new_location(soldier_location, board, mine_list):
    pressed = key.get_pressed()
    new_location = [soldier_location[0], soldier_location[1]]

        # Showing the secret screen
        if pressed[K_RETURN]:
            screen.display_gridscreen(soldier_location, mine_list)

        elif pressed[K_LEFT]:
            new_location[0] -= 1
        elif pressed[K_RIGHT]:
            new_location[0] += 1
        elif pressed[K_UP]:
            new_location[1] += 1
        elif pressed[K_DOWN]:
            new_location[1] -= 1

        return tuple(new_location)


def move_to_new_location(new_location, board):
    if 0 <= new_location[0] < ROWS_IN_BOARD and 0 <= new_location[1] < COLS_IN_BOARD:
        soldier_location = new_location
        initial.placement(board, 'soldier', soldier_location)

    display.update()