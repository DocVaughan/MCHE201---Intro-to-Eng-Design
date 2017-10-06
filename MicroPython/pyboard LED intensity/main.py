###############################################################################
# main.py
#
# main script to vary the brightness of the onboard blue LED
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

import pyb 	# import the pyboard module
import time	# import the time module

# Assign the 4th LED to variable BLUE_LED
BLUE_LED = pyb.LED(4)

print("Turning on LED")
BLUE_LED.on()			# Turn on at full brightness
time.sleep(1)			# Sleep 1 second

print("Setting to 1/2 intensity")
BLUE_LED.intensity(128)	# Set to ~1/2 intensity
time.sleep(1)			# Sleep 1 second

print("Setting to 1/4 intensity")
BLUE_LED.intensity(64)	# Set to ~1/4 intensity
time.sleep(1)			# Sleep 1 second

print("Setting to min. intensity")
BLUE_LED.intensity(1)	# Set to minimum intensity
time.sleep(1)			# Sleep 1 second

print("Turning off LED")
BLUE_LED.off()			# Turn it off