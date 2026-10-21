import os

import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN_PATH = os.path.join(os.path.dirname(__file__), 'crown.png')
CROWN = pygame.transform.scale(pygame.image.load(CROWN_PATH), (44, 25))
