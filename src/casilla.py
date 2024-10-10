
import pygame

from src.Color import Color
from src.Proxy import Proxy


class Casilla:

    def __init__(self, x, y, tamañoCasilla):
        self.color = Color.WHITE.value
        self.rect = pygame.Rect(x, y, tamañoCasilla, tamañoCasilla)

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def set_color(self):
        self.color = Proxy.get_color()

    def click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.set_color()
