import copy


class Personaje:
    
    velocidad=5
    Poder= 50
    Vida= 150
    enBatalla=False
    enEspera=False
    
    def __init__(self):
        self.atacar  = []
        self.caminar  = []
        self.morir    = []

    def getenBatalla(self):
        return self.enBatalla

    def getVida(self):
        return self.Vida

    def getPoder(self):
        return self.Poder
    
    def getVelocidad(self):
        if self.enBatalla or self.enEspera:
            return 0
        else:
            return 5
    
    def reducirVida(self,ataque):
        self.Vida=self.Vida-ataque

    def setenBatalla(self,estado):
        self.enBatalla = estado

    def setenEspera(self,estado):
        self.enEspera = estado

    def setSAtacar(self, atacar):
        self.atacar = atacar

    def setSCaminar(self, caminar):
        self.caminar = caminar

    def setSMorir(self, morir):
        self.morir = morir

    def getSprites(self):
        if self.enBatalla:
            return self.atacar
        elif self.enEspera:
            return self.caminar
        else:
            return self.caminar
    def setRectSprites(self, pos):
        for j in range(0,len(self.atacar)):
            self.atacar[j].rect.x=pos[0]
            self.atacar[j].rect.y=pos[1]
        for j in range(0,len(self.caminar)):
            self.caminar[j].rect.x=pos[0]
            self.caminar[j].rect.y=pos[1]
        for j in range(0,len(self.morir)):
            self.morir[j].rect.x=pos[0]
            self.morir[j].rect.y=pos[1]






    

