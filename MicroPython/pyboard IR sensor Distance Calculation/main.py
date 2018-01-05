###############################################################################
# main.py
#
# simple script to read the value of a the IR sensor every 500ms and print 
# its value to the REPL. In this version, we use a curve fit derived from the 
# sensor data sheet to approximate the distance to the nearest object in 
# front of the sensor based on its analog output.
# 
# The yellow cable from the sensor should be connected 
# to Pin X22 on the pyboard.
#
# The sensor outputs approximately:
#  * 3.1V at 4cm
#  * 0.3V at 30cm
#  * There is a nonlinear relationship between these values
#
# Sensor datasheet and application note:
#   http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a41sk_e.pdf
#   http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a_gp2y0d_series_appl_e.pdf
#
# Curve fit script:
#  https://git.io/vFwc7
#
# Created: 10/25/17
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

# We need the exponent function from the math module
# Since we're only using on function from the module, we can just import
# that function alone using the "from __ import __" style.
from math import exp

# Set up the analog-to-digital converter
IR_adc = pyb.ADC(pyb.Pin("X22"))

# Now read the pot every 500ms, forever
while (True):
    # Read the value of the flex sensor. It should be in the range 0-4095
    IR_value = IR_adc.read()
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    voltage = 3.3 / 4095 * IR_value

    
    # Always print out the ADC values, nicely formatted
    print("ADC:      {:5d}".format(IR_value))
    print("Voltage:  {:5.2f}".format(voltage))

    # Now, calculate the distance based on the ADC voltage
    distance = 72.72693033 * exp(-2.36147409 * voltage) + 5.43546275

    # If we get an answer outside of the range of the sensor, issue a warning.
    if distance > 40 or distance < 4:
        print("WARNING: Distance reading seems out of range.\n")
    else:
        print("Distance: {:5.2f}\n".format(distance))

    # sleep for 500ms
    time.sleep_ms(500)