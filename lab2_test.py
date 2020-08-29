import time
import grovepi

# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

# Connect the LED to digital port D5, D4
led = 5
ultrasonic_ranger = 4

grovepi.pinMode(led,"OUTPUT")
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

        if distant == threshold:
        	print("Threshold reached")

        # Send PWM signal to LED
        grovepi.analogWrite(led,i//4)

    except IOError:
        print("Error")
	except TypeError:
        print("Error")
    except IOError:
        print("Error")