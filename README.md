# Juanito y los argonautas

## Nombre:

Juanito y los argonautas

## Reseña:

El juego consiste en dos jugadores que escojeran una raza (elfos, humanos, orcos), los jugadores podran eleguir entre tres distintos tipos de guerreros, el objetivo del juego es destruir el castillo enemigo.  


## Patrones en el juego:

El juego esta compuesto por tres patrones de diseño, dos  creacionales y uno estructural. Los patrones creacionales son Abstrac Factory y Builder, estos patrones los utilizamos para crear tanto los personajes como el escenario, y el patron estructural es el patron Facade.

Para crear los movimientos del personaje se utiliza el patron Abstract Factory, de esta forma se cargan los Sprites de movimiento, de ataque y de muerte de cada personaje, teniendo en cuenta que se deben crear los Sprites de los tres diferentes tipos de personajes que hay en una misma raza. Despues de instanciar tolas las imagenes de los Sprites, se utiliza el patron Builder para construir los personajes al unir los Sprites de caminar, atacar y morir.

Tambien se utiliza el patron Abstract Factiry para crear las partes de la pantalla principal, es decir el producto final sera la imagen del respectivo castillo de la raza y el logo del tipo de personaje que se puede llegar a tener, y, a su vez se utiliza el patron Builder para unir los productos del Abstract Factory y construir un panel principal. 

El patron facade provee una interfaz unificada para un conjunto de interfaces en un subsistema, en este caso el panel pantallaPrincipal es la interfaz de alto nivel que unifica los paneles pantallaJuego y elegirRaza. 


## Estructura:

![Estructura](https://github.com/brayanpasa99/Patrones/blob/master/Patrones%20estructurales/Facade/Im%C3%A1genes/Estructura.png)


