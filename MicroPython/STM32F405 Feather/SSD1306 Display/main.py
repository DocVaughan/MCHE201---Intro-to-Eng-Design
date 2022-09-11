###############################################################################
# main.py
#
# Script to test the control of a SSD1306 OLED display from the MCHE201 
# breakout board
#
#
# Created: 02/28/19
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 
#
# TODO:
#   * 
###############################################################################

import pyb  # import the pyboard module
import time # import the time module

import machine
import ssd1306

# Initialize communication with the motor driver
i2c = machine.I2C(scl=machine.Pin('Y9'), sda=machine.Pin('Y10'))

# Cheap one from Amazon - http://amzn.com/B076WXR8N9
# oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)

# Qwiic OLED from Sparkfun - https://www.sparkfun.com/products/14532
oled = ssd1306.SSD1306_I2C(64, 48, i2c, 0x3d)

# Fill with black
oled.fill(0)

# Then add Hello World starting at pixel 0,0 (top left)
oled.text("Hello World", 0, 0)
# Add a 96 pixel long line white starting a pixel 0,10
oled.hline(0, 10, 96, 0xffff)

# Show that buffer
oled.show()

# Sleep 1s
time.sleep(1)

# Now, clear the buffer
oled.fill(0)

# create a 10x10 rectangle with corner at pixel 10,10
oled.rect(10,10,10,10,0xffff)

# Now, show it
oled.show()

time.sleep(1)

# Now, clear the buffer
oled.fill(0)

# create a 10x10 filled rectangle with corner at pixel 10,10
oled.fill_rect(10,10,10,10,0xffff)

# Now, show it
oled.show()

# An animate some motion around the OLED using the scroll method
for index in range(20):
    if index < 10:
        oled.scroll(4, 1)
    else:
        oled.scroll(4, -1)
    
    oled.show()
    time.sleep_ms(500)


# Fill with black
oled.fill(0)

# Then add some more text starting at at pixel 0,0 (top left)
# Each line is ~10 pixels high
oled.text("Coming soon to a", 0, 0)
oled.text("MCHE201 section", 0, 10)
oled.text("near you.", 0, 20)

oled.show()