# coding=utf-8
import sys

import pygame
from pygame.locals import *

from Jugador import Jugador

DIMENSIONES = (1100, 600)
COLOR_TEXTO = (243, 255, 0)


def main():
    '''print "1. Elfos"
    print "2. Orcos"
    print "3. Guerreros"

    raza = input("Seleccione la raza del jugador 1: ")

    Jugador1 = Jugador()
    Jugador2 = Jugador()
    if raza == 1:

        Jugador1.setParametros(False, 'Elfos')
        PersonajesJ1 = Jugador1.crearJugador()

    elif raza == 2:
        Jugador1.setParametros(False, 'Orcos')
        PersonajesJ1 = Jugador1.crearJugador()

    elif raza == 3:
        Jugador1.setParametros(False, 'Guerreros')
        PersonajesJ1 = Jugador1.crearJugador()

    raza = input("Seleccione la raza del jugador 2: ")

    if raza == 1:

        Jugador2.setParametros(True, 'Elfos')
        PersonajesJ2 = Jugador1.crearJugador()

    elif raza == 2:
        Jugador2.setParametros(True, 'Orcos')
        PersonajesJ2 = Jugador1.crearJugador()

    elif raza == 3:
        Jugador2.setParametros(True, 'Guerreros')
        PersonajesJ2 = Jugador1.crearJugador()'''

    pygame.init()

    ventana = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Mundo de razas")

    image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/FondoPrincipal.png'), DIMENSIONES);

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

        dibujar_botones(botones, ventana)

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
                                print "I'm here"
                                pide_raza()
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

def pide_raza():

    pygame.init()

    ventana_raza1 = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Escoger la raza jugador 1")

    Fuente = pygame.font.SysFont("Arial", 30)

    LabelElfo = Fuente.render("Elfos", 0, COLOR_TEXTO)
    LabelOrco = Fuente.render("Orcos", 0, COLOR_TEXTO)
    LabelGuerrero = Fuente.render("Guerreros", 0, COLOR_TEXTO)

    boton_sel_elfos = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Elfo/Elfo1.png"), (100, 100))
    rect_boton_sel_elfos = boton_sel_elfos.get_rect()
    rect_boton_sel_elfos.topleft = (100, 100)

    boton_sel_orcos = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Orco/Orco1.png"), (100, 100))
    rect_boton_sel_orcos = boton_sel_orcos.get_rect()
    rect_boton_sel_orcos.topleft = (100, 200)

    boton_sel_guerreros = pygame.transform.scale(pygame.image.load("Imagenes/Iconos/Guerrero/Guerrero1.png"), (100, 100))
    rect_boton_sel_guerreros = boton_sel_guerreros.get_rect()
    rect_boton_sel_guerreros.topleft = (100, 300)

    # Listado de botones en un diccionario
    botones = []

    botones.append({'nombre': "SelElfos", 'imagen': boton_sel_elfos, 'rect': rect_boton_sel_elfos, 'on_click': False})
    botones.append({'nombre': "SelOrcos", 'imagen': boton_sel_orcos, 'rect': rect_boton_sel_orcos, 'on_click': False})
    botones.append({'nombre': "SelGuerreros", 'imagen': boton_sel_guerreros, 'rect': rect_boton_sel_guerreros, 'on_click': False})

    imagen_fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/FondoRaza.png"), DIMENSIONES)

    while True:

        ventana_raza1.blit(imagen_fondo, (0, 0))
        ventana_raza1.blit(LabelElfo, (100, 90))
        ventana_raza1.blit(LabelGuerrero, (100, 190))
        ventana_raza1.blit(LabelOrco, (100, 290))

        dibujar_botones(botones, ventana_raza1)

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
                            print "Seleccionó Elfos"
                        elif boton['nombre'] == 'SelOrcos':
                            print "Selecionó Orcos"
                        elif boton['nombre'] == 'SelGuerreros':
                            print "Selecionó Guerreros"
                        else:
                            print "ERROR GRAVÍSIMO IMPERDONABLE"

        if event.type == MOUSEBUTTONUP:
            for boton in botones:
                boton['on_click'] = False



def dibujar_botones(lista_botones, ventana):
    for boton in lista_botones:
        if boton['on_click']:
            ventana.blit(boton['imagen'], boton['rect'])
        else:
            ventana.blit(boton['imagen'], boton['rect'])

if __name__ == "__main__":
    main()
