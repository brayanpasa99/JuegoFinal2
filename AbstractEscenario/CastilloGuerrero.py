from AbstractEscenario.AbstractCastillo import AbstractCastillo
from PersonajesSprites import PersonajesSprites


class CastilloGuerrero(AbstractCastillo):

    def getSCastillo(self, n):
        sprites = []
        for i in range(0, n):
            imagen = 'Imagenes/Castillos/CastilloRojo' + str(i + 1) + '.png'
            sprites.append(PersonajesSprites(imagen, (300, 700)))

        return sprites
