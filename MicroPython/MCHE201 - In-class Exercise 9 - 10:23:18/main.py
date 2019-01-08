###############################################################################
# main.py
#
# This script is one way to solve the 9th in-class exercise from MCHE201 in the 
# spring semester of 2018. In this version of the solution, we use nested loops
# check for the status of the button. To prevent multiple readings of the
# same button press, we have to be careful with the timing. Even so, this 
# solution is somewhat fragile to how fast/long the user presses the button
# for each transition change. There will be a limit, but you could perhaps tune 
# this solution to be more robust by changing the values in the various 
# time.sleep_ms() commands.
# 
# We keep track the time elapsed since the first press of the button and turn
# on an LED every second until the 5s limit is up. So, the LEDs serve as a 
# progress bar on the timer.
# 
# That exercise was given as:
# * Connect a pushbutton
# * Turn on the green LED
# * Once the button is pressed the first time, turn off all LEDs. 
# * Then, turn on 1 LED every 10s until the button is pressed again
# * When the button is pressed again, print the time elapsed between button pressed to the REPL
# * If more than 5s elapses:
#     - Print "You took too long!!!" to the REPL
#     - Turn on only the green LED again
#
# Created: 03/13/18
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

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X6", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# Turn on the green LED
GREEN_LED.on()

# This will loop forever, checking the button every 100ms
while (True):
    # read the state of the input
    input_state = input_pin.value()

    if (input_state):
        start_time = time.ticks_ms() # save the current time
        GREEN_LED.off()
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
            # Doing so will help "debounce" the switch. For more information on 
            # debouncing switches see:
            #  http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/debounce.html
            time.sleep_ms(100) 

            # read the state of the input
            input_state = input_pin.value()
            
            # Calculate the time elapsed in ms since we first pressed the button
            time_elapsed = time.ticks_diff(time.ticks_ms(), start_time)

            if (input_state):
                GREEN_LED.on()
                RED_LED.off()
                YELLOW_LED.off()
                BLUE_LED.off()
                print("Button pressed to stop.")
                print("Elapsed time = {}ms\n".format(time_elapsed))
                
                # Set button_timing to False because we are no longer in a 
                # timing part of the algorithm. This will break the while loop
                # that is looking for the 2nd press of the button, therefore
                # returning to looking for a first press.
                button_timing = False

                # We could also have another delay here, to force a longer 
                # separation between the pressing of the button to stop the 
                # timer and pressing the button to start the timer again.
                time.sleep_ms(200)
            else:
                # print("Elapsed ticks = {}ms\n".format(time_elapsed))
                if time_elapsed > 5000: # >5000ms
                    print("You took too long!!!")
                    
                    # We no longer want to look for the "timing" button press
                    button_timing = False
                    
                    # Turn off the LEDs
                    RED_LED.off()
                    GREEN_LED.off()
                    YELLOW_LED.off()
                    BLUE_LED.off()
                    
                elif time_elapsed > 4000: # >4000ms
                    BLUE_LED.on() 
                elif time_elapsed > 3000: # >3000ms
                    YELLOW_LED.on()   
                elif time_elapsed > 2000: # > 2000ms 
                    GREEN_LED.on()
                elif time_elapsed > 1000: # > 1000ms
                    RED_LED.on()

    time.sleep_ms(10)          # Sleep 10 milliseconds (0.1s)
