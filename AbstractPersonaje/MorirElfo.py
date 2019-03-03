from AbstractPersonaje.AbstractSMorir import AbstractSMorir
from PersonajesSprites import PersonajesSprites


class MorirElfo(AbstractSMorir):

    def getSMorir(self, num_elfo, n):
        morir = []
        for i in range(0, n):
            imagen = 'Imagenes/Elfos/' + num_elfo + '/Muerte/Muerte' + str(i + 1) + '.png'
            morir.append(PersonajesSprites(imagen, (50, 50)))

        return morir
