# Soil Moisture Project

Combines RaspberryPi Zerio, Stemma Soil Sensor, Light Sensor, Water Pump, and PiOLED display
to create a plant care system

You can find indiviual component test programs in the component_tests folder for the light sensor, moisture sensor, relay, and relay water pump

Files:
- control_OLED.py - Gets moisture, temperature, and light readings and displays on OLED
- control_lights.py - Turns on lights if light reading below a threshold (then turns them off and checks again)
- slkscr.tff - font files from kotte.org
- slkscrb.tff - font files from kottke.org

Additions:
- Update code to connect moisture sensor and water pump


Fritz Image:

![soil_moisture_light_oled_bb](https://user-images.githubusercontent.com/30374932/59544894-4bf7ef80-8edc-11e9-9910-c1339fdc2949.jpg)


Proto Image:
    
![IMG_2442](https://user-images.githubusercontent.com/30374932/59478458-eeea3400-8e1e-11e9-97fc-02d85fd160f4.jpg)