# Water pump cycle control based on soil moisture readings

################################
# Water Pump/Valve Imports and setup
################################

# Wiring

# Relay to Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 16 (GPIO 23)

# Relay should be wired in Normally Open configuration

# Import your config_system.py
# This contains your settings for the system
import sys
sys.path.insert(0, '/home/pi/virtEnv1/plant_care_system/')
import config_system as settings
import csv
## Other required imports and setup

import RPi.GPIO as GPIO
import time
import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

OutputPins = [23]

################################
# Soil Sensor Imports and setup
################################
# Soil Sensor Wiring

#    -  ----------------------------------------------------
#  -                           This is the board        GND                                                                                  
# -        <--Direction        side of the soil         VIN
# -                             sensor              I2C SDA
#  -                                                I2C SCL
#    -   ---------------------------------------------------

# Pi 3v3 to VIN 
# Pi GND to GND
# Pi SCL to SCL
# Pi SDA to SDA

from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# Setup for STEMMA sensor
i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

################################
# Program
################################

def water_cycle(moisture_threshold=799, water_for_seconds=3, after_watering_wait_minutes=120):

    # Make sure pump/valve off
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)

    print('Water Cycle Started')

    while True:
        touch = ss.moisture_read()
        print('Moisture: ', touch)
        if touch > moisture_threshold:
            time.sleep(10)
        
        elif touch <= moisture_threshold + 1:
            for i in OutputPins:
                GPIO.output(i, False)
                print('Relay On')
            time.sleep(water_for_seconds)
        
            for i in OutputPins:
                GPIO.output(i, True)
                print('Relay Off')
                print('Time: ', str(datetime.datetime.now().isoformat()))
                print('Will re-check moisture in ' + str(after_watering_wait_minutes) + ' minutes')
                
                # Record Data
                row = [datetime.datetime.now().isoformat(),
                           touch,
                           'True',
                           water_for_seconds]
                #print(row)
                with open('/home/pi/virtEnv1/plant_care_system/functions/water_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
                
                #time.sleep(60 * after_watering_wait_minutes)
                
                
            time.sleep(60 * after_watering_wait_minutes)
            

water_cycle(moisture_threshold=settings.settings['moisture_threshold'],
            water_for_seconds=settings.settings['water_for_seconds'],
            after_watering_wait_minutes=settings.settings['water_for_seconds'])
