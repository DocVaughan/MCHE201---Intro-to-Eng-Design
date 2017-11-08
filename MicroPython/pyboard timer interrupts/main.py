# main.py -- put your code here!

###############################################################################
# main.py
#
# Script demonstrating using the timer-based interrupts on the the pyboard
#
# These provide a way to trigger a command after a set amount of time without requiring 
# a timer.sleep() type function which would prohibit us from doing other things. In this 
# example, we'll just set up a couple timers to trigger at intervals, then enter a loop
# printing a counter. Their trigger should be inserted into the print statements. 
#
# A similar construct could be used to set a motor after a set amount of time running, etc
#
# For more information on the timers:
#    http://docs.micropython.org/en/latest/pyboard/tutorial/timer.html
#
# Created: 11/08/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   *
#
###############################################################################

import pyb
import machine
import time

# Set aside some memory for reporting any errors that occur in our interrupt
import micropython
micropython.alloc_emergency_exception_buf(100)

def handle_timer4_callback(timer):
    print("--- Hello from Timer 4! ---")

# We can set up a a frequency defined by the freq parameter (Hz)
# In this code, the timer will operate at 1/2 Hz
timer4 = pyb.Timer(4, freq=1/2)

# We then define the callback function to be called each time the timer is 
# triggered. We should only do simple/fast things in that callback function.
timer4.callback(handle_timer4_callback)

# Now, let's see it in action. In this while loop, we'll from Hello every 1/2
# second. We should see the timer callback print statement happening every 4
# prints from the while loop, since we're sleeping 500ms between them
for index in range(20):
    print("Hello from while loop")
    # sleep for 100ms
    time.sleep_ms(500)

# Once we're finished using the timer callback, we can/should disable it. This
# way it doesn't continued to be called.
#
# To disable to the callbacks, pass them None
timer4.callback(None)
print('Callback disabled\n\n')


# Let's set up the callback again and demonstrate how we can change the
# frequency it gets called
timer4.callback(handle_timer4_callback)

for index in range(20):
    print("Hello from while loop")
    
    # after 10 loops, let's change the callback freq to 10Hz
    # After this change, the callback should print 5 times for every single 
    # while loop print
    if index >= 9:
        timer4.init(freq=10)
    
    # sleep for 100ms
    time.sleep_ms(500)

# To disable to the callbacks, pass them None
timer4.callback(None)
print('Callback disabled\n\n')