from AbstractPersonaje.AbstractSMorir import AbstractSMorir
from PersonajesSprites import PersonajesSprites


class MorirOrco(AbstractSMorir):

    def getSMorir(self, num_orco, n):
        muerte = []
        for i in range(0, n):
            imagen = 'Imagenes/Orcos/' + num_orco + '/Muerte/Muerte' + str(i + 1) + '.png'
            muerte.append(PersonajesSprites(imagen, (50, 50)))

        return muerte
