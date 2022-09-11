###############################################################################
# main.py
#
# Main script to toggle a digital output on/off. In this case, we are using
# it to control a transistor, which is controlling a relay. The relay needs
# 5VDC to switch, so the pyboard cannot do so directly. We are effectively 
# using the transistor as a switch on the 5VDC power supply from the pyboard.
# The relay is connected to two LEDs. One is connected to the normally-closed
# output and will be on with the relay is not triggered. The other is connected
# to the normally-open output of the relay and will turn on when the relay is
# triggered.
# 
# The wiring should match that found in Circuit 13 of the SparkFun SIK guide
#  https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33/all#experiment-13-using-relays
#
# To use this script as is, connect the center pin (the base) of the NPN 
# transistor to pin X7 of the pyboard.
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

# Assign the output pin to variable output_pin
# We set it up as an output with a pulldown resistor
output_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# This loop will run 5 times
for counter in range(5):
    print("Turning green LED on, blue LED off")
    output_pin.value(1)         # Toggle the output_pin high/on
    time.sleep(1)               # Sleep 1 second

    print("Turning blue LED on, green LED off")
    output_pin.value(0)         # Toggle the output_pin high/on
    time.sleep(1)               # Sleep 1 second

