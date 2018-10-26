###############################################################################
# main.py
#
# Main script to toggle a digital output on/off. In this case, we are using
# it to control a pair of external LEDs connected to pin X7 of the pyboard. In
# this configuration, when the output pin is high, one LED will be on, and when
# the output pin is low, the other will be on. To turn both off, we need to 
# redefine the pin as an input.
#
# Created: 10/26/18
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


# This for loop will run 10 times
for counter in range(10):
    # Assign the output pint to variable output_pin
    # We set it up as an output with a pulldown resistor
    # We do this inside the loop because we have to change the pin 
    # configuration in order to turn off both LEDS, based on how we've wired
    # them. This is what allows us to control two LEDs with a single pyboard
    # digital output
    output_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
    
    print("Turning green LED on, red LED off")
    output_pin.value(0)         # Toggle the output_pin high/on
    time.sleep_ms(500)          # Sleep 500 milliseconds (0.5s)
    
    print("Turning red LED on, green LED off")
    output_pin.value(1)         # Toggle the output_pin high/on
    time.sleep_ms(500)          # Sleep 500 milliseconds (0.5s)
    
    # In this configuration to turn both off, we set the pin to be an input
    # We have to remember, however, to set it back to an output to be able to 
    # later turn either LED on
    print("Turning both off\n")
    output_pin = pyb.Pin("X7", pyb.Pin.IN) 
    time.sleep(1)         # Sleep 1 second
