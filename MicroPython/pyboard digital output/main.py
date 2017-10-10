###############################################################################
# main.py
#
# main script to toggle a digital output on/off
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

# Assign the output pint to variable output_pin
# We set it up as an output with a pulldown resistor
output_pin = pyb.Pin('X3', pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This for loop will run 5 times
for counter in range(10):
    print("Turning on")
    output_pin.value(1)         # Toggle the output_pin high/on
    time.sleep_ms(500)          # Sleep 500 milliseconds (0.5s)
    
    print("Turning off")
    output_pin.value(0)         # Toggle the output_pin low/off
    time.sleep_ms(1500)         # Sleep 1500 seconds (1.5s)
    
    
