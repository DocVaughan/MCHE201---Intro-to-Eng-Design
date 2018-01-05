###############################################################################
# main.py
#
# simple script to read the value of a soft potentiometer every 500ms and print 
# its value to the REPL. The middle-pin should be connected to Pin X22 on 
# the pyboard, and have a pull-down resistor of 10K connected to it as well. 
# One of the other pins should be connected to 3.3V, and the final pin to 
# ground.
#
# Created: 10/05/17
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

# Set up the analog-to-digital converter
adc = pyb.ADC(pyb.Pin("X22"))

# Now read the pot every 500ms, forever
while (True):
    # Read the value of the flex sensor. It should be in the range 0-4095
    pot_value = adc.read()
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    voltage = 3.3 / 4095 * pot_value
    
    if pot_value > 4091:
        location = "not pressing"
    elif pot_value > 3500:
        location = "high"
    elif pot_value < 500:
        location = "low"
    else:
        location = "middle"
    
    # print out the values, nicely formatted
    print("ADC:     {:5d}".format(pot_value))
    print("Voltage: {:5.2f}".format(voltage))
    if pot_value < 4000:
        print("You're pressing in the {} part of the pot.\n".format(location))
    else:
        print("It looks like you're not pressing the pot.\n")

    # sleep for 500ms
    time.sleep_ms(500)