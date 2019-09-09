# Configuration file for plant care system
# Use this to modify your system characteristics
# Like how long to have water on, lights on/off, et


# Use this dictionary to set your preferences

settings = {
            'light_threshold': 200000000, # Light reading below which to turn lights on
            'on_minutes': 40, # How many minutes to keep the lights on
            'off_minutes': 20, # How long to keep the lights off before checking again
            'moisture_threshold': 750, # mositure reading below which to turn on water
            'water_for_seconds': 10, # How long to turn water pump/valvue on for
            'after_watering_wait_minutes': 180, # minimum wait time before watering again
            'manual_water_add_seconds': 4 # how many seconds to add water when done manually
            }
