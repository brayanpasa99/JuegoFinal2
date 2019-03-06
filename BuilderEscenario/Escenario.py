class Escenario():

    def __init__(self):
        iconos = []
        castillo = []

    def setIconos(self, iconos):
        self.iconos = iconos

    def setSCastillo(self, castillo):
        self.castillo = castillo

    def getSprites(self):
        return [self.castillo, self.iconos]
