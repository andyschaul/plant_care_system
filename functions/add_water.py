# Program to add water manually
# Triggered by button in launch_controls.py

# Wiring

# Relay to Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 16 (GPIO 23)

# Import your config_system.py
# This contains your settings for the system
import sys
sys.path.insert(0, '/home/pi/virtEnv1/plant_care_system/')
import config_system as settings
import csv

import datetime

import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set Signal Pin (It's a list in case you have more than one pump/valve)
OutputPins = [23]


def add_water(manual_water_add_seconds):
    # Make Sure Relay is off first
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
    # Turn on pump/valve for seconds
    for i in OutputPins:
        GPIO.output(i, False)
        print('Adding Water for ' + str(manual_water_add_seconds) + ' seconds')
        time.sleep(manual_water_add_seconds)
    # Turn off pump/valve
    for i in OutputPins:
        GPIO.output(i, True)
        print('Done Adding Water')
        
    # Record Data
    row = [datetime.datetime.now().isoformat(),
               'Manually Added',
               'True',
               manual_water_add_seconds]
    #print(row)
    with open('/home/pi/virtEnv1/plant_care_system/functions/water_data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

add_water(manual_water_add_seconds=settings.settings['manual_water_add_seconds'])


