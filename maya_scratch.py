# import initial
# import random
# from consts import *
# from pygame import *
# import initial
#
#
def empty_matrix_board():
    matrix_board = []
    free_list = []

    for j in range(50):
        free_list.append("free")

    for i in range(25):
        matrix_board.append(free_list)

    return matrix_board

#
# def insert_mines_in_matrix_board():
#     board = empty_matrix_board()
#     for i in range(20):
#         mine_location = initial.random_tup_in_board()
#         while board[mine_location[0]][mine_location[1]] != "free":
#             mine_location = initial.random_tup_in_board()
#         board[mine_location[0]][mine_location[1]] = "mine"
#         initial.placement(board, 'mine', mine_location)

import pygame
from pygame import *

init()
running=True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    grass_screen()
    display.flip()
quit()

