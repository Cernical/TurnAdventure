#!/usr/bin/python
#!/bin/bash

import multiprocessing
import time
import subprocess
from playsound import playsound
from pygame.locals import *
from pygame import mixer
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

#Funciones----------------------------------------------------------------------
def Mod_combate():

    try:
        p = multiprocessing.Process(target=playsound, args=("batalla.mp3",))
        p.start()
    except:
        mixer.init()
        mixer.music.load("C:\\Users\esdom\Desktop\TurnAdventure-testing\intro.wav")
        mixer.music.play()

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
            print("¡Ha ganado el jugador!")
            print()
            input("Pulsa cualquier tecla para continuar: ")
            Combate = 0
            try:
                p.terminate()
            except:
                mixer.music.stop()

        else:
            if VidaJugador <= 0:
                print("¡Ha ganado tu enemigo!")
                print()
                input("Pulsa cualquier tecla para continuar: ")
                Combate = 0
                try:
                    p.terminate()
                except:
                    mixer.music.stop()

            else:
                #Selección Movimientos Jugador----------------------------------------------
                i = input("Selecciona movimiento (A,B y C): ")
                if i == "A" or i == "a":
                    from random import randrange
                    randomnumero1=(randrange(0,15))
                    VidaEnemigo = VidaEnemigo - randomnumero1
                    print("")
                    print("Has ocasionado",randomnumero1,"de daño")
                    time.sleep(3)
                else:
                    if i == "B" or i == "b":
                        from random import randrange
                        randomnumero1=(randrange(0,15))
                        VidaEnemigo = VidaEnemigo - randomnumero1
                        print("")
                        print("Has ocasionado",randomnumero1,"de daño")
                        time.sleep(3)
                    else:
                        if i == "C" or i == "c":
                            from random import randrange
                            randomnumero1=(randrange(0,15))
                            VidaEnemigo = VidaEnemigo - 8
                            print("")
                            print("Has ocasionado",randomnumero1,"de daño")
                            time.sleep(3)
                        else:
                            print("")
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


while Juego == 1:

    clear()
    p = multiprocessing.Process(target=playsound, args=("intro.mp3",))
    p.start()
    print("_______________________________________________________________________")
    print()
    print("                  ¡Bienvenido a TurnAdventure! v0.2.0")
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
        p.terminate()
        Mod_combate()
    else:
        if r == "2":
            p.terminate()
            Juego = 0
        else:
            p.terminate()
            print("")
            print("No has seleccionado un modo correcto")
            time.sleep(3)
