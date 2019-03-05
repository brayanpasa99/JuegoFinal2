from AbstractEscenario.CastilloElfo import CastilloElfo
from AbstractEscenario.CastilloGuerrero import CastilloGuerrero
from AbstractEscenario.CastilloOrco import CastilloOrco
from AbstractEscenario.FabricaPrincipalE import FabricaPrincipalE


class FabricaCastillo(FabricaPrincipalE):

    def crearIElfo(self):
        return CastilloElfo().getSCastillo(3)

    def crearIGuerrero(self):
        return CastilloGuerrero().getSCastillo(3)

    def crearIOrco(self):
        return CastilloOrco().getSCastillo(3)
