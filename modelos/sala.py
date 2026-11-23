
from modelos.servicio import Servicio


class Sala(Servicio):

    def __init__(self, identificador, nombre, precio_base, capacidad):

        super().__init__(identificador, nombre, precio_base)

        self.__capacidad = capacidad

        self.validar_parametros()

    def calcular_costo(self, duracion):

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero")

        return self._precio_base * duracion

    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio por hora: ${self._precio_base}\n"
            f"Capacidad: {self.__capacidad} personas"
        )

    def validar_parametros(self):

        if not isinstance(self._precio_base, (int, float)) or self._precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if not isinstance(self.__capacidad, int) or self.__capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo")
