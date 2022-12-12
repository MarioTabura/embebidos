import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)


leonardita = open('./leonardita.txt', 'r')
for line in leonardita:
    if('GPGGA' in line):
        coords = line.split(',')
        latitud_coords = coords[2].strip()
        longitud_coords = coords[4].strip()

        '''
        Obtención de cadenas de coordenadas por ángulo y minutos
        '''
        latitud = latitud_coords[:2]
        minutos_latitud = latitud_coords[2:]
        
        longitud = longitud_coords[1:3]
        minutos_longitud = longitud_coords[3:]
        
        '''
        Conversión de datos a tipo numérico
        '''
        if(latitud != '' or longitud != ''):
            latitud = float(latitud)
            minutos_latitud = float(minutos_latitud)
            longitud = float(longitud)
            minutos_longitud = float(minutos_longitud)
        else:
            continue


        #Descomentar para coordenadas de La Leonardita.
        #if(minutos_latitud <= 19.331 and minutos_latitud >= 19.326
        #        and minutos_longitud >= 10.58 and minutos_longitud <= 10.573):
        if(minutos_latitud >= 19.58 and minutos_latitud <= 19.62
                and minutos_longitud >= 10.93 and minutos_longitud <= 10.95):
            print(line, '*')
            print()
            GPIO.output(21,GPIO.HIGH)
            time.sleep(0.02)
            GPIO.output(21,GPIO.LOW)
        else:
            print(line)
            print()
            GPIO.output(21,GPIO.LOW)
            time.sleep(0.02)


leonardita.close()