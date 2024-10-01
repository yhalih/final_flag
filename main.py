from pygame import *
import screen
import sys

init()
running=True
while running:
    screen.grass_screen()
    display.flip()
    for event in event.get():
        if event.type == QUIT:
            running = False
sys.exit()
quit()



