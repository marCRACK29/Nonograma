import os
import pickle

from src.GestorCreacion import GestorCreacion
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

    #Metodo para guardar la partida en curso en memoria
    def guardar(self):
        try:
            gestor_type = type(self.gestor).__name__

            # Usar el nombre de la clase directamente
            if gestor_type == "GestorCreacion":
                ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion", "penguin.pkl")
            elif gestor_type == "GestorJuego":
                ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartida", "partida.pkl")
            else:
                print(f"Tipo de gestor no reconocido: {gestor_type}")
                return

            with open(ruta_guardado, "wb") as archivo:
                m = self.gestor.guardar_estado()
                pickle.dump(m, archivo)

        except Exception as e:
            print(f"Error al guardar: {str(e)}")
            import traceback
            traceback.print_exc()

    #Este metodo para cargar la ultima partida jugada en memoria
    def cargarPartida(self):
        try:
            gestor_type = type(self.gestor).__name__
            print(f"Tipo de gestor actual al cargar: {gestor_type}")

            if gestor_type == "GestorCreacion":
                print("Cargando desde GestorCreacion")
                ruta_cargado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion", "nonogramaUsuarioCreacion.pkl")
                print("Se carga creacion")
            elif gestor_type == "GestorJuego":
                print("Cargando desde GestorJuego")
                ruta_cargado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorJuego", "nonogramaUsuarioJuego.pkl")
                print("Se carga juego")
            else:
                print(f"Tipo de gestor no reconocido al cargar: {gestor_type}")
                return

            with open(ruta_cargado, "rb") as archivo:
                m = pickle.load(archivo)
                self.gestor.cargar_estado(m)

        except Exception as e:
            print(f"Error al cargar: {str(e)}")
            import traceback
            traceback.print_exc()

        with open(ruta_cargado, "rb") as archivo:
            m = pickle.load(archivo)
            self.gestor.cargar_estado(m)

    #metodo que permite cargar un nonograma Objetivo para poder jugar
    def cargarObjetivo(self, ruta_cargado):
        try:
            print(f"Intentando cargar desde: {ruta_cargado}")

            with open(ruta_cargado, "rb") as archivo:
                m = pickle.load(archivo)
                self.gestor.cargar_objetivo(m)

        except Exception as e:
            print(f"\n¡ERROR al cargar objetivo!: {str(e)}")
            import traceback
            traceback.print_exc()
