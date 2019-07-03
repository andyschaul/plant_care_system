# To turn lights on
# Trigger by button via launch_controls.py

# Relay Wiring

# Relay —> Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 18 (GPIO 24)

# Relay should be wired in Normally Open configuration

# To print time of readings
import datetime

# Light Sensor & Relay Setup
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_tsl2591
import time
i2c_light = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c_light)

#Relay Setup

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Add more pins here for other relays to control
OutputPins = [24]

# Function to control lights based on light sensor readings

def lights_on():
    '''A function to turn lights off'''
    # Make sure all the lights are off first
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)
        
lights_on()  
    