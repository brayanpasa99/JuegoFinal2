import pygame
from pygame.locals import *

from Jugador import Jugador

DIMENSIONES = (1000, 500)


def main():
    print "1. Elfos"
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
        PersonajesJ2 = Jugador1.crearJugador()

    pygame.init()

    ventana = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Campo de Batalla")

    image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/Fondo4.jpg'), (1000, 500));

    teclas = pygame.key.get_pressed()
    reloj = pygame.time.Clock()

    while True:

        ventana.blit(image_Fondo, (0, 0))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        Jugador1.dibujar(ventana, True, False, False)
        Jugador1.update()

        pygame.display.flip()
        #reloj.tick(60)

if __name__ == "__main__":
    main()
