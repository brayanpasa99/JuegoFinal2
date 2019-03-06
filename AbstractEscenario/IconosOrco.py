from AbstractEscenario.AbstractIconos import AbstractIconos
from PersonajesSprites import PersonajesSprites


class IconosOrco(AbstractIconos):

    def getIconos(self, n):
        sprites = []
        for i in range(0, n):
            imagen = 'Imagenes/Iconos/Orco/Orco' + str(i + 1) + '.png'
            sprites.append(PersonajesSprites(imagen, (50, 50)))

        return sprites
