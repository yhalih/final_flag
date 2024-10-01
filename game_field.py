from pygame import *
import time
import soldier
import result
import initial
from consts import *


def can_game_continue(soldier_location, mine_locations, flag_locations):
    # Collecting lists of locations
    legs_locations = soldier.soldier_legs(soldier_location)
    body_locations = soldier.soldier_body(soldier_location)

    can_continue = True

    # Checking if soldier stepped on mine
    for location in legs_locations:
        if location in mine_locations:
            can_continue = False

    # Checking if soldier reached the flag
    if can_continue:
        for location in body_locations:
            if location in flag_locations:
                can_continue = False

    return can_continue


def find_new_location(soldier_location, board):
    pressed = key.get_pressed()
    new_location = [soldier_location[0], soldier_location[1]]
    #
    # Showing the secret screen
    if pressed[K_RETURN]:
        # show secret screen
        time.sleep(1)

    elif pressed[K_LEFT]:
        new_location[0] -= 1
    elif pressed[K_RIGHT]:
        new_location[0] += 1
    elif pressed[K_UP]:
        new_location[1] += 1
    elif pressed[K_DOWN]:
        new_location[1] -= 1

    # move to new location if in range
    if 0 <= new_location[0] < ROWS_IN_BOARD and 0 <= new_location[1] < COLS_IN_BOARD:
        soldier_location = new_location
        initial.placement(board, 'soldier.png', soldier_location)

    display.update()

    return tuple(soldier_location)


def move_soldier(soldier_location, mine_locations, flag_locations, board):
    can_continue = True

    # make a move and then check if game ended
    while can_continue:
        soldier_location = find_new_location(soldier_location, board)
        can_continue = can_game_continue(soldier_location, mine_locations, flag_locations)

    # Once game has ended
    result.end(soldier_location, mine_locations)
