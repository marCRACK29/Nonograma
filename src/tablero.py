import pygame
from casilla import Casilla

# Clase que representa el tablero del juego y contiene las casillas
class Tablero:
    def __init__(self,tamaño, tamañoCasilla):
        self.tamaño = tamaño
        self.tamañoCasilla = tamañoCasilla
        self.casillas = [[Casilla(y * tamañoCasilla, x * tamañoCasilla, tamañoCasilla, y, x) for x in range(tamaño)] for y in range(tamaño)]

    # Metodo para dibujar el tablero en la pantalla, tiene un desplazamiento debido a los índices a los extremos
    def dibujar(self, screen, desplazamiento_x=0, desplazamiento_y=0):
        for fila in self.casillas:
            for casilla in fila:
                # Ajustar la posición de la casilla con el desplazamiento
                rect_original = casilla.rect
                rect_desplazado = pygame.Rect(
                    rect_original.x + desplazamiento_x,
                    rect_original.y + desplazamiento_y,
                    rect_original.width,
                    rect_original.height
                )
                pygame.draw.rect(screen, casilla.color, rect_desplazado)
                pygame.draw.rect(screen, (0, 0, 0), rect_desplazado, 1)

    # Metodo para manejar los eventos de click en las casillas
    def manejar_evento(self, evento, color_seleccionado):
        for fila in self.casillas:
            for casilla in fila:
                casilla.click(evento, color_seleccionado)

    # Metodo para obtener las casillas del tablero
    def getCasillas(self):
        return self.casillas
