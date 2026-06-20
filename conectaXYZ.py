#!/usr/bin/python
# -*- coding: utf-8 -*-

# =====================================================
# COPA FUTBOTMX 2026
# =====================================================

import random
import os

import datetime
import json
import socket

# import feedparser
# import urllib
# import urllib2
# import numpy
# from geopy.distance import vincenty
# from dateutil.relativedelta import relativedelta

# Variables globales
partido_segundos = 0
tiempo_actual = 1

gol_local = 0
gol_visita = 0

pelota_x = 15

equipo_local = "EQUIPO LOCAL MX"
equipo_visita = "EQUIPO VISITANTE"


def mostrarCopaFutbotMX():

    global partido_segundos
    global tiempo_actual

    # Si ya terminó el partido no hacer nada
    if tiempo_actual > 2:
        return

    partido_segundos += 15

    # Fin primer tiempo
    if partido_segundos > 300 and tiempo_actual == 1:

        #print ""
        print ("\033[1;43m=====================================\033[1;m")
        print ("\033[1;43m           MEDIO TIEMPO              \033[1;m")
        print ("\033[1;43m=====================================\033[1;m")

        tiempo_actual = 2
        partido_segundos = 0

        return

    # Fin segundo tiempo
    if partido_segundos > 300 and tiempo_actual == 2:

        #print ""
        print ("\033[1;41m=====================================\033[1;m")
        print ("\033[1;41m           FIN DEL PARTIDO           \033[1;m")
        print ("\033[1;41m=====================================\033[1;m")

        print ("")
        print ("\033[1;32m%s %d\033[1;m" % (equipo_local,gol_local))
        print ("\033[1;31m%s %d\033[1;m" % (equipo_visita,gol_visita))

        tiempo_actual = 3
        return

    generarEvento()
    dibujarCancha()


def generarEvento():

    global pelota_x
    global gol_local
    global gol_visita

    pelota_x += random.randint(-4,4)

    if pelota_x < 1:
        pelota_x = 1

    if pelota_x > 30:
        pelota_x = 30

    evento = random.randint(1,100)

    if evento <= 5:

        gol_local += 1

        print ("")
        print ("\033[1;42m#####################################\033[1;m")
        print ("\033[1;42m       GOOOOOOL FUTBOTMX !!!         \033[1;m")
        print ("\033[1;42m#####################################\033[1;m")

    elif evento >= 96:

        gol_visita += 1

        print ("")
        print ("\033[1;41m#####################################\033[1;m")
        print ("\033[1;41m        GOOOOOOL VISITANTE  !!!      \033[1;m")
        print ("\033[1;41m#####################################\033[1;m")

    elif evento <= 20:
        print ("\033[1;33mAtaque de FUTBOTMX\033[1;m")

    elif evento <= 40:
        print ("\033[1;36mDisparo a porteria\033[1;m")

    elif evento <= 60:
        print ("\033[1;35mRecuperacion en medio campo\033[1;m")

    elif evento <= 80:
        print ("\033[1;34mCentro al area\033[1;m")

    else:
        print ("\033[1;37mBalon circulando\033[1;m")


def dibujarCancha():

    global pelota_x
    global partido_segundos
    global tiempo_actual
    global gol_local
    global gol_visita

    print ("")
    print ("\033[1;42m=====================================\033[1;m")
    print ("\033[1;42m          COPA FUTBOTMX              \033[1;m")
    print ("\033[1;42m=====================================\033[1;m")

    #print ("\033[1;33mTIEMPO : %d\033[1;m") % tiempo_actual
    #print ("\033[1;36mSEGUNDOS : %03d / 300\033[1;m") % partido_segundos

    print ("")
    #print ("\033[1;32m%s %d\033[1;m  -  \033[1;31m%d %s\033[1;m") % (
    #    equipo_local,
    #    gol_local,
    #    gol_visita,
    #    equipo_visita
    #)

    print ("")

    linea = "|" + (" " * pelota_x) + "O" + (" " * (30 - pelota_x)) + "|"

    print ("\033[1;42m+--------------------------------+\033[1;m")
    print ("|                                |")
    print ("|                                |")
    print (linea)
    print ("|                                |")
    print ("|                                |")
    print ("\033[1;42m+--------------------------------+\033[1;m")

    porcentaje = int((float(partido_segundos) / 300.0) * 20)

    barra = "[" + ("#" * porcentaje) + ("-" * (20 - porcentaje)) + "]"

    print ("")
    print ("\033[1;33mAVANCE %s\033[1;m" % barra ) 
    print ("")