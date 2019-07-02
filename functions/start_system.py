# Start Plant Care System

import os

path = path = '/home/pi/virtEnv1/plant_care_system/functions/'

# Start Light Cycle
os.system('python3 ' + path + 'OLED_control.py &')
os.system('python3 ' + path + 'light_cycle.py &')
os.system('python3 ' + path + 'water_cycle.py &')
