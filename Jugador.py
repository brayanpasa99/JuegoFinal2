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

    def __init__(self):
        __segundo = False
        __raza = ''

    def setParametros(self, segundo, raza):
        self.__segundo = segundo
        self.__raza = raza

    def crearJugador(self):

        director = DirectorPersonaje()
        luchadores = []

        if self.__raza == 'Elfos':
            Elfo1 = ElfoPer1()
            Elfo2 = ElfoPer2()
            Elfo3 = ElfoPer3()

            director.setBuilder(Elfo1)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Elfo2)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Elfo3)
            luchadores.append(director.getPersonaje().getSprites())

            return luchadores

        if self.__raza == 'Orcos':
            Orco1 = OrcoPer1()
            Orco2 = OrcoPer2()
            Orco3 = OrcoPer3()

            director.setBuilder(Orco1)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Orco2)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Orco3)
            luchadores.append(director.getPersonaje().getSprites())

            return luchadores

        if self.__raza == 'Guerreros':
            Guerrero1 = GuerreroPer1()
            Guerrero2 = GuerreroPer2()
            Guerrero3 = GuerreroPer3()

            director.setBuilder(Guerrero1)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Guerrero2)
            luchadores.append(director.getPersonaje().getSprites())

            director.setBuilder(Guerrero3)
            luchadores.append(director.getPersonaje().getSprites())

            return luchadores
