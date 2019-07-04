# Configuration file for plant care system
# Use this to modify your system characteristics
# Like how long to have water on, lights on/off, et


# Use this dictionary to set your preferences

settings = {
            'light_threshold': 1704034, # Light reading below which to turn lights on
            'on_minutes': 20, # How many minutes to keep the lights on
            'off_minutes': 40, # How long to keep the lights off before checking again
            'water_for_seconds': 3, # How long to turn water pump/valvue on for
            'after_watering_wait_minutes': 120 # minimum wait time before watering again
            }
