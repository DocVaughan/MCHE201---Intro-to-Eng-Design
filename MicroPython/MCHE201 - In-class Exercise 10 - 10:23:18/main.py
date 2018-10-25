###############################################################################
# main.py
#
# This script is one way to solve the 10th in-class exercise from MCHE201 in the 
# spring semester of 2018. 
#
# That exercise was given as:
#* Connect
#   - a pushbutton
#   - the servomotor
# * Start the servo at 0deg
# * When the button is pressed, move servo to 30deg for 1sec, then back to 0
# * Only allow this to happen once per 30seconds
#
# In this version of the solution, check for the status of the button 
# repeatedly. Once it is pressed, we move the servo then sleep for 30s. This is
# not the most generalizable way to do this, but it does solve the problem at 
# hand. 
# 
# To generalize, you need to allow for other operations during the 30 seconds.
# These could happen inside the "button pressed" part of the code, in place of
# the pure sleep. For the final contest, you might still want long-ish delay
# here to prevent your machine from re-running if a trial 
#
# Created: 03/15/18
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 10/25/18- JEV - joshua.vaughan@louisiana.edu
#       - updated pin number to reflect upcoming MCHE201 breakout
#
# TODO:
#   * 
###############################################################################

import pyb  # import the pyboard module
import time # import the time module

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X6", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# For the pyboard:
#  Servo 1 is connected to X1, Servo 2 to X2, Servo 3 to X3, and Servo 2 to X4
# Here, we'll use the first position on the pyboard
servo1 = pyb.Servo(1)

# Now, we can control the angle of the servo
# The range of possible angles is -90 < angle < 90, but many servos can't move
# over that entire range. A safer range is -60 < angle < 60 or even 
# -45 < angle < 45
servo1.angle(0)

# This will loop forever, checking the button every 10ms
while (True):
    input_state = input_pin.value()   # read the state of the input
    
    if (input_state):
        print("The button was pressed. I'll move the servo now.\n")
        
        # Move the servo to 30 deg
        servo.angle(30)
        
        # Sleep for 1s
        time.sleep(1)
        
        # Now, move back to 0deg
        servo.angle(0)
        
        # sleep for 29seconds to disallow any other action during this time.
        time.sleep(29)
        
    else:
        print("Button is not pressed. I'll wait, then check again.\n")

    time.sleep_ms(10)          # Sleep 10 milliseconds (0.01s)