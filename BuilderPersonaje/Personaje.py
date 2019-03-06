import pygame

from pygame.locals import *

class Personaje:
    
    velocidad=5
    Poder= 50
    Vida= 500
    enBatalla=False
    enEspera=False

    def __init__(self,LadoJugador):
        self.atacar  = []
        self.caminar  = []
        self.morir    = []
        if LadoJugador==0:
            self.rect=pygame.Rect(900,375,50,50)
        elif LadoJugador==1:
            self.rect=pygame.Rect(100,375,50,50)
    def getRect(self):
        return self.rect

    def setRect(self,avance):
        self.rect.x=self.rect.x+avance

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
        for i in range(0,len(self.atacar)):
            self.atacar[i].setrect(self.rect)

    def setSCaminar(self, caminar):
        self.caminar = caminar
        for i in range(0,len(self.caminar)):
            self.caminar[i].setrect(self.rect)

    def setSMorir(self, morir):
        self.morir = morir
        for i in range(0,len(self.morir)):
            self.morir[i].setrect(self.rect)

    def getSprites(self):
        if self.enBatalla:
            return self.atacar
        elif self.enEspera:
            return self.caminar
        else:
            return self.caminar
    def setRectSprites(self):
        for j in range(0,len(self.atacar)):
            self.atacar[j].rect.x=self.rect.x
            self.atacar[j].rect.y=self.rect.y
        for j in range(0,len(self.caminar)):
            self.caminar[j].rect.x=self.rect.x
            self.caminar[j].rect.y=self.rect.y
        for j in range(0,len(self.morir)):
            self.morir[j].rect.x=self.rect.x
            self.morir[j].rect.y=self.rect.y
    





    

