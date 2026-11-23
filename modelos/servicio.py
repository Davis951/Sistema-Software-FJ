
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, identificador, nombre, precio_base):

        self._identificador = identificador
        self._nombre = nombre
        self._precio_base = precio_base
    @property
    def identificador(self):
        return self._identificador
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
