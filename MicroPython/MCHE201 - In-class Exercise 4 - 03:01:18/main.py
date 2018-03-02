# -----------------------------------------------------------------------------
# main.py
#
# This script includes several ways to print the odd numbers between 1 and 27
# to the MicroPython REPL. When the number is 13, we should print
# "Counter = 13... Bad Luck!!!" and turn on the red LED. We'll leverage the
# code written for the first in-class exercise, which printed the odd numbers
# from 1-27.
#
# This is typically the second example done by students
# in MCHE201: Introduction to Engineering Design
#
# Created: 03/01/18 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
#     - major change 2
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
#
# TODO:
#   * mm/dd/yy - Major bug to fix
#   # mm/dd/yy - Desired new feature
# -----------------------------------------------------------------------------

import pyb  # import the pyboard module
import time # import the time module (remove if not using)


# Assign the 1st LED to variable RED_LED
RED_LED = pyb.LED(1)

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X4", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# This will loop forever, checking the button every 100ms
while (True):
    # read the state of the input
    input_state = input_pin.value()

    if (input_state):
        print("The input is high (on).")
        RED_LED.on()
    else:
        print("The input is low (off).")
        RED_LED.off()

    # Sleep 100 milliseconds (0.1s)
    time.sleep_ms(100)
