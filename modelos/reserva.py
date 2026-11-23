
from datetime import datetime

from excepciones.errores import ReservaNoValidaError


class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion):

        if cliente is None:
            raise ReservaNoValidaError("Debe seleccionar un cliente")

        if servicio is None:
            raise ReservaNoValidaError("Debe seleccionar un servicio")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaNoValidaError("La duración debe ser mayor que cero")

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "PENDIENTE"
        self.__fecha = datetime.now()

    @property
    def identificador(self):
        return self.__identificador  

    
    def confirmar(self):

        if self.__estado != "PENDIENTE":
            raise ReservaNoValidaError(
                "Solamente se pueden confirmar reservas pendientes"
            )


        self.__estado = "CONFIRMADA"

    def cancelar(self):

        if self.__estado == "CANCELADA":
            raise ReservaNoValidaError(
                "La reserva ya se encuentra cancelada"
            )

        self.__estado = "CANCELADA"

    def procesar(self):

        if self.__estado != "CONFIRMADA":
            raise ReservaNoValidaError(
                "La reserva debe estar confirmada para procesarse"
            )

        self.__estado = "PROCESADA"

    def calcular_total(self):

        return self.__servicio.calcular_costo(self.__duracion)

    def mostrar_informacion(self):

        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente:\n{self.__cliente.mostrar_informacion()}\n"
            f"Servicio:\n{self.__servicio.describir_servicio()}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Total: ${self.calcular_total():,.2f}\n"
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}"
        )