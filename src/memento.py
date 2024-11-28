import copy

# Clase memento que guarda el estado del juego (tableroJugador, tableroObjetivo, vidas, ayudas)
class mementoJuego:
    def __init__(self, tableroJugador, tableroObjetivo, vidas, ayudas):
        self.tableroJugador = copy.deepcopy(tableroJugador)
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)
        self.vidas = vidas
        self.ayudas = ayudas

    # Retorna una tupla con los elementos del juego
    def get_state(self) -> tuple:
        return self.tableroJugador, self.tableroObjetivo, self.vidas, self.ayudas

# Clase memento que guarda solo el estado del tablero objetivo
class mementoCreacion:
    def __init__(self, tableroObjetivo):
        self.tableroObjetivo = copy.deepcopy(tableroObjetivo)

    # Retorna el tablero objetivo
    def get_state(self):
        return self.tableroObjetivo
