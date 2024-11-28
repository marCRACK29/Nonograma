import pygame
import os

# Clase que permite mostrar la cantidad de vidas restantes
class HP_counter:
    def __init__(self, maxLives):
        self.maxLives = maxLives
        self.scale = 4
        self.pos = (900,30)
        self.lives = maxLives
        src = os.path.dirname(os.path.abspath(__file__))
        self.heartImage = pygame.image.load(os.path.join(src,"assets", "heart.png"))
        self.noheartImage = pygame.image.load(os.path.join(src,"assets", "noHeart.png"))
    # Resta una vida
    def loseLife(self):
        self.lives -= 1
        if self.lives <= 0: self.lives = 0

    # Determina si el jugador sigue vivo
    def alive(self): return  self.lives > 0

    # Dibuja la cantidad de vidas restantes
    def draw(self, surface) -> None:
        imageToDraw = self.heartImage  # la imagen que dibujaremos dependerá de cuántos corazones queden
        for i in range(self.maxLives):
            if i == self.lives:
                imageToDraw = self.noheartImage
            x_offset = (i % 8) * imageToDraw.get_width()
            y_offset = (i // 8) * imageToDraw.get_height()
            surface.blit(imageToDraw, (self.pos[0] + x_offset, self.pos[1] + y_offset))
