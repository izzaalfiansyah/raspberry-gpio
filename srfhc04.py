import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trigger = 26
echo = 16

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trigger, GPIO.LOW)

def get_range():
	GPIO.output(trigger, True)
	time.sleep(0.00001)
	GPIO.output(trigger, False)
	timeout_counter = int(time.time())
	start = time.time()

	while GPIO.input(echo) == 0 and (int(time.time()) - timeout_counter) < 3:
		stop = time.time()

	elapsed = stop-start
	distance = elapsed * 34320
	distance = distance / 2

	return distance

while True:
	jarak = get_range()
	print('Jarak terukur : %.2f Cm' % jarak)
	time.sleep(1)
