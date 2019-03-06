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
    build1=None
    build2=None
    build3=None

    def __init__(self):
        segundo = False
        raza = ''
        
        

    def setParametros(self, segundo, raza):
        self.segundo = segundo
        self.raza = raza
        if self.raza == 'Elfos':
            self.build1 = ElfoPer1()
            self.build2 = ElfoPer2()
            self.build3 = ElfoPer3()
        elif self.raza == 'Orcos':
            self.build1 = OrcoPer1()
            self.build2 = OrcoPer2()
            self.build3 = OrcoPer3()
        elif self.raza == 'Guerreros':
            self.build1 = GuerreroPer1()
            self.build2 = GuerreroPer2()
            self.build3 = GuerreroPer3()

    def crearPersonaje(self,id):

        director = DirectorPersonaje()
        
        
        if id == 1:
            director.setBuilder(self.build1)
            
        elif id == 2:
            director.setBuilder(self.build2)
            
        elif id == 3:
            director.setBuilder(self.build3)

        self.Ejercito.append(director.getPersonaje())


    def dibujar(self, ventana):
        reloj = pygame.time.Clock()
        for i in range(0, len(self.Ejercito)):
            Char=self.Ejercito[i]
<<<<<<< HEAD
            for j in range(0,len(Char.getSprites())):
                Char.getSprites()[j].rect.x=Char.getSprites()[j].rect.x + 5
                Char.getSprites()[j].rect.y=375
                ventana.blit(Char.getSprites()[j].image,Char.getSprites()[j].rect)                
                pygame.display.update(Char.getSprites()[j].rect)
                reloj.tick(80)
=======
            for j in range(0,len(Char.getSCaminar())):
                Char.getSCaminar()[j].rect.x=Char.getSCaminar()[j].rect.x + 5
                Char.getSCaminar()[j].rect.y=Char.getSCaminar()[j].rect.y
                ventana.blit(Char.getSCaminar()[j].image,Char.getSCaminar()[j].rect)
                pygame.display.update(Char.getSCaminar()[j].rect)
                reloj = pygame.time.Clock()
                reloj.tick(27)


             
        """ if True:
            for i in range(0, len(self.__luchadores[0].getSCaminar())):
                self.__luchadores[0].getSCaminar()[i].rect.x = self.__luchadores[0].getSCaminar()[i].rect.x+ 5
                self.__luchadores[0].getSCaminar()[i].rect.y = self.__luchadores[0].getSCaminar()[i].rect.y
                ventana.blit(self.__luchadores[0].getSCaminar()[i].image, self.__luchadores[0].getSCaminar()[i].rect)
>>>>>>> dab1b889666cce5795f2b054184983726952c100
                



