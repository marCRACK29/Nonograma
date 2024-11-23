import pygame

from pygame import MOUSEBUTTONDOWN
from pygame.constants import USEREVENT

from Proxy import Proxy
from tablero import Tablero
from memento import mementoCreacion
from Color import Color
import math
from colorbutton import colorbutton

color_buttons = [
    colorbutton(image_base=pygame.image.load("assets/black.png"), image_flotante = pygame.image.load("assets/black_flotante.png"),pos=(1100, 50), color=Color.BLACK.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/blue.png"), image_flotante = pygame.image.load("assets/blue_flotante.png"),pos=(1160, 50), color=Color.BLUE.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/brown.png"), image_flotante = pygame.image.load("assets/brown_flotante.png"),pos=(1100, 110), color=Color.BROWN.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/celeste.png"), image_flotante = pygame.image.load("assets/celeste_flotante.png"),pos=(1160, 110), color=Color.LIGHT_BLUE.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/green.png"), image_flotante = pygame.image.load("assets/green_flotante.png"),pos=(1100, 170), color=Color.GREEN.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/greenL.png"),image_flotante = pygame.image.load("assets/greenL_flotante.png"), pos=(1160, 170), color=Color.LIGHT_GREEN.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/orange.png"), image_flotante = pygame.image.load("assets/orange_flotante.png"),pos=(1100, 230), color=Color.ORANGE.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/pink.png"), image_flotante = pygame.image.load("assets/pink_flotante.png"),pos=(1160, 230), color=Color.PINK.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/purple.png"), image_flotante = pygame.image.load("assets/purple_flotante.png"),pos=(1100, 290), color=Color.PURPLE.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/red.png"), image_flotante = pygame.image.load("assets/red_flotante.png"),pos=(1160, 290), color=Color.RED.value, size=(50, 50)),
    colorbutton(image_base=pygame.image.load("assets/yellow.png"), image_flotante = pygame.image.load("assets/yellow_flotante.png"),pos=(1130, 350), color=Color.YELLOW.value, size=(50, 50)),
]
n = 80
DESHACER = colorbutton(image_base=pygame.image.load("assets/deshacer.png"), image_flotante = pygame.image.load("assets/deshacer.png"),pos=(1050, 450), color=None, size=(n, n))
REHACER = colorbutton(image_base=pygame.image.load("assets/rehacer.png"), image_flotante = pygame.image.load("assets/rehacer.png"),pos=(1150, 450), color=None, size=(n, n))
class GestorCreacion:
    def __init__(self, tamañoTablero):
        self.tamañoTablero = tamañoTablero
        self.tamañoCasilla =  math.floor((-25*tamañoTablero)/10 + 75)
        self.tableroObjetivo = Tablero(tamañoTablero, self.tamañoCasilla)
        self.text_box = None  # Inicializa el cuadro de texto
        self.estado = False #Estado para finalizar creacion de nonograma
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
    def es_clic_valido(self, pos):
        # Calcula las coordenadas del tablero
        desfase_x = 300
        desfase_y = 165
        tamaño_tablero_px = self.tamañoTablero * self.tamañoCasilla

        # Obtén las coordenadas del clic
        x, y = pos

        # Verifica si el clic está dentro del área del tablero
        if (desfase_x <= x < desfase_x + tamaño_tablero_px and
                desfase_y <= y < desfase_y + tamaño_tablero_px):
            return True
        return False


    def draw(self, screen):
        for boton in color_buttons:
            boton.draw(screen)
        DESHACER.draw(screen)
        REHACER.draw(screen)
        #undo_button.draw(screen)
        #Metodo para dibujar el tablero en la pantalla
        #screen.fill((255, 255, 255))  # Limpia la pantalla con blanco
        desfase_x = 300
        desfase_y = 165
        self.tableroObjetivo.dibujar(screen, desfase_x, desfase_y)
        # Dibuja el cuadro de texto si está inicializado
        if self.text_box:
            self.text_box.draw()

    def handle_events(self, event, caretaker):
        #Manejar eventos de teclado y mouse
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Click izquierdo
                # Verificar si se hizo clic en algún botón de color
                for boton in color_buttons:
                    if boton.checkForInput(event.pos):
                        Proxy.set_color(boton.get_color())
                        return

                # Verificar si se hizo clic en los botones de deshacer/rehacer
                if DESHACER.checkForInput(event.pos):
                    caretaker.deshacer()
                    return
                elif REHACER.checkForInput(event.pos):
                    caretaker.rehacer()
                    return

                # Verificar si el clic está dentro del tablero
                if self.es_clic_valido(event.pos):
                    caretaker.añadirMemento()
                    self.tableroObjetivo.manejar_evento(event, Proxy.get_color())
        if self.text_box:
            self.text_box.process_events(event)
            if self.text_box.check_button():  # Si se presiona el botón de guardar
                nombre = self.text_box.getText()  # Obtiene el texto ingresado
                caretaker.añadir_en_catalogo(self.tamañoTablero, nombre)
                self.estado = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                caretaker.deshacer()
            elif event.key == pygame.K_r:
                caretaker.rehacer()

