import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

while True:
	try:
		id, text = reader.read()
		print('Silahkan letakkan ID anda!!')
		print('ID card anda	: ', id)
		print('Selamat datang	: ', text)
	finally:
		time.sleep(2)
		GPIO.cleanup()
