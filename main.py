from modelos.cliente import Cliente
from modelos.sala import Sala
from modelos.reserva import Reserva
from modelos.gestor import Gestor

from excepciones.errores import (
    ClienteNoValidoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError
)

from utilidades.log_config import logger
# 1. Crear un cliente
cliente1 = Cliente(
    1,
    "Carlos Ramirez",
    "carlos@gmail.com",
    "3001234567"
)

# 2. Crear una sala
sala1 = Sala(
    1,
    "Sala de reuniones",
    50000,
    10
)

# 3. Crear una reserva
reserva1 = Reserva(
    1,
    cliente1,
    sala1,
    3
)

# 4. Mostrar la información
print(reserva1.mostrar_informacion())
reserva1.confirmar()

print("DESPUÉS DE CONFIRMAR:")
print(reserva1.mostrar_informacion())
reserva1.cancelar()

print("DESPUÉS DE CANCELAR:")
print(reserva1.mostrar_informacion())
# Crear una nueva reserva para probar el procesamiento
reserva2 = Reserva(
    2,
    cliente1,
    sala1,
    2
)

reserva2.confirmar()
reserva2.procesar()

print("DESPUÉS DE PROCESAR:")
print(reserva2.mostrar_informacion())
# Crear el administrador del sistema
gestor = Gestor()

# Registrar el cliente
gestor.agregar_cliente(cliente1)

# Mostrar los clientes registrados
print("CLIENTES REGISTRADOS:")

for cliente in gestor.listar_clientes():
    print(cliente.mostrar_informacion())

# Registrar servicios
gestor.agregar_servicio(sala1)

# Mostrar los servicios registrados
print("SERVICIOS REGISTRADOS:")

for servicio in gestor.listar_servicios():
    print(servicio.describir_servicio())
    print("-------------------------")

# Registrar reservas
gestor.agregar_reserva(reserva1)
gestor.agregar_reserva(reserva2)

# Mostrar las reservas registradas
print("RESERVAS REGISTRADAS:")

for reserva in gestor.listar_reservas():
    print(reserva.mostrar_informacion())
    print("-------------------------")

# PRUEBA DE CLIENTE DUPLICADO

print("PRUEBA DE CLIENTE DUPLICADO:")

try:

    cliente_duplicado = Cliente(
        1,
        "Pedro Lopez",
        "pedro@gmail.com",
        "3101234567"
    )

    gestor.agregar_cliente(cliente_duplicado)

except ClienteNoValidoError as error:

    print("ERROR CONTROLADO:", error)

# PRUEBA DE SERVICIO DUPLICADO

print("PRUEBA DE SERVICIO DUPLICADO:")

try:

    gestor.agregar_servicio(sala1)

except ServicioNoDisponibleError as error:

    print("ERROR CONTROLADO:", error)

# PRUEBA DE RESERVA DUPLICADA

print("PRUEBA DE RESERVA DUPLICADA:")

try:

    gestor.agregar_reserva(reserva1)

except ReservaNoValidaError as error:

    print("ERROR CONTROLADO:", error)

logger.info("El sistema Software FJ se ha iniciado correctamente")

print("PRUEBA DE REGISTRO:")
print("Se ha enviado un evento al archivo de logs.")
print("\nPRUEBA DE MANEJO AVANZADO DE EXCEPCIONES:")

try:
    resultado = 100 / 5

except ZeroDivisionError as error:
    print("ERROR:", error)

else:
    print("Operación realizada correctamente:", resultado)

finally:
    print("Finalizó el proceso de cálculo")
print("\nPRUEBA DE ENCADENAMIENTO DE EXCEPCIONES:")

try:
    try:
        numero = int("hola")

    except ValueError as error:
        raise RuntimeError(
            "No fue posible convertir el texto a número"
        ) from error

except RuntimeError as error:
    print("ERROR CONTROLADO:", error)    
    print("PRUEBA DE CLIENTE CON NOMBRE VACÍO:")

try:
    cliente_invalido = Cliente(
        3,
        "",
        "invalido@gmail.com",
        "3001234567"
    )

except ValueError as error:
    print("ERROR CONTROLADO:", error)
    print("PRUEBA DE CORREO INVÁLIDO:")

try:
    cliente_invalido = Cliente(
        4,
        "Pedro Lopez",
        "pedrogmail.com",
        "3001234567"
    )

except ValueError as error:
    print("ERROR CONTROLADO:", error)
    print("PRUEBA DE RESERVA CON DURACIÓN INVÁLIDA:")

try:
    reserva_invalida = Reserva(
        3,
        cliente1,
        sala1,
        0
    )

except ReservaNoValidaError as error:
    print("ERROR CONTROLADO:", error)
    print("PRUEBA DE SERVICIO CON PRECIO INVÁLIDO:")

try:
    sala_invalida = Sala(
        2,
        "Sala de conferencias",
        0,
        20
    )

except ValueError as error:
    print("ERROR CONTROLADO:", error)