###############################################################################
# main.py
#
# main script to toggle the onboard LEDs to create a "Knight Rider" effect.
#
# Note: There are definitely more efficient ways to do this.
#
# Created: 03/15/19
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

import pyb      # import the pyboard module
import time     # import the time module

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)

# Create a list of those LEDs, so that we can use them via index
leds = (RED_LED, GREEN_LED, YELLOW_LED, BLUE_LED)

SLEEP_TIME = 100    # Number of ms to sleep between toggling LEDs

going = True        # True if we're moving from low to high number LEDs
counter = 1

# Turn on LED1 (Red) before the loop starts
leds[0].on()
time.sleep_ms(SLEEP_TIME)

try:
    # This for loop will run indefiniely. The finally will trun off all LEDs
    while(True):
        #print('counter = {:d}'.format(counter))
    
        if going:  # moving from low number LEDs to high
            leds[counter].toggle()      # This should turn on the counter LED
            leds[counter-1].toggle()    # and turn off counter-1
            time.sleep_ms(SLEEP_TIME) 
        
            # When we get to the end switch directions
            if counter == 3:
                going = False
            else:
                counter = counter + 1
        
        else:  # moving from high number LEDs to low
            leds[counter].toggle()      # This should turn off the counter LED
            leds[counter-1].toggle()    # and turn on counter-1
            time.sleep_ms(SLEEP_TIME) 
        
            # When we get to the end switch directions
            if counter == 1:
                going = True
            else:
                counter = counter - 1

finally:
    print("Turning off all LEDs...")
    # Turn off all LEDs
    for led in leds:
        led.off()