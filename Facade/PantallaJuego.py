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


        
            if len(Jugador1.Ejercito)>0 and len(Jugador2.Ejercito)>0:
                print(len(Jugador1.Ejercito))
                print(len(Jugador2.Ejercito))
                if pygame.sprite.collide_rect(Jugador1.rectE[0],Jugador2.rectE[0]):
                    Jugador1.Ejercito[len(Jugador1.Ejercito)-1].setenBatalla(True)    
                    Jugador2.Ejercito[len(Jugador2.Ejercito)-1].setenBatalla(True)
                        
                if Jugador1.Ejercito[0].getenBatalla() and Jugador2.Ejercito[0].getenBatalla():
                    print(Jugador1.Ejercito[0].getVida)
                    print(Jugador2.Ejercito[0].getVida)

                    Jugador1.Ejercito[0].reducirVida(Jugador2.Ejercito[0].getPoder())
                    Jugador2.Ejercito[0].reducirVida(Jugador1.Ejercito[0].getPoder())
                    pygame.time.delay(100)
                    if Jugador1.Ejercito[0].getVida() <= 0:

                        Jugador1.Ejercito.pop(0)
                        Jugador2.Ejercito[0].setenbatalla(False)
                    elif Jugador2.Ejercito[0].getVida() <= 0:
                        
                        Jugador2.Ejercito.pop(0)
                        Jugador1.Ejercito[0].setenbatalla(False)
            
            PaisajeJug1.dibujar(ventana)
            Jugador1.dibujar(ventana)
            PaisajeJug2.dibujar(ventana)
            Jugador2.dibujar(ventana)

            pygame.display.flip()
            reloj.tick(60)
