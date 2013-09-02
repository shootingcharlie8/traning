import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

while(1):
	lul = GPIO.input(11)
	print(lul)
	if lul:
		GPIO.output(12, True)
	else:
		GPIO.output(12, False)
	time.sleep(0.1)
