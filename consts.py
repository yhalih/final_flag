SIZE = 25

EMPTY_CELL= 'free'

ROWS_IN_BOARD = 25
COLS_IN_BOARD = 50

PIXEL_ROWS = ROWS_IN_BOARD * SIZE
PIXEL_COLS = COLS_IN_BOARD * SIZE
#
SOLDIER_START = (0, 0)

BUSH_BOMB_NUM = 20

ITEM_PROPORTION = {
    'soldier': (2, 4),
    'mine': (3, 1),
    'grass': (3, 1),
    'flag': (4, 3)
}

FLAG_LOCATION_CORNER = (COLS_IN_BOARD - ITEM_PROPORTION['flag'][0], ROWS_IN_BOARD - ITEM_PROPORTION['flag'][1])
FLAG_LOCATION_LIST= [(22, 46), (22, 47), (22, 48), (22, 49),
                      (23, 46), (23, 47), (23, 48), (23, 49),
                      (24, 46), (24, 47), (24, 48), (24, 49), ]

GREEN = (64, 200, 45)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

