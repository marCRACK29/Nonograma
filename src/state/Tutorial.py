import State, Inicio

class Tutorial(State):
    def go_to(self) -> None:
        self.context.transition_to(Inicio)

    def back_to(self) -> None:
        pass