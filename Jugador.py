import copy

import pygame

from BuilderPersonaje.DirectorPersonaje import DirectorPersonaje
from BuilderPersonaje.ElfoPer1 import ElfoPer1
from BuilderPersonaje.ElfoPer2 import ElfoPer2
from BuilderPersonaje.ElfoPer3 import ElfoPer3
from BuilderPersonaje.GuerreroPer1 import GuerreroPer1
from BuilderPersonaje.GuerreroPer2 import GuerreroPer2
from BuilderPersonaje.GuerreroPer3 import GuerreroPer3
from BuilderPersonaje.OrcoPer1 import OrcoPer1
from BuilderPersonaje.OrcoPer2 import OrcoPer2
from BuilderPersonaje.OrcoPer3 import OrcoPer3


class Jugador():

    Ejercito=[]

    def __init__(self):
        segundo = False
        raza = ''
        luchadores = []
        

    def setParametros(self, segundo, raza):
        self.segundo = segundo
        self.raza = raza

    def crearJugador(self):

        director = DirectorPersonaje()
        luchadores = []

        if self.raza == 'Elfos':
            Elfo1 = ElfoPer1()
            Elfo2 = ElfoPer2()
            Elfo3 = ElfoPer3()

            director.setBuilder(Elfo1)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Elfo2)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Elfo3)
            luchadores.append(director.getPersonaje())

            self.luchadores = luchadores

        if self.raza == 'Orcos':
            Orco1 = OrcoPer1()
            Orco2 = OrcoPer2()
            Orco3 = OrcoPer3()

            director.setBuilder(Orco1)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Orco2)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Orco3)
            luchadores.append(director.getPersonaje())

            self.luchadores = luchadores

        if self.raza == 'Guerreros':
            Guerrero1 = GuerreroPer1()
            Guerrero2 = GuerreroPer2()
            Guerrero3 = GuerreroPer3()

            director.setBuilder(Guerrero1)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Guerrero2)
            luchadores.append(director.getPersonaje())

            director.setBuilder(Guerrero3)
            luchadores.append(director.getPersonaje())

            self.luchadores = luchadores

    def CrearPersonaje(self,id):
        self.Ejercito.append(copy.deepcopy(self.luchadores[id]))
        #self.Ejercito.append(self.luchadores[id].clone(self.luchadores[id]))
        print("se crea un personaje ")
        print(len(self.Ejercito))

    def dibujar(self, ventana):

        for i in range(0, len(self.Ejercito)):
            Char=self.Ejercito[i]
            for j in range(0,len(Char.getSCaminar())):
                Char.getSCaminar()[j].rect.x=Char.getSCaminar()[j].rect.x + 5
                Char.getSCaminar()[j].rect.y=Char.getSCaminar()[j].rect.y
                ventana.blit(Char.getSCaminar()[j].image,Char.getSCaminar()[j].rect)
                pygame.display.flip()
                reloj = pygame.time.Clock()
                reloj.tick(20)

             
        """ if True:
            for i in range(0, len(self.__luchadores[0].getSCaminar())):
                self.__luchadores[0].getSCaminar()[i].rect.x = self.__luchadores[0].getSCaminar()[i].rect.x+ 5
                self.__luchadores[0].getSCaminar()[i].rect.y = self.__luchadores[0].getSCaminar()[i].rect.y
                ventana.blit(self.__luchadores[0].getSCaminar()[i].image, self.__luchadores[0].getSCaminar()[i].rect)
                
                pygame.display.flip()
                reloj = pygame.time.Clock()
                reloj.tick(20) """

    def update(self):
        pass

