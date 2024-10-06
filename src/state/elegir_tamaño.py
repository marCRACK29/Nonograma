import pygame
import os
from state import State
from toggle_button import ToggleButton

class ElegirTamaño(State):
    def __init__(self):
        self.background_color = (202, 228, 241)
        self.img_uno = self.load_image('der.png')
        self.img_dos = self.load_image('izq.png')
        self.buttonuno = ToggleButton(100, 100, self.img_uno, 0.8)
        self.buttondos = ToggleButton(300, 200, self.img_dos, 0.8)

    def load_image(self, filename) -> pygame.Surface:
        current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual del script
        project_root = os.path.dirname(os.path.dirname(current_dir))
        image_path_uno = os.path.join(project_root, 'resources', filename)
        return pygame.image.load(image_path_uno).convert_alpha()

    def go_to(self):
        from jugar import Jugar
        self.context.transition_to(Jugar())

    def back_to(self):
        from inicio import Inicio
        self.context.transition_to(Inicio())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttonuno.click():
                self.go_to()
            if self.buttondos.click():
                self.back_to()

    def draw(self, screen):
        # Dibujar la ventana gráfica
        screen.fill(self.background_color)
        # Dibujar botón
        self.buttonuno.draw(screen)
        self.buttondos.draw(screen)