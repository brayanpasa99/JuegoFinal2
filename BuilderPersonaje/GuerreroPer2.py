from AbstractPersonaje.AtacarGuerrero import AtacarGuerrero
from AbstractPersonaje.CaminarGuerrero import CaminarGuerrero
from AbstractPersonaje.MorirGuerrero import MorirGuerrero
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class GuerreroPer2(BuilderAbstract):

    def getSAtacar(self):
        return AtacarGuerrero().getSAtacar('Guerrero2', 7)

    def getSCaminar(self):
        return CaminarGuerrero().getSCaminar('Guerrero2', 7)

    def getSMorir(self):
        return MorirGuerrero().getSMorir('Guerrero2', 7)
