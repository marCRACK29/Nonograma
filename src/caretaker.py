import os
import pickle

from src.GestorCreación import GestorCreacion
from src.GestorJuego import GestorJuego


class Caretaker:
    def __init__(self, gestor):
        self.gestor = gestor
        self.mementos = []
        self.ruta_guardado = None

    def añadirMemento(self):
        m = self.gestor.guardar_estado()
        self.mementos.append(m)
        self.guardar()


    def guardar(self):
        print(f"El tipo de gestor es: {type(self.gestor).__name__}")
        if self.ruta_guardado is None:
            if type(self.gestor) is GestorCreacion:
                self.ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion", "nonogramaUsuarioCreacion.pkl")
            else:
                self.ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorJuego","nonogramaUsuarioJuego.pkl" )

        with open(self.ruta_guardado, "wb") as archivo:
            pickle.dump(self.mementos[len(self.mementos)-1], archivo)

    #Este metodo tiene que arreglarse para su buen funcionamiento posterior, beta
    def cargarPartida(self):
        ruta_guardado_partida = os.path.join(os.path.dirname(__file__), "guardadoPartida","nonogramaUsuario.pkl" )
        with open(ruta_guardado_partida, "rb") as archivo:
            m = pickle.load(archivo)
            self.gestor.cargar_estado(m)

    #metodo experimental enfocado a gestorJuego
    def cargarObjetivo(self):
        ruta_cargado= os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion",  "nonogramaUsuarioCreacion.pkl")
        with open(ruta_cargado, "rb") as archivo:
            m = pickle.load(archivo)  #Se carga un mementoCreacion desde memoria
            self.gestor.cargar_objetivo(m)
"""
if __name__ == '__main__':
    caretaker = Caretaker(GestorCreacion(20, 50))
    caretaker.cargarPartida()
    caretaker.añadirMemento()
    caretaker.guardar()
    #caretaker.cargarObjetivo
"""