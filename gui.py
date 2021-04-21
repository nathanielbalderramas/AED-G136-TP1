import random
import PySimpleGUI as sg
import os

"""
Este es un intento de implementar el juego de 2 o 3 con una interfaz gráfica.
"""
"""
Nomenclatura General:
RX -> Número de Ronda (R1, R2)
PX -> Número de Jugador (P1, P2)
DX -> Número de Dado (D1, D2, D3, D4)
"""

theme = random.choice(sg.theme_list())
sg.theme(theme)

dice_imgs = ["dice0.png",
             "dice1.png",
             "dice2.png",
             "dice3.png",
             "dice4.png",
             "dice5.png",
             "dice6.png"]
dice_imgs = [os.path.join(os.getcwd(), "img", dice) for dice in dice_imgs]

# Estructura de la GUI
main_layout = [[sg.Text("El Juego de 2 o 3"), sg.Text(size=(10, 1)), sg.Text("Current theme is: {}".format(theme))],
               [sg.Text("Jugador 1: "), sg.Text(size=(15, 1), key="-P1_name-"),
                sg.Text("0", key="-P1_score-", size=(3, 1)), sg.Button("Renombrar", key="-P1_rename-")],
               [sg.Text("Jugador 2: "), sg.Text(size=(15, 1), key="-P2_name-"),
                sg.Text("0", key="-P2_score-", size=(3, 1)), sg.Button("Renombrar", key="-P2_rename-")],
               [],
               [sg.Text("RONDA 1:"), sg.Button("Start!", key="-R1_start-")],
               [sg.Text("Jugador 1: "),
                sg.Image(filename=dice_imgs[0], key="-R1P1D1-"),
                sg.Image(filename=dice_imgs[0], key="-R1P1D2-"),
                sg.Image(filename=dice_imgs[0], key="-R1P1D3-"),
                sg.Button("Roll", disabled=True, key="-R1P1_roll-"),
                sg.Button("ReRoll", disabled=True, key="-R1P1_reroll-")],
               [sg.Text("Jugador 2: "),
                sg.Image(filename=dice_imgs[0], key="-R1P2D1-"),
                sg.Image(filename=dice_imgs[0], key="-R1P2D2-"),
                sg.Image(filename=dice_imgs[0], key="-R1P2D3-"),
                sg.Button("Roll", disabled=True, key="-R1P2_roll-"),
                sg.Button("ReRoll", disabled=True, key="-R1P2_reroll-")],
               [],
               [sg.Text("RONDA 2:"), sg.Button("Start!", key="-R2_start-", disabled=True)],
               [sg.Text("Jugador 1: "), sg.Image(filename=dice_imgs[0], key="-R2P1D1-"),
                sg.Image(filename=dice_imgs[0], key="-R2P1D2-"), sg.Image(filename=dice_imgs[0], key="-R2P1D3-"),
                sg.Button("Roll", disabled=True, key="-R2P1_roll-")],
               [sg.Text("Jugador 2: "), sg.Image(filename=dice_imgs[0], key="-R2P2D1-"),
                sg.Image(filename=dice_imgs[0], key="-R2P2D2-"), sg.Image(filename=dice_imgs[0], key="-R2P2D3-"),
                sg.Button("Roll", disabled=True, key="-R2P2_roll-")],
               [],
               [sg.Text("El ganador es: "), sg.Text(size=(15, 1), key="-WINNER-")],
               [sg.Button("Exit"), sg.Button("Restart")]]

window = sg.Window("TP1", main_layout, size=(450, 450))

# Inicializacion de variables de control
P1_name, P2_name = "Jugador 1", "Jugador 2"
R1_rolls, R2_rolls = 0, 0
P1_score, P2_score = 0, 0
R1P1_reroll, R1P2_reroll = 0, 0
R2P1_par, R2P2_par = None, None

