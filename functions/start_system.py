# Start Plant Care System
# Triggered via button from launch_controls
# Starts water cycle, light cycle, and display readings

import os

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
os.system('python3 ' + path + 'OLED_control.py &')
os.system('python3 ' + path + 'light_cycle.py &')
os.system('python3 ' + path + 'water_cycle.py &')
