import pygame, sys
from button import Button
from GestorJuego import GestorJuego
from GestorCreacion import GestorCreacion
from caretaker import Caretaker
from vidas import HP_counter
from text_box import Text_box
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nonograma")

BG = pygame.image.load("assets/Background.png")

class ScrollBar:
    def __init__(self, x, y, width, height, total_items, item_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.total_items = total_items
        self.item_height = item_height
        self.visible_items = height // item_height
        self.scroll_ratio = self.visible_items / total_items if total_items > 0 else 0
        self.scroll_position = 0

    def draw(self, screen):
        # Dibuja la barra de desplazamiento
        pygame.draw.rect(screen, (200, 200, 200), self.rect)  # Fondo de la barra
        if self.scroll_ratio < 1:
            scroll_height = int(self.rect.height * self.scroll_ratio)
            scroll_y = int(self.scroll_position * self.scroll_ratio)
            scroll_rect = pygame.Rect(self.rect.x, self.rect.y + scroll_y, self.rect.width, scroll_height)
            pygame.draw.rect(screen, (100, 100, 100), scroll_rect)  # Barra de desplazamiento

    def update(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0]:  # Si el botón izquierdo del mouse está presionado
                mouse_y = mouse_pos[1] - self.rect.y
                self.scroll_position = max(0, min(mouse_y / self.rect.height * self.total_items, self.total_items - self.visible_items))

    def get_scroll_offset(self):
        return int(self.scroll_position)


def get_font(size) -> pygame.font.Font:
    return pygame.font.Font("assets/font.ttf", size)

#Menú para continuar jugando
def continuar_partida():
    gestor_juego = GestorJuego(10) # Crear un gestor de juego con el tamaño del nonograma seleccionado
    caretaker = Caretaker(gestor_juego)
    caretaker.cargarPartida()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        PLAY_TEXT = get_font(45).render("Nonograma", True, "White") # Titulo
        PLAY_RECT = PLAY_TEXT.get_rect(midtop=(640, 100)) # Posicion del titulo
        SCREEN.blit(PLAY_TEXT, PLAY_RECT) # Dibujar el titulo en la pantalla

        # A continuación los botones para esta ventana
        PLAY_BACK = Button(image=None, pos=(1100, 460),
                           text_input="BACK", font=get_font(75), base_color="Black", color_flotante="Green")

        # Cambiar el color del boton si el mouse esta encima
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Un manejador de eventos para los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            gestor_juego.handle_events(event, caretaker)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                # Dibujar el tablero de juego en la pantalla
        if not gestor_juego.contadorVidas.alive():
            caretaker.borrarPartida()
            main_menu()
        if gestor_juego.nonogramaFinalizado():
            caretaker.borrarPartida()
            win()

        gestor_juego.draw(SCREEN)
        pygame.display.update() #

# Ventana donde se muestra el nonograma
def play(tamaño, ruta_nonograma):
    gestor_juego = GestorJuego(tamaño) # Crear un gestor de juego con el tamaño del nonograma seleccionado
    if True:  # TODO: reemplazar por logica de "si se va a jugar con vidas"
        cantidad_vidas = 3
        vidas = HP_counter(cantidad_vidas)
        gestor_juego.contadorVidas = vidas
        gestor_juego.numVidas = vidas.lives
    caretaker = Caretaker(gestor_juego)
    caretaker.cargarObjetivo(ruta_nonograma)

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        PLAY_TEXT = get_font(45).render("Nonograma", True, "White") # Titulo
        PLAY_RECT = PLAY_TEXT.get_rect(midtop=(640, 100)) # Posicion del titulo
        SCREEN.blit(PLAY_TEXT, PLAY_RECT) # Dibujar el titulo en la pantalla

        # A continuación los botones para esta ventana
        PLAY_BACK = Button(image=None, pos=(1100, 460),
                           text_input="BACK", font=get_font(75), base_color="Black", color_flotante="Green")

        # Cambiar el color del boton si el mouse esta encima
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Un manejador de eventos para los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            gestor_juego.handle_events(event, caretaker)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                # Dibujar el tablero de juego en la pantalla
        if not gestor_juego.contadorVidas.alive():
            caretaker.borrarPartida()
            main_menu()
        if gestor_juego.nonogramaFinalizado():
            caretaker.borrarPartida()
            win()

        gestor_juego.draw(SCREEN)
        pygame.display.update() #
def win():
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        WIN_TEXT = get_font(45).render("Ganaste", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        WIN_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", color_flotante="Green")

        for button in [WIN_BACK]:
            button.changeColor(WIN_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Ventana donde se muestra el tutorial
def tutorial():
    while True:
        TUTORIAL_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        TUTORIAL_TEXT = get_font(45).render("Tutorial", True, "White")
        TUTORIAL_RECT = TUTORIAL_TEXT.get_rect(midtop=(640, 100))
        SCREEN.blit(TUTORIAL_TEXT, TUTORIAL_RECT)

        TUTORIAL_BACK = Button(image=None, pos=(640, 460),
                               text_input="BACK", font=get_font(75), base_color="White", color_flotante="Green")
        TUTORIAL_PLAY = Button(image=None, pos=(640, 560),
                               text_input="IR A JUGAR", font=get_font(75), base_color="White", color_flotante="Green")
        TUTORIAL_CREACION = Button(image=None, pos=(640, 660),
                                 text_input="IR A CREACION", font=get_font(75), base_color="White", color_flotante="Green")

        for button in [TUTORIAL_BACK, TUTORIAL_PLAY, TUTORIAL_CREACION]:
            button.changeColor(TUTORIAL_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BACK.checkForInput(TUTORIAL_MOUSE_POS):
                    main_menu()
                if TUTORIAL_PLAY.checkForInput(TUTORIAL_MOUSE_POS):
                    catalogo()
                if TUTORIAL_CREACION.checkForInput(TUTORIAL_MOUSE_POS):
                    creacion()

        pygame.display.update()

def elegir_tamaño_creacion():
    while True:
        ELEGIR_TAMAÑO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        ELEGIR_TAMAÑO_TEXT = get_font(45).render("Elegir Tamaño", True, "White")
        ELEGIR_TAMAÑO_RECT = ELEGIR_TAMAÑO_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(ELEGIR_TAMAÑO_TEXT, ELEGIR_TAMAÑO_RECT)

        TAMAÑO_10 = Button(image=None, pos=(640, 260),
                           text_input="10 x 10", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_15 = Button(image=None, pos=(640, 360),
                           text_input="15 x 15", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_20 = Button(image=None, pos=(640, 460),
                           text_input="20 x 20", font=get_font(60), base_color="White", color_flotante="Green")
        ELEGIR_TAMAÑO_BACK = Button(image=None, pos=(640, 560),
                               text_input="BACK", font=get_font(60), base_color="White", color_flotante="Green")

        for button in [TAMAÑO_10, TAMAÑO_15, TAMAÑO_20, ELEGIR_TAMAÑO_BACK]:
            button.changeColor(ELEGIR_TAMAÑO_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ELEGIR_TAMAÑO_BACK.checkForInput(ELEGIR_TAMAÑO_MOUSE_POS):
                    main_menu()
                if TAMAÑO_10.checkForInput(ELEGIR_TAMAÑO_MOUSE_POS):
                    creacion(10)
                if TAMAÑO_15.checkForInput(ELEGIR_TAMAÑO_MOUSE_POS):
                    creacion(15)
                if TAMAÑO_20.checkForInput(ELEGIR_TAMAÑO_MOUSE_POS):
                    creacion(20)

        pygame.display.update()

# Ventana donde el usuario podrá crear su propio nonograma
def creacion(tamañoTablero):
    gestor_creacion = GestorCreacion(tamañoTablero)
    caretaker = Caretaker(gestor_creacion)

    while True:
        CREACION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        CREACION_TEXT = get_font(45).render("Creacion", True, "White")
        CREACION_RECT = CREACION_TEXT.get_rect(midtop=(640, 100))
        SCREEN.blit(CREACION_TEXT, CREACION_RECT)

        CREACION_BACK = Button(image=None, pos=(1100, 560),
                           text_input="BACK", font=get_font(50), base_color="Black", color_flotante="Green")

        CREACION_GUARDAR = Button(image=None, pos=(1050, 660),
                           text_input="GUARDAR", font=get_font(50), base_color="Black", color_flotante="Green")

        for button in [CREACION_BACK, CREACION_GUARDAR]:
            button.changeColor(CREACION_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            gestor_creacion.handle_events(event, caretaker)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREACION_BACK.checkForInput(CREACION_MOUSE_POS):
                    main_menu()
                # Poner un condicional de que pasaria si se presiona el boton de guardar
                if CREACION_GUARDAR.checkForInput(CREACION_MOUSE_POS):
                    gestor_creacion.text_box = Text_box(SCREEN)

            if gestor_creacion.estado == True:
                main_menu()
        gestor_creacion.draw(SCREEN)
        pygame.display.update()

# Ventana donde se muestra el catálogo de nonogramas
def catalogo():
    while True:
        CATALOGO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")


        CATALOGO_TEXT = get_font(45).render("Catalogo", True, "White")
        CATALOGO_RECT = CATALOGO_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(CATALOGO_TEXT, CATALOGO_RECT)

        # Botones para los diferentes tamaños
        TAMAÑO_10 = Button(image=None, pos=(640, 260),
                           text_input="10 x 10", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_15 = Button(image=None, pos=(640, 360),
                           text_input="15 x 15", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_20 = Button(image=None, pos=(640, 460),
                           text_input="20 x 20", font=get_font(60), base_color="White", color_flotante="Green")
        CATALOGO_BACK = Button(image=None, pos=(640, 560),
                               text_input="BACK", font=get_font(60), base_color="White", color_flotante="Green")
        #CATALOGO_PLAY = Button(image=None, pos=(640, 560),
                              # text_input="JUGAR", font=get_font(75), base_color="White", color_flotante="Green")

        # Cambiar el color del boton si el mouse esta encima
        for button in [TAMAÑO_10, TAMAÑO_15, TAMAÑO_20, CATALOGO_BACK]:
            button.changeColor(CATALOGO_MOUSE_POS)
            button.update(SCREEN)

        # Un manejador de eventos para los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CATALOGO_BACK.checkForInput(CATALOGO_MOUSE_POS):
                    main_menu()
                #if CATALOGO_PLAY.checkForInput(CATALOGO_MOUSE_POS):
                    #play()
                if TAMAÑO_10.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("10x10")
                if TAMAÑO_15.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("15x15")
                if TAMAÑO_20.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("20x20")
        pygame.display.update()

def mostrar_nonogramas(tamaño):
    import os
    tamaño_int = int(tamaño.split('x')[0])  # Se extrae el tamaño del nonograma
    # Ruta al directorio de catálogo para el tamaño seleccionado
    ruta_catalogo = os.path.join("catalogo", tamaño)

    # Obtener lista de nonogramas disponibles
    try:
        nonogramas = [f for f in os.listdir(ruta_catalogo) if f.endswith('.pkl')]
    except FileNotFoundError:
        nonogramas = []

    scrollbar = ScrollBar(1100, 150, 20, 500, len(nonogramas), 60)  # Ajusta la posición y tamaño de la barra

    while True:
        SCREEN.fill("black")

        # Título
        TITULO = get_font(45).render(f"Nonogramas {tamaño}", True, "White")
        TITULO_RECT = TITULO.get_rect(center=(640, 50))
        SCREEN.blit(TITULO, TITULO_RECT)

        # Mostrar lista de nonogramas
        y_pos = 150 - scrollbar.get_scroll_offset() * 60  # Ajusta la posición de los botones según el desplazamiento
        botones_nonogramas = []
        for i, nonograma in enumerate(nonogramas):
            if i >= scrollbar.get_scroll_offset() and i < scrollbar.get_scroll_offset() + 8:  # Muestra solo 8 nonogramas a la vez
                nombre = nonograma.replace('.pkl', '')
                boton = Button(image=None, pos=(640, y_pos),
                               text_input=nombre, font=get_font(35),
                               base_color="White", color_flotante="Green")
                botones_nonogramas.append(boton)
                y_pos += 60

        BACK = Button(image=None, pos=(640, 660),
                      text_input="BACK", font=get_font(75),
                      base_color="White", color_flotante="Green")

        MOUSE_POS = pygame.mouse.get_pos()

        for boton in botones_nonogramas + [BACK]:
            boton.changeColor(MOUSE_POS)
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    catalogo()
                for i, boton in enumerate(botones_nonogramas):
                    if boton.checkForInput(MOUSE_POS):
                        # Aquí cargarías el nonograma seleccionado
                        ruta_nonograma = os.path.join(ruta_catalogo, nonogramas[i])
                        play(tamaño_int, ruta_nonograma)

        scrollbar.update(MOUSE_POS, pygame.mouse.get_pressed())  # Actualiza la barra deslizable
        scrollbar.draw(SCREEN)  # Dibuja la barra deslizable

        pygame.display.update()
# Ventana principal del menú, la primera en mostrarse
def main_menu():
    import os
    while True:
        SCREEN.blit(BG, (0, 0)) # Fondo de pantalla

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("NONOGRAMA", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        saved_game_exists = os.path.exists('guardadoPartida/partidaGuardada.pkl')

        # A continuación los botones para esta ventana (cuatro botones)
        #PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", color_flotante="White")
        if saved_game_exists:
            CONTINUAR_BUTTON = Button(image=None, pos=(640, 250),
                                      text_input="CONTINUAR", font=get_font(50), base_color="#d7fcd4",
                                      color_flotante="White")

        CATALOGO_BUTTON = Button(image=None, pos=(640, 350),
                                 text_input="JUGAR", font=get_font(50), base_color="#d7fcd4", color_flotante="White")

        CREACION_BUTTON = Button(image=None, pos=(640, 450),
                                 text_input="CREACION", font=get_font(50), base_color="#d7fcd4", color_flotante="White")


        TUTORIAL_BUTTON = Button(image=None, pos=(640, 550),
                                 text_input="TUTORIAL", font=get_font(50), base_color="#d7fcd4", color_flotante="White")
        QUIT_BUTTON = Button(image=None, pos=(640, 650),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", color_flotante="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT) # Dibujar el titulo en la pantalla

        # Cambiar el color del boton si el mouse esta encima
        buttons = [CATALOGO_BUTTON, TUTORIAL_BUTTON, CREACION_BUTTON, QUIT_BUTTON]
        if saved_game_exists:
            buttons.append(CONTINUAR_BUTTON)

        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Un manejador de eventos para los botones (se realizan las "transiciones")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if saved_game_exists and CONTINUAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    continuar_partida()
                if CATALOGO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    catalogo()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tutorial()
                if CREACION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    elegir_tamaño_creacion()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()