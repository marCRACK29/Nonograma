import pygame
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

    def checkForInput(self, position) -> bool:
        # Comprobar si la posición del click está dentro del rectángulo del botón
        if self.rect.collidepoint(position):
            return True
        return False

    def get_color(self) -> tuple:
        return self.color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.image_flotante, self.rect)
        else:
            screen.blit(self.image_base, self.rect)

"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Boton de color")

    # Crear un rectángulo de color inicial (rojo)
    initial_color = (255, 0, 0)
    image_base = pygame.Surface((50, 50))  # Crear una superficie rectangular
    image.fill(initial_color)  # Llenar el rectángulo con el color rojo

    # Crear el botón
    boton = colorbutton(image, (400, 400), initial_color)

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Si se hace clic con el botón izquierdo del ratón
                    if boton.checkForInput(event.pos):
                        # Cambiar color del botón al verde cuando se haga clic
                        boton.set_color((0, 255, 0))  # Cambiar el color a verde

        # Limpiar la pantalla
        screen.fill((255, 255, 255))  # Fondo blanco

        # Dibujar el botón
        boton.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

# Llamar a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
"""