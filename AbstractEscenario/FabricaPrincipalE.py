import abc

class FabricaPrincipalE():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def crearIElfo(self):
        pass

    @abc.abstractmethod
    def crearIOrco(self):
        pass

    @abc.abstractmethod
    def crearIGuerrero(self):
        pass
