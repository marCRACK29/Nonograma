import pygame
from pygame import MOUSEBUTTONDOWN
from src.Proxy import Proxy
from src.tablero import Tablero
from src.memento import mementoCreacion
from src.Color import Color
import math
from src.colorbutton import colorbutton

color_buttons = [
    colorbutton(image=pygame.image.load("assets/black.png"), pos=(1100, 50), color=Color.BLACK.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/blue.png"), pos=(1160, 50), color=Color.BLUE.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/brown.png"), pos=(1100, 110), color=Color.BROWN.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/celeste.png"), pos=(1160, 110), color=Color.LIGHT_BLUE.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/green.png"), pos=(1100, 170), color=Color.GREEN.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/greenL.png"), pos=(1160, 170), color=Color.LIGHT_GREEN.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/orange.png"), pos=(1100, 230), color=Color.ORANGE.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/pink.png"), pos=(1160, 230), color=Color.PINK.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/purple.png"), pos=(1100, 290), color=Color.PURPLE.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/red.png"), pos=(1160, 290), color=Color.RED.value, size=(50, 50)),
    colorbutton(image=pygame.image.load("assets/yellow.png"), pos=(1130, 350), color=Color.YELLOW.value, size=(50, 50)),
]
class GestorCreacion:
    def __init__(self, tamañoTablero):
        self.tableroObjetivo = Tablero(tamañoTablero, math.floor((-25*tamañoTablero)/10 + 75))

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
        for boton in color_buttons:
            boton.draw(screen)
        #Metodo para dibujar el tablero en la pantalla
        #screen.fill((255, 255, 255))  # Limpia la pantalla con blanco
        desfase_x = 150
        desfase_y = 150
        self.tableroObjetivo.dibujar(screen, desfase_x, desfase_y)

    def handle_events(self, event, caretaker):
        #Manejar eventos de teclado y mouse
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for boton in color_buttons:
                    if boton.checkForInput(event.pos):
                        Proxy.set_color(boton.get_color())
                        break
                caretaker.añadirMemento()
        self.tableroObjetivo.manejar_evento(event, Proxy.get_color())
