from AbstractPersonaje.AbstractSCaminar import AbstractSCaminar
from PersonajesSprites import PersonajesSprites


class CaminarGuerrero(AbstractSCaminar):

    def getSCaminar(self, num_guerrero, n):
        caminar = []
        for i in range(0, n):
            imagen = 'Imagenes/Guerreros/' + num_guerrero + '/Caminar/Caminar' + str(i + 1) + '.png'
            caminar.append(PersonajesSprites(imagen, (50, 50)))

        return caminar
