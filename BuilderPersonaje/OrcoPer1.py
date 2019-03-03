from AbstractPersonaje.AtacarOrco import AtacarOrco
from AbstractPersonaje.CaminarOrco import CaminarOrco
from AbstractPersonaje.MorirOrco import MorirOrco
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class OrcoPer1(BuilderAbstract):

    def getSAtacar(self):
        return AtacarOrco().getSAtacar('Orco1', 7)

    def getSCaminar(self):
        return CaminarOrco().getSCaminar('Orco1', 7)

    def getSMorir(self):
        return MorirOrco().getSMorir('Orco1', 7)
