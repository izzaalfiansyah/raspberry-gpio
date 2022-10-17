import RPi.GPIO as GPIO
import time

pin = 9

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)
