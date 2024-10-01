from pygame import *

import sys
import initial
from consts import *
def grass_screen():
    screen.fill(GREEN)
    initial.random_bush_bomb('grass', screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG_LOCATION)


init()
screen = initial.creating_empty_board()

running=True
while running:
    grass_screen()

    for event in event.get():
        if event.type == QUIT:
            running = False

sys.exit()
quit()

#