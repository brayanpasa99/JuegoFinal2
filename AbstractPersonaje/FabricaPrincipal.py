import abc

class FabricaPrincipal():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def crearSElfo(self):
        pass

    @abc.abstractmethod
    def crearSOrco(self):
        pass

    @abc.abstractmethod
    def crearSGuerrero(self):
        pass
