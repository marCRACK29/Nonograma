import pygame
from pygame import MOUSEBUTTONDOWN

from src.Proxy import Proxy
from src.tablero import Tablero
from src.memento import mementoCreacion
from src.Color import Color
class GestorCreacion:

    def __init__(self, tamañoTablero, tamañoCasilla):
        self.tableroObjetivo = Tablero(tamañoTablero, tamañoCasilla)

    def guardar_estado(self):
        m = mementoCreacion(self.tableroObjetivo)
        print("Guardado")
        return m

    def cargar_estado(self, memento):
        tablero_cargado = memento.get_state()
        if isinstance(tablero_cargado, tuple):
            self.tableroObjetivo = tablero_cargado[0]  # Si es una tupla, tomar el primer elemento
        else:
            self.tableroObjetivo = tablero_cargado
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
                caretaker.cargarPartida()
            elif event.key == pygame.K_1:
                Proxy.set_color(Color.BLACK)
            elif event.key == pygame.K_2:
                Proxy.set_color(Color.WHITE)
            elif event.key == pygame.K_3:
                Proxy.set_color(Color.YELLOW)
            elif event.key == pygame.K_4:
                Proxy.set_color(Color.PINK)
            elif event.key == pygame.K_5:
                Proxy.set_color(Color.BLUE)
        self.tableroObjetivo.manejar_evento(event)
