from pygame import *
import random
from consts import *
import soldier
import proportion


def placement(board, item_, wanted_place):
    pic_item = image.load(f'bin png/{item_}.png')
    pic_item = transform.scale(pic_item, proportion.pixelize(ITEM_PROPORTION[item_]))
    board.blit(pic_item, proportion.pixelize(wanted_place))
    # display.flip()


def random_tup_in_board(item):
    item_size = ITEM_PROPORTION[item]
    rand_row = random.randrange(ROWS_IN_BOARD - (item_size[1]))
    rand_col = random.randrange(COLS_IN_BOARD - (item_size[0]))
    rand_tup = (rand_col, rand_row)
    return rand_tup


def random_bush_list(bush_num):
    places_list = []
    while len(places_list) < bush_num:
        rand_tup = random_tup_in_board(GRASS_STR)
        if rand_tup not in places_list:
            places_list.append(rand_tup)
            # placement(green_screen, GRASS_STR, rand_tup)
    return places_list


def placing_bushes_list(screen):
    bush_list = random_bush_list(BUSH_NUM)
    for bush_location in bush_list:
        placement(screen, GRASS_STR, bush_location)


def drawgrid(mine_screen):
    size = SIZE
    for x in range(0, PIXEL_COLS, size):
        for y in range(0, PIXEL_ROWS, size):
            rect = Rect(x, y, size, size)
            draw.rect(mine_screen, GREEN, rect, 1)
