from AbstractPersonaje.FabricaPrincipal import FabricaPrincipal
from AbstractPersonaje.MorirElfo import MorirElfo
from AbstractPersonaje.MorirGuerrero import MorirGuerrero
from AbstractPersonaje.MorirOrco import MorirOrco


class FabricaMorir(FabricaPrincipal):

    def crearSElfo(self):
        return MorirElfo().getSMorir()

    def crearSOrco(self):
        return MorirOrco().getSMorir()

    def crearSGuerrero(self):
        return MorirGuerrero().getSMorir()
