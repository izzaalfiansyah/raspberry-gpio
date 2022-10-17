import RPi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

item = dht11.DHT11(pin=19)
nilai = item.read()

while True:
    if nilai.is_valid():
        print('Suhu       : %-3.1f C' % nilai.temperature)
        print('Kelembaban : %-3.1f %' % nilai.humidity)
    else:
        print('Error : %d' % nilai.error_code)
    time.sleep(2)
    GPIO.cleanup()
