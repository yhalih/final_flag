from pygame import *
import random
from consts import *
import soldier
import proportion



def placement(board, item_, wanted_place):
    pic_item = image.load(f'bin png/{item_}.png').convert()
    pic_item = transform.scale(pic_item, proportion.pixelize(ITEM_PROPORTION[item_]))
    board.blit(pic_item, proportion.pixelize(wanted_place))
    # display.flip()


def random_tup_in_board():
    rand_row = random.randrange(ROWS_IN_BOARD)
    rand_col = random.randrange(COLS_IN_BOARD)
    rand_tup = (rand_row, rand_col)
    return rand_tup


def random_bush(green_screen , bomb_bush_num=BUSH_BOMB_NUM):
    places_list = []
    while len(places_list) < bomb_bush_num:
        rand_tup = random_tup_in_board()
        while rand_tup in places_list:
            rand_tup = random_tup_in_board()
        places_list.append(rand_tup)
        placement(green_screen, 'grass', rand_tup)

    return green_screen




#
def drawGrid(board):
    blocksize = SIZE  # Set the size of the grid block
    for x in range(PIXEL_COLS, blocksize):
        for y in range(0, PIXEL_ROWS, blocksize):
            rect = Rect(x, y, blocksize, blocksize)
            draw.rect(board, WHITE, rect, 1)
