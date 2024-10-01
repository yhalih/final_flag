import initial
import random

import soldier
from consts import *
from pygame import *
import initial


def empty_matrix():
    matrix = []

    for i in range(25):
        free_list = []
        for j in range(50):
            free_list.append("free")
        matrix.append(free_list)
    return matrix


def insert_flag_soldier_matrix():
    matrix = empty_matrix()
    flag_locations = [(22, 46), (22, 47), (22, 48), (22, 49),
                      (23, 46), (23, 47), (23, 48), (23, 49),
                      (24, 46), (24, 47), (24, 48), (24, 49), ]
    for i in range(len(flag_locations)):
        location = flag_locations[i]
        x = location[0]
        y = location[1]
        matrix[x][y] = "flag"

    soldier_start_legs = soldier.soldier_legs((0, 0))
    soldier_start_body = soldier.soldier_body((0, 0))

    for location in soldier_start_body:
        matrix[location[0]][location[1]] = "body"
    for location in soldier_start_legs:
        matrix[location[0]][location[1]] = "legs"
    return matrix


def insert_mines_in_matrix_board():
    matrix = insert_flag_soldier_matrix()
    for i in range(20):
        mine_location = initial.random_tup_in_board()
        while matrix[mine_location[0]][mine_location[1]] != "free":
            mine_location = initial.random_tup_in_board()
        matrix[mine_location[0]][mine_location[1]] = "mine"
    return matrix


matrix = insert_mines_in_matrix_board()
for row in matrix:
    print(row)