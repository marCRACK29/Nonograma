from src.Color import Color


class Proxy:
    color = Color.BLACK.value
    @classmethod
    def set_color(self, color):
        self.color = color.value
    @classmethod
    def get_color(self):
        return self.color
