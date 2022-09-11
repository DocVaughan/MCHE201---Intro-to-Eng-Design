###############################################################################
# main.py
#
# This is a template script showing how to start a device based on the 
# start signal closing. It assumes that the external digital input connected to
# pin X6. The internal pull-down resistor is used. 
#
# Created: 10/26/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 09/29/18 - JEV - Changed pin to match upcoming MCHE201 breakout
#
# TODO:
#   * 
###############################################################################

import pyb  # import the pyboard module
import time # import the time module

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X6", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# This will loop forever, checking the button every 10ms
while (True):
    input_state = input_pin.value()   # read the state of the input
    
    if (input_state):
        print("The start button is pressed. I'll run the main code now.\n")
        # Main code could be here
        #   or
        # A call to a function containing the main control logic could be here

        # If what runs here is less than 30 sec. long, you'll need to account
        # for that condition. If not, then the start signal will still be "on"
        # when this part of your code finishes. So, it will still be True and 
        # therefore start running again.

    else:
        print("Start button is not pressed. I'll wait, then check again.\n")

    time.sleep_ms(10)          # Sleep 10 milliseconds (0.01s)