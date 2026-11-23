
import modelos.entidad


class Cliente(modelos.entidad.Entidad):

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if not self.__nombre or not self.__nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio")

        if "@" not in self.__correo:
            raise ValueError("El correo electrónico no es válido")

        if not self.__telefono.isdigit() or len(self.__telefono) < 7:
            raise ValueError("El teléfono debe contener al menos 7 números")

    def mostrar_informacion(self):

        return (
            f"ID: {self._identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
