import sys

import pygame
from pygame.locals import *

from Jugador import Jugador

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)
DICONOS = (200, 200)

class PantallaJuego():

    def __init__(self):
        self.Jugador1 = Jugador()
        self.Jugador2 = Jugador()

    def setJugadores(self, Jug1, Jug2):
        self.Jugador1 = Jug1
        self.Jugador2 = Jug2

    def batalla(self):
        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Campo de Batalla")

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/Fondo4.jpg'), (1000, 500));


        reloj = pygame.time.Clock()


        while True:

            teclas = pygame.key.get_pressed()
            ventana.blit(image_Fondo, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        self.Jugador1.crearPersonaje(1)
                    if event.key == K_2:
                        self.Jugador1.crearPersonaje(2)
                    if event.key == K_3:
                        self.Jugador1.crearPersonaje(3)

            self.Jugador1.dibujar(ventana, True, False, False)
            self.Jugador1.update()

        pygame.display.update()
        #reloj.tick(27)
