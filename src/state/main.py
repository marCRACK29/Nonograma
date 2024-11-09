import pygame
from context import Context
from inicio import Inicio   

def main():
    pygame.init() # Inicializa Pygame

    pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Nonograma")

    # Crear la primera ventana en mostrarse
    initial_state = Inicio()
    # Crear el contexto con el estado inicial
    context = Context(initial_state)

    # Ejecutar el contexto
    context.run()

if __name__ == "__main__":
    main()
