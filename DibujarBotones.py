class DibujarBotones():

    def dibujar_botones(self, lista_botones, ventana):
        for boton in lista_botones:
            if boton['on_click']:
                ventana.blit(boton['imagen'], boton['rect'])
            else:
                ventana.blit(boton['imagen'], boton['rect'])
