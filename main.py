# coding=utf-8
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
                    exit()
                    '''pygame.quit()
                    break'''

                if event.type == MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                        if boton['on_click']:
                            if boton['nombre'] == 'BotonJugar':
                                print "I'm here"
                                pide_raza_1()
                            else:
                                print "ERROR GRAVISIMO IMPERDONABLE"

        #Jugador1.dibujar(ventana, True, False, False)
        #Jugador1.update()

        pygame.display.flip()
        #reloj.tick(60)

def pide_raza_1():
    pass


def dibujar_botones(lista_botones, ventana):
    for boton in lista_botones:
        if boton['on_click']:
            ventana.blit(boton['imagen'], boton['rect'])
        else:
            ventana.blit(boton['imagen'], boton['rect'])

if __name__ == "__main__":
    main()
