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


    def guardar(self):
        if self.ruta_guardado is None:
            if isinstance(self.gestor, GestorCreacion):
                #nombre = input("Nombre del nonograma: ")
                nombre = "nonogramaUsuario"
                self.ruta_guardado = os.path.join(os.path.dirname(__file__), "catalogo", nombre + ".pkl")
            else:
                self.ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartida","nonogramaUsuario.pkl" )

        with open(self.ruta_guardado, "wb") as archivo:
            pickle.dump(self.mementos[len(self.mementos)-1], archivo)

    def cargarPartida(self):
        with open(self.ruta_guardado, "rb") as archivo:
            m = pickle.load(archivo)
            self.gestor.cargar_estado(m)

    #metodo experimental
    def cargarObjetivo(self):
        #nombre = input("Nombre del nonograma: ")
        nombre = "nonogramaUsuario"
        ruta_guardado = os.path.join(os.path.dirname(__file__), "catalogo", nombre + ".pkl")
        with open(ruta_guardado, "rb") as archivo:
            m = pickle.load(archivo)
            self.gestor.cargar_objetivo(m)


