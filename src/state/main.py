import pygame
from state import State
from context import Context
from tutorial import Tutorial  # Asegúrate de que este archivo contiene la clase Tutorial

def main():
    # Inicializa Pygame
    pygame.init()
    # Configura un modo de video antes de crear cualquier objeto de estado
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nonograma")

    # Crea una instancia del estado inicial
    initial_state = Tutorial()

    # Crea el contexto con el estado inicial
    context = Context(initial_state)

    # Ejecuta el contexto
    context.run()

if __name__ == "__main__":
    main()
