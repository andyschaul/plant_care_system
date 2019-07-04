#!/usr/bin/python

# File in rc.local to run at startup
# sudo nano /etc/rc.local
# sudo /home/pi/virtEnv1/plant_care_system/functions/launch_controls.py &

# Code to launch button controls for plant care system
# http://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# To activate venv
activator = '/home/pi/virtEnv1/bin/activate_this.py'
exec(open(activator).read(), {'__file__': activator})



# Circuit
# Button -- Pi
# Common -- dasiy chain each button - resistor -- 3.3V
# Signal -- GPIO (see below for pins)

import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set button pins
red = 10 #off reset
green = 31 #start
blue = 33 # add water
yellow = 37 # add fertilizer
white = 36 # turn lights on
black = 32 # turn lights off

# Red Button - stops & resets system
GPIO.setup(red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# Green Button -  starts system
GPIO.setup(green, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Blue Button - adds water
GPIO.setup(blue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Yellow Button - adds fertilizer
GPIO.setup(yellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# White Button - ,manually turn lights on
GPIO.setup(white, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Black Button - manually turn lights off
GPIO.setup(black, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

path = '/home/pi/virtEnv1/plant_care_system/functions/'

while True: # Run forever
    # Stop and Reset
    if GPIO.input(red) == GPIO.HIGH:
        print("Turning Off System")
        os.system('python3 ' + path + 'reset_system.py')
    # Start System    
    if GPIO.input(green) == GPIO.HIGH:
        print("Turning System On")
        os.system('python3 ' + path + 'start_system.py')
    # Add Water    
    if GPIO.input(blue) == GPIO.HIGH:
        print("Adding Water")
        os.system('python3 ' + path + 'add_water.py')
    # Add Fertilizer    
    if GPIO.input(yellow) == GPIO.HIGH:
        print("In the future this will add liquid fertilizer")
        #os.system('python3 ' + path + 'add_water.py')
    # Add Fertilizer    
    if GPIO.input(white) == GPIO.HIGH:
        print("Manual Light On Mode")
        os.system('python3 ' + path + 'lights_on.py')
    # Add Fertilizer    
    if GPIO.input(black) == GPIO.HIGH:
        print("Manual Light Off Mode")
        os.system('python3 ' + path + 'lights_off.py')
