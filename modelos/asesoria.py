
from modelos.servicio import Servicio


class Asesoria(Servicio):

    def __init__(self, identificador, nombre, precio_base, especialidad):

        super().__init__(identificador, nombre, precio_base)

        self.__especialidad = especialidad

        self.validar_parametros()

    def calcular_costo(self, duracion, descuento=0):

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero")

        if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        subtotal = self._precio_base * duracion

        return subtotal - (subtotal * descuento / 100)

    def describir_servicio(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio por hora: ${self._precio_base}\n"
            f"Especialidad: {self.__especialidad}"
        )

    def validar_parametros(self):

        if not isinstance(self._precio_base, (int, float)) or self._precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if not isinstance(self.__especialidad, str) or not self.__especialidad.strip():
            raise ValueError("La especialidad es obligatoria")
