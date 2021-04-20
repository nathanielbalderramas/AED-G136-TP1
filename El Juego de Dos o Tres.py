# Título, mensaje de bienvenida y reglas
print('El juego de dos o tres')
print('======================')
print('\n¡Bienvenido!')
# Redactar Reglas de Juego

# Carga de nombre de jugadores y comienzo del juego
jugador1 = input('Jugador 1, ingrese su nombre: ')
jugador2 = input('Jugador 2, ingrese su nombre: ')
start = input('\nPresione Enter para comenzar')
import random
puntaje1 = 0
puntaje2 = 0

# Mensaje 1ra ronda, Jugador 1
print('Primera Ronda\nTurno de ', jugador1)
start = input('\nPresione Enter para lanzar el primer dado')
dado1 = random.randint(1,6)
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = random.randint(1,6)
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = random.randint(1,6)
print('\nEl tercer dado quedó en:', dado3)

#Proceso: Cálculo de puntaje jugador 1 primera ronda
if dado1 == dado2 and dado1 == dado3:
    puntaje1 = puntaje1 + 6
    print(jugador1, 'obtiene 6 puntos')
else:
    if dado1 == dado2:
        puntaje1 = puntaje1 + 3
        print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
        start = input('\nPresione Enter para volver a lanzar el dado distinto')
        dado3 = random.randint(1,6)
        print('\nEl tercer dado quedó en:', dado3)
        if dado3 == dado1:
            puntaje1 = puntaje1 + 3
            print(jugador1, 'obtiene 3 puntos')
    else:
        if dado1 == dado3:
            puntaje1 = puntaje1 + 3
            print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
            start = input('\nPresione Enter para volver a lanzar el dado distinto')
            dado2 = random.randint(1,6)
            print('\nEl segundo dado quedó en:', dado2)
            if dado2 == dado1:
                puntaje1 = puntaje1 + 3
                print(jugador1, 'obtiene 3 puntos')
        else:
            if dado2 == dado3:
                puntaje1 = puntaje1 + 3
                print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
                start = input('\nPresione Enter para volver a lanzar el dado distinto')
                dado1 = random.randint(1,6)
                print('\nEl primer dado quedó en:', dado1)
                if dado1 == dado2:
                    puntaje1 = puntaje1 + 3
                    print(jugador1, 'obtiene 3 puntos')
print('En esta ronda', jugador1, 'obtuvo', puntaje1, 'puntos')

# Jugador 2
print('\nTurno de ', jugador2)
start = input('\nPresione Enter para lanzar el primer dado')
dado1 = random.randint(1,6)
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = random.randint(1,6)
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = random.randint(1,6)
print('\nEl tercer dado quedó en:', dado3)

#Proceso: Cálculo de puntaje jugador 2 primera ronda
if dado1 == dado2 and dado1 == dado3:
    puntaje2 = puntaje2 + 6
    print(jugador2, 'obtiene 6 puntos')
else:
    if dado1 == dado2:
        puntaje2 = puntaje2 + 3
        print(jugador2, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
        start = input('\nPresione Enter para volver a lanzar el dado distinto')
        dado3 = random.randint(1,6)
        print('\nEl tercer dado quedó en:', dado3)
        if dado3 == dado1:
            puntaje2 = puntaje2 + 3
            print(jugador2, 'obtiene 3 puntos')
    else:
        if dado1 == dado3:
            puntaje2 = puntaje2 + 3
            print(jugador2, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
            start = input('\nPresione Enter para volver a lanzar el dado distinto')
            dado2 = random.randint(1,6)
            print('\nEl segundo dado quedó en:', dado2)
            if dado2 == dado1:
                puntaje2 = puntaje2 + 3
                print(jugador2, 'obtiene 3 puntos')
        else:
            if dado2 == dado3:
                puntaje2 = puntaje2 + 3
                print(jugador2, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
                start = input('\nPresione Enter para volver a lanzar el dado distinto')
                dado1 = random.randint(1,6)
                print('\nEl primer dado quedó en:', dado1)
                if dado1 == dado2:
                    puntaje2 = puntaje2 + 3
                    print(jugador2, 'obtiene 3 puntos')
print('En esta ronda', jugador2, 'obtuvo', puntaje2, 'puntos')

print('\nPuntajes Parciales: ', jugador1, 'tiene', puntaje1, 'puntos y', jugador2, 'tiene', puntaje2, 'puntos')
