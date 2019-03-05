from BuilderEscenario.Escenario import Escenario


class DirectorEscenario():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getEscenario(self):
        escenario = Escenario()

        iconos = self.__builder.getIconos()
        escenario.setIconos(iconos)

        castillo = self.__builder.getSCastillo()
        escenario.setSCastillo(castillo)

        return escenario
