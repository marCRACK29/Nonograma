from casilla import Casilla
import pygame

class Tablero:
    def __init__(self,tamaño, tamañoCasilla):
        self.tamaño = tamaño
        self.tamañoCasilla = tamañoCasilla
        self.casillas = [[Casilla(y * tamañoCasilla, x * tamañoCasilla, tamañoCasilla, y, x) for x in range(tamaño)] for y in range(tamaño)]

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

    def manejar_evento(self, evento, color_seleccionado):
        for fila in self.casillas:
            for casilla in fila:
                casilla.click(evento, color_seleccionado)

    def getCasillas(self):
        return self.casillas
"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tablero")

    tablero = Tablero(30, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            tablero.manejar_evento(event)

        tablero.dibujar(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
"""