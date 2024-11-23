import math

from pygame import MOUSEBUTTONDOWN

from colorbutton import colorbutton
from memento import mementoJuego, mementoCreacion
from tablero import Tablero
from Color import Color
from Proxy import Proxy
import pygame

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
DESHACER = colorbutton(image_base=pygame.image.load("assets/deshacer.png"), image_flotante = pygame.image.load("assets/deshacer.png"),pos=(1050, 600), color=None, size=(n, n))
REHACER = colorbutton(image_base=pygame.image.load("assets/rehacer.png"), image_flotante = pygame.image.load("assets/rehacer.png"),pos=(1150, 600), color=None, size=(n, n))

class GestorJuego:

    def __init__(self, tamañoTablero):
        self.numeritosFilas = []
        self.numeritosColumnas = []
        self.tamañoTablero = tamañoTablero
        self.tamañoCasilla = math.floor((-25*tamañoTablero)/10 + 75)
        self.tableroObjetivo = Tablero(tamañoTablero, self.tamañoCasilla )
        self.tableroJugador = Tablero(tamañoTablero, self.tamañoCasilla)
        self.ayudas = None
        self.contadorVidas = None #contador de vidas se setea externamente si se va a jugar con vidas, es un HP_counter
        self.numVidas = None #numero de vidas iniciales, es un entero

    def nonogramaFinalizado(self):
        for i in range(self.tamañoTablero):
            for j in range(self.tamañoTablero):
                color_objetivo = self.tableroObjetivo.getCasillas()[i][j].get_color()
                color_jugador = self.tableroJugador.getCasillas()[i][j].get_color()
                if color_objetivo != color_jugador:
                    return False
        return True

    def setearAyudas(self, ayudas):
        if self.ayudas is None:
            self.ayudas = ayudas
        else:
            pass


    def guardar_estado(self):
        m = mementoJuego(self.tableroJugador, self.tableroObjetivo, self.contadorVidas.lives, self.ayudas)
        #print("Creando mementoJuego")
        return m

    def cargar_estado(self, memento):
        tableros_cargados = memento.get_state()
        if isinstance(tableros_cargados, tuple):
            self.tableroJugador = tableros_cargados[0]  # Si es una tupla, tomar el primer elemento
            self.tableroObjetivo = tableros_cargados[1]  # Si es una tupla, tomar el segundo elemento
        else:
            self.tableroJugador = tableros_cargados[0]
            self.tableroObjetivo = tableros_cargados[1]
        print("Cargado")
        self.setearAyudas(tableros_cargados[3])
        self.tamañoTablero = self.tableroObjetivo.tamaño
        self.tamañoCasilla = self.tableroJugador.tamañoCasilla


    #Metodo que permite cargar un tablero objetivo usando un mementoCreacion
    def cargar_objetivo(self, memento):
        tablero_cargado = memento.get_state()
        if isinstance(tablero_cargado, tuple):
            self.tableroObjetivo = tablero_cargado[0]  # Si es una tupla, tomar el primer elemento
        else:
            self.tableroObjetivo = tablero_cargado
        self.pistasColumnas()
        self.pistasFilas()
        self.setearAyudas(3)

    #Metodo que pinta una casilla correcta para ayudar al jugador
    def ayuda(self):
        for i in range(self.tamañoTablero):
            for j in range(self.tamañoTablero):
                color_objetivo = self.tableroObjetivo.getCasillas()[i][j].get_color()
                color_jugador = self.tableroJugador.getCasillas()[i][j].get_color()
                if color_objetivo != Color.WHITE.value and color_jugador == Color.WHITE.value:
                    self.tableroJugador.getCasillas()[i][j].set_color(color_objetivo)
                    return

    #Metodo que verifica que la última casilla pintada haya sido correcta
    def comprobar(self, i, j, color):
        colorJugador = color
        colorObjetivo = self.tableroObjetivo.getCasillas()[i][j].get_color()
        if(colorJugador == colorObjetivo):
            print ("Correcto") #print de prueba
        else :
            print ("Incorrecto") #print de prueba
            if self.contadorVidas is not None:
                self.contadorVidas.loseLife()

    #Metodo para determinar pistas numéricas paras las filas dado un nonograma Objetivo
    def pistasFilas(self):
        casillas = self.tableroObjetivo.getCasillas() #obtiene una lista de casillas del tablero objetivo.
        numeritosFilas = [] # crea una lista para almacenar secuencias de color y tamaño para cada fila.
        for columna in range(self.tamañoTablero): # Itera sobre cada columna del tablero
            pfila = [] # una lista temporal para almacenar las secuencias de colores y sus longitudes en la columna.
            color_actual = Color.WHITE.value #Color actual
            contador = 0  # cuenta la longitud de la secuencia de colores actuales.
            for fila in range (self.tamañoTablero): # se itera sobre cada fila de la columna actual
                color_casilla = casillas[fila][columna].get_color() #obtiene el color de la casilla actual
                # Si el color cambia y el color previo no era blanco, guarda la secuencia
                if color_actual != color_casilla:
                    if color_actual != Color.WHITE.value:
                        pfila.append([contador, color_actual])
                    #reinicia el contador o continúa según el nuevo color
                    contador = 1 if color_casilla != Color.WHITE.value else 0
                    color_actual = color_casilla
                elif color_casilla != Color.WHITE.value:
                    contador += 1

            if contador > 0 and color_actual != Color.WHITE.value:
                pfila.append([contador, color_actual])
            numeritosFilas.append(pfila)
        self.numeritosFilas = numeritosFilas #Se guarda como valor de clase

    def pistasColumnas(self):
        casillas = self.tableroObjetivo.getCasillas()
        numeritosColumnas = []  # Arreglo que almacenará todas las pistas numéricas de columnas
        for fila in range(self.tamañoTablero):
            datos_aux = []  # Arreglo que almacenará los pares (cantidad, color) presentes en la fila dada
            color_actual = Color.WHITE.value  # Color actual
            contador = 0  # Contador para la secuencia actual
            for columna in range(self.tamañoTablero):
                color_casilla = casillas[fila][columna].get_color()
                # Si el color cambia
                if color_actual != color_casilla:
                    if color_actual != Color.WHITE.value:
                        datos_aux.append([contador, color_actual])

                    contador = 1 if color_casilla != Color.WHITE.value else 0
                    color_actual = color_casilla
                elif color_casilla != Color.WHITE.value:
                    contador += 1

            # No olvidar la última secuencia si termina con color
            if contador > 0 and color_actual != Color.WHITE.value:
                datos_aux.append([contador, color_actual])
            numeritosColumnas.append(datos_aux)
        self.numeritosColumnas = numeritosColumnas #Se guarda como valor de la clase

    def draw(self, screen):
        for boton in color_buttons:
            boton.draw(screen)
        DESHACER.draw(screen)
        REHACER.draw(screen)

        tamañoCasilla = self.tamañoCasilla
        desfase_x = 300
        desfase_y = 165
        fuente = pygame.font.Font(None, 20)
        for col, pistas in enumerate(self.numeritosColumnas):
            y_pos = desfase_y- 20  # Empezamos arriba del tablero
            x_pos = desfase_x + (col * tamañoCasilla) + (tamañoCasilla // 2)
            for pista in reversed(pistas):  # Reversed para que se apilen hacia arriba
                cantidad = str(pista[0])
                color = pista[1]
                text = fuente.render(cantidad, True, color)
                text_rect = text.get_rect(center=(x_pos, y_pos))
                screen.blit(text, text_rect)
                y_pos -= 20  # Movemos hacia arriba para la siguiente pista

        # Dibujar pistas de filas (izquierda del tablero)
        for fila, pistas in enumerate(self.numeritosFilas):
            x_pos = desfase_x - 20  # Empezamos a la izquierda del tablero
            y_pos = desfase_y + (fila * tamañoCasilla) + (tamañoCasilla // 2)
            for pista in reversed(pistas):  # Reversed para que se alineen de derecha a izquierda
                cantidad = str(pista[0])
                color = pista[1]
                text = fuente.render(cantidad, True, color)
                text_rect = text.get_rect(center=(x_pos, y_pos))
                screen.blit(text, text_rect)
                x_pos -= 20  # Movemos hacia la izquierda para la siguiente pista

        self.tableroJugador.dibujar(screen, desfase_x, desfase_y)  # Dibuja el tablero del jugador
        if self.contadorVidas is not None:
            self.contadorVidas.draw(screen)

        # Dibujar la cantidad de ayudas disponibles
        ayudas_text = f"Ayudas disponibles: {self.ayudas}"
        ayudas_render = fuente.render(ayudas_text, True, (0, 0, 0))  # Color negro
        screen.blit(ayudas_render, (900, desfase_y - 50))  # Posición encima del tablero

    def handle_events(self, event, caretaker):
        #Manejar eventos de teclado y mouse
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for boton in color_buttons:
                    if boton.checkForInput(event.pos):
                        Proxy.set_color(boton.get_color())
                        break
                caretaker.añadirMemento()
                self.tableroJugador.manejar_evento(event, Proxy.get_color())

                if DESHACER.checkForInput(event.pos):
                    caretaker.deshacer()
                if REHACER.checkForInput(event.pos):
                    caretaker.rehacer();

            elif event.button == 3:  # Click derecho
                caretaker.añadirMemento()
                self.tableroJugador.manejar_evento(event, Color.WHITE.value)
        if event.type == pygame.KEYDOWN:
            """if event.key == pygame.K_d:
                caretaker.deshacer()
            elif event.key == pygame.K_r:
                caretaker.rehacer()"""
            if event.key == pygame.K_a:
                if self.ayudas > 0:
                    caretaker.añadirMemento()
                    self.ayudas = self.ayudas - 1
                    self.ayuda()
                else:
                    print("No hay más ayudas")

            elif event.key == pygame.K_l:
                caretaker.cargarPartida()

        if event.type == pygame.USEREVENT:
            self.comprobar(event.fila, event.columna, event.color)


"""
def main():
    from src.caretaker import Caretaker
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("gestor")

    gestor = GestorJuego(10, 50)
    caretaker = Caretaker(gestor)
    caretaker.cargarObjetivo()  # Cargar el tablero objetivo al inicio

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