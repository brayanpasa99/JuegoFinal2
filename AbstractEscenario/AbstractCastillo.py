import abc


class AbstractCastillo():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getSCastillo(self):
        pass
