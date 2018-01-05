###############################################################################
# main.py
#
# This is the code for the "Placebo" machine for the fall 2017 MCHE 201 final
# contest:
#   http://www.ucs.louisiana.edu/~jev9637/MCHE201_StarWars.html
#
# The machine just releases two tennis balls onto the track once the start 
# signal is sensed. Hobby-style servos are used as the release mechanism.
# As written, it is set up for the pyboard LITE servo pin assignments. See the 
# comments in the script for changes necessary for the pyboard.
#
#
# See the link below for information on external interrupts in MicroPython
#   http://docs.micropython.org/en/latest/pyboard/library/pyb.ExtInt.html?highlight=interrupt
#
# Created: 11/21/17
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



def handle_start_signal(line):
    """ 
    This function will run every time the start signal state changes from
    low to high. We use it to change the value of the start_trial variable
    from False to True. This will cause the while loop below to end, and the
    main part of the code to run.
    """
    # We need the global modifier here to enable changing 
    # the value of a global variable (start_trial in this case)
    global start_trial 

    # Turn on the green LED to indicate the trial is starting, but only
    # if this is our first time starting the trial
    if start_trial == False:
        GREEN_LED.on()  

    start_trial = True


# Define the servo object. The numbering scheme differs between the pyboard and
# the pyboard LITE.
# 
# For the pyboard:
#  Servo 1 is connected to X1, Servo 2 to X2, Servo 3 to X3, and Servo 2 to X4
#
# For the pyboard LITE:
#  Servo 1 is connected to X3, Servo 2 to X4, Servo 3 to X1, and Servo 2 to X2

# Here, we'll use the first position on the pyboard
servo1 = pyb.Servo(1)
servo2 = pyb.Servo(2)


# This flag variable will be checked in the main part of the script, and 
# changed by an interrupt handler function attached to the track banana plugs
start_trial = False 

# Assign the start pin to variable start_pin
# We set it up as an input with a pulldown resistor and add an interrupt to 
# handle when it is pressed. This interrupt looks for rising edges, meaning 
# when the state changes from low to high
start_pin = pyb.ExtInt(pyb.Pin('X7'), 
                       pyb.ExtInt.IRQ_RISING, 
                       pyb.Pin.PULL_DOWN, 
                       handle_start_signal)

# Let's also set up the green LED to turn on when we sense the start button
GREEN_LED = pyb.LED(2)


# ----------------- The main part of the script starts here -----------------
# This will loop until the value of start_trial becomes true
while (not start_trial):
    print("Waiting for the start signal...\n")
    time.sleep_ms(100) # Sleep 100 milliseconds (0.1s)


#-- Your control algorithm would go here in place of these print statements --
print("The trial is starting!!!")

# Move the servos to release the tennis balls
servo1.angle(-60)
servo2.angle(60)

# wait 1 second
time.sleep(1)

# reset the servos to 0 angle
servo1.angle(0)
servo2.angle(0)
 
# Finally, turn off the Green LED
print("The trial is finished.\n")
GREEN_LED.off() # Turn off the green LED to indicate that the trial is finished