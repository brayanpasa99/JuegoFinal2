import abc

class BuilderAbstractE():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getIconos(self):
        pass

    @abc.abstractmethod
    def getSCastillo(self):
        pass
