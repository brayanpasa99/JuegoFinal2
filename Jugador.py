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


class JugadorIzq():

    rectE=[]
    Ejercito=[]
    build1=None
    build2=None
    build3=None

    def __init__(self):
        raza = ''
        
        

    def setParametros(self, raza):
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
      
        self.Ejercito.append(director.getPersonaje(1))
        self.rectE.append(self.Ejercito[len(self.Ejercito)-1].getRect())
        


    def dibujar(self, ventana):
        reloj = pygame.time.Clock()
        if len(self.Ejercito)>0:

            for i in range(0, len(self.Ejercito)):
                Char=self.Ejercito[i]
                Char.setRectSprites()
                for j in range(0,len(Char.getSprites())):
                    Char.setRect(Char.getVelocidad())
                    ventana.blit(Char.getSprites()[j].image,Char.getRect())    
                    pygame.display.update(Char.getRect())
                reloj.tick(60)
                
class JugadorDer():

    rectE=[]    
    Ejercito=[]
    build1=None
    build2=None
    build3=None

    def __init__(self):
        raza = ''
        
    

    def setParametros(self, raza):
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

        
        self.Ejercito.append(director.getPersonaje(0))
        self.rectE.append(self.Ejercito[len(self.Ejercito)-1].getRect())

        


    def dibujar(self, ventana):
        reloj = pygame.time.Clock()
        if len(self.Ejercito)>0:
            
            for i in range(0, len(self.Ejercito)):
                Char=self.Ejercito[i]
                Char.setRectSprites()
                for j in range(0, len(Char.getSprites())):
                    Char.setRect(-1*Char.getVelocidad())
                    aux=pygame.transform.flip(Char.getSprites()[j].image,True,False)
                    ventana.blit(aux, Char.getRect())                
                    pygame.display.update(Char.getRect())
                reloj.tick(60)
                    



