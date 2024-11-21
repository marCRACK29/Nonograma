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

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def click(self, evento, color_seleccionado):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button in [1, 3]:
            # Ajustar la posición del mouse según el desplazamiento
            mouse_pos = (
                evento.pos[0] - 300,  # Desplazamiento_x
                evento.pos[1] - 165   # Desplazamiento_y
            )
            if self.rect.collidepoint(mouse_pos):
                self.set_color(color_seleccionado)
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {
                'columna': self.columna,
                'fila': self.fila,
                'color': self.color
                }))
