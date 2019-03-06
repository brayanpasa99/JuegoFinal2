# coding=utf-8
import sys

import pygame
from pygame.locals import *

from DibujarBotones import DibujarBotones
from Facade.PantallaJuego import PantallaJuego
from Jugador import Jugador

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)
DICONOS = (200, 200)

class ElegirRaza():

    def __init__(self):
        self.Jugador1 = Jugador()
        self.Jugador2 = Jugador()

    def pide_raza(self, num_jugador, segundo):

        pygame.init()
        crear = True

        ventana_raza = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Escoger raza de jugadores")

        Fuente = pygame.font.SysFont("Arial", 30)
        FuenteTitulo = pygame.font.SysFont("Arial", 50)

        LabelElfo = Fuente.render("Elfos", 0, COLOR_TEXTO)
        LabelOrco = Fuente.render("Orcos", 0, COLOR_TEXTO)
        LabelGuerrero = Fuente.render("Guerreros", 0, COLOR_TEXTO)
        LabelSelRaza = FuenteTitulo.render("Seleccione la raza del jugador "+str(num_jugador), 0, COLOR_TEXTO)

        boton_sel_elfos = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Elfo/Elfo1.png"), DICONOS)
        rect_boton_sel_elfos = boton_sel_elfos.get_rect()
        rect_boton_sel_elfos.topleft = (200, 300)

        boton_sel_orcos = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Orco/Orco1.png"), DICONOS)
        rect_boton_sel_orcos = boton_sel_orcos.get_rect()
        rect_boton_sel_orcos.topleft = (500, 300)

        boton_sel_guerreros = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Guerrero/Guerrero1.png"), DICONOS)
        rect_boton_sel_guerreros = boton_sel_guerreros.get_rect()
        rect_boton_sel_guerreros.topleft = (800, 300)

        # Listado de botones en un diccionario
        botones = []

        botones.append({'nombre': "SelElfos", 'imagen': boton_sel_elfos, 'rect': rect_boton_sel_elfos, 'on_click': False})
        botones.append({'nombre': "SelOrcos", 'imagen': boton_sel_orcos, 'rect': rect_boton_sel_orcos, 'on_click': False})
        botones.append({'nombre': "SelGuerreros", 'imagen': boton_sel_guerreros, 'rect': rect_boton_sel_guerreros, 'on_click': False})

        if not segundo:
            imagen_fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/FondoRaza.png"), DIMENSIONES)
        else:
            imagen_fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/FondoRaza2.png"), DIMENSIONES)

        while crear:

            ventana_raza.blit(imagen_fondo, (0, 0))
            ventana_raza.blit(LabelElfo, (250, 250))
            ventana_raza.blit(LabelGuerrero, (550, 250))
            ventana_raza.blit(LabelOrco, (850, 250))
            ventana_raza.blit(LabelSelRaza, (300, 100))

            DibujarBotones().dibujar_botones(botones, ventana_raza)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                        if boton['on_click']:
                            if boton['nombre'] == 'SelElfos':
                                if not segundo:
                                    return 'Elfos'
                                    crear = False
                                elif segundo and num_jugador == 2:
                                    return 'Elfos'
                                    crear = False

                            elif boton['nombre'] == 'SelOrcos':
                                if not segundo:
                                    self.Jugador1.setParametros(False, 'Orcos')
                                    crear = False
                                else:
                                    self.Jugador1.setParametros(True, 'Orcos')
                                    crear = False

                            elif boton['nombre'] == 'SelGuerreros':
                                if not segundo:
                                    self.Jugador1.setParametros(False, 'Guerreros')
                                    crear = False
                                else:
                                    self.Jugador1.setParametros(True, 'Guerreros')
                                    crear = False

                            else:
                                print "ERROR GRAVÍSIMO IMPERDONABLE"

            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

            pygame.display.flip()

    def getJugadores(self):

        return self.Jugador1
