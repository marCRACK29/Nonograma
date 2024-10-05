import State, Inicio

class Jugar(State):
    def go_to(self) -> None:
        self.context.transition_to(Inicio)

    def back_to(self) -> None:
        pass