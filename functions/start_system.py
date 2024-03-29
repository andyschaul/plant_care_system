# Start Plant Care System
# Triggered via button from launch_controls
# Starts water cycle, light cycle, and display readings

import os
import time
# Use this to print your config_system.py settings
import sys
sys.path.insert(0, '/home/pi/virtEnv1/plant_care_system/')
import config_system as settings
print(settings.settings)

#############################
# Kill Running .py files 
#############################

import os

path_kill = '/home/pi/virtEnv1/plant_care_system/functions'

def kill_processes():
    '''
    Function to kill currently running py files in project
    '''
    for filename in os.listdir(path_kill):
        #print(filename)
        if filename == 'reset_system.py':
            pass
        if filename == 'launch_controls.py':
            pass
        elif filename.endswith('.py'):
            cmd = 'pkill -f ' + str(filename)
            os.system(cmd)

#############################
# Start system
#############################

path = '/home/pi/virtEnv1/plant_care_system/functions/'

# Start Light Cycle
time.sleep(1)
os.system('python3 ' + path + 'OLED_control.py &')
time.sleep(1)
os.system('python3 ' + path + 'light_cycle.py &')
time.sleep(1)
os.system('python3 ' + path + 'water_cycle.py &')
time.sleep(1)
os.system('python3 ' + path + 'record_data.py &')
