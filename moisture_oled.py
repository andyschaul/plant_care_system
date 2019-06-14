# Example: https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage

#OLED Imports
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Soild Sensor Imports
from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

# Setup for STEMMA sensor
i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

# Setup for OLED

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the

font = ImageFont.truetype('/home/pi/slkscrb.ttf', 8)

while True:
    #Get moisture and temperature readings
    touch = ss.moisture_read()
    temp = ss.get_temp()
    temp = 9/5 * temp + 32
    print('Temp: ', str(temp))
    print('Moisutre: ', str(touch))
    time.sleep(1)



    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Write four lines of text.
    draw.text((x, top+0), "Moisture: " + str(touch), font=font, fill=255)
    draw.text((x, top+8), "Temp: " + str(round(temp, 2)), font=font, fill=255)
    draw.text((x, top+16), "Water Smartly!", font=font, fill=255)
    draw.text((x, top+25), "", font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(1)
    disp.fill(0)

  
        
        





