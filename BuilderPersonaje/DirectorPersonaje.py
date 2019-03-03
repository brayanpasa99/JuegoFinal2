from BuilderPersonaje.Personaje import Personaje


class DirectorPersonaje:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPersonaje(self):
        personaje = Personaje()

        SpritesAtacar = self.__builder.getSAtacar()
        personaje.setSAtacar(SpritesAtacar)

        SpritesCaminar = self.__builder.getSCaminar()
        personaje.setSCaminar(SpritesCaminar)

        SpritesMorir = self.__builder.getSMorir()
        personaje.setSMorir(SpritesMorir)

        return personaje

