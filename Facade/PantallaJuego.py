import random
import sys

import pygame
from pygame.locals import *

from Jugador import *
from Paisaje import Paisaje

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)
DICONOS = (200, 200)
FONDOS = ['Fondo1.png', 'Fondo2.png', 'Fondo3.jpg', 'Fondo4.jpg', 'Fondo5.png']

class PantallaJuego():

    def batalla(self, Raza1, Raza2):


        Jugador1 = JugadorIzq()
        Jugador2 = JugadorDer()
        Jugador1.setParametros(Raza1)
        Jugador2.setParametros(Raza2)

        PaisajeJug1 = Paisaje()
        PaisajeJug1.setParametros(False, Raza1, 0)
        PaisajeJug1.crearPaisaje()

        PaisajeJug2 = Paisaje()
        PaisajeJug2.setParametros(True, Raza2, 0)
        PaisajeJug2.crearPaisaje()

        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Campo de Batalla")

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/'+FONDOS[random.randrange(5)]), DIMENSIONES)

        reloj = pygame.time.Clock()


        while True:

            teclas = pygame.key.get_pressed()
            ventana.blit(image_Fondo, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        Jugador1.crearPersonaje(1)
                    if event.key == K_2:
                        Jugador1.crearPersonaje(2)
                    if event.key == K_3:
                        Jugador1.crearPersonaje(3)
                    if event.key == K_j:
                        Jugador2.crearPersonaje(1)
                    if event.key == K_k:
                        Jugador2.crearPersonaje(2)
                    if event.key == K_l:
                        Jugador2.crearPersonaje(3)


            PaisajeJug1.dibujar(ventana)
            Jugador1.dibujar(ventana)
            PaisajeJug2.dibujar(ventana)
            Jugador2.dibujar(ventana)

            # pygame.time.delay(40)

            print len(Jugador1.Ejercito), len(Jugador2.Ejercito)
            if len(Jugador1.Ejercito)>0 and len(Jugador2.Ejercito)>0:
                if Jugador1.rectE[len(Jugador1.Ejercito)-1].colliderect(Jugador2.rectE[len(Jugador1.Ejercito)-1]):
                    Jugador1.Ejercito[len(Jugador1.Ejercito)-1].setenBatalla(True)
                    for i in range(0,len(Jugador1.Ejercito)-1):
                        Jugador1.Ejercito[i].setenEspera(True)
                    Jugador2.Ejercito[len(Jugador2.Ejercito)-1].setenBatalla(True)
                    for i in range(0,len(Jugador2.Ejercito)-1):
                        Jugador2.Ejercito[i].setenEspera(True)
                else:
                    Jugador1.Ejercito[len(Jugador1.Ejercito)-1].setenBatalla(False)
                    for i in range(0,len(Jugador1.Ejercito)-1):
                        Jugador1.Ejercito[i].setenEspera(False)
                    Jugador2.Ejercito[len(Jugador2.Ejercito)-1].setenBatalla(False)
                    for i in range(0,len(Jugador2.Ejercito)-1):
                        Jugador2.Ejercito[i].setenEspera(False)

            pygame.display.flip()
            reloj.tick(60)
