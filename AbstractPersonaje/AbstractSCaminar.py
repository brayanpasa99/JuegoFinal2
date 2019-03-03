import abc


class AbstractSCaminar():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getSCaminar(self):
        pass
