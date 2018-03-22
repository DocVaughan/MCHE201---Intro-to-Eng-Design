###############################################################################
# main.py
#
# This script is one way to solve the 11th in-class exercise from MCHE201 in the 
# spring semester of 2018. 
# 
# That exercise was given as:
# * Connect:
#     - the IR sensor 
#     - a pushbutton
# * Wait for the pushbutton to be pressed
# * Once it is pressed:
#     - Read the IR sensor every 100ms for 30 seconds
#     - Print its value to the REPL
#     - If objects are closer than 6 inches, turn on the red LED
#     - Otherwise, turn on the green LED
# * After 30 seconds, turn off all the LEDs
#  
#
# The sensor outputs approximately:
#  * 3.1V at 4cm
#  * 0.3V at 30cm
#  * There is a nonlinear relationship between these values
#
# Sensor datasheet and application note:
# http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a41sk_e.pdf
# http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a_gp2y0d_series_appl_e.pdf
#
#
# Created: 03/15/18
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

# Assign the input pin to variable input_pin
# We set it up as an input with a pulldown resistor
input_pin = pyb.Pin("X4", pyb.Pin.IN, pull=pyb.Pin.PULL_DOWN)

# Set up the analog-to-digital converter for the IR sensor
IR_adc = pyb.ADC(pyb.Pin("X22"))

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)


while (True):
    input_state = input_pin.value()   # read the state of the input
    
    if (input_state):
        print("The button was pressed. Checking the IR sensor now.\n")
        start_time = time.ticks_ms() # save the current time
        
        while (time.ticks_diff(time.ticks_ms(), start_time) < 30000):
            # Read the value of the IR sensor. It should be in the range 0-4095
            IR_value = IR_adc.read()
    
            # We can convert the value to the voltage we are reading. 
            # 0=0V and 4095=3.3V
            voltage = 3.3 / 4095 * IR_value
    
            # print out the values, nicely formatted
            print("ADC:     {:5d}".format(IR_value))
            print("Voltage: {:5.2f}\n".format(voltage))
            
            if (voltage > 0.85): # This was the 6in voltage for my sensor
                print("WARNING: Object within 6 inches.\n")
                RED_LED.on()
                GREEN_LED.off()
            else:
                RED_LED.off()
                GREEN_LED.on()

            # sleep for 100ms
            time.sleep_ms(100)
        
        # Now, turn off both LEDs
        RED_LED.off()
        GREEN_LED.off()
        
        # sleep for 10ms before checking the button again
        time.sleep_ms(10)