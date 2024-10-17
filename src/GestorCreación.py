import pygame
from src.tablero import Tablero
from src.memento import mementoCreacion

class GestorCreacion:

    def __init__(self, tamañoTablero, tamañoCasilla):
        self.tableroObjetivo = Tablero(tamañoTablero, tamañoCasilla)

    def guardar_estado(self):
        m = mementoCreacion(self.tableroObjetivo)
        print("Guardado")
        return m

    def cargar_estado(self, memento):
        self.tableroObjetivo = memento.get_state()
        print("Cargado")


def main():
    from src.caretaker import Caretaker
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("gestor")

    gestor = GestorCreacion(20, 50)
    caretaker = Caretaker(gestor)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    caretaker.añadirMemento()
                    caretaker.guardar()
                elif event.key == pygame.K_l:
                    caretaker.cargarPartida()

            gestor.tableroObjetivo.manejar_evento(event)

        gestor.tableroObjetivo.dibujar(screen)
        pygame.display.flip()

if __name__ == '__main__':

    main()