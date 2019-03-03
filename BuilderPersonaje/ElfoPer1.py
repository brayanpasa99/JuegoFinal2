from AbstractPersonaje.AtacarElfo import AtacarElfo
from AbstractPersonaje.CaminarElfo import CaminarElfo
from AbstractPersonaje.MorirElfo import MorirElfo
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class ElfoPer1(BuilderAbstract):

    def getSAtacar(self):
        return AtacarElfo().getSAtacar('Elfo1', 5)

    def getSCaminar(self):
        return CaminarElfo().getSCaminar('Elfo1', 3)

    def getSMorir(self):
        return MorirElfo().getSMorir('Elfo1', 5)
