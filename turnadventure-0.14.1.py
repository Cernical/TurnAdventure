#!/usr/bin/python
#!/bin/bash

import sys #Necesario para los argumentos en CMD
import time #Necesario para el tiempo de espera
import subprocess #Necesario para usar el sistema y sus funciones
from random import randrange #Necesario para el generador aleatorio
clear = lambda: subprocess.call('cls||clear', shell=True) #Llamada al sistema

#Comprobación del modulo de pygame----------------------------------------------
try:
    #Necesario para la música---------------------------------------------------
    from pygame.locals import *
    from pygame import mixer
    import pygame
except:
    modo_compatibilidad = 1 #Placeholder del try--------------------------------
#-------------------------------------------------------------------------------

#Creacion Archivo Requerimientos (Para comprobar si se realizó el setup)--------
try:
    archivo = open("./requirements.conf", "x")
except:
    print()
else:
    archivo = open("./requirements.conf", "w")
    archivo.write("0")
    archivo.close()
#-------------------------------------------------------------------------------

#Dependencias-------------------------------------------------------------------
archivo = open("./requirements.conf", "r")
contenido = archivo.read()

if contenido == "0":
    try:
        subprocess.call("./requirements/debian.sh")
        archivo = open("./requirements.conf", "w")
        archivo.write("1")
        archivo.close()
    except:
        try:
            subprocess.call("./requirements/arch.sh")
            archivo = open("./requirements.conf", "w")
            archivo.write("1")
            archivo.close()
        except:
            subprocess.call("./requirements/windows.bat")
            archivo = open("./requirements.conf", "w")
            archivo.write("1")
            archivo.close()
#-------------------------------------------------------------------------------

Juego = 1
modo_compatibilidad = 0

#System Inputs------------------------------------------------------------------
try:
    if sys.argv[1] == "music_off":
        modo_compatibilidad = 1
except:
    null = 1

#Comprobación del módulo de pygame----------------------------------------------
if modo_compatibilidad == 0:
    try:
        mixer.init()
        mixer.music.load("./music/opening.mp3")
        mixer.music.play(1)
    except:
        modo_compatibilidad = 1
        clear()
        print("No se ha encontrado el modulo de pygame, puedes instalarlo usando: pip install pygame")
        print("Se iniciará el juego sin música...")
        time.sleep(3)
#-------------------------------------------------------------------------------

#Funciones----------------------------------------------------------------------
def perro(posicion):

    #Stats----------------------------------------------------------------------
    nivel_perro = 1

    randomnumero1=(randrange(50,60)) #Vida--------------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_vida_min
    s_vida_min = 50
    #---------------------------------------------------------------------------
    bonus_vida = nivel_perro*5
    global vida_perro
    vida_perro = randomnumero1 + bonus_vida

    randomnumero1=(randrange(15,20)) #Velocidad---------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_velocidad_min
    s_velocidad_min = 15
    #---------------------------------------------------------------------------
    bonus_velocidad = nivel_perro*2
    global velocidad_perro
    velocidad_perro = randomnumero1 + bonus_velocidad

    randomnumero1=(randrange(21,25)) #Ataque------------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_ataque_min
    s_ataque_min = 21
    #---------------------------------------------------------------------------
    bonus_ataque = nivel_perro*5
    global ataque_perro
    ataque_perro = randomnumero1 + bonus_ataque

    randomnumero1=(randrange(15,20)) #Defensa-----------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_defensa_min
    s_defensa_min = 15
    #---------------------------------------------------------------------------
    bonus_defensa = nivel_perro*3
    global defensa_perro
    defensa_perro = randomnumero1 + bonus_defensa

    #Skins----------------------------------------------------------------------
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

