#!/usr/bin/python
#!/bin/bash

import time
import subprocess

try:
    from pygame.locals import *
    from pygame import mixer
except:
    modo_compatibilidad = 1 #Placeholder del try--------------------------------

from random import randrange
clear = lambda: subprocess.call('cls||clear', shell=True)

#Dependencias-------------------------------------------------------------------
"""try:
    subprocess.call("debian.sh")
except:
    try:
        subprocess.call("arch.sh")
    except:
        subprocess.call("windows.bat")
"""

Juego = 1
modo_compatibilidad = 0
null = 1 #Placeholder de los if-------------------------------------------------

#Comprobación del módulo de pygame----------------------------------------------
try:
    mixer.init()
    mixer.music.load("./music/intro.mp3")
    mixer.music.play(-1)
except:
    modo_compatibilidad = 1
    clear()
    print("No se ha encontrado el modulo de pygame, puedes instalarlo usando: pip install pygame")
    print("Se iniciará el juego sin música...")
    time.sleep(3)

#Funciones----------------------------------------------------------------------
def Mod_combate():

    if modo_compatibilidad == 0:
        mixer.music.load("./music/lance.mp3")
        mixer.music.play(-1)
    else:
        null

    VidaJugador = 100
    VelocidadJugador = 20
    VidaEnemigo = 100
    VelocidadEnemigo = 20

    Combate = 1

    while Combate == 1:

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

        clear()
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
        print()

        #¿Ha acabado la partida?
        if VidaEnemigo <= 0:
            if modo_compatibilidad == 0:
                mixer.music.stop()
                mixer.music.load("./music/victory.mp3")
                mixer.music.play(-1)
            else:
                null
            print("¡Ha ganado el jugador!")
            print()
            input("Pulsa cualquier tecla para continuar: ")
            Combate = 0
            if modo_compatibilidad == 0:
                mixer.music.stop()
                mixer.music.load("./music/intro.mp3")
                mixer.music.play(-1)
            else:
                null
        else:
            if VidaJugador <= 0:
                if modo_compatibilidad == 0:
                    mixer.music.stop()
                else:
                    null
                print("¡Ha ganado tu enemigo!")
                print()
                input("Pulsa cualquier tecla para continuar: ")
                Combate = 0
                if modo_compatibilidad == 0:
                    mixer.music.load("./music/intro.mp3")
                    mixer.music.play(-1)
                else:
                    null
            else:
                #Selección Movimientos Jugador----------------------------------------------
                i = input("Selecciona movimiento (A,B y C): ")
                if i == "A" or i == "a":
                    randomnumero1=(randrange(0,35))
                    VidaEnemigo = VidaEnemigo - randomnumero1
                    print("")
                    print("Has ocasionado",randomnumero1,"de daño")
                    time.sleep(3)
                else:
                    if i == "B" or i == "b":
                        randomnumero1=(randrange(0,35))
                        VidaEnemigo = VidaEnemigo - randomnumero1
                        print("")
                        print("Has ocasionado",randomnumero1,"de daño")
                        time.sleep(3)
                    else:
                        if i == "C" or i == "c":
                            randomnumero1=(randrange(0,35))
                            VidaEnemigo = VidaEnemigo - randomnumero1
                            print("")
                            print("Has ocasionado",randomnumero1,"de daño")
                            time.sleep(3)
                        else:
                            print("")
                            print("No has elegido un ataque correcto")

                #Selección Movimientos NPC--------------------------------------------------
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

#Menú---------------------------------------------------------------------------
while Juego == 1:

    clear()
    print("_______________________________________________________________________")
    print()
    print("                  ¡Bienvenido a TurnAdventure! v0.5.0")
    print("_______________________________________________________________________")
    print()
    print("- Modo Random (1)")
    print()
    print("- Salir (2)")
    print()
    print("-----------------------------------------------------------------------")
    print("")

    r = input("Seleccione modo de juego: ")
    if r == "1":
        if modo_compatibilidad == 0:
            mixer.music.stop()
            Mod_combate()
        else:
            Mod_combate()
    else:
        if r == "2":
            if modo_compatibilidad == 0:
                mixer.music.stop()
                Juego = 0
            else:
                Juego = 0
        else:
            print("")
            print("No has seleccionado un modo correcto")
            time.sleep(3)
