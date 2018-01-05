###############################################################################
# main.py
#
# simple script to read the value of a potentiometer every 500ms and print 
# its value to the REPL. The "middle" pin of the potentiometer should be 
# connected to Pin X22 on the pyboard.One of the outer pins should be connected
# to A3V3 (Pin X23) and the other to AGND (PIN X24), as shown below.
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

    # Read the value of the potentiometer. It should be in the range 0-4095
    pot_value = adc.read()
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    voltage = 3.3 / 4095 * pot_value
    
    # print out the values, nicely formatted
    print("The ADC value is {}, which is a voltage of {:.2f}.".format(pot_value, voltage))

    # sleep for 500ms
    time.sleep_ms(500)