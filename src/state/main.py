import pygame
from context import Context
from inicio import Inicio
from src.GestorCreación import GestorCreacion
from src.caretaker import Caretaker
from src.GestorJuego import GestorJuego

def main():
    pygame.init() # Inicializa Pygame

    pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Nonograma")

    # Crear la primera ventana en mostrarse
    initial_state = Inicio()
    gestor = GestorJuego(10, 50)
    caretaker = Caretaker(gestor)
    caretaker.cargarObjetivo()
    # Crear el contexto con el estado inicial
    context = Context(initial_state)

    # Ejecutar el contexto
    context.run(caretaker)

if __name__ == "__main__":
    main()
