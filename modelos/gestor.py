from utilidades.log_config import logger
from excepciones.errores import ClienteNoValidoError
from excepciones.errores import ServicioNoDisponibleError
from excepciones.errores import ReservaNoValidaError
class Gestor:

    def __init__(self):

        # Listas para almacenar la información
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def agregar_cliente(self, cliente):

        for cliente_existente in self.__clientes:

            if cliente_existente.identificador == cliente.identificador:
                logger.warning("Intento de registrar un cliente duplicado")
                raise ClienteNoValidoError(
    "Ya existe un cliente con ese identificador"
)
          

        self.__clientes.append(cliente)
        logger.info("Cliente registrado correctamente")
        print("Cliente registrado correctamente")

    # Registrar servicios
    def agregar_servicio(self, servicio):

        for servicio_existente in self.__servicios:

            if servicio_existente.identificador == servicio.identificador:
                logger.warning("Intento de registrar un servicio duplicado")
                raise ServicioNoDisponibleError(
    "Ya existe un servicio con ese identificador"
)
                

        self.__servicios.append(servicio)
        logger.info("Servicio registrado correctamente")
        print("Servicio registrado correctamente")
    # Registrar reservas
    def agregar_reserva(self, reserva):

        for reserva_existente in self.__reservas:

            if reserva_existente.identificador == reserva.identificador:
                logger.warning("Intento de registrar una reserva duplicada")
                raise ReservaNoValidaError(
                    "Ya existe una reserva con ese identificador"
                )

        self.__reservas.append(reserva)
        logger.info("Reserva registrada correctamente")
        print("Reserva registrada correctamente")

    # Mostrar todos los clientes
    def listar_clientes(self):

        return self.__clientes

    # Mostrar todos los servicios
    def listar_servicios(self):

        return self.__servicios

    # Mostrar todas las reservas
    def listar_reservas(self):

        return self.__reservas
