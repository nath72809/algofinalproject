import pygame
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = time.Clock()



game = True

while game != False:
    pygame.display.update()
    clock.tick(40)