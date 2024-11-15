import pygame
from state import State
from src.GestorJuego import GestorJuego
from src.caretaker import Caretaker
from src.vidas import HP_counter

class Jugar(State):
    def __init__(self):
        self.background_color = (202, 228, 241)

        self.texto = pygame.font.SysFont('Arial', 30) # Texto para saber en que estado estamos.
        self.frase = self.texto.render('Estas en jugar', True, (0, 0, 0))

        self.img_uno = self.load_image('der.png')

        self.gestor = GestorJuego(10, 50)
        if True:#TODO: reemplazar por logica de "si se va a jugar con vidas"
            vidas = HP_counter(3,4,(900,30))
            vidas.setHeartImage(self.load_image("heart.png"))
            vidas.setNoheartImage(self.load_image("noHeart.png"))
            self.gestor.contadorVidas = vidas

        self.caretaker = Caretaker(self.gestor)
        self.caretaker.cargarObjetivo()

    def go_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio())

    def back_to(self) -> None:
        pass

    def handle_events(self, event) -> None:
        self.gestor.handle_events(event, self.caretaker)
        if not self.gestor.contadorVidas.alive():
            self.go_to()

    def draw(self, screen) -> None:
        screen.fill(self.background_color) # Fondo de la pantalla
        screen.blit(self.frase, (100, 50)) # Texto de la pantalla
        self.gestor.draw(screen) # Dibuja gestor

