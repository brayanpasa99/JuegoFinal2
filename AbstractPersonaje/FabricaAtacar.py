from AbstractPersonaje.AtacarElfo import AtacarElfo
from AbstractPersonaje.AtacarGuerrero import AtacarGuerrero
from AbstractPersonaje.AtacarOrco import AtacarOrco
from AbstractPersonaje.FabricaPrincipal import FabricaPrincipal


class FabricaAtacar(FabricaPrincipal):

    def crearSElfo(self):
        return AtacarElfo().getSAtacar()

    def crearSOrco(self):
        return AtacarOrco().getSAtacar()

    def crearSGuerrero(self):
        return AtacarGuerrero().getSAtacar()
