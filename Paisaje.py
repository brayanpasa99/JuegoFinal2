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

    def setParametros(self, segundo, raza):
        self.segundo = segundo
        self.raza = raza
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
        if not self.segundo:
            ventana.blit(Castillo[0].image, Castillo[0].rect)
            ventana.blit(Iconos[0].image, Iconos[0].rect)


