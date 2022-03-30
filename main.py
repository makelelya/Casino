import pygame

import button
from images import *


pygame.display.set_caption('CASINO')
screen = pygame.display.set_mode((1000, 700))


exit_button = button.Button(screen.get_width() - 950, screen.get_height() - 370, exit)
settings_button = button.Button(screen.get_width() - 955, screen.get_height() - 480, settings)
prof_button = button.Button(screen.get_width() - 975, screen.get_height() - 600, prof)


def draw():
    screen.blit(menu, (0, 0))
    screen.blit(blackjack, (520, 80))
    screen.blit(casino, (520, 360))
    exit_button.draw(screen)
    settings_button.draw(screen)
    prof_button.draw(screen)


pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    draw()
    pygame.display.flip()

pygame.quit()
