###############################################################################
# main.py
#
# main script to read a digital input connected to pin X1. The internal 
# pull-down resistor is used. 
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

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin('X3', pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# This will loop forever, checking the button every 100ms
while (True):
    input_state = input_pin.value()   # read the state of the input
    
    if (input_state):
        print("The input is high (on).\n")
    else:
        print("The input is low (off).\n")
    
    time.sleep_ms(100)          # Sleep 100 milliseconds (0.1s)