import pygame, sys, os

from math import ceil
from button import Button
from GestorJuego import GestorJuego
from GestorCreacion import GestorCreacion
from caretaker import Caretaker
from vidas import HP_counter
from text_box import Text_box

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720)) # Tamaño de la ventana
pygame.display.set_caption("Nonograma") # Título de la ventana

BG = pygame.image.load("assets/Background.png")

# Función para cargar la fuente personalizada que se muestra en el juego
def get_font(size) -> pygame.font.Font:
    return pygame.font.Font("assets/font.ttf", size)

# Menú para continuar jugando
def continuar_partida():
    gestor_juego = GestorJuego(10) # Crear un gestor de juego con el tamaño del nonograma seleccionado
    caretaker = Caretaker(gestor_juego)
    caretaker.cargarPartida()

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        # A continuación los botones para esta ventana
        PLAY_BACK = Button(image=None, pos=(1100, 600),
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

# Ventana donde se muestra el nonograma en blanco para jugarlo
def play(tamaño, ruta_nonograma):
    gestor_juego = GestorJuego(tamaño) # Crear un gestor de juego con el tamaño del nonograma seleccionado
    if True:
        cantidad_vidas = ceil(tamaño / 2) # Calcular la cantidad de vidas según el tamaño del nonograma
        vidas = HP_counter(cantidad_vidas)
        gestor_juego.contadorVidas = vidas
        gestor_juego.numVidas = vidas.lives
    caretaker = Caretaker(gestor_juego)
    caretaker.cargarObjetivo(ruta_nonograma)

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos() # Variable para obtener la posición del mouse

        SCREEN.fill("White") # Fondo de la pantalla

        # A continuación los botones para esta ventana
        PLAY_BACK = Button(image=None, pos=(1100, 600),
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
            sin_vidas(tamaño, ruta_nonograma) # Mostrar ventana de perder
        if gestor_juego.nonogramaFinalizado():
            caretaker.borrarPartida()
            win() # Mostrar ventana de ganar

        gestor_juego.draw(SCREEN)
        pygame.display.update() #

# Ventana que se muestra al completar un nonograma
def win():
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        WIN_TEXT = get_font(45).render("Ganaste", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        WIN_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", color_flotante="Green")


        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Cargar el contenido del tutorial
def cargar_contenido_tutorial():
    with open("tutorial_text.txt",'r',encoding='utf-8') as file:
        content = file.read()
        pages = [page.strip().split('</title>', 1) for page in content.split("</page>")]
        return pages

# Ventana donde se muestra el tutorial
def tutorial():
    # Botones para navegar entre páginas
    FLECHA_IZQUIERDA = Button(image=None, pos=(100, 360),
                              text_input="<", font=get_font(75),
                              base_color="White", color_flotante="Green")
    FLECHA_DERECHA = Button(image=None, pos=(1180, 360),
                            text_input=">", font=get_font(75),
                            base_color="White", color_flotante="Green")

    TUTORIAL_BACK = Button(image=None, pos=(640, 580),
                           text_input="BACK", font=get_font(35), base_color="White", color_flotante="Green")
    TUTORIAL_PLAY = Button(image=None, pos=(640, 620),
                           text_input="IR A JUGAR", font=get_font(35), base_color="White", color_flotante="Green")
    TUTORIAL_CREACION = Button(image=None, pos=(640, 660),
                               text_input="IR A CREACION", font=get_font(35), base_color="White",
                               color_flotante="Green")

    pagina_actual = 0
    #paginas_tutorial estan guardadas de la forma [[titulo1,contenido1],[titulo2,contenido2]...etc]
    paginas_tutorial = cargar_contenido_tutorial()

    while True:
        TUTORIAL_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        TUTORIAL_TITLE = get_font(40).render(paginas_tutorial[pagina_actual][0], True, "White")
        TUTORIAL_RECT = TUTORIAL_TITLE.get_rect(midtop=(640, 30))

        TUTORIAL_TITLE_BODY_TEXT = get_font(25).render(paginas_tutorial[pagina_actual][1], True, "White")
        TUTORIAL_RECT_BODY = TUTORIAL_TITLE.get_rect(topleft=(200, 100))

        SCREEN.blit(TUTORIAL_TITLE, TUTORIAL_RECT)
        SCREEN.blit(TUTORIAL_TITLE_BODY_TEXT, TUTORIAL_RECT_BODY)

        for button in [TUTORIAL_BACK, TUTORIAL_PLAY, TUTORIAL_CREACION]:
            button.changeColor(TUTORIAL_MOUSE_POS)
            button.update(SCREEN)

        if pagina_actual != 0:
            FLECHA_IZQUIERDA.changeColor(TUTORIAL_MOUSE_POS)
            FLECHA_IZQUIERDA.update(SCREEN)

        if pagina_actual != len(paginas_tutorial)-1:
            FLECHA_DERECHA.changeColor(TUTORIAL_MOUSE_POS)
            FLECHA_DERECHA.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Redireccionar a la pagina correspondiente
                if TUTORIAL_BACK.checkForInput(TUTORIAL_MOUSE_POS):
                    main_menu()
                if TUTORIAL_PLAY.checkForInput(TUTORIAL_MOUSE_POS):
                    catalogo()
                if TUTORIAL_CREACION.checkForInput(TUTORIAL_MOUSE_POS):
                    elegir_tamaño_creacion()
                if FLECHA_IZQUIERDA.checkForInput(TUTORIAL_MOUSE_POS):
                    pagina_actual -= 1
                    if pagina_actual<0: pagina_actual += 1
                if FLECHA_DERECHA.checkForInput(TUTORIAL_MOUSE_POS):
                    pagina_actual += 1
                    if pagina_actual >= len(paginas_tutorial): pagina_actual -= 1

        pygame.display.update()

# Ventana donde el usuario podrá elegir el tamaño del nonograma que desea crear
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
            if event.type == pygame.MOUSEBUTTONDOWN: # Redireccionar a la pagina correspondiente
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
    gestor_creacion = GestorCreacion(tamañoTablero) # Crear un gestor de creación con el tamaño del nonograma seleccionado
    caretaker = Caretaker(gestor_creacion) # Crear un caretaker para guardar los mementos
    caretaker.añadirMemento() # Añadir un memento al caretaker

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
                if TAMAÑO_10.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("10x10")
                if TAMAÑO_15.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("15x15")
                if TAMAÑO_20.checkForInput(CATALOGO_MOUSE_POS):
                    mostrar_nonogramas("20x20")
        pygame.display.update()

# Ventana donde se muestra la lista de nonogramas disponibles para jugar acorde al tamaño
def mostrar_nonogramas(tamaño):
    tamaño_int = int(tamaño.split('x')[0])  # Se extrae el tamaño del nonograma
    # Ruta al directorio de catálogo para el tamaño seleccionado
    ruta_catalogo = os.path.join("catalogo", tamaño)

    # Obtener lista de nonogramas disponibles
    try:
        nonogramas = [f for f in os.listdir(ruta_catalogo) if f.endswith('.pkl')]
    except FileNotFoundError:
        nonogramas = []

    pagina_actual = 0
    items_por_pagina = 8  # Número de nonogramas por página

    while True:
        SCREEN.fill("black")

        # Título
        TITULO = get_font(45).render(f"Nonogramas {tamaño}", True, "White")
        TITULO_RECT = TITULO.get_rect(center=(640, 50))
        SCREEN.blit(TITULO, TITULO_RECT)

        # Mostrar lista de nonogramas según la página actual
        inicio = pagina_actual * items_por_pagina
        fin = inicio + items_por_pagina
        nonogramas_visibles = nonogramas[inicio:fin]

        y_pos = 150
        botones_nonogramas = []
        for nonograma in nonogramas_visibles:
            nombre = nonograma.replace('.pkl', '')
            boton = Button(image=None, pos=(640, y_pos),
                           text_input=nombre, font=get_font(35),
                           base_color="White", color_flotante="Green")
            botones_nonogramas.append(boton)
            y_pos += 60

        # Botones para navegar entre páginas
        FLECHA_IZQUIERDA = Button(image=None, pos=(100, 360),
                                  text_input="<", font=get_font(75),
                                  base_color="White", color_flotante="Green")
        FLECHA_DERECHA = Button(image=None, pos=(1180, 360),
                                text_input=">", font=get_font(75),
                                base_color="White", color_flotante="Green")

        # Botón de regreso
        BACK = Button(image=None, pos=(640, 660),
                      text_input="BACK", font=get_font(75),
                      base_color="White", color_flotante="Green")

        MOUSE_POS = pygame.mouse.get_pos()

        # Dibujar botones
        for boton in botones_nonogramas + [BACK, FLECHA_IZQUIERDA, FLECHA_DERECHA]:
            boton.changeColor(MOUSE_POS)
            boton.update(SCREEN)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    catalogo()
                if FLECHA_IZQUIERDA.checkForInput(MOUSE_POS) and pagina_actual > 0:
                    pagina_actual -= 1
                if FLECHA_DERECHA.checkForInput(MOUSE_POS) and fin < len(nonogramas):
                    pagina_actual += 1
                for i, boton in enumerate(botones_nonogramas):
                    if boton.checkForInput(MOUSE_POS):
                        # Cargar el nonograma seleccionado
                        ruta_nonograma = os.path.join(ruta_catalogo, nonogramas[inicio + i])
                        play(tamaño_int, ruta_nonograma)

        pygame.display.update()

# Ventana donde se muestra la lista de nonogramas disponibles para eliminar acorde al tamaño
def eliminar_nonogramas(tamaño):
    tamaño_int = int(tamaño.split('x')[0])  # Se extrae el tamaño del nonograma
    ruta_catalogo = os.path.join("catalogo", tamaño)

    # Obtener lista de nonogramas disponibles
    try:
        nonogramas = [f for f in os.listdir(ruta_catalogo) if f.endswith('.pkl')]
    except FileNotFoundError:
        nonogramas = []

    pagina_actual = 0
    items_por_pagina = 8  # Número de nonogramas por página

    while True:
        SCREEN.fill("black")

        # Título
        TITULO = get_font(45).render(f"Eliminar Nonogramas {tamaño}", True, "White")
        TITULO_RECT = TITULO.get_rect(center=(640, 50))
        SCREEN.blit(TITULO, TITULO_RECT)

        # Mostrar lista de nonogramas según la página actual
        inicio = pagina_actual * items_por_pagina
        fin = inicio + items_por_pagina
        nonogramas_visibles = nonogramas[inicio:fin]

        y_pos = 150
        botones_nonogramas = []
        for nonograma in nonogramas_visibles:
            nombre = nonograma.replace('.pkl', '')
            boton = Button(image=None, pos=(640, y_pos),
                           text_input=nombre, font=get_font(35),
                           base_color="White", color_flotante="Red")
            botones_nonogramas.append(boton)
            y_pos += 60

        # Botones para navegar entre páginas
        FLECHA_IZQUIERDA = Button(image=None, pos=(100, 360),
                                  text_input="<", font=get_font(75),
                                  base_color="White", color_flotante="Green")
        FLECHA_DERECHA = Button(image=None, pos=(1180, 360),
                                text_input=">", font=get_font(75),
                                base_color="White", color_flotante="Green")

        # Botón de regreso
        BACK = Button(image=None, pos=(640, 660),
                      text_input="BACK", font=get_font(75),
                      base_color="White", color_flotante="Green")

        MOUSE_POS = pygame.mouse.get_pos()

        # Dibujar botones
        for boton in botones_nonogramas + [BACK, FLECHA_IZQUIERDA, FLECHA_DERECHA]:
            boton.changeColor(MOUSE_POS)
            boton.update(SCREEN)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    main_menu()
                if FLECHA_IZQUIERDA.checkForInput(MOUSE_POS) and pagina_actual > 0:
                    pagina_actual -= 1
                if FLECHA_DERECHA.checkForInput(MOUSE_POS) and fin < len(nonogramas):
                    pagina_actual += 1
                for i, boton in enumerate(botones_nonogramas):
                    if boton.checkForInput(MOUSE_POS):
                        # Confirmar eliminación
                        ruta_nonograma = os.path.join(ruta_catalogo, nonogramas[inicio + i])
                        if confirmar_eliminacion(nonogramas[inicio + i]):
                            os.remove(ruta_nonograma)
                            nonogramas.pop(inicio + i)  # Actualizar la lista
                            break  # Volver a renderizar la lista después de eliminar

        pygame.display.update()

# Ventana donde se muestran los tamaños de nonogramas disponibles para eliminar
def elegir_tamaño_eliminar():
    while True:
        ELIMINAR_TAMAÑO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        ELIMINAR_TAMAÑO_TEXT = get_font(45).render("Eliminar Tamaño", True, "White")
        ELIMINAR_TAMAÑO_RECT = ELIMINAR_TAMAÑO_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(ELIMINAR_TAMAÑO_TEXT, ELIMINAR_TAMAÑO_RECT)

        TAMAÑO_10 = Button(image=None, pos=(640, 260),
                           text_input="10 x 10", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_15 = Button(image=None, pos=(640, 360),
                           text_input="15 x 15", font=get_font(60), base_color="White", color_flotante="Green")
        TAMAÑO_20 = Button(image=None, pos=(640, 460),
                           text_input="20 x 20", font=get_font(60), base_color="White", color_flotante="Green")
        ELIMINAR_TAMAÑO_BACK = Button(image=None, pos=(640, 560),
                                      text_input="BACK", font=get_font(60), base_color="White", color_flotante="Green")

        for button in [TAMAÑO_10, TAMAÑO_15, TAMAÑO_20, ELIMINAR_TAMAÑO_BACK]:
            button.changeColor(ELIMINAR_TAMAÑO_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ELIMINAR_TAMAÑO_BACK.checkForInput(ELIMINAR_TAMAÑO_MOUSE_POS):
                    main_menu()
                if TAMAÑO_10.checkForInput(ELIMINAR_TAMAÑO_MOUSE_POS):
                    eliminar_nonogramas("10x10")
                if TAMAÑO_15.checkForInput(ELIMINAR_TAMAÑO_MOUSE_POS):
                    eliminar_nonogramas("15x15")
                if TAMAÑO_20.checkForInput(ELIMINAR_TAMAÑO_MOUSE_POS):
                    eliminar_nonogramas("20x20")

        pygame.display.update()

# Ventana de confirmación para eliminar un nonograma
def confirmar_eliminacion(nonograma):
    while True:
        SCREEN.fill("black")

        # Mensaje de confirmación
        CONFIRM_TEXT = get_font(45).render(f"¿Eliminar '{nonograma}'?", True, "White")
        CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(CONFIRM_TEXT, CONFIRM_RECT)

        # Botones "SÍ" y "NO"
        SI_BUTTON = Button(image=None, pos=(480, 400),
                           text_input="SÍ", font=get_font(50),
                           base_color="Green", color_flotante="White")
        NO_BUTTON = Button(image=None, pos=(800, 400),
                           text_input="NO", font=get_font(50),
                           base_color="Red", color_flotante="White")

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [SI_BUTTON, NO_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SI_BUTTON.checkForInput(MOUSE_POS):
                    return True
                if NO_BUTTON.checkForInput(MOUSE_POS):
                    return False

        pygame.display.update()

# Ventana que se muestra al perder todas las vidas
def sin_vidas(tamaño, ruta_nonograma):
    while True:
        SCREEN.fill("black")

        # Mensaje
        CONFIRM_TEXT = get_font(45).render(f"Perdiste", True, "White")
        CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(CONFIRM_TEXT, CONFIRM_RECT)

        # Botones "Volver al Menú" y "Volver a jugar"
        MENU_BUTTON = Button(image=None, pos=(640, 400),
                           text_input="Volver al Menú", font=get_font(50),
                           base_color="Green", color_flotante="White")
        JUGAR_BUTTON = Button(image=None, pos=(640, 500),
                           text_input="Volver a jugar", font=get_font(50),
                           base_color="Green", color_flotante="White")

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [MENU_BUTTON, JUGAR_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MOUSE_POS):
                    main_menu() # Volver al menú principal
                if JUGAR_BUTTON.checkForInput(MOUSE_POS):
                    play(tamaño, ruta_nonograma) # Volver a jugar

        pygame.display.update()

# Ventana principal del menú, la primera en mostrarse y la que tiene "enlaces" a las demás ventanas
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))  # Fondo de pantalla

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("NONOGRAMA", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        saved_game_exists = os.path.exists('guardadoPartida/partidaGuardada.pkl')

        # Botones del menú principal
        if saved_game_exists:
            CONTINUAR_BUTTON = Button(image=None, pos=(300, 250),
                                      text_input="CONTINUAR", font=get_font(50), base_color="White",
                                      color_flotante="Green")

        CATALOGO_BUTTON = Button(image=None, pos=(300, 350),
                                 text_input="JUGAR", font=get_font(50), base_color="White", color_flotante="Green")

        ELIMINAR_BUTTON = Button(image=None, pos=(1000, 400),
                                 text_input="ELIMINAR", font=get_font(50), base_color="White", color_flotante="Red")

        CREACION_BUTTON = Button(image=None, pos=(300, 450),
                                 text_input="CREACIÓN", font=get_font(50), base_color="White", color_flotante="Green")

        TUTORIAL_BUTTON = Button(image=None, pos=(300, 550),
                                 text_input="TUTORIAL", font=get_font(50), base_color="White", color_flotante="Green")

        QUIT_BUTTON = Button(image=None, pos=(300, 650),
                             text_input="QUIT", font=get_font(50), base_color="White", color_flotante="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)  # Dibujar el título en la pantalla

        # Lista de botones
        buttons = [CATALOGO_BUTTON, TUTORIAL_BUTTON, CREACION_BUTTON, QUIT_BUTTON, ELIMINAR_BUTTON]
        if saved_game_exists:
            buttons.append(CONTINUAR_BUTTON)

        # Cambiar el color de los botones si el mouse está encima
        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Manejo de eventos para los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Redireccionar a la página correspondiente
                if saved_game_exists and CONTINUAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    continuar_partida()
                if CATALOGO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    catalogo()
                if ELIMINAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    elegir_tamaño_eliminar()  # Nuevo menú para eliminar nonogramas
                if CREACION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    elegir_tamaño_creacion()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tutorial()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()