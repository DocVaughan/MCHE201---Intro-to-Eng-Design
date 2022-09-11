###############################################################################
# main.py
#
# main script to manually read the state of the onboard button indefinitely
# It waits 1s between each reading. 
# If the button is pressed, it prints "Button Pressed!" over UART
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

# Assign the Switch object for the onboard button to variable button
button = pyb.Switch()

while (True):
    # button() is True if the button is pressed
    if (button()): 
        print("Button Pressed!")
    
    time.sleep_ms(100) # Sleep 100ms between reading