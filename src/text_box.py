
import pygame
import pygame_gui


class Text_box():
    def __init__(self,screen,xy=(100,300),wh=(600,50)):
        """
        :param screen : Surface
            the screen the text box will be in
        :param xy: (int,int)
            tuple with x and y coordinates of the text box
        :param wh: (int,int)
            tuple with width and height of the text box
        """
        self.screen = screen
        self.manager = pygame_gui.UIManager((screen.width,screen.height))
        self._textBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(xy,wh),manager=self.manager)
        self.clock = pygame.time.Clock()
    def setText(self,value):
        self._textBox.set_text(value)
    def getText(self):
        return self._textBox.get_text()
    def process_events(self, event):
        self.manager.process_events(event)
    def draw(self):
        self.manager.update(self.clock.tick()/1000.0)
        self.manager.draw_ui(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("text_input_demo")

    entrada = Text_box(screen) #<---
    #entrada = Text_box(screen,(100,300),(600,50)) #<---
"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            entrada.process_events(event) #<---

        screen.fill("blue")

        entrada.draw() #<---

        new_text = pygame.font.SysFont("calibri", 50).render(f"text: {entrada.getText()}", True, "black")
        new_text_rect = new_text.get_rect(center=(screen.width/2, screen.height*2/3))
        screen.blit(new_text, new_text_rect)
        pygame.display.update()

if __name__ == '__main__':
    main()
"""