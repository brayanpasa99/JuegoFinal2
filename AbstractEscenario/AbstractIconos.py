import abc


class AbstractIconos():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getIconos(self):
        pass
