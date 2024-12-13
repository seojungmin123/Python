import pygame
import sys
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

w = 480
h = 640

pad = pygame.display.set_mode((w,h))
pygame.display.set_caption("Shooting Game")

pad.fill((244,170,170))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
