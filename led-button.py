import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

inputButton = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(inputButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

status = False
inputLama = True

while True:
    statusBaru = GPIO.input(inputButton)
    if statusBaru == False and inputLama == True:
        status = not status
        print('1')
        time.sleep(0.2)
    inputLama = statusBaru
    GPIO.output(14, status)
