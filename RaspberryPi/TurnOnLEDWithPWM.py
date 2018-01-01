import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

ledState = True #up cycle
pwmLevel = 0;

PWM = GPIO.PWM(18, 50) #set output to 50hz
PWM.start(pwmLevel) #duty cycle ratio is 50

try:

	while True:
		inputVal = GPIO.input(15)
		if inputVal == True:
			if ledState == True:
				pwmLevel = pwmLevel + 10
				PWM.ChangeDutyCycle(pwmLevel)
				if pwmLevel >= 100:
					ledState = False
			else:
				pwmLevel = pwmLevel - 10
				PWM.ChangeDutyCycle(pwmLevel)
				if pwmLevel <= 0:
					ledState = True
		time.sleep(.15)
except KeyboardInterrupt:
	GPIO.cleanup()
	
