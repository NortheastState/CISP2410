import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

ledState = False

try:
	while True :
		if GPIO.input(15) == True:
			if ledState == True:
				GPIO.output(16, False)
				ledState = False
			else:
				GPIO.output(16, True)
				ledState = True

		time.sleep(0.15)
except KeyboardInterrupt:
	GPIO.cleanup()
