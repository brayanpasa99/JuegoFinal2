from AbstractEscenario.CastilloOrco import CastilloOrco
from AbstractEscenario.IconosOrco import IconosOrco
from BuilderEscenario.BuilderAbstractE import BuilderAbstractE


class OrcoEscenario(BuilderAbstractE):

    def getIconos(self):
        return IconosOrco().getIconos(3)

    def getSCastillo(self):
        return CastilloOrco().getSCastillo(3)
