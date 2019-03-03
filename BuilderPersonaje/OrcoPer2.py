from AbstractPersonaje.AtacarOrco import AtacarOrco
from AbstractPersonaje.CaminarOrco import CaminarOrco
from AbstractPersonaje.MorirOrco import MorirOrco
from BuilderPersonaje.BuilderAbstract import BuilderAbstract


class OrcoPer2(BuilderAbstract):

    def getSAtacar(self):
        return AtacarOrco().getSAtacar('Orco2', 7)

    def getSCaminar(self):
        return CaminarOrco().getSCaminar('Orco2', 7)

    def getSMorir(self):
        return MorirOrco().getSMorir('Orco2', 7)
