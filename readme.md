# TP1 - G136
Integrantes:

 - Ávila, Matias (93599)
 - Balderramas, Nathaniel (92334)
 - Silva, Gabriela (92708)

## Diagrama de flujo:
https://drive.google.com/file/d/1mJVUXZvPgSbAPZCmwILx8mNa6Ej4YvKT/view?usp=sharing


## Consigna:
https://uv.frc.utn.edu.ar/mod/assign/view.php?id=141066

## Transcripto:
Implementación de un Juego de Dados: *El Juego de Dos o Tres*.

Se solicita desarrollar un programa que permita implementar un juego de dados simple; "el Juego de Dos o Tres". 

El juego se basa en lanzar dados y acumular puntos en base a los valores obtenidos. Su tarea será desarrollar un programa Python que simule el desarrollo del juego.

Se juega con 3 dados y se enfrentan 2 jugadores. El juego se desarrolla en 2 rondas, y en cada ronda ambos jugadores pueden sumar puntos según las reglas de esa ronda.

Al comenzar, el programa debe solicitar los nombres de ambos jugadores, simular dos rondas según las reglas detalladas a continuación e informar el resultado final del juego. Las reglas de puntuación que corresponden a cada ronda del juego son las siguientes:

### Reglas de la Primera Ronda

El primer jugador lanza los 3 dados.

a) Si los tres dados fueran iguales el jugador suma 6 puntos. Por ejemplo, si el jugador obtiene los siguientes dados, sumará 6 puntos:

b) Si el jugador tuviera dos dados iguales y uno distinto (como en el ejemplo que sigue), entonces el jugador vuelve a tirar, pero únicamente el dado distinto (que en el caso del ejemplo es el dado con valor 1). Si al volver a lanzar ese dado logra que los tres dados sean iguales (como por ejemplo que se obtenga un 5 en el caso descripto), entonces sumará los 6 puntos en esa ronda. Si el dado relanzado sigue siendo distinto a los dos que eran iguales, el jugador sumará 3 puntos en esa ronda.

c) Si los tres dados fueran todos distintos, entonces obtiene 0 puntos y no puede volver a tirar ningún dado en esa ronda. Por ejemplo, en este caso:

Finalizada la jugada del primer jugador, inicia el segundo jugador tirando los tres dados y determinando su puntaje con las mismas reglas que el primer jugador: 6 puntos si los tres dados son iguales, relanzando un dado si fueran 2 dados iguales (obteniendo 3 puntos si sólo consigue 2 iguales) y 0 si los tres dados son distintos.

### Reglas de la Segunda Ronda

a) El primer jugador vuelve a lanzar los 3 dados, y se considera que apuesta todo el puntaje de la ronda anterior a par/impar (el programa debe pedir que el jugador elija si apuesta por par o impar).

b) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, entonces suma el dado de mayor valor a su puntaje de la ronda anterior; en caso contrario, resta el dado de menor valor a su puntaje anterior.

c) Si efectivamente la suma en la segunda jugada es de la paridad elegida, entonces el programa debe controlar si además los tres dados fueron de la paridad elegida, y en ese caso, se duplica el puntaje total.

Se repite la jugada para el segundo jugador con las mismas reglas que el primero.

### Final del Juego:

Gana el jugador que más puntaje haya obtenido.

Al terminar el juego, el programa debe informar el nombre de cada jugador y su puntaje total. Además, debe indicar el nombre del ganador (o mostrar un mensaje informando que se produjo un empate).
