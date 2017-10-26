import RPi.GPIO as GPIO                           
GPIO.setmode(GPIO.BOARD)

high = 1
low = 0
#define a funcao que ira acender o led
def acendeled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, high)
#define a funcao que ira apagar o led
def apagaled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, low)