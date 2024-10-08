import pygame
import os
from abc import ABC, abstractmethod

class State(ABC):
    # Las clases concretas puedan acceder a transition_to
    @property
    def context(self) -> 'Context':
        return self._context

    @context.setter
    def context(self, context: 'Context') -> None:
        self._context = context

    # Todas las clases que ocupen la interfaz State obtendran las imagenes de la misma carpeta resources
    # Metodo no abstracto para que las clases lo ocupen sin tener que implementarlo
    def load_image(self, filename: str) -> pygame.Surface:
        current_dir = os.path.dirname(os.path.abspath(__file__)) # Obtener la ruta del directorio actual del script
        project_root = os.path.dirname(os.path.dirname(current_dir))
        image_path_uno = os.path.join(project_root, 'resources', filename)
        return pygame.image.load(image_path_uno).convert_alpha()

    @abstractmethod
    def go_to(self) -> None:
        pass

    @abstractmethod
    def back_to(self) -> None:
        pass

    @abstractmethod
    def handle_events(self, event) -> None:
        pass

    @abstractmethod
    def draw(self, screen) -> None:
        pass