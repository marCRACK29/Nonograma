import pygame

# Clase que representa un botón de color
class colorbutton:
    def __init__(self, image_base, image_flotante, pos, color, size=(50, 50)):
        self.image_base = image_base
        self.image_flotante = image_flotante
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.color = color
        self.size = size
        self.image_base = pygame.transform.scale(self.image_base, self.size)
        self.image_flotante = pygame.transform.scale(self.image_flotante, self.size)
        self.rect = self.image_base.get_rect(center=(self.x_pos, self.y_pos))

    # Comprobar si el botón ha sido clickeado
    def checkForInput(self, position) -> bool:
        # Comprobar si la posición del click está dentro del rectángulo del botón
        if self.rect.collidepoint(position):
            return True
        return False

    # Obtener el color del botón
    def get_color(self):
        return self.color

    # Dibujar el botón en la pantalla
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        # Para cambiar el color del botón si el cursor se encuentra sobre él
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.image_flotante, self.rect)
        else:
            screen.blit(self.image_base, self.rect)

