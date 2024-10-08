import pygame
from state import State
from toggle_button import ToggleButton

class Jugar(State):
    def __init__(self):
        self.background_color = (202, 228, 241)

        self.texto = pygame.font.SysFont('Arial', 30) # Texto para saber en que estado estamos.
        self.frase = self.texto.render('Estas en jugar', True, (0, 0, 0))

        self.img_uno = self.load_image('der.png')
        self.button_uno = ToggleButton(100, 100, self.img_uno, 0.8)

    def go_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio())

    def back_to(self) -> None:
        pass

    def handle_events(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_uno.click():
                self.go_to()

    def draw(self, screen) -> None:
        screen.fill(self.background_color) # Fondo de la pantalla
        screen.blit(self.frase, (100, 50)) # Texto de la pantalla
        self.button_uno.draw(screen) # Botones de la pantalla