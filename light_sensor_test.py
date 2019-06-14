# test tsl2591 light sensor
# install by sudo pip3 install python-tsl2591
import board
import busio
import adafruit_tsl2591
import time
i2c_light = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c_light)

while True:
    print('Light: {0}lux'.format(sensor.lux))
    print('Visible: {0}'.format(sensor.lux))
    print('Infrared: {0}'.format(sensor.infrared))
    time.sleep(1)