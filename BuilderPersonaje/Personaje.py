import copy


class Personaje:

    Poder= 50
    Vida= 150
    enBatalla=False

    def __init__(self):
        self.atacar  = []
        self.caminar  = []
        self.morir    = []
    
    def setenBatalla(self,estado):
        self.enBatalla = estado

    def setSAtacar(self, atacar):
        self.atacar = atacar

    def setSCaminar(self, caminar):
        self.caminar = caminar

    def setSMorir(self, morir):
        self.morir = morir

    def getSprites(self):
        if self.enBatalla:
            return self.atacar
        else:
            return self.caminar





    

