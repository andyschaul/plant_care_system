# This file runs the light sensor and light relay
# It connets the two in order to turn lights on
# only if reading is below a provided threshold
# Keeps them on for a provided number of minutes
# And shuts them off for a provided number of minutes
# before checking the light reading and starting the
# cycle over

# Trigger by launch_controls.py along with water_cycle.py

# To print time of readings
import datetime

# Light Sensor Setup
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

def light_control(threshold=1704034, on_minutes=5, off_minutes=40):
    '''A function to control grow lights based on light
        sensor readings.
        
        Parameters:
        ----------
        threshold: int
            light sensor (visible) reading below which to turn lights on
            default is 1704034
            
        on_minutes: int
            how long the light should be on for per on/off cycle
            default is 5
        
        off_minutes: int
            how long the light should be off for per on/off cycle
            default is 40
        
        '''
    print('Light Cycle Started')
    
    # Make sure all the lights are off first
    for i in OutputPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
        
    # Program to turn light on if sensor reading below a threshold

    while True:
        #print('Light: {0}lux'.format(sensor.lux))
        #print('Visible: {0}'.format(sensor.visible))
        #print('Infrared: {0}'.format(sensor.infrared))
        #print('Full Spectrum: {0}'.format(sensor.infrared + sensor.visible))
        
        # Turn off lights if on and Record full spectrum value
        for i in OutputPins:
            GPIO.output(i, True)
            time.sleep(2)
        level = sensor.visible
        print('Level: {0}'.format(level))
        time.sleep(1)
        
        # If value below a threshold, turn the relay light on
        # Then keep the light on for a time
        # Turn it off to check light level again
        
        if level < threshold:
            for i in OutputPins:
                GPIO.output(i, False)
                print('Relay On')
                # This is what time the light status was changed
                print('Time: ' + str(datetime.datetime.now().isoformat()))
                # This is how long to keep the light on for (seconds)
                print('Light will be on for: ' + str(on_minutes) + ' minutes') 
                print('Then it will be off for ' + str(off_minutes) + ' minutes.')
                time.sleep(60* on_minutes)
                # Turn light off to get a fair light reading for next round
                GPIO.output(i, True)
                print('Relay Off')
                time.sleep(60*60)
            
        elif level > 1704034:
            for i in OutputPins:
                GPIO.output(i, True)
                print('Relay Off')
                # This is what time the light status was changed
                print('Time: ' + str(datetime.datetime.now().isoformat()))
                print('Light will be off for: ' + str(off_minutes) + ' minutes')
                time.sleep(60 * off_minutes)
        
light_control()
