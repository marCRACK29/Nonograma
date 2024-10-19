
import pygame

from src.Color import Color
from src.Proxy import Proxy


class Casilla:

    def __init__(self, x, y, tamañoCasilla, fila, columna):
        self.color = Color.WHITE.value
        self.rect = pygame.Rect(x, y, tamañoCasilla, tamañoCasilla)
        #Posicion fila y columna de la casilla en el tablero
        self.fila = fila
        self.columna = columna

    def dibujar(self, screen):
        pygame.draw.rect(screen, Color.BLACK.value, self.rect)
        pygame.draw.rect(screen, self.color, self.rect.inflate(-2,-2))

    def set_color(self):
        self.color = Proxy.get_color()

    def get_color(self):
        return self.color

    def click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.set_color()
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'columna': self.columna, 'fila': self.fila}))
