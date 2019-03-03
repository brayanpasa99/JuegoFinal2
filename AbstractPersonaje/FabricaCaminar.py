from AbstractPersonaje.CaminarElfo import CaminarElfo
from AbstractPersonaje.CaminarGuerrero import CaminarGuerrero
from AbstractPersonaje.CaminarOrco import CaminarOrco
from AbstractPersonaje.FabricaPrincipal import FabricaPrincipal


class FabricaCaminar(FabricaPrincipal):

    def crearSElfo(self):
        return CaminarElfo().getSCaminar()

    def crearSOrco(self):
        return CaminarOrco().getSCaminar()

    def crearSGuerrero(self):
        return CaminarGuerrero().getSCaminar()
