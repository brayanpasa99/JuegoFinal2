from AbstractPersonaje.AtacarElfo import AtacarElfo
from AbstractPersonaje.CaminarElfo import CaminarElfo
from AbstractPersonaje.MorirElfo import MorirElfo
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class ElfoPer2(BuilderAbstract):

    def getSAtacar(self):
        return AtacarElfo().getSAtacar('Elfo2', 5)

    def getSCaminar(self):
        return CaminarElfo().getSCaminar('Elfo2', 3)

    def getSMorir(self):
        return MorirElfo().getSMorir('Elfo2', 5)