# Event loop :)
while True:
    event, values = window.read()
    print()
    print(event, values)

    # Renombrar jugadores
    if event == "-P1_rename-":
        rename_layout = [[sg.Text("Escriba el nuevo nombre: "), sg.InputText(P1_name, size=(30, 1), key="-rename_out-"),
                          sg.Button("Rename", key="-rename_update-"), sg.Button("Cancel", key="-rename_cancel-")]]
        name_window = sg.Window("Renombrar al Jugador 1", [*rename_layout])
        name_event, name_values = name_window.read()
        name_window.close()
        if name_event == "-rename_update-":
            P1_name = name_values["-rename_out-"]
            window["-P1_name-"].update(P1_name)

    if event == "-P2_rename-":
        rename_layout = [[sg.Text("Escriba el nuevo nombre: "), sg.InputText(P2_name, size=(30, 1), key="-rename_out-"),
                          sg.Button("Rename", key="-rename_update-"), sg.Button("Cancel", key="-rename_cancel-")]]
        name_window = sg.Window("Renombrar al Jugador 1", rename_layout)
        name_event, name_values = name_window.read()
        name_window.close()
        if name_event == "-rename_update-":
            P2_name = name_values["-rename_out-"]
            window["-P2_name-"].update(P2_name)


    # Comienza la primera ronda
    if event == "-R1_start-":
        window["-R1P1_roll-"].update(disabled=False)
        window["-R1P2_roll-"].update(disabled=False)
        window["-R1_start-"].update(disabled=True)

    # Tirada del primer jugador
    if event == "-R1P1_roll-":
        R1P1D1 = random.randint(1, 6)
        R1P1D2 = random.randint(1, 6)
        R1P1D3 = random.randint(1, 6)

        # Evaluar si hay iguales
        if R1P1D1 == R1P1D2 and R1P1D1 == R1P1D3:
            P1_score += 6
            R1_rolls += 1
        elif R1P1D1 == R1P1D2:
            R1P1_reroll = "-R1P1D3-"
            R1P1_compare = R1P1D1
        elif R1P1D1 == R1P1D3:
            R1P1_reroll = "-R1P1D2-"
            R1P1_compare = R1P1D1
        elif R1P1D2 == R1P1D3:
            R1P1_reroll = "-R1P1D1-"
            R1P1_compare = R1P1D2
        else:
            R1_rolls += 1

        # Verificacion de reroll
        if R1P1_reroll:
            P1_score += 3
            window["-R1P1_reroll-"].update(disabled=False)

        if R1_rolls >= 2:
            window["-R2_start-"].update(disabled=False)

        # Interfaz de jugada (R1P1)
        window["-R1P1D1-"].update(dice_imgs[R1P1D1])
        window["-R1P1D2-"].update(dice_imgs[R1P1D2])
        window["-R1P1D3-"].update(dice_imgs[R1P1D3])
        window["-R1P1_roll-"].update(disabled=True)
        window["-P1_score-"].update(P1_score)

    # Re lanzado del Jugador 1
    if event == "-R1P1_reroll-":
        R1P1D4 = random.randint(1, 6)
        if R1P1D4 == R1P1_compare:
            P1_score += 3
        R1_rolls += 1

        window[R1P1_reroll].update(dice_imgs[R1P1D4])
        window["-R1P1_reroll-"].update(disabled=True)
        window["-P1_score-"].update(P1_score)

        if R1_rolls >= 2:
            window["-R2_start-"].update(disabled=False)

    # Tirada del segundo jugador
    if event == "-R1P2_roll-":
        # Roll Jugador 2
        R1P2D1 = random.randint(1, 6)
        R1P2D2 = random.randint(1, 6)
        R1P2D3 = random.randint(1, 6)

        # Codigo de ronda 1, Jugador 2
        if R1P2D1 == R1P2D2 == R1P2D3:
            P2_score += 6
            R2_rolls += 1
        elif R1P2D1 == R1P2D2:
            R1P2_reroll = "-R1P2D3-"
            R1P2_compare = R1P2D1
        elif R1P2D1 == R1P2D3:
            R1P2_reroll = "-R1P2D2-"
            R1P2_compare = R1P2D1
        elif R1P2D2 == R1P2D3:
            R1P2_reroll = "-R1P2D1-"
            R1P2_compare = R1P2D2
        else:
            R1_rolls += 1

        if R1P2_reroll:
            P2_score += 3
            window["-R1P2_reroll-"].update(disabled=False)

        window["-R1P2D1-"].update(dice_imgs[R1P2D1])
        window["-R1P2D2-"].update(dice_imgs[R1P2D2])
        window["-R1P2D3-"].update(dice_imgs[R1P2D3])
        window["-R1P2_roll-"].update(disabled=True)
        window["-P2_score-"].update(P2_score)

        if R1_rolls >= 2:
            window["-R2_start-"].update(disabled=False)

    if event == "-R1P2_reroll-":
        R1P2D4 = random.randint(1, 6)
        if R1P2D4 == R1P2_compare:
            P2_score += 3
        R1_rolls += 1

        window["-P2_score-"].update(P2_score)
        window[R1P2_reroll].update(dice_imgs[R1P2D4])
        window["-R1P2_reroll-"].update(disabled=True)

        if R1_rolls >= 2:
            window["-R2_start-"].update(disabled=False)

    if event == "-R2_start-":
        window["-R2_start-"].update(disabled=True)
        window["-R2P1_roll-"].update(disabled=False)
        window["-R2P2_roll-"].update(disabled=False)

    if event == "-R2P1_roll-":
        # GUI de la apuesta
        par_layout = [[sg.Text("Seleccione su apuesta: ")],
                      [sg.Radio("Par", "P1_bet")],
                      [sg.Radio("Impar", "P1_bet")],
                      [sg.Button("Confirmar")]]
        par_window = sg.Window("Apuesta Jugador 1", par_layout)
        par_event, par_values = par_window.read()
        par_window.close()
        print(par_event, par_values)

        R2P1_par = par_values[0]
        # Roll Jugador 1
        R2P1D1 = random.randint(1, 6)
        R2P1D2 = random.randint(1, 6)
        R2P1D3 = random.randint(1, 6)

        mayor, menor = R2P1D1, R2P1D1
        if R2P1D2 > mayor:
            mayor = R2P1D2
        if R2P1D3 > mayor:
            mayor = R2P1D3
        if R2P1D2 < menor:
            menor = R2P1D2
        if R2P1D3 < menor:
            menor = R2P1D3

        suma = R2P1D1 + R2P1D2 + R2P1D3

        if R2P1_par:
            if suma % 2 == 0:
                P1_score += mayor
                if R2P1D1 % 2 == 0 and R2P1D2 % 2 == 0 and R2P1D3 % 2 == 0:
                    P1_score *= 2
            else:
                P1_score -= menor

        else:
            if suma % 2 == 1:
                P1_score += mayor
                if R2P1D1 % 2 == 1 and R2P1D2 % 2 == 1 and R2P1D3 % 2 == 1:
                    P1_score *= 2
            else:
                P1_score -= menor

        window["-R2P1D1-"].update(dice_imgs[R2P1D1])
        window["-R2P1D2-"].update(dice_imgs[R2P1D2])
        window["-R2P1D3-"].update(dice_imgs[R2P1D3])
        window["-R2P1_roll-"].update(disabled=True)
        window["-P1_score-"].update(P1_score)

        R2_rolls += 1
        if R2_rolls == 2:
            if P1_score == P2_score:
                winner = "Nadie, es un empate..."
            elif P1_score > P2_score:
                winner = P1_name
            else:
                winner = P2_name

            window["-WINNER-"].update(winner)

    if event == "-R2P2_roll-":
        # GUI de la apuesta
        par_layout = [[sg.Text("Seleccione su apuesta: ")],
                      [sg.Radio("Par", "P2_bet")],
                      [sg.Radio("Impar", "P2_bet")],
                      [sg.Button("Confirmar")]]
        par_window = sg.Window("Apuesta Jugador 2", par_layout)
        par_event, par_values = par_window.read()
        par_window.close()
        print(par_event, par_values)

        R2P2_par = par_values[0]

        # Roll Jugador 2
        R2P2D1 = random.randint(1, 6)
        R2P2D2 = random.randint(1, 6)
        R2P2D3 = random.randint(1, 6)

        mayor, menor = R2P2D1, R2P2D1
        if R2P2D2 > mayor:
            mayor = R2P2D2
        if R2P2D3 > mayor:
            mayor = R2P2D3
        if R2P2D2 < menor:
            menor = R2P2D2
        if R2P2D3 < menor:
            menor = R2P2D3

        suma = R2P2D1 + R2P2D2 + R2P2D3

        if R2P2_par:
            if suma % 2 == 0:
                P2_score += mayor
                if R2P2D1 % 2 == 0 and R2P2D2 % 2 == 0 and R2P2D3 % 2 == 0:
                    P2_score *= 2
            else:
                P2_score -= menor

        else:
            if suma % 2 == 1:
                P2_score += mayor
                if R2P2D1 % 2 == 1 and R2P2D2 % 2 == 1 and R2P2D3 % 2 == 1:
                    P2_score *= 2
            else:
                P2_score -= menor

        R2_rolls += 1
        if R2_rolls == 2:
            if P1_score == P2_score:
                winner = "Nadie, es un empate..."
            elif P1_score > P2_score:
                winner = P1_name
            else:
                winner = P2_name
            window["-WINNER-"].update(winner)

        window["-R2P2D1-"].update(dice_imgs[R2P2D1])
        window["-R2P2D2-"].update(dice_imgs[R2P2D2])
        window["-R2P2D3-"].update(dice_imgs[R2P2D3])
        window["-R2P2_roll-"].update(disabled=True)
        window["-P2_score-"].update(P2_score)
        R2_rolls += 1

    if event == "Restart":
        # restart variables and score
        R1_rolls, R2_rolls = 0, 0
        P1_score, P2_score = 0, 0
        R1P1_reroll, R1P2_reroll = 0, 0
        R2P1_par, R2P2_par = None, None

        # restart dice images
        window["-R1P1D1-"].update(dice_imgs[0])
        window["-R1P1D2-"].update(dice_imgs[0])
        window["-R1P1D3-"].update(dice_imgs[0])
        window["-R1P2D1-"].update(dice_imgs[0])
        window["-R1P2D2-"].update(dice_imgs[0])
        window["-R1P2D3-"].update(dice_imgs[0])
        window["-R2P1D1-"].update(dice_imgs[0])
        window["-R2P1D2-"].update(dice_imgs[0])
        window["-R2P1D3-"].update(dice_imgs[0])
        window["-R2P2D1-"].update(dice_imgs[0])
        window["-R2P2D2-"].update(dice_imgs[0])
        window["-R2P2D3-"].update(dice_imgs[0])

        # restart buttons
        window["-R1_start-"].update(disabled=False)
        window["-R1P1_roll-"].update(disabled=True)
        window["-R1P1_reroll-"].update(disabled=True)
        window["-R1P2_roll-"].update(disabled=True)
        window["-R1P2_reroll-"].update(disabled=True)
        window["-R2_start-"].update(disabled=True)
        window["-R2P1_roll-"].update(disabled=True)
        window["-R2P2_roll-"].update(disabled=True)

        # restart score and winner
        window["-P1_score-"].update(0)
        window["-P2_score-"].update(0)
        window["-WINNER-"].update("")

    if event == "Exit":
        break
    if event == sg.WIN_CLOSED:
        break
window.close()
