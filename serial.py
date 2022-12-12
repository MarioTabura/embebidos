from time import sleep
import RPi.GPIO as GPIO
import serial

led = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
def ledon_off():
    global led

    led = not led
    GPIO.output(5, led)
    print(led)

ser = serial.Serial("/dev/ttyS0", 9600)
ser.write('Hola mundo !!!\n'.encode())
sleep(0.03)

while True:
	received_data = ser.read()
	sleep(0.03)
	data_left = ser.inWaiting()
	received_data += ser.read(data_left)
	print(received_data)
	ser.write(received_data)
    #if(minutos_latitud >= 19.58 and minutos_latitud <= 19.62 and minutos_longitud >= 10.93 and minutos_longitud <= 10.95):
    #    print(line, '*')
    #    print()
    #    GPIO.output(21,GPIO.HIGH)
    #    time.sleep(0.02)
    #    GPIO.output(21,GPIO.LOW)
    ##else:
    #    print(line)
    #    print()
    #    GPIO.output(21,GPIO.LOW)
    #    time.sleep(0.02)
    #if(received_data == '$GNGGA, 141417.00, 1919.551820'.encode()):
    #    ledon_off()
