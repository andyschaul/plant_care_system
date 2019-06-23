# Test light sensor and light relay

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
    # On and off times
    on_minutes = 20
    off_minutes = 20
    
    if level < 1704034:
        for i in OutputPins:
            GPIO.output(i, False)
            print('Relay On')
            # This is how long to keep the light on for (seconds)
            print('Light will be on for: ' + str(on_minutes) + ' minutes') 
            time.sleep(60* on_minutes)
            # Turn light off to get a fair light reading for next round
            GPIO.output(i, True)
            print('Relay Off')
            time.sleep(2)
        
    elif level > 1704034:
        for i in OutputPins:
            GPIO.output(i, True)
            print('Relay Off')
            print('Light will be off for: ' + str(off_minutes) + ' minutes')
            time.sleep(60 * off_minutes)
    
