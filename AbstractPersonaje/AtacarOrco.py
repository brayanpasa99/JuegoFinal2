from AbstractPersonaje.AbstractSAtacar import AbstractSAtacar
from PersonajesSprites import PersonajesSprites


class AtacarOrco(AbstractSAtacar):

    def getSAtacar(self, num_orco, n):
        atacar = []
        for i in range(0, n):
            imagen = 'Imagenes/Orcos/' + num_orco + '/Ataque/Ataque' + str(i + 1) + '.png'
            atacar.append(PersonajesSprites(imagen, (50, 50)))

        return atacar
