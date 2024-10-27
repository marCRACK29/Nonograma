import pygame
from pygame import MOUSEBUTTONDOWN
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

    def draw(self, screen):
        #Metodo para dibujar el tablero en la pantalla
        screen.fill((255, 255, 255))  # Limpia la pantalla con blanco
        self.tableroObjetivo.dibujar(screen)  # Dibuja el tablero del jugador

    def handle_events(self, event, caretaker):
        #Manejar eventos de teclado y mouse
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                caretaker.añadirMemento()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                caretaker.cargar()
        self.tableroObjetivo.manejar_evento(event)

"""
def main():
    from src.caretaker import Caretaker
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("gestor")

    gestor = GestorCreacion(20, 50)
    caretaker = Caretaker(gestor)
    if type(gestor) is GestorCreacion:
        print("creacion")

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
"""