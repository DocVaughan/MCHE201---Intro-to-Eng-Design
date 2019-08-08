# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality controlling a WS2812 RGB LED 
# array (often called neopixels). The data line of the array should be 
# connected to the MOSI pin of an SPI port on the board. In the code here, we 
# use SPI1 on the pyboard, whose MOSI pin is X8. 
#
# This is written largely assuming the LED array is a strip. As written, it 
# will loop set the entire strip to a dim brightness of a RGBW color, then 
# loop through the length of the LED strip making NUM_CYCLE LEDs bright in that
# color. Once once cycle is complete, the color changes. It will do this 
# indefinitely. A KeyboardInterrupt or other exception should turn all the 
# LEDs off.
#
# Note: The order of the tuples used is GRB, *NOT* RGB
# 
# The neoSPI.py file must also be on the pyboard for this script to work
#    https://github.com/nickovs/ws2812-SPI
#
#
# Created: 04/06/19 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 
#
# TODO:
#   * mm/dd/yy - Major bug to fix
#   # mm/dd/yy - Desired new feature
# -----------------------------------------------------------------------------

import machine
import pyb
import time

# Import the library to control the LEDs
import neoSPI

NUM_LEDS = 30   # Number of LEDs in the array
NUM_CYCLE = 5   # Number of LEDS to cycle to bright in the effect

# Define the tuples of GRB colors for each color we want to show
OFF = (0,0,0)
WHITE_HIGH = (255,255,255)
WHITE_LOW = (16,16,16)
RED_HIGH = (0,255,0)
RED_LOW = (0,16,0)
GREEN_HIGH = (255,0,0)
GREEN_LOW = (16,0,0)
BLUE_HIGH = (0,0,255)
BLUE_LOW = (0,0,16)
YELLOW_HIGH = (200,100,0)
YELLOW_LOW = (10,20,0)

# Collect the colors into list for low brightness and high brightness
COLORS_LOW = (WHITE_LOW, RED_LOW, GREEN_LOW, BLUE_LOW, YELLOW_LOW)
COLORS_HIGH = (WHITE_HIGH, RED_HIGH, GREEN_HIGH, BLUE_HIGH, YELLOW_HIGH)
NUM_COLORS = len(COLORS_LOW)

# Define the SPI port to use
# The data line of the array should be connected to the MOSI pin of an SPI port 
# on the board. In the code here, we use SPI1 on the pyboard, whose MOSI pin 
# is X8.
sp = machine.SPI(1)
sp.init(baudrate=3200000)

# Now, define the NeoPixel object, passing the SPI port and NUM_LEDS
neo = neoSPI.NeoPixel(sp, NUM_LEDS)

# Define some variables to help us keep track of where we are in the cycle
index = 0           # Place in the cycle
going = True        # direction our LEDs are "moving"
color_index = 0     # current color as an index in the COLOR_ lists above

try:
    while(True):
        # Fill with low brightness to start
        neo[:] = COLORS_LOW[color_index]

        # Check which direction our LEDs are "moving". If we reach the end of
        # the LED array, we switch directions
        if (index + NUM_CYCLE >= NUM_LEDS):
            going = False
         
        elif (index <= 0):
            going = True
            
            # Move to the next color. We use the modulus (%) operator to ensure
            # that the index stays within the length of the COLORS_LOW and 
            # COLORS_HIGH arrays
            color_index = (color_index + 1) % NUM_COLORS

        # Use the direction of the "motion" of the LEDs to decide how to move
        # the bright LEDs
        if going:
            for n in range(NUM_CYCLE):
                neo[index + n] = COLORS_HIGH[color_index]
        
            index = index + 1

        else:
            for n in range(NUM_CYCLE):
                neo[index + NUM_CYCLE - n - 1] = COLORS_HIGH[color_index]

            index = index - 1

        # Write the array of values to the LED array
        neo.write()

        time.sleep(0.01)

except:
    # Turn all the LEDs off
    neo[:] = OFF
    neo.write()
    
    # Still raise the exception
    raise