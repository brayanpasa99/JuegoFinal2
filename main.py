from Facade.Fachada import Fachada


def main():

    fachada = Fachada()
    fachada.operacion()


if __name__ == "__main__":
    main()



























































'''print "1. Elfos"
    print "2. Orcos"
    print "3. Guerreros"

    raza = input("Seleccione la raza del jugador 1: ")

    Jugador1 = JugadorIzq()
    Jugador2 = JugadorDer()

    if raza == 1:

        Jugador1.setParametros('Elfos')
        

    elif raza == 2:
        Jugador1.setParametros('Orcos')

        

    elif raza == 3:
        Jugador1.setParametros('Guerreros')
       

    raza = input("Seleccione la raza del jugador 2: ")

    if raza == 1:

        Jugador2.setParametros('Elfos')
        

    elif raza == 2:
        Jugador2.setParametros('Orcos')
        

    elif raza == 3:
        Jugador2.setParametros('Guerreros')
        

    pygame.init()

    ventana = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Campo de Batalla")

    image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/Fondo4.jpg'), (1000, 500))

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
                
        Jugador1.dibujar(ventana)
        Jugador2.dibujar(ventana)
        pygame.display.flip()
        # reloj.tick(20)'''
