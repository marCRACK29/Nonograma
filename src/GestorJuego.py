from src.memento import mementoJuego
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
        self.tableroJugador, self.tableroObjetivo = memento.get_state()
        print("Cargado")

    def cargar_objetivo(self, memento):
        self.tableroObjetivo = memento.get_state()

    def pista(self):
        for i in range(self.tamañoTablero):
            for ii in range(self.tamañoTablero):
                C1 = self.tableroObjetivo.getCasillas()[i][ii].get_color()
                C2 =self.tableroJugador.getCasillas()[i][ii].get_color()
                if (C1 != Color.WHITE.value and C2 == Color.WHITE.value):
                    self.tableroJugador.getCasillas()[i][ii].set_color(C1)
                    break

    def comprobar(self, i, ii):
        if(self.tableroJugador.getCasillas()[i][ii].get_color() == self.tableroObjetivo.getCasillas()[i][ii].get_color()):
            print ("Correcto") #printe de prueba
        else :
            print ("Incorrecto") #print de prueba

def main():
    from src.caretaker import Caretaker
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("gestor")

    gestor = GestorJuego(20, 50)
    caretaker = Caretaker(gestor)
    caretaker.cargarObjetivo()


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
                    caretaker.cargar()
            elif event.type == pygame.USEREVENT:
                gestor.comprobar(event.fila, event.columna)

            gestor.tableroJugador.manejar_evento(event)

        gestor.tableroJugador.dibujar(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

