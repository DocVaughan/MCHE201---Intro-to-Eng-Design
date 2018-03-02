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
GREEN_LED = pyb.LED(2)

# Assign the Switch object for the onboard button # to variable button
button = pyb.Switch()

# The condition for this while is always true, so # it runs forever
while (True):
    # button() is True if the button is pressed
    if (button()):
    	print("Button Pressed!")
        GREEN_LED.on()
        RED_LED.off()
    else:
        print("Button not pressed.")
        GREEN_LED.off()
        RED_LED.on()

	time.sleep_ms(100) # Sleep 100ms between reading
