import pygame

from Color import Color

# Clase que representa una casilla del tablero
class Casilla:
    def __init__(self, x, y, tamañoCasilla, fila, columna):
        self.color = Color.WHITE.value
        self.rect = pygame.Rect(x, y, tamañoCasilla, tamañoCasilla)
        # Posición fila y columna de la casilla en el tablero
        self.fila = fila
        self.columna = columna

    # Dibujar la casilla en la pantalla
    def dibujar(self, screen):
        pygame.draw.rect(screen, Color.BLACK.value, self.rect)
        pygame.draw.rect(screen, self.color, self.rect.inflate(-2,-2))

    # Cambiar el color de la casilla cuando se hace click en ella después de presionar un colorbutton
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    # Verificar si la casilla fue clickeada
    def click(self, evento, color_seleccionado):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button in [1, 3]: # 1 para los clicks en botones, 3 para poner la casilla en blanco
            # Ajustar la posición del mouse según el desplazamiento
            mouse_pos = (
                evento.pos[0] - 300,  # Desplazamiento_x
                evento.pos[1] - 165   # Desplazamiento_y
            )
            if self.rect.collidepoint(mouse_pos):
                self.set_color(color_seleccionado) # Cambiar el color de la casilla
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {
                'columna': self.columna,
                'fila': self.fila,
                'color': self.color
                }))
