import RPi.GPIO as GPIO                           
GPIO.setmode(GPIO.BOARD)

high = 1
low = 0
def acendeled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, high)

def apagaled(pino_led):
    GPIO.setup(pino_led, GPIO.OUT)
    GPIO.output(pino_led, low)