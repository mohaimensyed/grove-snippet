import time
import grovepi
from grovepi import *
from grove_rgb_lcd import *
from time import sleep

# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

# Connect the LED to digital port D5, D4
ultrasonic_ranger = 4

setRGB(0,255,0)

time.sleep(1)
i = 0

while True:
	try:
		# Read resistance from Potentiometer
		i = grovepi.analogRead(potentiometer)
		threshold = i / 2
		print(threshold)

		distant = ultrasonicRead(ultrasonic_ranger)
		print(distant,'cm')

		if distant <= threshold:
			print("Threshold reached")
			setRGB(255,0,0)
			obj = "OBJ PRES"
		else:
			setRGB(0,255,0)
			obj = ""

		t = str(threshold)
		d = str(distant)

		setText_norefresh("T:" + t + "cm  " + obj + "D :" + d)

	except TypeError:
		print("Error")
	except IOError:
		print("Error")

	sleep(0.2)