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
try:
    subprocess.call("./requirements/debian.sh")
except:
    try:
        subprocess.call("./requirements/arch.sh")
    except:
        subprocess.call("./requirements/windows.bat")

Juego = 1
modo_compatibilidad = 0
null = 1 #Placeholder de los if-------------------------------------------------

#Comprobación del módulo de pygame----------------------------------------------
try:
    mixer.init()
    mixer.music.load("./music/titulo.mp3")
    mixer.music.play(-1)
except:
    modo_compatibilidad = 1
    clear()
    print("No se ha encontrado el modulo de pygame, puedes instalarlo usando: pip install pygame")
    print("Se iniciará el juego sin música...")
    time.sleep(3)

#Funciones----------------------------------------------------------------------
def perro(posicion):

    nivel_perro = 1
    randomnumero1=(randrange(50,75))
    bonus_vida = nivel_perro*5
    global vida_perro
    vida_perro = randomnumero1 + bonus_vida

    randomnumero1=(randrange(10,20))
    bonus_velocidad = nivel_perro*2
    global velocidad_perro
    velocidad_perro = randomnumero1 + bonus_velocidad

    if posicion == "enemigo":
        print("                                                                /^ ^\ ")
        print("                                                               / 0 0 \ ")
        print("                                                               V\ Y /V ")
        print("                                                                / - \ ")
        print("                                                               /    | ")
        print("                                                              V__) || ")
    else:
        if posicion == "aliado":
            print("   /^ ^\ ")
            print("  / 0 0 \ ")
            print("  V\ Y /V ")
            print("   / - \ ")
            print("  /    | ")
            print(" V__) || ")
        else:
            null

def buho(posicion):

    nivel_buho = 1
    randomnumero1=(randrange(35,50))
    bonus_vida = nivel_buho*3
    global vida_buho
    vida_buho = randomnumero1 + bonus_vida

    randomnumero1=(randrange(30,50))
    bonus_velocidad = nivel_buho*3
    global velocidad_buho
    velocidad_buho = randomnumero1 + bonus_velocidad

    if posicion == "aliado":
        print("  /\ /\ ")
        print(" ((ovo)) ")
        print(" ():::() ")
        print("   VVV ")
    else:
        if posicion == "enemigo":
            print("                                                                 /\ /\ ")
            print("                                                                ((ovo)) ")
            print("                                                                ():::() ")
            print("                                                                  VVV ")
        else:
            null

def Mod_combate():

    if modo_compatibilidad == 0:
        mixer.music.load("./music/oak.mp3")
        mixer.music.play(-1)
    else:
        null

    #Selección personajes-------------------------------------------------------
    clear()
    print()
    buho("aliado")
    print()
    print("(1)")
    print()
    perro("aliado")
    print()
    print("(2)")
    print()
    respuesta = input("¿Qué personaje quieres seleccionar? (1,2): ")

    #Asignación de parámetros jugador y enemigo---------------------------------
    if respuesta == "1":
        buho(0)
        VidaJugador = vida_buho
        VelocidadJugador = velocidad_buho
    else:
        perro(0)
        VidaJugador = vida_perro
        VelocidadJugador = velocidad_perro

    respuesta_enemigo=(randrange(0,3))
    if respuesta_enemigo == 1:
        buho(0)
        VidaEnemigo = vida_buho
        velocidadEnemigo = velocidad_buho
    else:
        perro(0)
        VidaEnemigo = vida_perro
        velocidadEnemigo = velocidad_perro

    #Inicio del combate---------------------------------------------------------
    Combate = 1

    if modo_compatibilidad == 0:
        mixer.music.stop()
        mixer.music.load("./music/trainer.mp3")
        mixer.music.play(-1)
    else:
        null

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
        #Mostrar personajes-----------------------------------------------------
        if respuesta_enemigo == 1:
            buho("enemigo")
        else:
            perro("enemigo")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        #Mostrar personajes-----------------------------------------------------
        if respuesta == "1":
            buho("aliado")
        else:
            perro("aliado")
        print("          ", barra2, VidaJugador)
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
                mixer.music.load("./music/titulo.mp3")
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
                    mixer.music.load("./music/titulo.mp3")
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
    print("                  ¡Bienvenido a TurnAdventure! v0.6.0")
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

#Bugs---------------------------------------------------------------------------
#línea 140: si NPC y Jugador seleccionan mismo animal, ambos tendrán los mismos stats
