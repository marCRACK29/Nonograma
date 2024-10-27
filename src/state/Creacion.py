import pygame
from state import State
from toggle_button import ToggleButton
from src.GestorCreación import GestorCreacion
from src.caretaker import Caretaker

class Creacion(State):
    def __init__(self):
        self.background_color = (202, 228, 241)

        self.texto = pygame.font.SysFont('Arial', 30) # Texto para saber en que estado estamos.
        self.frase = self.texto.render('Estas en creación', True, (0, 0, 0))

        self.gestor = GestorCreacion(10, 50)
        self.caretaker = Caretaker(self.gestor)

    def go_to(self) -> None:
        pass

    def back_to(self) -> None:
        pass

    def handle_events(self, event, caretaker) -> None:
        self.gestor.handle_events(event, caretaker)

    def draw(self, screen) -> None:
        screen.fill(self.background_color) # Fondo de la pantalla
        screen.blit(self.frase, (100, 50)) # Texto de la pantalla
        self.gestor.draw(screen) # Dibuja gestor