def buho(posicion):

    #Stats----------------------------------------------------------------------
    nivel_buho = 1

    randomnumero1=(randrange(40,50)) #Vida--------------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_vida_min
    s_vida_min = 40
    #---------------------------------------------------------------------------
    bonus_vida = nivel_buho*3
    global vida_buho
    vida_buho = randomnumero1 + bonus_vida

    randomnumero1=(randrange(20,25)) #Velocidad---------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_velocidad_min
    s_velocidad_min = 20
    #---------------------------------------------------------------------------
    bonus_velocidad = nivel_buho*3
    global velocidad_buho
    velocidad_buho = randomnumero1 + bonus_velocidad

    randomnumero1=(randrange(18,24)) #Ataque------------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_ataque_min
    s_ataque_min = 18
    #---------------------------------------------------------------------------
    bonus_ataque = nivel_buho*5
    global ataque_buho
    ataque_buho = randomnumero1 + bonus_ataque

    randomnumero1=(randrange(18,22)) #Defensa-----------------------------------
    #Para pantalla de stats-----------------------------------------------------
    global s_defensa_min
    s_defensa_min = 18
    #---------------------------------------------------------------------------
    bonus_defensa = nivel_buho*3
    global defensa_buho
    defensa_buho = randomnumero1 + bonus_defensa

    #Skins----------------------------------------------------------------------
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

def Mod_combate():

    #Carga efectos sonido-------------------------------------------------------
    if modo_compatibilidad == 0:
        hit = mixer.Sound("./music/normalHit.mp3")
        criticalHit = mixer.Sound("./music/criticalHit.mp3")
        lowhealth = mixer.Sound("./music/lowhealth.mp3")

        mixer.music.load("./music/oak.mp3")
        mixer.music.play(-1)
