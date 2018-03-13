###############################################################################
# main.py
#
# This script is one way to solve the 8th in-class exercise from MCHE201 in the 
# spring semester of 2018. In this version of the solution, we use nested loops
# check for the status of the button. To prevent multiple readings of the
# same button press, we have to be careful with the timing. Even so, this 
# solution is somewhat fragile to how fast/long the user presses the button
# for each transition change. There will be a limit, but you could perhaps tune 
# this solution to be more robust by changing the values in the various 
# time.sleep_ms() commands.
# 
# That exercise was given as:
# * Connect a pushbutton
# * Turn on the green LED
# * When the pushbutton is pressed
#     - Turn on the red LED
#     - Turn off the green LED
# * When the button is pressed again
#     - Turn off the red LED
#     - Turn on the green LED
#     - Print the time elapsed between button pressed to the REPL
#
# Created: 03/13/18
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

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin('X4', pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# Turn on the green LED
GREEN_LED.on()

# This will loop forever, checking the button every 100ms
while (True):
    # read the state of the input
    input_state = input_pin.value()

    if (input_state):
        start_time = time.ticks_ms()
        GREEN_LED.off()
        RED_LED.on()
        print("Button pressed to start.\n")

        # We could also have another delay here, to force a longer separation 
        # between the pressing of the button to start the timer and pressing
        # the button to end the timer.
        time.sleep_ms(200)

        button_timing = True # If true, we are waiting for the second button

        # Since we just set the button_timing value to true, this loop will 
        # run. Inside it, if we detect a press of the button, we'll set 
        # button_timing to false, stopping this loop.
        while (button_timing):
            # In this while loop, we'll place the sleep time at the beginning
            # Doing so will "debounce" the switch. For more information on 
            # debouncing switches see:
            #  http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/debounce.html
            time.sleep_ms(10) 
        
            # read the state of the input
            input_state = input_pin.value()

            if (input_state):
                end_time = time.ticks_ms()
                GREEN_LED.on()
                RED_LED.off()
                print("Button pressed to stop.")

                time_elapsed = time.ticks_diff(end_time, start_time)
                print("Elapsed ticks = {}\n".format(time_elapsed))
                button_timing = False
                
                
                # We could also have another delay here, to force a longer 
                # separation between the pressing of the button to stop the 
                # timer and pressing the button to start the timer again.
                time.sleep_ms(200)

    time.sleep_ms(10)          # Sleep 10 milliseconds (0.1s)
