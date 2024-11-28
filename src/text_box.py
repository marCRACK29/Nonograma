import pygame
import pygame_gui

# Clase que permite ingresar texto en una ventana
class Text_box():
    def __init__(self,screen,xy=(100,300),wh=(600,50)):
        """
        :param screen : Surface
            La pantalla en la que estará el cuadro de texto.
        :param xy: (int, int)
            Tupla con las coordenadas x e y del cuadro de texto.
        :param wh: (int, int)
            Tupla con el ancho y la altura del cuadro de texto.
        """
        self.screen = screen
        self.manager = pygame_gui.UIManager((screen.width,screen.height))
        self._textBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(xy,wh),manager=self.manager)
        self.clock = pygame.time.Clock()
        # Crear un botón para guardar el texto
        self.save_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(xy[0] + wh[0] + 10, xy[1], 100, 50),
            text='Guardar',
            manager=self.manager
        )

    # Establecer el texto del cuadro de texto
    def setText(self,value):
        self._textBox.set_text(value)

    # Obtener el texto ingresado
    def getText(self):
        return self._textBox.get_text()

    # Procesar eventos (como clicks de mouse) en la interfaz
    def process_events(self, event):
        self.manager.process_events(event)

    # Dibujar el cuadro de texto
    def draw(self):
        self.manager.update(self.clock.tick()/1000.0)
        self.manager.draw_ui(self.screen)

    # Verificar si se presiona el botón de guardar
    def check_button(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.save_button:
                    self.texto_guardado = self.getText()  # Almacena el texto ingresado
                    print(f"Texto guardado: {self.texto_guardado}")  # Imprime el texto guardado
                    return True  # Indica que se debe cerrar la ventana
        return False  # No se debe cerrar la ventana
