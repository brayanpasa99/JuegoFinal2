from AbstractPersonaje.AtacarElfo import AtacarElfo
from AbstractPersonaje.CaminarElfo import CaminarElfo
from AbstractPersonaje.MorirElfo import MorirElfo
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class ElfoPer3(BuilderAbstract):

    def getSAtacar(self):
        return AtacarElfo().getSAtacar('Elfo3', 5)

    def getSCaminar(self):
        return CaminarElfo().getSCaminar('Elfo3', 3)

    def getSMorir(self):
        return MorirElfo().getSMorir('Elfo3', 5)
