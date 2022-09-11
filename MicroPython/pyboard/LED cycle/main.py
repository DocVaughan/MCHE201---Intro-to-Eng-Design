###############################################################################
# main.py
#
# main script to toggle the all the onboard LEDs 5 times
#
# Created: 10/03/17
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

import pyb      # import the pyboard module
import time     # import the time module

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)

# This for loop will run 10 times to light the LEDs 5 times
for counter in range(10):
    RED_LED.toggle()     # Toggle the RED_LED
    GREEN_LED.toggle()   # Toggle the GREEN_LED
    YELLOW_LED.toggle()  # Toggle the YELLOW_LED
    BLUE_LED.toggle()    # Toggle the BLUE_LED
    time.sleep(2)        # Sleep 2 seconds