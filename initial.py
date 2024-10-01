from pygame import *
import random
from consts import *
import soldier
import proportion


def creating_empty_board():
    screen = display.set_mode((PIXEL_COLS, PIXEL_ROWS))
    return screen


def placement(board, item_, wanted_place):
    pic_item = image.load(f'C:\\Users\\jbt\\Desktop\\python\\group_project_flag_game\\bin\\{item_}.png').convert()
    pic_item = transform.scale(pic_item, proportion.pixelize(ITEM_PROPORTION[item_]))
    board.blit(pic_item, proportion.pixelize(wanted_place))
    #display.flip()



def random_tup_in_board():
    rand_x = random.randrange(COLS_IN_BOARD)
    rand_y = random.randrange(COLS_IN_BOARD)
    rand_tup = (rand_x, rand_y)
    return rand_tup


def random_bush_bomb(repeted_item, board, bomb_bush_num=BUSH_BOMB_NUM):
    places_list = []
    flag_and_start = [soldier.soldier_legs(SOLDIER_START), FLAG]
    while len(places_list) < bomb_bush_num:
        rand_tup = random_tup_in_board()
        if rand_tup not in places_list and rand_tup not in flag_and_start:
            places_list.append(rand_tup)
            placement(board, repeted_item, rand_tup)

    return places_list
