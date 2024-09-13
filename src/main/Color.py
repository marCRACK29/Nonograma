import pygame
from enum import Enum

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    BROWN = (165, 42, 42)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    GRAY = (128, 128, 128)
    LIGHT_BLUE = (173, 216, 230)

    green_img = pygame.image.load("src/main/resources/green.png")
    red_img = pygame.image.load("src/main/resources/red.png")
    blue_img = pygame.image.load("src/main/resources/blue.png")