#-------------------------------------------------------------------------------

    Supervivencia = 1
    victorias = 0
    continuarPartida = 0

    while Supervivencia == 1:

        #Asignación de parámetros jugador y enemigo-----------------------------
        asignacion = 1

        #Comprobación transcurso partida y restauración de vida-----------------
        if continuarPartida == 0:
            while asignacion == 1:

                print()
                #Selección personajes-------------------------------------------
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

                if respuesta == "1":
                    buho(0)
                    VidaJugador = vida_buho
                    VidaTotalJugador = VidaJugador #Asignación para calculo de barra.v------
                    VelocidadJugador = velocidad_buho
                    AtaqueJugador = ataque_buho
                    DefensaJugador = defensa_buho
                    asignacion = 0
                else:
                    if respuesta == "2":
                        perro(0)
                        VidaJugador = vida_perro
                        VidaTotalJugador = VidaJugador #Asignación para calculo de barra.v------
                        VelocidadJugador = velocidad_perro
                        AtaqueJugador = ataque_perro
                        DefensaJugador = defensa_perro
                        asignacion = 0
                    else:
                        print()
                        print("No has seleccionado un personaje correcto")
                        time.sleep(3)
        else:
            VidaJugador = VidaTotalJugador #restauración de vida----------------

        respuesta_enemigo=(randrange(1,3))
        if respuesta_enemigo == 1:
            buho(0)
            VidaEnemigo = vida_buho
            VidaTotalEnemigo = VidaEnemigo #Asignación para calculo de barra.v------
            VelocidadEnemigo = velocidad_buho
            AtaqueEnemigo = ataque_buho
            DefensaEnemigo = defensa_buho
        else:
            perro(0)
            VidaEnemigo = vida_perro
            VidaTotalEnemigo = VidaEnemigo #Asignación para calculo de barra.v------
            VelocidadEnemigo = velocidad_perro
            AtaqueEnemigo = ataque_perro
            DefensaEnemigo = defensa_perro

        #Inicio del combate---------------------------------------------------------
        Combate = 1
        calculoVelocidad = 1

        if modo_compatibilidad == 0:
            musica = (randrange(1,3))
            if musica == 1:
                mixer.music.stop()
                mixer.music.load("./music/trainer.mp3")
                mixer.music.play(-1)
            else:
                mixer.music.stop()
                mixer.music.load("./music/wild.mp3")
                mixer.music.play(-1)

        combateIniciado = 0
        pocavida = 0

        while Combate == 1: #Inicio modulo de combate-------------------------------

            #Asociar porcentajes con vida Enemigo-----------------------------------
            ochentaporciento = VidaTotalEnemigo*0.8
            sesentaporciento = VidaTotalEnemigo*0.65
            cincuentaporciento = VidaTotalEnemigo*0.5
            treintaporciento = VidaTotalEnemigo*0.35
            diezporciento = VidaTotalEnemigo*0.15

            if VidaEnemigo <= 0:
                barra1 = "|      |"
                VidaEnemigo = 0
            else:
                if VidaEnemigo <= diezporciento:
                    barra1 = "|█     |"
                else:
                    if VidaEnemigo <= treintaporciento:
                        barra1 = "|██    |"
                    else:
                        if VidaEnemigo <= cincuentaporciento:
                            barra1 = "|███   |"
                        else:
                            if VidaEnemigo <= sesentaporciento:
                                barra1 = "|████  |"
                            else:
                                if VidaEnemigo <= ochentaporciento:
                                    barra1 = "|█████ |"
                                else:
                                    barra1 = "|██████|"

                #Asociar porcentajes con vida Jugador-------------------------------
                ochentaporciento = VidaTotalJugador*0.8
                sesentaporciento = VidaTotalJugador*0.65
                cincuentaporciento = VidaTotalJugador*0.5
                treintaporciento = VidaTotalJugador*0.35
                diezporciento = VidaTotalJugador*0.15

                if VidaJugador <= 0:
                    barra2 = "|      |"
                    VidaJugador = 0
                else:
                    if VidaJugador <= diezporciento:
                        barra2 = "|█     |"

                        if pocavida == 0:
                            mixer.music.stop()
                            #lowhealth.play(-1)
                            mixer.music.load("./music/lowhealthBW.mp3")
                            mixer.music.play(-1)
                            pocavida = 1
                    else:
                        if VidaJugador <= treintaporciento:
                            barra2 = "|██    |"

                            if pocavida == 0:
                                mixer.music.stop()
                                #lowhealth.play(-1)
                                mixer.music.load("./music/lowhealthBW.mp3")
                                mixer.music.play(-1)
                                pocavida = 1
                        else:
                            if VidaJugador <= cincuentaporciento:
                                barra2 = "|███   |"
                            else:
                                if VidaJugador <= sesentaporciento:
                                    barra2 = "|████  |"
                                else:
                                    if VidaJugador <= ochentaporciento:
                                        barra2 = "|█████ |"
                                    else:
                                        barra2 = "|██████|"

            #Campo de batalla---------------------------------------------------
            if combateIniciado == 0:
                #Mensaje bienvenida-------------------------------------------------
                clear()
                if respuesta_enemigo == 1:
                    print("¡Te vas a enfrentar a BUHO!")
                    print()
                    time.sleep(3)
                    combateIniciado = 1
                else:
                    if respuesta_enemigo != 1:
                        print("¡Te vas a enfrentar a PERRO!")
                        print()
                        time.sleep(3)
                        combateIniciado = 1
            clear()
            print("_______________________________________________________________________")
            print("")
            #Mostrar nombre y barra---------------------------------------------
            if respuesta_enemigo == 1: print("                                                 ","BUHO",barra1)
            if respuesta_enemigo != 1: print("                                              ","PERRO",barra1)
            #Mostrar personajes-------------------------------------------------
            if respuesta_enemigo == 1:
                buho("enemigo")
            else:
                perro("enemigo")
            print("         /\ ")
            print("                              /\  ")
            print("                                               /\  ")
            print("")
            print("                /\  ")
            print("")
            print("                                  /\                       /\ ")
            print("")
            #Mostrar personajes-----------------------------------------------------
            if respuesta == "1":
                buho("aliado")
            else:
                perro("aliado")
            #Mostrar nombre y barra---------------------------------------------
            if respuesta == "1": print("        ","BUHO",barra2,VidaJugador,"/",VidaTotalJugador)
            if respuesta != "1": print("         ","PERRO",barra2,VidaJugador,"/",VidaTotalJugador)
            print("_______________________________________________________________________")
            print()

            #¿Ha acabado la partida?
            if VidaEnemigo <= 0:
                if modo_compatibilidad == 0:
                    #if pocavida == 1:
                    #    lowhealth.stop()

                    mixer.music.stop()
                    mixer.music.load("./music/victory.mp3")
                    mixer.music.play(-1)

                victorias = victorias + 1
                print("¡Ha ganado el jugador!",victorias,"victorias!")
                print()
                input("Pulsa cualquier tecla para continuar: ")
                Combate = 0
                continuarPartida = 1

                #En caso de salir al ganar--------------------------------------
                #if modo_compatibilidad == 0:
                #    mixer.music.stop()
                #    mixer.music.load("./music/titulo.mp3")
                #    mixer.music.play(-1)

            else:
                if VidaJugador <= 0:
                    if modo_compatibilidad == 0:
                        mixer.music.stop()

                    print("¡Ha ganado tu enemigo!")
                    print()
                    input("Pulsa cualquier tecla para continuar: ")
                    Combate = 0
                    Supervivencia = 0
                    if modo_compatibilidad == 0:
                        mixer.music.load("./music/titulo.mp3")
                        mixer.music.play(-1)

                else:
                    #i = input("Selecciona movimiento (Ataque (A)): ")

                    #Cálculo Velocidad----------------------------------------------
                    while calculoVelocidad == 1:
                        if VelocidadJugador >= VelocidadEnemigo:
                            jugadorAtaca = 1
                            enemigoAtaca = 0
                            calculoVelocidad = 0
                        else:
                            enemigoAtaca = 1
                            jugadorAtaca = 0
                            calculoVelocidad = 0
                    #---------------------------------------------------------------
                    #Cálculo de acumulador velocidad--------------------------------
                    if VelocidadJugador >= VelocidadEnemigo:
                        acumuladorVelocidadJugador = VelocidadJugador - VelocidadEnemigo
                        if acumuladorVelocidadJugador >= VelocidadEnemigo:
                            jugadorAtaca = jugadorAtaca + 1
                            acumuladorVelocidadJugador = 0

                    else:
                        acumuladorVelocidadEnemigo = VelocidadEnemigo - VelocidadJugador
                        if acumuladorVelocidadEnemigo >= VelocidadJugador:
                            enemigoAtaca = enemigoAtaca + 1
                            acumuladorVelocidadEnemigo = 0

                    #---------------------------------------------------------------

                    #Turnos---------------------------------------------------------
                    if jugadorAtaca >= enemigoAtaca:
                        i = input("Selecciona movimiento (Ataque (A)): ")
                        #Selección Movimientos Jugador------------------------------
                        if i == "A" or i == "a":
                            DañoRealizado = AtaqueJugador - DefensaEnemigo

                            #Bonus daño aleatorio-----------------------------------
                            DañoRandom = 0
                            critico = 0

                            randomnumero2=(randrange(1,5))
                            if randomnumero2 == 1:
                                if DañoRealizado > 10:
                                    DañoRandom = DañoRealizado * 0.1
                                else:
                                    DañoRandom = DañoRandom + 1
                                DañoRealizado = DañoRealizado + DañoRandom
                            else:
                                if randomnumero2 == 2:
                                    if DañoRealizado > 10:
                                        DañoRandom = DañoRealizado * 0.2
                                    else:
                                        DañoRandom = DañoRandom + 2
                                    DañoRealizado = DañoRealizado + DañoRandom
                                else:
                                    if randomnumero2 == 3:
                                        if DañoRealizado > 10:
                                            DañoRandom = DañoRealizado * 0.3
                                        else:
                                            DañoRandom = DañoRandom + 3
                                        DañoRealizado = DañoRealizado + DañoRandom
                                    else:
                                        if DañoRealizado > 10:
                                            DañoRandom = DañoRealizado * 2
                                            critico = 1
                                        else:
                                            DañoRandom = DañoRandom + 8
                                            critico = 1
                                        DañoRealizado = DañoRealizado + DañoRandom

                            DañoRealizado = int(DañoRealizado) #Pueden aparecer FP
                            VidaEnemigo = VidaEnemigo - DañoRealizado

                            #hit sound------------------------------------------
                            if modo_compatibilidad == 0:
                                if critico == 0:
                                    #mixer.music.stop()
                                    hit.play()
                                else:
                                    #mixer.music.stop()
                                    criticalHit.play()

                            print("")
                            print("Has ocasionado",DañoRealizado,"de daño")
                            if critico == 1:
                                print()
                                print("¡Ataque Crítico!")
                                print("")

                            time.sleep(3)
                            jugadorAtaca = jugadorAtaca - 1
                            enemigoAtaca = enemigoAtaca + 1
                        else:
                            if i == "B" or i == "b":
                                randomnumero1=(randrange(0,35))
                                VidaEnemigo = VidaEnemigo - randomnumero1
                                print("")
                                print("Has ocasionado",randomnumero1,"de daño")
                                time.sleep(3)
                                jugadorAtaca = jugadorAtaca - 1
                                enemigoAtaca = enemigoAtaca + 1
                            else:
                                if i == "C" or i == "c":
                                    randomnumero1=(randrange(0,35))
                                    VidaEnemigo = VidaEnemigo - randomnumero1
                                    print("")
                                    print("Has ocasionado",randomnumero1,"de daño")
                                    time.sleep(3)
                                    jugadorAtaca = jugadorAtaca - 1
                                    enemigoAtaca = enemigoAtaca + 1
                                else:
                                    print("")
                                    print("No has elegido un ataque correcto")
                                    time.sleep(3)

                    else:
                        if enemigoAtaca > jugadorAtaca:

                            #Selección Movimientos NPC--------------------------------------------------
                            #randomnumero1=(randrange(1,3))          #Rango de suma
                            randomnumero1 = 1

                            if randomnumero1 == 1:
                                DañoRealizado = AtaqueEnemigo - DefensaJugador

                                #Bonus daño aleatorio-----------------------------------
                                DañoRandom = 0
                                critico = 0

                                randomnumero2=(randrange(1,5))
                                if randomnumero2 == 1:
                                    if DañoRealizado > 10:
                                        DañoRandom = DañoRealizado * 0.1
                                    else:
                                        DañoRandom = DañoRandom + 1
                                    DañoRealizado = DañoRealizado + DañoRandom
                                else:
                                    if randomnumero2 == 2:
                                        if DañoRealizado > 10:
                                            DañoRandom = DañoRealizado * 0.2
                                        else:
                                            DañoRandom = DañoRandom + 2
                                        DañoRealizado = DañoRealizado + DañoRandom
                                    else:
                                        if randomnumero2 == 3:
                                            if DañoRealizado > 10:
                                                DañoRandom = DañoRealizado * 0.3
                                            else:
                                                DañoRandom = DañoRandom + 3
                                            DañoRealizado = DañoRealizado + DañoRandom
                                        else:
                                            if DañoRealizado > 10:
                                                DañoRandom = DañoRealizado * 2
                                                critico = 1
                                            else:
                                                DañoRandom = DañoRandom + 8
                                                critico = 1
                                            DañoRealizado = DañoRealizado + DañoRandom

                                DañoRealizado = int(DañoRealizado) #Pueden aparecer FP--
                                VidaJugador = VidaJugador - DañoRealizado

                                if modo_compatibilidad == 0:
                                    if critico == 0:
                                        #mixer.music.stop()
                                        hit.play()
                                    else:
                                        #mixer.music.stop()
                                        criticalHit.play()

                                print("El enemigo ha causado",DañoRealizado,"de daño")
                                if critico == 1:
                                    print()
                                    print("¡Ataque Crítico!")

                                time.sleep(3)
                                enemigoAtaca = enemigoAtaca - 1
                                jugadorAtaca = jugadorAtaca + 1
                            else:
                                if randomnumero1 == 2:
                                    VidaJugador = VidaJugador - 17
                                    print("")
                                    print("El enemigo ha causado 17 de daño")
                                    time.sleep(3)
                                    enemigoAtaca = enemigoAtaca - 1
                                    jugadorAtaca = jugadorAtaca + 1
                                else:
                                    VidaJugador = VidaJugador - 8
                                    print("")
                                    print("El enemigo ha causado 8 de daño")
                                    time.sleep(3)
                                    enemigoAtaca = enemigoAtaca - 1
                                    jugadorAtaca = jugadorAtaca + 1

