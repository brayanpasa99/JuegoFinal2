from AbstractPersonaje.AbstractSAtacar import AbstractSAtacar
from PersonajesSprites import PersonajesSprites


class AtacarElfo(AbstractSAtacar):

    def getSAtacar(self, num_elfo, n):
        sprites = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/' + num_elfo + '/Ataque/Ataque' + str(i + 1) + '.png'
            sprites.append(PersonajesSprites(imagen, (50, 50)))

        return sprites
