###############################################################################
# main.py
#
# Main script to toggle a digital output on/off. In this case, we are using
# it to control a transistor, which is acting like a on/off switch for 
# controlling a LED. As we've seen before we do not need the transistor to 
# control an LED, but it provides an easy example setup. In general, we could a 
# transistor to effectively switch a higher-current or higher-voltage load. 
# When using a transistor this way, be sure to stay within its voltage and 
# current limits. 
# 
#
# To use this script as is, connect the center pin (the base) of the NPN 
# transistor to pin X7 of the pyboard.
#
# Created: 10/27/18
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

# Assign the output pin to variable output_pin
# We set it up as an output with a pulldown resistor
output_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This loop will run 5 times
for counter in range(5):
    print("Turning LED on")
    output_pin.value(1)         # Toggle the output_pin high/on
    time.sleep(1)               # Sleep 1 second

    print("Turning LED off")
    output_pin.value(0)         # Toggle the output_pin high/on
    time.sleep(1)               # Sleep 1 second

