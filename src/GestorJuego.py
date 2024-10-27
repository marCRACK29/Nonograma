from pygame import MOUSEBUTTONDOWN
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
            for j in range(self.tamañoTablero):
                C1 = self.tableroObjetivo.getCasillas()[i][j].get_color()
                C2 =self.tableroJugador.getCasillas()[i][j].get_color()
                if (C1 != Color.WHITE.value and C2 == Color.WHITE.value):
                    self.tableroJugador.getCasillas()[i][j].set_color(C1)
                    break

    def comprobar(self, i, j):
        if(self.tableroJugador.getCasillas()[i][j].get_color() == self.tableroObjetivo.getCasillas()[i][j].get_color()):
            print ("Correcto") #print de prueba
        #else :
            #print ("Incorrecto") #print de prueba

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
                caretaker.cargar()
        elif event.type == pygame.USEREVENT:
            self.comprobar(event.fila, event.columna)

        # Llama al manejo de eventos del tablero del jugador
        self.tableroJugador.manejar_evento(event)


