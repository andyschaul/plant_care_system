# Program to add water manually
# Triggered by button in launch_controls.py

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

# Set Signal Pin (It's a list in case you have more than one pump/valve)
OutputPins = [23]


def add_water(seconds):
    # Make Sure Relay is off first
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
    # Turn on pump/valve for seconds
    for i in OutputPins:
        GPIO.output(i, False)
        print('Adding Water')
        time.sleep(seconds)
    # Turn off pump/valve
    for i in OutputPins:
        GPIO.output(i, True)
        print('Done Adding Water')

add_water(3)


