from AbstractPersonaje.AtacarGuerrero import AtacarGuerrero
from AbstractPersonaje.CaminarGuerrero import CaminarGuerrero
from AbstractPersonaje.MorirGuerrero import MorirGuerrero
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class GuerreroPer3(BuilderAbstract):

    def getSAtacar(self):
        return AtacarGuerrero().getSAtacar('Guerrero3', 7)

    def getSCaminar(self):
        return CaminarGuerrero().getSCaminar('Guerrero3', 7)

    def getSMorir(self):
        return MorirGuerrero().getSMorir('Guerrero3', 7)
