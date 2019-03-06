# coding=utf-8
import sys

import pygame
from pygame.locals import *

from DibujarBotones import DibujarBotones
from Facade.ElegirRaza import ElegirRaza
from Facade.PantallaJuego import PantallaJuego

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)

class PantallaPrincipal():

    def mostrarpantalla(self):
        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Mundo de razas")

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/FondoPrincipal.png'), DIMENSIONES)

        FuenteTitulo = pygame.font.SysFont("Chiller", 80)
        LabelTitulo = FuenteTitulo.render("Juanito y Los Argonautas", 0, COLOR_TEXTO)

        #Botón de jugar
        boton_jugar = pygame.transform.scale(pygame.image.load('Imagenes/Botones/Jugar.png'), (300, 100))
        rect_boton_jugar = boton_jugar.get_rect()
        rect_boton_jugar.topleft = (400, 200)

        botones = []

        botones.append({'nombre': "BotonJugar", 'imagen': boton_jugar, 'rect': rect_boton_jugar, 'on_click': False})


        teclas = pygame.key.get_pressed()
        reloj = pygame.time.Clock()

        while True:

            ventana.blit(image_Fondo, (0, 0))
            ventana.blit(LabelTitulo, (300, 50))

            DibujarBotones().dibujar_botones(botones, ventana)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == MOUSEBUTTONDOWN:
                        mouse = event.pos
                        for boton in botones:
                            boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                            if boton['on_click']:
                                if boton['nombre'] == 'BotonJugar':
                                    Jugadores = []
                                    PantallaJuego().batalla(ElegirRaza().pide_raza(1, False), ElegirRaza().pide_raza(2, True))

                                else:
                                    print "ERROR GRAVISIMO IMPERDONABLE"

            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

            #Jugador1.dibujar(ventana, True, False, False)
            #Jugador1.update()

            pygame.display.flip()
            pygame.display.update()
            #reloj.tick(60)
