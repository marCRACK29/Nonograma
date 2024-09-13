from src.main.Color import Color
from src.main.utils.ColorButton import ColorButton
from ..main import screen

class ButtonRow:
    def __init__(self, colorHolder):
        self.colorHolder = colorHolder
        self.buttonGreen = ColorButton(100,200, Color.green_img, 0.5, colorHolder, Color.GREEN)
        self.buttonRed = ColorButton(200,200, Color.red_img, 0.5, colorHolder, Color.RED)
        self.buttonBlue = ColorButton(300,200, Color.blue_img, 0.5, colorHolder, Color.BLUE)

    def draw(self):
        screen.blit(self.buttonGreen.image, (self.buttonGreen.rect.x, self.buttonGreen.rect.y))
        screen.blit(self.buttonRed.image, (self.buttonRed.rect.x, self.buttonRed.rect.y))
        screen.blit(self.buttonBlue.image, (self.buttonBlue.rect.x, self.buttonBlue.rect.y))



