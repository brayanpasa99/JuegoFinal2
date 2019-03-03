from AbstractPersonaje.AtacarGuerrero import AtacarGuerrero
from AbstractPersonaje.CaminarGuerrero import CaminarGuerrero
from AbstractPersonaje.MorirGuerrero import MorirGuerrero
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class GuerreroPer1(BuilderAbstract):

    def getSAtacar(self):
        return AtacarGuerrero().getSAtacar('Guerrero1', 8)

    def getSCaminar(self):
        return CaminarGuerrero().getSCaminar('Guerrero1', 7)

    def getSMorir(self):
        return MorirGuerrero().getSMorir('Guerrero1', 7)
