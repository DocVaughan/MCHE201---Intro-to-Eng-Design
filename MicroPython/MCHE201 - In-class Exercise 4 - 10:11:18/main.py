# -----------------------------------------------------------------------------
# main.py
#
# When the external pushbutton is pressed, one of the onboard LEDs will turn on.
# When it is not pressed, the LED should be off.
#
# This is typically the fourth example done by students
# in MCHE201: Introduction to Engineering Design
#
# Created: 03/01/18 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 10/16/18 - JEV - joshua.vaughan@louisiana.edu
#       - updated commenting to reflect real example
#
# TODO:
#   * mm/dd/yy - Major bug to fix
# -----------------------------------------------------------------------------

import pyb  # import the pyboard module
import time # import the time module (remove if not using)


# Assign the 1st LED to variable RED_LED
RED_LED = pyb.LED(1)

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X6", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

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
