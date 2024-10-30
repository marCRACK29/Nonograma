from aptdaemon.logger import WHITE
from pygame import MOUSEBUTTONDOWN
from src.memento import mementoJuego, mementoCreacion
from src.tablero import Tablero
from src.Color import Color
from src.Proxy import Proxy
import pygame

class GestorJuego:

    def __init__(self, tamañoTablero, tamañoCasilla):
        self.numeritosFilas = []
        self.numeritosColumnas = []
        self.tamañoTablero = tamañoTablero
        self.tableroObjetivo = Tablero(tamañoTablero, tamañoCasilla)
        self.tableroJugador = Tablero(tamañoTablero, tamañoCasilla)

    def guardar_estado(self):
        m = mementoJuego(self.tableroJugador, self.tableroObjetivo)
        print("Creando mementoJuego")
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
        self.print_numeritos()

    #Metodo solo para verificar pistas numericas de filas y columnas, una vez implementadas las pistas de forma gráfica quitar este metodo
    def print_numeritos(self):
        self.pistasFilas()
        self.pistasColumnas()
        print("\n=== Numeritos de las Filas ===")
        for i, columna in enumerate(self.numeritosFilas):
            print(f"Fila {i}:", end=" ")
            if columna:
                for valor in columna:
                    print(valor, end=" ")
            else:
                print("vacía", end="")
            print()  # Nueva línea después de cada columna
        print("===============================\n")
        print("\n=== Numeritos de las Columnas ===")
        for i, columna in enumerate(self.numeritosColumnas):
            print(f"Columna {i}:", end=" ")
            if columna:
                for valor in columna:
                    print(valor, end=" ")
            else:
                print("vacía", end="")
            print()  # Nueva línea después de cada columna
        print("===============================\n")

    #Metodo que pinta una casilla correcta para ayudar al jugador
    def ayuda(self):
        for i in range(self.tamañoTablero):
            for j in range(self.tamañoTablero):
                C1 = self.tableroObjetivo.getCasillas()[i][j].get_color()
                C2 =self.tableroJugador.getCasillas()[i][j].get_color()
                if (C1 != Color.WHITE.value and C2 == Color.WHITE.value):
                    self.tableroJugador.getCasillas()[i][j].set_color(C1)
                    break

    #Método que verifica que la ultima casilla pintada haya sido correcta
    def comprobar(self, i, j, color):
        colorJugador = color
        colorObjetivo = self.tableroObjetivo.getCasillas()[i][j].get_color()
        if(colorJugador == colorObjetivo):
            print ("Correcto") #print de prueba
        else :
            print ("Incorrecto") #print de prueba

    #Metodo para determinar pistas numéricas paras las filas dado un nonograma Objetivo
    def pistasFilas(self):
        casillas = self.tableroObjetivo.getCasillas()
        numeritosFilas = [] #Arreglo que almacenará todas las pistas numéricas de filas
        for columna in range(self.tamañoTablero):
            datos_aux = [] #Arreglo que almacenará los pares (cantidad, color) presentes en la columna dada
            color_actual = Color.WHITE.value #Color actual
            contador = 0  # Contador para la secuencia actual
            datos_contador = 0  # Contador para el índice de datos en datos_aux
            for fila in range (self.tamañoTablero):
                color_casilla = casillas[fila][columna].get_color()
                # Si el color cambia
                if color_actual != color_casilla:
                    # Si veníamos contando un color no blanco
                    if color_actual != Color.WHITE.value:
                        datos_aux.append([contador, color_actual])
                        datos_contador += 1

                    # Si el nuevo color no es blanco, empezamos a contar
                    if color_casilla != Color.WHITE.value:
                        contador = 1
                        color_actual = color_casilla
                    else:
                        contador = 0
                        color_actual = Color.WHITE.value

                # Si el color es el mismo y no es blanco
                elif color_casilla != Color.WHITE.value:
                    contador += 1
                    # No olvidar la última secuencia si termina con color
            if contador > 0 and color_actual != Color.WHITE.value:
                datos_aux.append([contador, color_actual])
            numeritosFilas.append(datos_aux)
        self.numeritosFilas = numeritosFilas #Se guarda como valor de clase

    def pistasColumnas(self):
        casillas = self.tableroObjetivo.getCasillas()
        numeritosColumnas = []  # Arreglo que almacenará todas las pistas numéricas de columnas
        for fila in range(self.tamañoTablero):
            datos_aux = []  # Arreglo que almacenará los pares (cantidad, color) presentes en la fila dada
            color_actual = Color.WHITE.value  # Color actual
            contador = 0  # Contador para la secuencia actual
            datos_contador = 0  # Contador para el índice de datos en datos_aux
            for columna in range(self.tamañoTablero):
                color_casilla = casillas[fila][columna].get_color()
                # Si el color cambia
                if color_actual != color_casilla:
                    # Si veníamos contando un color no blanco
                    if color_actual != Color.WHITE.value:
                        datos_aux.append([contador, color_actual])
                        datos_contador += 1

                    # Si el nuevo color no es blanco, empezamos a contar
                    if color_casilla != Color.WHITE.value:
                        contador = 1
                        color_actual = color_casilla
                    else:
                        contador = 0
                        color_actual = Color.WHITE.value

                # Si el color es el mismo y no es blanco
                elif color_casilla != Color.WHITE.value:
                    contador += 1
                    # No olvidar la última secuencia si termina con color
            if contador > 0 and color_actual != Color.WHITE.value:
                datos_aux.append([contador, color_actual])
            numeritosColumnas.append(datos_aux)
        self.numeritosColumnas = numeritosColumnas #Se guarda como valor de la clase



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
            elif event.key == pygame.K_1:
                Proxy.set_color(Color.BLACK)
            elif event.key == pygame.K_2:
                Proxy.set_color(Color.RED)
            elif event.key == pygame.K_3:
                Proxy.set_color(Color.YELLOW)
            elif event.key == pygame.K_4:
                Proxy.set_color(Color.PINK)
            elif event.key == pygame.K_5:
                Proxy.set_color(Color.BLUE)
        self.tableroJugador.manejar_evento(event)
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