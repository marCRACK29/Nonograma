from Color import Color

class Proxy:
    @classmethod
    def set_color(self, color):
        self.color = color
    @classmethod
    def get_color(self):
        return self.color
