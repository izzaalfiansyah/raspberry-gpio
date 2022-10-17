import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 14

GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 100)

dc = 0
pwm.start(dc)

try:
    while True:
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
            print(dc)
        for dc in range(95, 0, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
            print(dc)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
