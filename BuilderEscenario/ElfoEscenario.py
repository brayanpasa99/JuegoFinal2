from AbstractEscenario.CastilloElfo import CastilloElfo
from AbstractEscenario.IconosElfo import IconosElfo
from BuilderEscenario.BuilderAbstractE import BuilderAbstractE


class ElfoEscenario(BuilderAbstractE):

    def getIconos(self):
        return IconosElfo().getIconos(3)

    def getSCastillo(self):
        return CastilloElfo().getSCastillo(3)
