import pygame
import os
from state import State
from toggle_button import ToggleButton

class Tutorial(State):
    def __init__(self):
        self.background_color = (202, 228, 241)
        # Obtener la ruta del directorio actual del script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Subir dos niveles de directorio (desde src/state a la raíz del proyecto)
        project_root = os.path.dirname(os.path.dirname(current_dir))
        # Construir la ruta completa al archivo de imagen
        image_path = os.path.join(project_root, 'resources', 'der.png')
        self.img = pygame.image.load(image_path).convert_alpha()
        self.button = ToggleButton(100, 100, self.img, 0.8)


    def go_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio())

    def back_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.click():
                self.go_to()

    def draw(self, screen):
        # Dibujar la ventana gráfica
        screen.fill(self.background_color)
        # Dibujar botón
        self.button.draw(screen)
