import copy


class mementoJuego:
    def __init__(self, tableroJugador, tableroObjetivo, vidas, ayudas):
        self.tableroJugador = copy.deepcopy(tableroJugador)
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)
        self.vidas = vidas
        self.ayudas = ayudas
    def get_state(self):
        return self.tableroJugador, self.tableroObjetivo, self.vidas, self.ayudas

class mementoCreacion:
    def __init__(self, tableroObjetivo):
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)

    def get_state(self):
        return self.tableroObjetivo
