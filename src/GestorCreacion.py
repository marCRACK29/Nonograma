import pygame

from pygame import MOUSEBUTTONDOWN
from Proxy import Proxy
from tablero import Tablero
from memento import mementoCreacion
from Color import Color
import math
from colorbutton import ColorButton

# Gama de colorbutton's que se presentan en la pantalla al momento de crear un nonograma
color_buttons = [
    ColorButton(image_base=pygame.image.load("assets/black.png"), image_flotante = pygame.image.load("assets/black_flotante.png"), pos=(1100, 50), color=Color.BLACK.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/blue.png"), image_flotante = pygame.image.load("assets/blue_flotante.png"), pos=(1160, 50), color=Color.BLUE.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/brown.png"), image_flotante = pygame.image.load("assets/brown_flotante.png"), pos=(1100, 110), color=Color.BROWN.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/celeste.png"), image_flotante = pygame.image.load("assets/celeste_flotante.png"), pos=(1160, 110), color=Color.LIGHT_BLUE.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/green.png"), image_flotante = pygame.image.load("assets/green_flotante.png"), pos=(1100, 170), color=Color.GREEN.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/greenL.png"), image_flotante = pygame.image.load("assets/greenL_flotante.png"), pos=(1160, 170), color=Color.LIGHT_GREEN.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/orange.png"), image_flotante = pygame.image.load("assets/orange_flotante.png"), pos=(1100, 230), color=Color.ORANGE.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/pink.png"), image_flotante = pygame.image.load("assets/pink_flotante.png"), pos=(1160, 230), color=Color.PINK.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/purple.png"), image_flotante = pygame.image.load("assets/purple_flotante.png"), pos=(1100, 290), color=Color.PURPLE.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/red.png"), image_flotante = pygame.image.load("assets/red_flotante.png"), pos=(1160, 290), color=Color.RED.value, size=(50, 50)),
    ColorButton(image_base=pygame.image.load("assets/yellow.png"), image_flotante = pygame.image.load("assets/yellow_flotante.png"), pos=(1130, 350), color=Color.YELLOW.value, size=(50, 50)),
]

# Botones de deshacer y rehacer
n = 80
DESHACER = ColorButton(image_base=pygame.image.load("assets/deshacer.png"), image_flotante = pygame.image.load("assets/deshacer.png"), pos=(1050, 460), color=None, size=(n, n))
REHACER = ColorButton(image_base=pygame.image.load("assets/rehacer.png"), image_flotante = pygame.image.load("assets/rehacer.png"), pos=(1150, 460), color=None, size=(n, n))

# Clase que se encarga de la creación de un nonograma, proporcionando las herramientas necesarias
class GestorCreacion:
    def __init__(self, tamañoTablero):
        self.tamañoTablero = tamañoTablero
        self.tamañoCasilla =  math.floor((-25*tamañoTablero)/10 + 75)
        self.tableroObjetivo = Tablero(tamañoTablero, self.tamañoCasilla)
        self.text_box = None  # Inicializa el cuadro de texto
        self.estado = False #Estado para finalizar creacion de nonograma

    # Metodo que crea y retorna un "memento" con el estado actual del tableroObjetivo
    def guardar_estado(self):
        m = mementoCreacion(self.tableroObjetivo)
        print("Guardado")
        return m

    # Metodo que restaura el estado de self.tableroObjetivo usando un memento pasado como parámetro
    def cargar_estado(self, memento):
        tablero_cargado = memento.get_state()
        if isinstance(tablero_cargado, tuple):
            self.tableroObjetivo = tablero_cargado[0]  # Si es una tupla, tomar el primer elemento
        else:
            self.tableroObjetivo = tablero_cargado
        print("Cargado")

    # Metodo que verifica si el clic se encuentra dentro del tablero
    def es_clic_valido(self, pos) -> bool:
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

    # Dibuja los elementos en pantalla
    def draw(self, screen):
        for boton in color_buttons:
            boton.draw(screen)

        DESHACER.draw(screen)
        REHACER.draw(screen)

        desfase_x = 300
        desfase_y = 165
        self.tableroObjetivo.dibujar(screen, desfase_x, desfase_y)
        # Dibuja el cuadro de texto si está inicializado
        if self.text_box:
            self.text_box.draw()

    # Maneja los eventos de teclado y mouse
    def handle_events(self, event, caretaker):

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

