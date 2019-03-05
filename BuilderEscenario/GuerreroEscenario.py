from AbstractEscenario.IconosGuerrero import IconosGuerrero
from BuilderEscenario.BuilderAbstractE import BuilderAbstractE


class GuerreroEscenario(BuilderAbstractE):

    def getIconos(self):
        return IconosGuerrero().getIconos(3)

    def getSCastillo(self):
        return CastilloGuerrero()
