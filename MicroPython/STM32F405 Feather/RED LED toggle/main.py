###############################################################################
# main.py
#
# main script to toggle the onboard red LED 5 times
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

import pyb  # import the pyboard module
import time # import the time module

# Assign the 1st LED to variable RED_LED
RED_LED = pyb.LED(1)

# # This for loop will run 5 times
# for counter in range(5):
#   RED_LED.on()    # Turn the RED_LED on
#   time.sleep(2)   # Sleep 2 seconds while on
#   RED_LED.off()   # Turn the LED off
#   time.sleep(2)   # Sleep 2 seconds while off

# Comment the for loop above and 
# Uncomment the below to run the alternate solution
# This for loop will run 10 times
for counter in range(10):
    RED_LED.toggle()  # Toggle the RED_LED on
    time.sleep(2)     # Sleep 2 seconds