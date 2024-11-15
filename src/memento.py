import copy


class mementoJuego:
    def __init__(self, tableroJugador, tableroObjetivo):
        self.tableroJugador = copy.deepcopy(tableroJugador)
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)

    def get_state(self):
        return self.tableroJugador, self.tableroObjetivo

class mementoCreacion:
    def __init__(self, tableroObjetivo):
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)

    def get_state(self):
        return self.tableroObjetivo
