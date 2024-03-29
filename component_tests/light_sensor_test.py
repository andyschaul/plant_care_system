# test tsl2591 light sensor

import board
import busio
import adafruit_tsl2591
import time
i2c_light = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c_light)

while True:
    print('Light: {0}lux'.format(sensor.lux))
    print('Visible: {0}'.format(sensor.visible))
    print('Infrared: {0}'.format(sensor.infrared))
    print('Full Spectrum: {0}'.format(sensor.infrared + sensor.visible))
    time.sleep(1)