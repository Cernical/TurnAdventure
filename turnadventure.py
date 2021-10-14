#!/usr/bin/python

import time
import subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)

juego = 1
VidaJugador = 100
VidaEnemigo = 100

while juego == 1:
    clear()

    if VidaEnemigo <= 0:
        barra1 = ""
        VidaEnemigo = 0
    else:
        if VidaEnemigo <= 39:
            barra1 = "██ "
        else:
            if VidaEnemigo <= 49:
                barra1 = "███ "
            else:
                if VidaEnemigo <= 76:
                    barra1 = "████ "
                else:
                    if VidaEnemigo <= 89:
                        barra1 = "█████ "
                    else:
                        barra1 = "██████"

        if VidaJugador <= 0:
            barra2 = ""
            VidaJugador = 0
        else:
            if VidaJugador <= 39:
                barra2 = "██ "
            else:
                if VidaJugador <= 49:
                    barra2 = "███ "
                else:
                    if VidaJugador <= 76:
                        barra2 = "████ "
                    else:
                        if VidaJugador <= 89:
                            barra2 = "█████ "
                        else:
                            barra2 = "██████"

    print("_______________________________________________________________________")
    print("")
    print("                                                   ", barra1, VidaEnemigo)
    print("                                                                /^ ^\ ")
    print("                                                               / 0 0 \ ")
    print("                                                               V\ Y /V ")
    print("                                                                / - \ ")
    print("                                                               /    | ")
    print("                                                              V__) || ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(" /\ /\ ")
    print("((ovo)) ")
    print("():::() ")
    print("  VVV ")
    print("       ", barra2, VidaJugador)
    print("_______________________________________________________________________")

    #¿Ha acabado la partida?
    if VidaEnemigo <= 0:
        print("¡Ha ganado el jugador!")
        juego = 0
    else:
        if VidaJugador <= 0:
            print("¡Ha ganado tu enemigo!")
            juego = 0
        else:
            #Selección Movimientos Jugador----------------------------------------------
            i = input("Selecciona movimiento (A,B y C): ")
            if i == "A" or i == "a":
                VidaEnemigo = VidaEnemigo - 25
                print("")
                print("Has ocasionado 25 de daño")
                time.sleep(3)
            else:
                if i == "B" or i == "b":
                    VidaEnemigo = VidaEnemigo - 17
                    print("")
                    print("Has ocasionado 17 de daño")
                    time.sleep(3)
                else:
                    if i == "C" or i == "c":
                        VidaEnemigo = VidaEnemigo - 8
                        print("")
                        print("Has ocasionado 8 de daño")
                        time.sleep(3)
                    else:
                        print("No has elegido un ataque correcto")

            #Selección Movimientos NPC--------------------------------------------------
            from random import randrange
            randomnumero1=(randrange(1,3))          #Rango de suma
            if randomnumero1 == 1:
                VidaJugador = VidaJugador - 25
                print("")
                print("El enemigo ha causado 25 de daño")
                time.sleep(3)
            else:
                if randomnumero1 == 2:
                    VidaJugador = VidaJugador - 17
                    print("")
                    print("El enemigo ha causado 17 de daño")
                    time.sleep(3)
                else:
                    VidaJugador = VidaJugador - 8
                    print("")
                    print("El enemigo ha causado 8 de daño")
                    time.sleep(3)
