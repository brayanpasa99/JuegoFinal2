import pygame

from BuilderEscenario.DirectorEscenario import DirectorEscenario
from BuilderEscenario.ElfoEscenario import ElfoEscenario
from BuilderEscenario.GuerreroEscenario import GuerreroEscenario
from BuilderEscenario.OrcoEscenario import OrcoEscenario


class Paisaje():

    build1=None
    EscenarioFinal = None

    def __init__(self):
        self.segundo = False
        self.raza = ''
        self.estadoCastillo = 0

    def setParametros(self, segundo, raza, n_estado):
        self.segundo = segundo
        self.raza = raza
        self.estadoCastillo = n_estado
        if self.raza == 'Elfos':
            self.build1 = ElfoEscenario()
        elif self.raza == 'Orcos':
            self.build1 = OrcoEscenario()
        elif self.raza == 'Guerreros':
            self.build1 = GuerreroEscenario()

    def crearPaisaje(self):

        director = DirectorEscenario()

        director.setBuilder(self.build1)

        self.EscenarioFinal = director.getEscenario()

    def dibujar(self, ventana):
        reloj = pygame.time.Clock()
        Castillo = self.EscenarioFinal.getSprites()[0]
        Iconos = self.EscenarioFinal.getSprites()[1]
        if self.segundo:
            Castillo[self.estadoCastillo].rect.topleft = (900, 100)
            ventana.blit(Castillo[self.estadoCastillo].image, Castillo[self.estadoCastillo].rect)
            Iconos[0].rect.topleft = (710, 100)
            ventana.blit(Iconos[0].image, Iconos[0].rect)
            Iconos[1].rect.topleft = (770, 100)
            ventana.blit(Iconos[1].image, Iconos[1].rect)
            Iconos[2].rect.topleft = (830, 100)
            ventana.blit(Iconos[2].image, Iconos[2].rect)
        elif not self.segundo:
            Castillo[self.estadoCastillo].rect.topleft = (-100, 100)
            ventana.blit(pygame.transform.flip(Castillo[self.estadoCastillo].image, True, False), Castillo[self.estadoCastillo].rect)
            Iconos[0].rect.topleft = (200, 100)
            ventana.blit(Iconos[0].image, Iconos[0].rect)
            Iconos[1].rect.topleft = (260, 100)
            ventana.blit(Iconos[1].image, Iconos[1].rect)
            Iconos[2].rect.topleft = (320, 100)
            ventana.blit(Iconos[2].image, Iconos[2].rect)


