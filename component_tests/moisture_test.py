import time
from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
    touch = ss.moisture_read()
    temp = ss.get_temp()
    print('Temp: ', str(temp))
    print('Moisutre: ', str(touch))
    time.sleep(1)