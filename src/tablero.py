from src.casilla import Casilla

class Tablero:
    def __init__(self,tamaño, tamañoCasilla):
        self.tamaño = tamaño
        self.casillas = [[Casilla(x * tamañoCasilla, y * tamañoCasilla, tamañoCasilla, x, y) for x in range(tamaño)] for y in range(tamaño)]

    def dibujar(self, screen):
        for fila in self.casillas:
            for casilla in fila:
                casilla.dibujar(screen)

    def manejar_evento(self, evento):
        for fila in self.casillas:
            for casilla in fila:
                casilla.click(evento)

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