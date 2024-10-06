from state import State

class Inicio(State):
    def go_to(self) -> None:
        from elegir_tamaño import ElegirTamaño
        self.context.transition_to(ElegirTamaño)

    def back_to(self) -> None:
        pass