import abc

class BuilderAbstract:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getSAtacar(self):
        pass

    @abc.abstractmethod
    def getSCaminar(self):
        pass

    @abc.abstractmethod
    def getSMorir(self):
        pass
