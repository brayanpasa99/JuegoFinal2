##Juanito y los argonautas

## Nombre:

Juanito y los argonautas

## Reseña:

El juego consiste en dos jugadores que escogerán una raza (elfos, humanos, orcos), los jugadores podrán elegir entre tres distintos tipos de guerreros, el objetivo del juego es destruir el castillo enemigo.  


## Patrones en el juego:

El juego está compuesto por tres patrones de diseño, dos creacionales y uno estructural. Los patrones creacionales son Abstrac Factory y Builder, estos patrones los utilizamos para crear tanto los personajes como el escenario, y el patrón estructural es el patrón Facade que lo utilizamos para dar una interfaz unificada.

Para crear los movimientos del personaje se utiliza el patrón Abstract Factory, de esta forma se cargan los Sprites de movimiento, de ataque y de muerte de cada personaje, teniendo en cuenta que se deben crear los Sprites de los tres diferentes tipos de personajes que hay en una misma raza. Después de instanciar tolas las imágenes de los Sprites, se utiliza el patrón Builder para construir los personajes al unir dichos Sprites .

También se utiliza el patrón Abstract Factory para crear las partes de la pantalla principal, es decir el producto final será la imagen del respectivo castillo de la raza y el logo del tipo de personaje que se puede llegar a tener, y, a su vez, se utiliza el patrón Builder para unir los productos del Abstract Factory y construir un panel principal. 

El patrón Facade provee una interfaz unificada para un conjunto de interfaces en un subsistema, en este caso el panel pantallaPrincipal es la interfaz de alto nivel que unifica los paneles pantallaJuego y elegirRaza.



## Estructura:

![Estructura](https://github.com/brayanpasa99/JuegoFinal2/blob/master/Diagrama%20juego.png)

## Imagenes del juego

![Estructura](https://github.com/brayanpasa99/JuegoFinal2/blob/master/imagen.png)
