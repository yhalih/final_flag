from consts import *


def pixelize(item_):
    x_item = item_[0]
    y_item = item_[1]
    pix_item= (x_item * SIZE, y_item * SIZE)
    return pix_item
