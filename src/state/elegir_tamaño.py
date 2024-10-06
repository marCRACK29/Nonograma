from state import State

class ElegirTamaño(State):
    def go_to(self) -> None:
        from jugar import Jugar
        self.context.transition_to(Jugar)

    def back_to(self) -> None:
        from inicio import Inicio
        self.context.transition_to(Inicio)