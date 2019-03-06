from Facade.ElegirRaza import ElegirRaza
from Facade.PantallaPrincipal import PantallaPrincipal


class Fachada():

    def __init__(self):
        self._pantallaprincipal = PantallaPrincipal()
        self._elegirRaza = ElegirRaza()

    def operacion(self):
        self._pantallaprincipal.mostrarpantalla()
