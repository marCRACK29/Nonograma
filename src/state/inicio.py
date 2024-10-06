import pygame
import os
from state import State
from toggle_button import ToggleButton

class Inicio(State):
    def __init__(self):
        self.background_color = (202, 228, 241)
        current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual del script
        project_root = os.path.dirname(os.path.dirname(current_dir))# Subir dos niveles de directorio (desde src/state a la raíz del proyecto)
        image_path_uno = os.path.join(project_root, 'resources', 'der.png')# Construir la ruta completa al archivo de imagen
        image_path_dos = os.path.join(project_root, 'resources', 'izq.png')
        self.img_uno = pygame.image.load(image_path_uno).convert_alpha()
        self.img_dos = pygame.image.load(image_path_dos).convert_alpha()
        self.buttonuno = ToggleButton(100, 100, self.img_uno, 0.8)
        self.buttondos = ToggleButton(300, 200, self.img_dos, 0.8)

    def go_to(self) -> None:
        from elegir_tamaño import ElegirTamaño
        self.context.transition_to(ElegirTamaño())

    def back_to(self) -> None:
        from tutorial import Tutorial
        self.context.transition_to(Tutorial())

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
