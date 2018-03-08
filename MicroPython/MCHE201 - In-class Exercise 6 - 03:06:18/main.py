###############################################################################
# main.py
#
# This script is one way to solve the 6th in-class exercise from MCHE201 in the
# spring semester of 2018.
#
# # That exercise was given as:
#  * Vary the intensity of the onboard blue LED based on how hard you are 
#    pressing on the FSR
#  * Pressing harder should make the light brighter
#
# The pin connected to Pin X22 on the pyboard, should have a pull-down resistor
#  of 10K connected to it as well. The other pin of the FSR flex sensor should 
# be connected to 3.3V.
#
# Created: 03/08/18
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

# Assign the 4th LED to variable BLUE_LED
BLUE_LED = pyb.LED(4)

# Set up the analog-to-digital converter
fsr_adc = pyb.ADC(pyb.Pin("X22"))

# Define some constants based on the FSR we're using.
# These would likely need to be tuned based on your particular setup.
#
# Determine the MIN_VALUE by connecting the sensor and not touching it. It 
# should be zero, but will likely not be exactly zero.
MIN_VALUE = 5  
#
# Determine the MAX_VALUE by squeezing the sensor as hard as you can
# This value should not exceed 4095.
MAX_VALUE = 4000 

# The intensity of the LED ranges between 0 (off) and 255 (full-on). So, we
# need to map the range of sensor readings to these numbers. We'll make a 
# simple linear mapping between the two. 
LED_MIN = 0
LED_MAX = 255

SLOPE = (LED_MAX - LED_MIN) / (MAX_VALUE - MIN_VALUE)
INTERCEPT = -SLOPE * MIN_VALUE


# Now read the pot every 500ms, forever
while (True):
    # Read the value of the FSR. It should be in the range 0-4095
    fsr_value = fsr_adc.read()
    
    # I'll work directly with the ADC value 0-4095. You could also convert
    # to voltage and use that number to determine how hard the FSR is being
    # pressed. The code below would do this conversion.
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    # voltage = 3.3 / 4095 * fsr_value

    # Now, we calculate the brightness of the LED using the linear mapping.
    # We have to change its type to an integer in order to use it in the 
    # LED intensity method. To do so, just wrap the equations in int()
    brightness = int(SLOPE * fsr_value + INTERCEPT)
            
    # print out the values, nicely formatted
    print("\nADC:       {:5d}".format(fsr_value))
    print("Intensity  {:5d}".format(brightness))
    
    # Now, set the intensity of the LED
    # Note: The brightness will not seem to vary linearly to your eye. Our
    # eyes do not map the intensity of light that way.
    # For more information, see:
    #  https://en.wikipedia.org/wiki/Luminous_intensity
    BLUE_LED.intensity(brightness)
    
    # sleep for 100ms
    time.sleep_ms(100)