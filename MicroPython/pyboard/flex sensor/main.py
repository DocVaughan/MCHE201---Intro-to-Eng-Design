###############################################################################
# main.py
#
# simple script to read the value of a flex sensor every 500ms and print 
# its value to the REPL. The pin connected to Pin X22 on the pyboard, should 
# have a pull-up resistor of 10K connected to it as well. The other pin of the
# flex sensor should be connected to ground.
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
    flex_value = adc.read()
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    voltage = 3.3 / 4095 * flex_value
    
    # print out the values, nicely formatted
    print("ADC:     {:5d}".format(flex_value))
    print("Voltage: {:5.2f}\n".format(voltage))

    # sleep for 500ms
    time.sleep_ms(500)