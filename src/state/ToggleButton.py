import pygame

SCREEN_WIDTH  = 500
SCREEN_HEIGHT  = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class ToggleButton:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def click(self):
        #obtener posición del mouse
        pos = pygame.mouse.get_pos()
        #verificar si el mouse está sobre el botón
        if self.rect.collidepoint(pos):
            #verificar si se hizo click en el botón izquierdo
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True

    def desclick(self):
        #Resetear clicked si el mouse no está presionado
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

