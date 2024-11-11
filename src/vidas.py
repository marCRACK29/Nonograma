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
        self.heartImage = image
    def setNoheartImage(self, image):
        self.noheartImage = image

    def draw(self, surface) -> None:
        imageToDraw = self.heartImage
        for i in range(self.maxLives):
            if(i==self.lives): imageToDraw = self.noheartImage
            surface.blit(self.image, (self.pos[0] + self.scale*i, self.pos[1]))
