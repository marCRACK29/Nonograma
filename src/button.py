# Clase que representa un botón sin un color asociado, pero al cual se
# le puede asignar una imagen y un texto.

class Button():
    def __init__(self, image, pos, text_input, font, base_color, color_flotante):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.color_flotante = base_color, color_flotante
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # Metodo que actualiza la posición del botón en la pantalla.
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    # Metodo que verifica si el botón ha sido presionado.
    def checkForInput(self, position) -> bool:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # Metodo que cambia el color del texto del botón si el cursor se encuentra sobre él.
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.color_flotante)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)