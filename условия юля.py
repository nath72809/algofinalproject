from pygame import *
from random import randint

run = True
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if not finish:

    time.delay(20)
display.update()