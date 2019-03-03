import abc

class FabricaPrincipal():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def crearSAtacar(self):
        pass

    @abc.abstractmethod
    def crearSCaminar(self):
        pass

    @abc.abstractmethod
    def crearMorir(self):
        pass
