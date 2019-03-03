class Personaje:

    def __init__(self):
        self.__atacar  = []
        self.__caminar  = []
        self.__morir    = []

    def setSAtacar(self, atacar):
        self.__atacar = atacar

    def setSCaminar(self, caminar):
        self.__caminar = caminar

    def setSMorir(self, morir):
        self.__morir = morir
