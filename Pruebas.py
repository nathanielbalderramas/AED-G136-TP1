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
dado1 = int(input())
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = int(input())
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = int(input())
print('\nEl tercer dado quedó en:', dado3)

# Proceso: Cálculo de puntaje jugador 1 primera ronda
if dado1 == dado2 and dado1 == dado3:
    puntaje1 = puntaje1 + 6
    print(jugador1, 'obtiene 6 puntos')
else:
    if dado1 == dado2:
        puntaje1 = puntaje1 + 3
        print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
        start = input('\nPresione Enter para volver a lanzar el dado distinto')
        dado3 = int(input())
        print('\nEl tercer dado quedó en:', dado3)
        if dado3 == dado1:
            puntaje1 = puntaje1 + 3
            print(jugador1, 'obtiene 3 puntos')
    else:
        if dado1 == dado3:
            puntaje1 = puntaje1 + 3
            print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
            start = input('\nPresione Enter para volver a lanzar el dado distinto')
            dado2 = int(input())
            print('\nEl segundo dado quedó en:', dado2)
            if dado2 == dado1:
                puntaje1 = puntaje1 + 3
                print(jugador1, 'obtiene 3 puntos')
        else:
            if dado2 == dado3:
                puntaje1 = puntaje1 + 3
                print(jugador1, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
                start = input('\nPresione Enter para volver a lanzar el dado distinto')
                dado1 = int(input())
                print('\nEl primer dado quedó en:', dado1)
                if dado1 == dado2:
                    puntaje1 = puntaje1 + 3
                    print(jugador1, 'obtiene 3 puntos')
print('\nEn esta ronda', jugador1, 'obtuvo', puntaje1, 'puntos')

# Jugador 2
print('\nTurno de ', jugador2)
start = input('\nPresione Enter para lanzar el primer dado')
dado1 = int(input())
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = int(input())
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = int(input())
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
        dado3 = int(input())
        print('\nEl tercer dado quedó en:', dado3)
        if dado3 == dado1:
            puntaje2 = puntaje2 + 3
            print(jugador2, 'obtiene 3 puntos')
    else:
        if dado1 == dado3:
            puntaje2 = puntaje2 + 3
            print(jugador2, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
            start = input('\nPresione Enter para volver a lanzar el dado distinto')
            dado2 = int(input())
            print('\nEl segundo dado quedó en:', dado2)
            if dado2 == dado1:
                puntaje2 = puntaje2 + 3
                print(jugador2, 'obtiene 3 puntos')
        else:
            if dado2 == dado3:
                puntaje2 = puntaje2 + 3
                print(jugador2, 'obtiene 3 puntos y vuelve a tirar el dado que dio distinto')
                start = input('\nPresione Enter para volver a lanzar el dado distinto')
                dado1 = int(input())
                print('\nEl primer dado quedó en:', dado1)
                if dado1 == dado2:
                    puntaje2 = puntaje2 + 3
                    print(jugador2, 'obtiene 3 puntos')
print('En esta ronda', jugador2, 'obtuvo', puntaje2, 'puntos')

print('\nPuntajes Parciales: ', jugador1, 'tiene', puntaje1, 'puntos y', jugador2, 'tiene', puntaje2, 'puntos')
start = input('\nPresione enter para pasar a la Segunda Ronda')
# Segunda Ronda
# Turno de Jugador1

print('\nSegunda Ronda\n\nTurno de ', jugador1)
print('Debe apostar por resultado par o impar')
print('Si apuesta a par ingrese cualquier número par, si apuesta a impar ingrese cualquier número impar')
apuesta1 = int(input('Su apuesta: '))
if apuesta1 %2 == 0:
    print(jugador1, 'apuesta a resultado par')
else:
    print(jugador1, 'apuesta a resultado impar')
start = input('\nPresione Enter para lanzar el primer dado')
dado1 = int(input())
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = int(input())
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = int(input())
print('\nEl tercer dado quedó en:', dado3)

# Proceso: Cálculo de puntaje jugador 1 Segunda Ronda
mayor1 = max(dado1, dado2, dado3)
menor1 = min(dado1, dado2, dado3)
suma1 = dado1 + dado2 + dado3
if suma1 %2 == 0:
    print('La suma de los dados es par!')
else:
    print('La suma de los dados es impar!')
if suma1 %2 == apuesta1 %2:
    puntaje1 = puntaje1 + mayor1
    print(jugador1, 'obtiene', mayor1, 'puntos')
    if dado1 %2 == apuesta1 %2 and dado2 %2 == apuesta1 %2 and dado3 %2 == apuesta1 %2:
        print('Todos los dados coinciden con la apuesta!!', jugador1, 'duplica su puntaje')
        puntaje1 = puntaje1 *2
        print(jugador1, 'tiene', puntaje1, 'puntos')
else:
    if puntaje1 > 0 and menor1 < puntaje1:
        puntaje1 = puntaje1 - menor1
        print(jugador1, 'pierde', menor1, 'puntos')
    else:
        if puntaje1 > 0 and menor1 > puntaje1:
            puntaje1 = 0
            print(jugador1, 'pierde todos sus puntos')
        else:
            print(jugador1, 'no obtiene puntos en esta ronda')

# Turno de Jugador2
print('\n\nTurno de ', jugador2)
start = input('Presione Enter para continuar')
print('Debe apostar por resulado par o impar')
print('Si apuesta a par ingrese cualquier número par, si apuesta a impar ingrese cualquier número impar')
apuesta2 = int(input('Su apuesta: '))
if apuesta2 %2 == 0:
    print(jugador2, 'apuesta a resultado par')
else:
    print(jugador2, 'apuesta a resultado impar')

start = input('\nPresione Enter para lanzar el primer dado')
dado1 = int(input())
print('\nEl primer dado quedó en:', dado1)
start = input('\nPresione Enter para lanzar el segundo dado')
dado2 = int(input())
print('\nEl segundo dado quedó en:', dado2)
start = input('\nPresione Enter para lanzar el tercer dado')
dado3 = int(input())
print('\nEl tercer dado quedó en:', dado3)

# Proceso: Cálculo de puntaje jugador 2 Segunda Ronda
mayor2 = max(dado1, dado2, dado3)
menor2 = min(dado1, dado2, dado3)
suma2 = dado1 + dado2 + dado3
if suma2 %2 == 0:
    print('La suma de los dados es par!')
else:
    print('La suma de los dados es impar!')
if suma2 %2 == apuesta2 %2:
    puntaje2 = puntaje2 + mayor2
    print(jugador2, 'obtiene', mayor2, 'puntos')
    if dado1 %2 == apuesta2 %2 and dado2 %2 == apuesta2 %2 and dado3 %2 == apuesta2 %2:
        print('Todos los dados coinciden con la apuesta!!', jugador2, 'duplica su puntaje')
        puntaje2 = puntaje2 *2
        print(jugador2, 'tiene', puntaje2, 'puntos')
else:
    if puntaje2 > 0 and menor2 < puntaje2:
        puntaje2 = puntaje2 - menor2
        print(jugador2, 'pierde', menor2, 'puntos')
    else:
        if puntaje2 > 0 and menor2 > puntaje2:
            puntaje2 = 0
            print(jugador2, 'pierde todos sus puntos')
        else:
            print(jugador2, 'no obtiene puntos en esta ronda')

print('FIN DE LA PARTIDA')
start = input('Presione Enter para ver los puntajes')
print(jugador1, 'obtuvo', puntaje1, 'puntos y', jugador2, 'obtuvo', puntaje2, 'puntos')
if puntaje1 == puntaje2:
    print('El resultado es empate!')
else:
    if puntaje1 > puntaje2:
        print('El ganador es', jugador1,'!!!')
    else:
        print('El ganador es', jugador2,'!!!')
print('\nGracias por jugar!\nHasta pronto!')
# Créditos
