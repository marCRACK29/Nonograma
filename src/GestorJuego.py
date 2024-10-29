from pygame import MOUSEBUTTONDOWN
from src.memento import mementoJuego, mementoCreacion
from src.tablero import Tablero
from src.Color import Color
import pygame

class GestorJuego:

    def __init__(self, tamañoTablero, tamañoCasilla):
        self.tamañoTablero = tamañoTablero
        self.tableroObjetivo = Tablero(tamañoTablero, tamañoCasilla)
        self.tableroJugador = Tablero(tamañoTablero, tamañoCasilla)

    def guardar_estado(self):
        m = mementoJuego(self.tableroJugador, self.tableroObjetivo)
        print("Guardado")
        return m

    def cargar_estado(self, memento):
        tableros_cargados = memento.get_state()
        if isinstance(tableros_cargados, tuple):
            self.tableroJugador, self.tableroObjetivo = tableros_cargados
        else:
            self.tableroJugador = tableros_cargados
        print("Cargado")

    #Metodo que permite cargar un tablero objetivo usando un mementoCreacion
    def cargar_objetivo(self, memento):
        tablero_cargado = memento.get_state()
        if isinstance(tablero_cargado, tuple):
            self.tableroObjetivo = tablero_cargado[0]  # Si es una tupla, tomar el primer elemento
        else:
            self.tableroObjetivo = tablero_cargado
        print("Objetivo cargado")

        # Debug: verificar el estado después de cargar
        print("Estado del tablero después de cargar:")
        for fila in self.tableroObjetivo.getCasillas():
            print([casilla.get_color() for casilla in fila])

    def pista(self):
        for i in range(self.tamañoTablero):
            for j in range(self.tamañoTablero):
                C1 = self.tableroObjetivo.getCasillas()[i][j].get_color()
                C2 =self.tableroJugador.getCasillas()[i][j].get_color()
                if (C1 != Color.WHITE.value and C2 == Color.WHITE.value):
                    self.tableroJugador.getCasillas()[i][j].set_color(C1)
                    break

    def comprobar(self, i, j):
        print(f"Color jugador: {self.tableroJugador.getCasillas()[i][j].get_color()}, Color objetivo: {self.tableroObjetivo.getCasillas()[i][j].get_color()}")
        print(f"Casillas a comparar: {i},{j}")
        if(self.tableroJugador.getCasillas()[i][j].get_color() == self.tableroObjetivo.getCasillas()[i][j].get_color()):
            print ("Correcto") #print de prueba
        else :
            print ("Incorrecto") #print de prueba

    def draw(self, screen):
        #Metodo para dibujar el tablero en la pantalla
        screen.fill((255, 255, 255))  # Limpia la pantalla con blanco
        self.tableroJugador.dibujar(screen)  # Dibuja el tablero del jugador

    def handle_events(self, event, caretaker):
        #Manejar eventos de teclado y mouse
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                caretaker.añadirMemento()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                caretaker.cargarPartida()
        self.tableroJugador.manejar_evento(event)
        if event.type == pygame.USEREVENT:
            self.comprobar(event.fila, event.columna)


"""
def main():
    from src.caretaker import Caretaker
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("gestor")

    gestor = GestorJuego(10, 50)
    caretaker = Caretaker(gestor)
    caretaker.cargarObjetivo()  # Cargar el tablero objetivo al inicio

    print("Estado inicial del tablero objetivo:")
    for fila in gestor.tableroObjetivo.getCasillas():
        print([casilla.get_color() for casilla in fila])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    caretaker.añadirMemento()

            gestor.handle_events(event, caretaker)

        gestor.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
"""