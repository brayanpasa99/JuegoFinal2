from AbstractEscenario.AbstractCastillo import AbstractCastillo
from PersonajesSprites import PersonajesSprites


class CastilloOrco(AbstractCastillo):

    def getSCastillo(self, n):
        sprites = []
        for i in range(0, n):
            imagen = 'Imagenes/Castillos/CastilloVerde' + str(i + 1) + '.png'
            sprites.append(PersonajesSprites(imagen, (300, 700)))

        return sprites
