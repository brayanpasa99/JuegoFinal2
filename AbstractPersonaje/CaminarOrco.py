from AbstractPersonaje.AbstractSCaminar import AbstractSCaminar
from PersonajesSprites import PersonajesSprites


class CaminarOrco(AbstractSCaminar):

    def getSCaminar(self, num_orco, n):
        caminar = []
        for i in range(0, n):
            imagen = 'Imagenes/Orcos/' + num_orco + '/Caminar/Caminar' + str(i + 1) + '.png'
            caminar.append(PersonajesSprites(imagen, (50, 50)))

        return caminar
