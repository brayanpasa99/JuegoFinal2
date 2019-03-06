import pygame

from BuilderEscenario.DirectorEscenario import DirectorEscenario
from BuilderEscenario.ElfoEscenario import ElfoEscenario
from BuilderEscenario.GuerreroEscenario import GuerreroEscenario
from BuilderEscenario.OrcoEscenario import OrcoEscenario

COLOR_TEXTO = (243, 255, 0)

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
        Fuente = pygame.font.SysFont("Arial", 30)
        reloj = pygame.time.Clock()
        Castillo = self.EscenarioFinal.getSprites()[0]
        Iconos = self.EscenarioFinal.getSprites()[1]
        if self.segundo:
            Castillo[self.estadoCastillo].rect.topleft = (900, 100)
            ventana.blit(Castillo[self.estadoCastillo].image, Castillo[self.estadoCastillo].rect)

            LabelJ = Fuente.render("J", 0, COLOR_TEXTO)
            Iconos[0].rect.topleft = (710, 100)
            ventana.blit(LabelJ, (730, 60))
            ventana.blit(Iconos[0].image, Iconos[0].rect)

            LabelK = Fuente.render("K", 0, COLOR_TEXTO)
            Iconos[1].rect.topleft = (770, 100)
            ventana.blit(LabelK, (790, 60))
            ventana.blit(Iconos[1].image, Iconos[1].rect)

            LabelL = Fuente.render("L", 0, COLOR_TEXTO)
            Iconos[2].rect.topleft = (830, 100)
            ventana.blit(LabelL, (850, 60))
            ventana.blit(Iconos[2].image, Iconos[2].rect)
        elif not self.segundo:
            Castillo[self.estadoCastillo].rect.topleft = (-100, 100)
            ventana.blit(pygame.transform.flip(Castillo[self.estadoCastillo].image, True, False), Castillo[self.estadoCastillo].rect)

            Label1 = Fuente.render("1", 0, COLOR_TEXTO)
            Iconos[0].rect.topleft = (200, 100)
            ventana.blit(Label1, (220, 60))
            ventana.blit(Iconos[0].image, Iconos[0].rect)

            Label2 = Fuente.render("2", 0, COLOR_TEXTO)
            Iconos[1].rect.topleft = (260, 100)
            ventana.blit(Label2, (280, 60))
            ventana.blit(Iconos[1].image, Iconos[1].rect)

            Label3 = Fuente.render("3", 0, COLOR_TEXTO)
            Iconos[2].rect.topleft = (320, 100)
            ventana.blit(Label3, (340, 60))
            ventana.blit(Iconos[2].image, Iconos[2].rect)


