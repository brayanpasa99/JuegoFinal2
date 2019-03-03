import abc


class AbstractSMorir():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getSMorir(self):
        pass
