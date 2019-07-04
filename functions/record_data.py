# This file gathers light, moisture, and temperature
# and records them in a file

# Links:
# https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage
# https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor
# https://learn.adafruit.com/adafruit-tsl2591/wiring-and-test

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

# to install soil sensor package use sudo pip3 install adafruit-circuitpython-seesaw

# Light Sensor Wiring

# Pi 3v3 to VIN 
# Pi GND to GND
# Pi SCL to SCL
# Pi SDA to SDA

# To install light sensor package use sudo pip3 install adafruit_tsl291 (double check this)


#OLED Imports
import time
import datetime
import csv
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Soild Sensor Imports
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# Light Sensor Imports (TSL2591)
import board
import adafruit_tsl2591

def record_data():
    '''
    Funtion to record time, moisture, temp, and light data
    '''
    print('Recording Data')
    
    # Setup for Light sensor
    i2c_light = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tsl2591.TSL2591(i2c_light)

    # Setup for STEMMA sensor
    i2c_bus = busio.I2C(SCL, SDA)

    ss = Seesaw(i2c_bus, addr=0x36)

    while True:
        # Get moisture and temperature readings
        touch = ss.moisture_read()
        temp = ss.get_temp()
        temp = 9/5 * temp + 32
        #print('Temp: ', str(temp))
        #print('Moisture: ', str(touch))
        # Get visible light reading
        light = sensor.visible
        #print('Light: ', str(light))
        #print('-----------------------------------')

        # Write data to csv
        row = [datetime.datetime.now().isoformat(),
               touch,
               temp,
               light]
        #print(row)
        with open('/home/pi/virtEnv1/plant_care_system/functions/sensor_data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)
        
        time.sleep(3600)

# Run function
record_data()









