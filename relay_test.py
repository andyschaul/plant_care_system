# Program to test relay

# Wiring

# Relay —> Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 18 (GPIO 24)


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

OutputPins = [24]

for i in OutputPins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)


while True:
    for i in OutputPins:
        GPIO.output(i, True)
        print('Relay On')
    time.sleep(2)
    
    for i in OutputPins:
        GPIO.output(i, False)
        print('Relay Off')
    time.sleep(2)