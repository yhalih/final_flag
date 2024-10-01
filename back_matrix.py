import initial
import soldier
from consts import *


def empty_matrix(matrix):
    for i in range(25):
        free_list = []
        for j in range(50):
            free_list.append("free")
        matrix.append(free_list)
    return matrix


def insert_flag_soldier_matrix(matrix):
    flag_locations = FLAG_LOCATION_LIST
    for i in range(len(flag_locations)):
        location = flag_locations[i]
        row = location[0]
        col = location[1]
        matrix[row][col] = "flag"

    soldier_start_legs = soldier.soldier_legs((0, 0))
    soldier_start_body = soldier.soldier_body((0, 0))

    for location in soldier_start_body:
        matrix[location[0]][location[1]] = "body"
    for location in soldier_start_legs:
        matrix[location[0]][location[1]] = "legs"


def insert_mines_in_matrix_board(matrix):
    insert_flag_soldier_matrix(matrix)
    mine_list = []
    for i in range(20):
        mine_location = initial.random_tup_in_board(MINE_STR)
        while matrix[mine_location[1]][mine_location[0]] != "free":
            mine_location = initial.random_tup_in_board(MINE_STR)
        matrix[mine_location[1]][mine_location[0]] = "mine"
        mine_list.append(mine_location)

    return mine_list  # important for grid screen


def create_whole_matrix(matrix):
    whole_matrix = empty_matrix(matrix)
    mine_list = insert_mines_in_matrix_board(whole_matrix)
    return mine_list
