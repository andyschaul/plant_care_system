# Program to test relay for water pump

# Wiring

# Relay to Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 16 (GPIO 23)


import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

OutputPins = [23]

for i in OutputPins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, True)



for i in OutputPins:
    GPIO.output(i, False)
    print('Adding Water')
    time.sleep(3)

for i in OutputPins:
    GPIO.output(i, True)
    print('Done Adding Water')


