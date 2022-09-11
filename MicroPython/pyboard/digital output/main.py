###############################################################################
# main.py
#
# main script to toggle a digital output on/off. In this case, we are using
# it to control an external LED connected to pin X7 of the pyboard.
#
# Created: 10/03/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 10/23/18 - JEV - joshua.vaughan@louisiana.edu
#       - Changed pin to reflect upcoming MCHE201 breakout board
#       - Better commenting
# TODO:
#   * 
###############################################################################

import pyb  # import the pyboard module
import time # import the time module

# Assign the output pint to variable output_pin
# We set it up as an output with a pulldown resistor
output_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This for loop will run 10 times
for counter in range(10):
    print("Turning on")
    output_pin.value(1)         # Toggle the output_pin high/on
    time.sleep_ms(500)          # Sleep 500 milliseconds (0.5s)
    
    print("Turning off")
    output_pin.value(0)         # Toggle the output_pin low/off
    time.sleep_ms(1500)         # Sleep 1500 seconds (1.5s)
