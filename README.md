# Soil Moisture Project

Combines RaspberryPi Zerio, Stemma Soil Sensor, PiOLED display
to check soild moisture and temperature readings once per second
and dislays them on screen

Files:
- plant_system_test.py - test soil sensor, OLED, and light sensor (light switch and water pump to be added)
- moisture_test.py - used to test sensor initially
- light_sensor_test.py - used to test sensor initially
- relay_test.py - used to test relay switch for light
- slkscr.tff - font files from kotte.org
- slkscrb.tff - font files from kottke.org

Additions:
- Add TSL2591 Light Sensor
- Use light readings to trigger light turn on/off
- Add water source and pump triggered by moisture readings


Fritz Image:

![soil_moisture_light_oled_bb](https://user-images.githubusercontent.com/30374932/59544894-4bf7ef80-8edc-11e9-9910-c1339fdc2949.jpg)


Proto Image:
    
![IMG_2442](https://user-images.githubusercontent.com/30374932/59478458-eeea3400-8e1e-11e9-97fc-02d85fd160f4.jpg)