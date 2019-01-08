###############################################################################
# main.py
#
# simple script to read the value of a the IR sensor every 500ms and print 
# its value to the REPL. In this version, we use a curve fit derived from the 
# sensor data sheet to approximate the distance to the nearest object in 
# front of the sensor based on its analog output. We'll also smooth the data
# using an Exponential Moving Average. For more info
# 
# The yellow cable from the sensor should be connected 
# to Pin X20 on the pyboard.
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
# Created: 11/11/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 09/29/18 - JEV - Changed pin to match upcoming MCHE201 breakout
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
IR_adc = pyb.ADC(pyb.Pin("X20"))

# For the choices below, we more-or-less are approximating using an average of 
# the 10 values to determine the current value. You should tune these values 
# based on much smoothing the signal needs and how much time elapses between
# your sensor readings.
alpha = 0.9
beta = 1 - alpha

# We need to define a value here to use the first time through the loop
last_filtered_value = 0

# Now read the pot every 500ms, forever
while (True):
    # Read the value of the flex sensor. It should be in the range 0-4095
    IR_value = IR_adc.read()
    
    filtered_value = alpha * last_filtered_value + beta * IR_value
    last_filtered_value = filtered_value # save the current value for next loop
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    raw_voltage = 3.3 / 4095 * IR_value
    filtered_voltage = 3.3 / 4095 * filtered_value

    # printing this should clear the REPL
    # We can fake a screen where only the values update
    print("\033[2J\033[;H")
        
    # Print out the ADC values, comparing the raw and filtered
    print("               Raw     \tFiltered")
    print("ADC:          {:5d}   \t {:5d}".format(IR_value, int(filtered_value)))
    print("Voltage:      {:5.2f} \t {:5.2f}".format(raw_voltage, filtered_voltage))

    # Now, calculate the distance based on the filtered ADC voltage
    raw_distance = 72.72693033 * exp(-2.36147409 * raw_voltage) + 5.43546275
    distance = 72.72693033 * exp(-2.36147409 * filtered_voltage) + 5.43546275

    # If we get an answer outside of the range of the sensor, issue a warning.
    if distance > 40 or distance < 4:
        print("WARNING: Distance reading seems out of range.\n")
    else:
        print("Distance:     {:5.2f} \t {:5.2f}\n".format(raw_distance, distance))

    # sleep for 100ms (0.1s)
    time.sleep_ms(100)