import RPi.GPIO as GPIO                           
GPIO.setmode(GPIO.BOARD)
import time

high = 1
low = 0
tempo = 2

def acendeled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, high)

def apagaled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, low)

while(1):
    acendeled(8)
    time.sleep(tempo)
    apagaled(8)
    time.sleep(tempo)
