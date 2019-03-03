from BuilderPersonaje.DirectorPersonaje import DirectorPersonaje
from BuilderPersonaje.PElfo1 import PElfo1


def main():
    Elfo1 = PElfo1()

    director = DirectorPersonaje()

    # Build Jeep
    print "Jeep"
    director.setBuilder(Elfo1)
    elfo = director.getPersonaje()
