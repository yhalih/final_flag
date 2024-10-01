from pygame import *
import random
from consts import *
import soldier
import proportion


def creating_empty_board():
    screen = display.set_mode((PIXEL_COLS, PIXEL_ROWS))
    return screen

def empty_matrix():
    matrix = []
    free_list = []

    for j in range(COLS_IN_BOARD):
        free_list.append(EMPTY_CELL)

    for i in range(ROWS_IN_BOARD):
        matrix.append(free_list)

    return matrix

def placement(board, item_, wanted_place):
    pic_item = image.load(f'bin png/{item_}.png').convert()
    pic_item = transform.scale(pic_item, proportion.pixelize(ITEM_PROPORTION[item_]))
    board.blit(pic_item, proportion.pixelize(wanted_place))
    # display.flip()


def random_tup_in_board():
    rand_x = random.randrange(COLS_IN_BOARD)
    rand_y = random.randrange(COLS_IN_BOARD)
    rand_tup = (rand_y, rand_x)
    return rand_tup


def random_bush_bomb(repeted_item, board, bomb_bush_num=BUSH_BOMB_NUM):
    places_list = []
    flag_and_start = [soldier.soldier_legs(SOLDIER_START), FLAG_LOCATION]
    while len(places_list) < bomb_bush_num:
        rand_tup = random_tup_in_board()
        if rand_tup not in places_list and rand_tup not in flag_and_start:
            places_list.append(rand_tup)
            placement(board, repeted_item, rand_tup)

    return places_list

def insert_mines_in_matrix_board():
    board = empty_matrix()
    for i in range(20):
        mine_location = random_tup_in_board()
        while board[mine_location[0]][mine_location[1]] != "free":
            mine_location = random_tup_in_board()
        board[mine_location[0]][mine_location[1]] = "mine"
        placement(board, 'mine', mine_location)


#
def drawGrid(board):
    blocksize = SIZE #Set the size of the grid block
    for x in range(PIXEL_COLS, blocksize):
        for y in range(0, PIXEL_ROWS, blocksize):
            rect = Rect(x, y, blocksize, blocksize)
            draw.rect(board, WHITE , rect, 1)