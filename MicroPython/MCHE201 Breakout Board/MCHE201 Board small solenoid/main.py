###############################################################################
# main.py
#
# Main script to toggle a digital output on/off. In this case, we are using
# it to control a MOSFET, which is acting like a on/off switch for 
# controlling a the small 5V solenoid.
# 
# IMPORTANT: Do NOT leave the small solenoid in the MCHE201 kit on for extended
#            periods of time.
#
# To use this script as is to pin Y3 of the pyboard, which is connected to the
# 5V mosfet controlled output on the MCHE201 board.
#
# Created: 03/28/19
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
solenoid = pyb.Pin("Y3", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This loop will run 5 times over the 5V solenoid output
for counter in range(5):
    print("Turning MOSFET on, Solenoid should retract.")
    solenoid.high()
    time.sleep_ms(100)           # Sleep 100ms
    
    print("Turning MOSFET off, Solenoid should extend via its spring.")
    solenoid.low()
    time.sleep(1)               # Sleep 1 second