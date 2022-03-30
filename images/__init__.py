import pygame
pygame.init()


def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)


blackjack = load_image('images/blackjack.png', (400, 220))
casino = load_image('images/casino.png', (400, 200))
settings = load_image('images/settings.png', (420, 280))
exit = load_image('images/quit.png', (400, 300))
prof = load_image('images/prof.png', (465, 220))
menu = load_image('images/menu.jpg', (1300, 800))

