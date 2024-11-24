import copy
import os
import pickle

from vidas import HP_counter


class Caretaker:
    def __init__(self, gestor):
        self.gestor = gestor
        self.mementos = []
        self.ruta_guardado = None
        self.undo_stack = []
        self.redo_stack = []
        self.EstadoBase = None

    def deshacer(self):
        if len(self.undo_stack) >= 1:
            # Guardar el estado actual en la pila de rehacer
            self.redo_stack.append(self.gestor.guardar_estado())
            # Cargar el último memento
            m = self.undo_stack.pop()
            self.mementos.append(m)
            self.gestor.cargar_estado(m)
            self.guardar()
        else:
            self.gestor.cargar_estado(copy.deepcopy(self.EstadoBase))

    def rehacer(self):
        if self.redo_stack:
            # Guardar el estado actual en la pila de deshacer
            self.undo_stack.append(self.gestor.guardar_estado())
            # Cargar el último memento de rehacer
            m = self.redo_stack.pop()
            self.mementos.append(m)
            self.gestor.cargar_estado(m)
            self.guardar()

    def borrarPartida(self):
        try:
            ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartida", "partidaGuardada.pkl")
            if os.path.exists(ruta_guardado):
                os.remove(ruta_guardado)
                print("Partida guardada eliminada con éxito.")
            else:
                print("No se encontró ninguna partida guardada para eliminar.")
        except Exception as e:
            print(f"Error al intentar borrar la partida: {str(e)}")

    def añadirMemento(self):
        m = self.gestor.guardar_estado()
        self.mementos.append(m)  #Se agrega memento al stack de mementos
        self.undo_stack.append(m) #Se agrega memento al stack de undo
        self.redo_stack.clear()
        self.guardar() #Se guarda el memento en memoria

    #Metodo para guardar la partida en curso en memoria
    def guardar(self):
        try:
            gestor_type = type(self.gestor).__name__

            # Usar el nombre de la clase directamente
            if gestor_type == "GestorCreacion":
                ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion", "guardadoCreacion.pkl")
            elif gestor_type == "GestorJuego":
                ruta_guardado = os.path.join(os.path.dirname(__file__), "guardadoPartida", "partidaGuardada.pkl")
            else:
                print(f"Tipo de gestor no reconocido: {gestor_type}")
                return

            with open(ruta_guardado, "wb") as archivo:
                pickle.dump(self.mementos[-1], archivo)

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
                ruta_cargado = os.path.join(os.path.dirname(__file__), "guardadoPartidaGestorCreacion", "guardadoCreacion.pkl")
            elif gestor_type == "GestorJuego":
                print("Cargando desde GestorJuego")
                ruta_cargado = os.path.join(os.path.dirname(__file__), "guardadoPartida", "partidaGuardada.pkl")
            else:
                print(f"Tipo de gestor no reconocido al cargar: {gestor_type}")
                return

            with open(ruta_cargado, "rb") as archivo:
                m = pickle.load(archivo)
                print(f"Memento cargado: {m}")  # Verifica el contenido del memento
                self.gestor.cargar_estado(m)

            if gestor_type == "GestorJuego":
                print("Cargando pistas del juego")
                print(f"Vidas: {m.get_state()[2]}")
                vidas = HP_counter(m.get_state()[2])
                self.gestor.contadorVidas = vidas
                self.gestor.numVidas = vidas.lives
                self.gestor.pistasFilas()
                self.gestor.pistasColumnas()
                m = self.gestor.guardar_estado()
                self.EstadoBase = m
                #self.mementos.append(m)  # Se agrega memento al stack de mementos
                #self.undo_stack.append(m)  # Se agrega memento al stack de undo
               # self.redo_stack.clear()

        except FileNotFoundError:
            print("¡ERROR! El archivo de guardado no se encontró.")
        except Exception as e:
            print(f"Error al cargar: {str(e)}")
            import traceback
            traceback.print_exc()

    #Metodo que permite guardar en catalogo el nonograma creado por usuario
    def añadir_en_catalogo(self, tamaño, nombre):
        carpeta = ""
        if(tamaño == 10):
            carpeta = "10x10"
        elif(tamaño == 15):
            carpeta = "15x15"
        elif(tamaño == 20):
            carpeta = "20x20"
        ruta_catalogo = os.path.join(os.path.dirname(__file__), "catalogo", carpeta, nombre + ".pkl")
        self.gestor.guardar_estado()
        with open(ruta_catalogo, "wb") as archivo:
            pickle.dump(self.mementos[-1], archivo)


    #metodo que permite cargar un nonograma Objetivo para poder jugar
    def cargarObjetivo(self, ruta_cargado):
        try:
            print(f"Intentando cargar desde: {ruta_cargado}")

            with open(ruta_cargado, "rb") as archivo:
                m = pickle.load(archivo)
                self.gestor.cargar_objetivo(m)
                self.EstadoBase = self.gestor.guardar_estado()
                #self.mementos.append(m)  # Se agrega memento al stack de mementos
                #self.undo_stack.append(m)  # Se agrega memento al stack de undo
                #self.redo_stack.clear()

        except Exception as e:
            print(f"\n¡ERROR al cargar objetivo!: {str(e)}")
            import traceback
            traceback.print_exc()
