from pygame import *



finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
