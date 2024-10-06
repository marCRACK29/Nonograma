import pygame

class ToggleButton:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def click(self)-> bool:
        accion = False
        #obtener posición del mouse
        pos = pygame.mouse.get_pos()
        presionado = pygame.mouse.get_pressed()[0] #para el botón izquierdo del mouse
        #verificar si el mouse está sobre el botón
        if self.rect.collidepoint(pos):
            #verificar si se hizo click en el botón izquierdo
            if presionado == 1 and self.clicked == False:
                self.clicked = True
                accion = True
            elif presionado == 0:
                self.clicked = False

        return accion

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

