import sys

import pygame
from pygame.locals import *

from BuilderEscenario.DirectorEscenario import DirectorEscenario
from Jugador import Jugador

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)
DICONOS = (200, 200)

class PantallaJuego():

    def batalla(self, Raza1, Raza2):

        Jugador1 = Jugador()
        Jugador2 = Jugador()
        Jugador1.setParametros(False, Raza1)
        Jugador2.setParametros(True, Raza2)

        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Campo de Batalla")

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/Fondo4.jpg'), DIMENSIONES)

        reloj = pygame.time.Clock()


        while True:

            teclas = pygame.key.get_pressed()
            ventana.blit(image_Fondo, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        Jugador1.crearPersonaje(1)
                    if event.key == K_2:
                        Jugador1.crearPersonaje(2)
                    if event.key == K_3:
                        Jugador1.crearPersonaje(3)

                    # pygame.time.delay(40)

            Jugador1.dibujar(ventana)
            pygame.display.flip()
