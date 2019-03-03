from AbstractPersonaje.AbstractSCaminar import AbstractSCaminar
from PersonajesSprites import PersonajesSprites


class CaminarElfo(AbstractSCaminar):

    def getSCaminar(self, num_elfo, n):
        caminar = []
        for i in range(0, n):
            imagen = 'Imagenes/Elfos/' + num_elfo + '/Caminar/Caminar' + str(i + 1) + '.png'
            caminar.append(PersonajesSprites(imagen, (50, 50)))

        return caminar
