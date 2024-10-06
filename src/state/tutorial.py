from state import State

class Tutorial(State):
    def go_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio)

    def back_to(self) -> None:
        pass