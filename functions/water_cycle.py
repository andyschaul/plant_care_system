# Water pump cycle control based on soil moisture readings

################################
# Water Pump/Valve Imports and setup
################################

# Wiring

# Relay to Pi
# GND - GND
# VCC - 5V
# IN1 - Pin 16 (GPIO 23)


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

def water_cycle(interval_minutes=120):

    # Make sure pump/valve off
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)

    print('Water Cycle Started')

    while True:
        touch = ss.moisture_read()
        print('Moisture: ', touch)
        if touch >= 799:
            time.sleep(10)
        
        elif touch <= 800:
            for i in OutputPins:
                GPIO.output(i, False)
                print('Relay On')
            time.sleep(3)
        
            for i in OutputPins:
                GPIO.output(i, True)
                print('Relay Off')
                print('Time: ', str(datetime.datetime.now().isoformat()))
                print('Will re-check moisture in ' + str(interval_minutes) + ' minutes')
            time.sleep(60 * interval_minutes)
            

water_cycle()
