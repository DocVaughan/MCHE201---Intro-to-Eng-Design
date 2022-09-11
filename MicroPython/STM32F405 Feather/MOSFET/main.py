###############################################################################
# main.py
#
# Main script to toggle a digital output on/off. In this case, we are using
# it to control a MOSFET, which is acting like a on/off switch for 
# controlling a 5V solenoid.
#
# To use this script as is, connect the center pin ... to pin Y3 of the pyboard.
#
# Created: 11/02/18
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

# Assign the output pin to variable mosfet_pin
# We set it up as an output with a pulldown resistor
mosfet_pin = pyb.Pin("Y3", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This loop will run 5 times
for counter in range(5):
    print("Turning MOSFET on, Solenoid should retract.")
    mosfet_pin.high()
    time.sleep_ms(50)           # Sleep 25ms
    
    print("Turning MOSFET off, Solenoid should extend via its spring.")
    mosfet_pin.low()
    time.sleep(1)               # Sleep 1 second


