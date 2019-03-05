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
        Jugador1.crearJugador()
        

    elif raza == 2:
        Jugador1.setParametros(False, 'Orcos')
        Jugador1.crearJugador()

        

    elif raza == 3:
        Jugador1.setParametros(False, 'Guerreros')
        Jugador1.crearJugador()
       

    raza = input("Seleccione la raza del jugador 2: ")

    if raza == 1:

        Jugador2.setParametros(True, 'Elfos')
        Jugador2.crearJugador()

    elif raza == 2:
        Jugador2.setParametros(True, 'Orcos')
        Jugador2.crearJugador()

    elif raza == 3:
        Jugador2.setParametros(True, 'Guerreros')
        Jugador2.crearJugador()

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
                    pygame.quit()
                    break
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        Jugador1.CrearPersonaje(0)


        

        
        Jugador1.dibujar(ventana)
        Jugador1.update()

        pygame.display.flip()
        #reloj.tick(60)

if __name__ == "__main__":
    main()
