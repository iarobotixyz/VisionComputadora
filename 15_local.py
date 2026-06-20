#!/usr/bin/python
# -*- encoding: utf-8 -*- 
import time
import datetime
import feedparser
import conectaXYZ
#from geopy.distance import vincenty
#from dateutil.relativedelta import relativedelta
import urllib
#import urllib2
#from espeak import espeak
import os
##Dispostxt codir=conectaXYZ.actualizaDireccionesTXT(la,lo)
import json
os.environ["GOOGLE_API_KEY"] = "AIzaSyCxBWCC87N1-5gTbZU2dlBjgu2yjaVOJaE"
import numpy as np
import socket
import sys

# Enlazar el socket a la dirección dada en la línea de comando
localIP     = "192.168.1.69"
localPort   = 9005
#bufferSize  = 1024
#msgFromServer       = "CopaFutbotMX"
#bytesToSend         = str.encode(msgFromServer)
#UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPServerSocket.bind((localIP, localPort))

os.system ("cls") #clear linux

print("\033[10;10H "+"\033[1;42m --------------------º! RELOJ XYZ !º-------------------- \033[1;m"+"\033[1;m")
print("\033[1;31m Local IP\033[1;m"), localIP
print("\033[1;31m Port\033[1;m"), localPort
print ("\033[1;31m Tarjeta Roja\033[1;m")
print ("\033[1;32m Green like Grass\033[1;m")
print ("\033[1;33m Minuto\033[1;m")
print ("\033[1;34m Reparacion\033[1;m")
print ("\033[1;35m Equipo\033[1;m")
print ("\033[1;36m IDENTIFICADOR\033[1;m")
print ("\033[1;37m Cambio Robot\033[1;m")
print ("\033[1;38m #1\033[1;m")
print ("\033[1;39m #2\033[1;m")

print ("\033[1;40m Penal\033[1;m")
print ("\033[1;41m Agregar NUEVA FUNCION\033[1;m")
print ("\033[1;42m Pausa\033[1;m")
print ("\033[1;43m SEGUIMIENTO DE PELOTA\033[1;m")
print ("\033[1;44m Tiro Esquina\033[1;m")
print ("\033[1;45m AutoGol\033[1;m")
print ("\033[1;46m Tarjeta Amarilla\033[1;m")
print ("\033[1;47m Amonestado\033[1;m")
print ("\033[1;48m Robot Dañado\033[1;m")
#print "errror de programado"
print("\033[1;42m========================================================\033[1;m")
print("\033[1;42m                 COPA FUTBOTMX 2026                     \033[1;m")
print("\033[1;42m========================================================\033[1;m")
print ("\033[1;33mTIEMPO 1        000 / 300 SEGUNDOS\033[1;m")

print ("\033[1;32mEQUIPO LOCAL MX 0\033[1;m  -  \033[1;31m0 EQUIPO VISITANTE\033[1;m")
#print ''
#print '\033[1;42m+--------------------------------------------------+\033[1;m'
#print '|                     |                            |'
#print '|                     |                            |'
#print '|                     O                            |'
#print '|                     |                            |'
#print '|                     |                            |'
#print '\033[1;42m+--------------------------------------------------+\033[1;m'
#print '\033[1;43m SEGUIMIENTO DE PELOTA EN VIVO \033[1;m'

#espeak.set_voice("mx")
#espeak.synth("hola prueba")

#print "Pausa"
#time.sleep(20)

#os.system("espeak -v mb-vz1 'Hola Mundo'")
#espeak -ves+f4 -a 200 "fuera!" 2>/dev/null

fechajson=str(datetime.datetime.now())[:19]
data = {}
data[localIP] = []
data[localIP].append({
    'IMEI': '0987654321',
    'CUENTA': 'sysadmin',
    'IDMV': '0987654321',
    'NOMBRE': 'NameMV',
    'FECHA': fechajson,
    'LAT': '0',
    'LON': '0',
    'ODOM': '0',
    'ODOMV': '0',
    'DIR': '0'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

#print "Conectado a base"
os.system("espeak -ves+f4 -a 200 'Conectando a Base de Datos' 2>/dev/null")

envRecMsj=False
horaEx=False
segundoEx=False
segundoQEx=False
t0=time.time()#tiempo 0 de lectura de base para apagado de autos
minutoAc=0
sismoinicial=0
url = 'http://www.roboticaxyz.com'
s='<p>'
while True:

    #captura de una fecha
    fecha=datetime.datetime.now()
    
    fechajson=str(datetime.datetime.now())[:19]

    #espera de hora exacta para envio de mensajes
    ttmr=datetime.datetime.now().timetuple()
    ts=time.time()
    dtNow=datetime.datetime.now()
    cero=0
    trei=30.0
    quin=15.0

    if round(ttmr[5])==quin and segundoQEx==False:
        segundoQEx=True
        #print segundo
        #print "Segundo", dtNow
        #print "si en algun momento se ocupa 15 desarrollar por este metodo"
        conectaXYZ.mostrarCopaFutbotMX() 
    elif round(ttmr[5])!=quin and segundoQEx==True:#cualquier minuto
        #print "Cambia False T diferente de 30 y segundo true"
        segundoQEx=False
        conectaXYZ.mostrarCopaFutbotMX()
    
    if round(ttmr[5])==trei and segundoEx==False:
        segundoEx=True
        #print segundo
        #print "Segundo", dtNow
        #print "si 30"
        conectaXYZ.mostrarCopaFutbotMX()
    elif round(ttmr[5])!=trei and segundoEx==True:#cualquier minuto
        #print "Cambia False T diferente de 30 y segundo true"
        segundoEx=False
    

    if ttmr[4]==cero and horaEx==False:#hora exacta 0 minutos
        horaEx=True
        if ttmr[3]==0:#si son las 12pm
            conectaXYZ.printc("Reseteo de contadores",0,5)
        if ttmr[3]==10:#si son las 10am
            conectaXYZ.printc("Las 10 de la manana",0,5)
            #os.system("espeak -ves+f4 -a 100 'Son las 10 de la mañana' 2>/dev/null")
            #envRecMsj=True cancela mensajes recurrentes 
    elif ttmr[4]!=cero and horaEx==True:#cualquier minuto
        horaEx=False

    #espera del minuto exacta para mensajes recurrentes
    if ttmr[4]!=minutoAc:#entra una vez cada minuto
        #print '\033[1;33mFecha y Hora\033[1;m', dtNow
                        
        minutoAc=ttmr[4]
        
        # Crea TCP/IP socket

        print("INICIANDO SERVIDOR FutBotMX")
