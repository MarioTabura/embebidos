from time import sleep
import RPi.GPIO as GPIO
import serial

led = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT)
def ledon_off():
    global led

    led = not led
    GPIO.output(21, led)
    print(led)

ser = serial.Serial("/dev/ttyS0", 9600)
ser.write('Recibiendo datos\n'.encode())
sleep(0.03)

while True:
    received_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    print(received_data)
    ser.write(received_data)
    for line in received_data:
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
    
    
            if(minutos_latitud >= 19.58 and minutos_latitud <= 19.62 and minutos_longitud >= 10.93 and minutos_longitud <= 10.95):
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
            if(received_data == '$GNGGA, 141417.00, 1919.551820'.encode()):
                ledon_off()
