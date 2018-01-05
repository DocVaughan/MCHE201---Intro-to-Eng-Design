###############################################################################
# main.py
#
# This is a template script showing how to start a device based on the 
# start signal closing. It assumes that the external digital input connected to
# pin X4. The internal pull-down resistor is used. In this version, we use an
# interrupt to change the value of a flag variable. This is the more advanced
# way to sense a condition like this and how it would/should be done once you
# have some experience.
#
# See the link below for information on external interrupts in MicroPython
#   http://docs.micropython.org/en/latest/pyboard/library/pyb.ExtInt.html?highlight=interrupt
#
# Created: 10/26/17
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


# This flag variable will be checked in the main part of the script, and 
# changed by an interrupt handler function attached to the track banana plugs
start_trial = False 

# Assign the start pin to variable start_pin
# We set it up as an input with a pulldown resistor and add an interrupt to 
# handle when it is pressed. This interrupt looks for rising edges, meaning 
# when the state changes from low to high
start_pin = pyb.ExtInt(pyb.Pin('X4'), 
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

# Just print out periods while our "trial" is running. This should last 2s
for _ in range(40):
    print(".")
    time.sleep_ms(50) # sleep 50ms

print("The trial is finished.\n")
GREEN_LED.off() # Turn off the green LED to indicate that the trial is finished