# File to reset system (turn off lights and water cycles)
# Kills running files in project and resets hardware to off
# Trigger by button via launch_controls.py


#############################
# Kill Running .py files 
#############################

import os

path = '/home/pi/virtEnv1/plant_care_system/functions/'

def kill_processes():
    '''
    Function to kill currently running py files in project
    '''
    for filename in os.listdir(path):
        print(filename)
        if filename == 'reset_system.py':
            pass
        elif filename == 'launch_controls.py':
            pass
        elif filename.endswith('.py'):
            cmd = 'pkill -f ' + str(filename)
            print(cmd)
            os.system(cmd)

#############################
# Reset Lights and Water to Off  
#############################

def reset_hardware():
    '''Resets lights and water pump to off positions
        refers to other files'''
    
    path = '/home/pi/virtEnv1/plant_care_system/functions/'
    
    os.system('python3 ' + path + 'lights_off.py')
    os.system('python3 ' + path + 'water_off.py')
    
    
#############################
# Reset Lights and Water to Off  
#############################

def relaunch_controls():
    os.system('/home/pi/virtEnv1/plant_care_system/functions/launch_controls.py &')
    

#############################
# Run above functions
#############################

kill_processes()
#relaunch_controls()
reset_hardware()
