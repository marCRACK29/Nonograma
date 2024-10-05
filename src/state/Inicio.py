import State, ElegirTamaño

class Inicio(State):
    def go_to(self) -> None:
        self.context.transition_to(ElegirTamaño)

    def back_to(self) -> None:
        pass