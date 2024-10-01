from pygame import *
from consts import *
import pygame
import screen
import back_matrix
import game_field
import sys

pygame.init()
g_screen = display.set_mode((PIXEL_COLS, PIXEL_ROWS))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.create_grass_screen(g_screen)
    display.flip()

    matrix = []
    mine_list = back_matrix.create_whole_matrix(matrix)

    game_field.move_soldier(SOLDIER_START, mine_list, FLAG_LOCATION_LIST, g_screen)

    display.flip()

pygame.quit()