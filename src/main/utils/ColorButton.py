import pygame

class ColorButton():
    def __init__(self, x, y, image, scale, colorHolder, color):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._colorHolder = colorHolder #privado
        self._color = color
        self.clicked = False

    def click(self):
        #obtener posición del mouse
        pos = pygame.mouse.get_pos()
        #verificar si el mouse está sobre el botón
        if self.rect.collidepoint(pos):
            #verificar si se hizo click en el botón izquierdo
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self._colorHolder.set_color(self._color)

    def desactivate(self):
        #Resetear clicked si el mouse no está presionado
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

"""
    def draw(self):
        #dibujar boton en screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
"""
