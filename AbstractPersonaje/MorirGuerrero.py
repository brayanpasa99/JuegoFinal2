from AbstractPersonaje.AbstractSMorir import AbstractSMorir
from PersonajesSprites import PersonajesSprites


class MorirGuerrero(AbstractSMorir):

    def getSMorir(self, num_guerrero, n):
        muerte = []
        for i in range(0, n):
            imagen = 'Imagenes/Guerreros/' + num_guerrero + '/Muerte/Muerte' + str(i + 1) + '.png'
            muerte.append(PersonajesSprites(imagen, (50, 50)))

        return muerte
