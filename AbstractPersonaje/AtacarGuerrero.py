from AbstractPersonaje.AbstractSAtacar import AbstractSAtacar
from PersonajesSprites import PersonajesSprites


class AtacarGuerrero(AbstractSAtacar):

    def getSAtacar(self, num_guerrero, n):
        atacar = []
        for i in range(0, n):
            imagen = 'Imagenes/Guerreros/' + num_guerrero + '/Ataque/Ataque' + str(i + 1) + '.png'
            atacar.append(PersonajesSprites(imagen, (50, 50)))

        return atacar
