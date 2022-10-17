import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ldr = 17
led = 14
tunda = 2
nilai = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)


def rcTime(ldr):
    count = 0
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(tunda)
    GPIO.setup(ldr, GPIO.IN)

    while GPIO.input(ldr) == GPIO.LOW:
        count += 1

    return count


try:
    while True:
        print('nilai LDR : ')
        nilai = rcTime(ldr)
        print(nilai)

        if nilai >= 2500:
            print('LED menyala')
            GPIO.output(led, True)
        else:
            print('LED padam')
            GPIO.output(led, False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
