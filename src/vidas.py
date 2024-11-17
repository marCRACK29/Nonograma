from cgi import maxlen

import pygame
import os

from pygame.examples.cursors import image


class HP_counter:

    def __init__(self, maxLives, scale, position):
        self.maxLives = maxLives
        self.scale = scale
        self.pos = position
        self.lives = maxLives
    def loseLife(self):
        self.lives -= 1
        if self.lives <= 0: self.lives = 0
    def alive(self): return  self.lives > 0

    def setHeartImage(self, image):
        self.heartImage = pygame.transform.scale(image,(image.get_width()*self.scale,image.get_height()*self.scale))
    def setNoheartImage(self, image):
        self.noheartImage = pygame.transform.scale(image,(image.get_width()*self.scale,image.get_height()*self.scale))

    def draw(self, surface) -> None:
        imageToDraw = self.heartImage #the image that we will draw will depend on how many hearts there are left
        for i in range(self.maxLives):
            if i==self.lives: imageToDraw = self.noheartImage
            surface.blit(imageToDraw, (self.pos[0] + imageToDraw.get_width()*i, self.pos[1]))
"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("vidas draw test")

    v = HP_counter(3,3,(400,100))
    #we need a global image-loading function, this only works on my computer. Eh, it's for testing anyway
    v.setHeartImage(pygame.image.load("/home/felicia/Desktop/carpeta/proprog/Nonograma/resources/heart.png"))
    v.setNoheartImage(pygame.image.load("/home/felicia/Desktop/carpeta/proprog/Nonograma/resources/noHeart.png"))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("blue")
        v.draw(screen)
        pygame.display.update()
        pygame.time.delay(500)
        v.loseLife()

if __name__ == '__main__':
    main()
"""