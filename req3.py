import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

while(1):
	lul = GPIO.input(11)
;	print(lul)
	if lul:
		print('IO 11 is open')
	else:
		print('IO 11 is closed')
	time.sleep(0.1)
