import copy


class mementoJuego:
    def __init__(self, tableroJugador, tableroObjetivo, vidas):
        self.tableroJugador = copy.deepcopy(tableroJugador)
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)
        self.vidas = vidas
    def get_state(self):
        return self.tableroJugador, self.tableroObjetivo, self.vidas

class mementoCreacion:
    def __init__(self, tableroObjetivo):
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)

    def get_state(self):
        return self.tableroObjetivo
