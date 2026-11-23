
from modelos.servicio import Servicio


class Equipo(Servicio):

    def __init__(self, identificador, nombre, precio_base, cantidad_disponible):

        super().__init__(identificador, nombre, precio_base)

        self.__cantidad_disponible = cantidad_disponible

        self.validar_parametros()

    def calcular_costo(self, duracion, cantidad=1):

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        if cantidad > self.__cantidad_disponible:
            raise ValueError("No hay suficientes equipos disponibles")

        return self._precio_base * duracion * cantidad

    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio por equipo y hora: ${self._precio_base}\n"
            f"Equipos disponibles: {self.__cantidad_disponible}"
        )

    def validar_parametros(self):

        if not isinstance(self._precio_base, (int, float)) or self._precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if not isinstance(self.__cantidad_disponible, int) or self.__cantidad_disponible <= 0:
            raise ValueError("La cantidad disponible debe ser un entero positivo")
