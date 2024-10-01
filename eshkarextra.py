# def empty_matrix_board():
#     matrix_board = []
#     free_list = []
#
#     for j in range(50):
#         free_list.append("free")
#
#     for i in range(25):
#         matrix_board.append(free_list)
#
#     return matrix_board
#
# matrix_ = empty_matrix_board()
# for row in matrix_:
#     print (*row)
#
# import pygame
# pygame.init()
# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 1000
#
# run= True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
# pygame.quit()
#
#
#
#
# import pygame
#
# import initial
# from consts import *
# def creating_another_screen(screen):
#     screen.fill (BLACK)
#     for i in range (25):
#         for j in range (50):
#             pygame.draw.rect(screen, BLACK,  20, 1)
#
#
import pygame
from consts import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def drawgrid():
    size = SIZE
    for x in range (0, SCREEN_WIDTH, size):
        for y in range (0,SCREEN_HEIGHT, size):
            rect= pygame.Rect(x, y, size, size)
            pygame.draw.rect(screen, GREEN, rect, 1)
pygame.init()

run= True
while run:
    drawgrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
pygame.quit()

# pygame.init()
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# player = pygame.Rect((300, 250, 50, 50))
#
# run = True
# while run:
#     top_x= []
#     for i in range (25):
#         top_y = []
#         for j in range (50):
#             fun= pygame.draw.rect(screen, GREEN, player, 1)
#             top_y += fun
#         top_x += fun
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#     pygame.display.update()
# pygame.quit()

# to soldier modoul
# def soldier_legs (x_index, y_index):
#     x_index1 = x_index + 3
#     x_index2 = x_index1
#     y_index1 = y_index
#     y_index2 = y_index1 + 1
#     tup1 = (x_index1, y_index1)
#     tup2 = (x_index2, y_index2)
#     list_tuple= [tup1,tup2]
#     return list_tuple
#
# print(soldier_legs(0,0))
#
# def soldier_body(x_index, y_index):
#     list = []
#     for i in range (2):
#         list.append((x_index, y_index))
#         counter =0
#         for i in range (3):
#             new_x_index = x_index + 1 + counter
#             counter += 1
#             list.append((new_x_index, y_index))
#         y_index += 1
#     return list
#
# print(soldier_body(0,0))
#
#
#
#


#
#     tup_list= soldier_legs(0,0)
#     x1= tup_list [0][0]
#     y1 = tup_list [0] [1]
#     x2= tup_list [1][0]
#     y2 = tup_list [1][1]
#     for i in range (3):
#         num_x= x1 - 1
#         num_x2= x2 -1
#         new_tup= (num_x, x1)
#         new_tup1 = (num_x2, y1)
#         list_tup= [new_tup, new_tup1]
#
#     return list_tup
# print(soldier_body(0, 0))


#
# tup= []
# x2 = x1
# y2= y2+ 1
# for i in range (2):
#     x_body = x1 + 1
#     y_body = y1
#     x_body1 = x1 +1
#     y_body1 = y2
# tup1= (x1, y1)
# tup2= ()
#
#
#
