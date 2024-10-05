import State, Inicio, Jugar

class ElegirTamaño(State):
    def go_to(self) -> None:
        self.context.transition_to(Jugar)

    def back_to(self) -> None:
        self.context.transition_to(Inicio)