class mementoJuego:
    def __init__(self, tableroJugador, tableroObjetivo):
        self.tableroJugador = tableroJugador
        self.tableroObjetivo = tableroObjetivo

    def get_state(self):
        return self.tableroJugador, self.tableroObjetivo

class mementoCreacion:
    def __init__(self, tableroObjetivo):
        self.tableroObjetivo = tableroObjetivo

    def get_state(self):
        return self.tableroObjetivo
