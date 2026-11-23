
class ErrorSistema(Exception):
    pass


class ClienteNoValidoError(ErrorSistema):
    pass


class ServicioNoDisponibleError(ErrorSistema):
    pass


class ReservaNoValidaError(ErrorSistema):
    pass


class ReservaNoEncontradaError(ErrorSistema):
    pass
