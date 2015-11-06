#! /usr/bin/env python

###############################################################################
# MCHE201_ControlBox.py
#
# Code to control the MCHE201 competition
#  1. Listens for switch to be pressed
#  2. When pressed, closes 4 relays for 30sec and 4 LEDs on
#
#
# Created: 11/03/15
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   *
#
###############################################################################

import pifacedigitalio
import time

# creates a PiFace Digtal object
pfd = pifacedigitalio.PiFaceDigital() 

try:
    while True:
    
        contest_start = pfd.switches[0].value
        
        if contest_start:
            # Close all the relays
            pfd.relays[0].value = 1 
            pfd.relays[1].value = 1
            pfd.output_pins[2].value = 1
            pfd.output_pins[3].value = 1
    
            # Turn on the LEDS
            pfd.output_pins[7].value = 1
            pfd.output_pins[6].value = 1
            pfd.output_pins[5].value = 1
            pfd.output_pins[4].value = 1
            
            # Get the current time
            start_time = time.time()
            
            while (time.time() - start_time < 30) and not pfd.switches[1].value:
                time.sleep(0.1)
            
            # Open all the relays
            pfd.relays[0].value = 0 
            pfd.relays[1].value = 0
            pfd.output_pins[2].value = 0
            pfd.output_pins[3].value = 0
    
            # Turn off the LEDS
            pfd.output_pins[7].value = 0
            pfd.output_pins[6].value = 0
            pfd.output_pins[5].value = 0
            pfd.output_pins[4].value = 0

except(KeyboardInterrupt, SystemExit):
    pass