def StatsTotales(posicion):

    clear()

    print()
    buho(posicion)
    print()
    print("Vida:",s_vida_min)
    print("Ataque:",s_ataque_min)
    print("Defensa:",s_defensa_min)
    print("Velocidad:",s_velocidad_min)
    print()
    perro(posicion)
    print()
    print("Vida:",s_vida_min)
    print("Ataque:",s_ataque_min)
    print("Defensa:",s_defensa_min)
    print("Velocidad:",s_velocidad_min)
    print("")

    input("Pulse una tecla para continuar: ")

def Introduccion():

    #Regla-01234567890123456789012345678901234567890123456789012345678901234567890
    #                                         |
    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((ovo))________________________________")
    print("                                ():::() ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((-v-))________________________________")
    print("                                ():::() ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((ovo))________________________________")
    print("                                ():::() ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((-v-))________________________________")
    print("                             (/ /):::(\ \) ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((ovo))________________________________")
    print("                               (/):::(\) ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((ovo))________________________________")
    print("                                ():::() ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("________________________________((-v-))________________________________")
    print("                             (/ /):::(\ \) ")
    print("                                  VVV ")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("                                ((ovo)) ")
    print("_____________________________(/ /):::(\ \)_____________________________")
    print("                                  VVV ")
    print("")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("                                ((-v-)) ")
    print("                             (/ /):::(\ \) ")
    print("__________________________________VVV__________________________________")
    print("")
    print("")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("/\        /\            /\            /\        /\          /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("                                 /\ /\ ")
    print("                                ((ovo)) ")
    print("                             (/ /):::(\ \) ")
    print("                                  VVV")
    print("")
    print("_______________________________________________________________________")
    print("")
    print("")
    print("            /\              /\                  /\         /\ ")
    print("     /\           /\            /\       /\            /\        /\ ")
    print("_______________________________________________________________________")
    time.sleep(1)

    clear()
    print("_______________________________________________________________________")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("_______________________________________________________________________")
    time.sleep(1)

#Introduccion-------------------------------------------------------------------
Introduccion()

if modo_compatibilidad == 0:
    mixer.music.load("./music/titulo.mp3")
    mixer.music.play(-1)

#Menú---------------------------------------------------------------------------
while Juego == 1:

    #Regla-01234567890123456789012345678901234567890123456789012345678901234567890
    #                                         |
    clear()
    print("_______________________________________________________________________")
    print()
    print("           ¡Bienvenido a TurnAdventure! v0.14.1 (Farfetch'd)")
    print("_______________________________________________________________________")
    print()
    print("- Modo Random (1)")
    print()
    print("- Modo Stats (2)")
    print()
    print("- Salir (3)")
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
            StatsTotales("aliado")
        else:
            if r == "3":
                if modo_compatibilidad == 0:
                    mixer.music.stop()
                    Juego = 0
                else:
                    Juego = 0
            else:
                print("")
                print("No has seleccionado un modo correcto")
                time.sleep(3)
