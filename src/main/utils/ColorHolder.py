from src.main.Color import Color

class ColorHolder:
    def __init__(self):
        self.color = Color.WHITE

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

