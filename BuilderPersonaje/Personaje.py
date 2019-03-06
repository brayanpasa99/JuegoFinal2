import copy


class Personaje:

    def __init__(self):
        self.atacar  = []
        self.caminar  = []
        self.morir    = []
        

    def setSAtacar(self, atacar):
        self.__atacar = atacar

    def setSCaminar(self, caminar):
        self.__caminar = caminar

    def setSMorir(self, morir):
        self.__morir = morir

    def getSAtacar(self):
        return self.__atacar

    def getSMorir(self):
        return self.__morir

    def getSCaminar(self):
        return  self.__caminar

    def clone(self, copiar):
        return copy.deepcopy(copiar)
   
    #def getSprites(self):
        #return [self.__atacar, self.__morir, self.__caminar]

