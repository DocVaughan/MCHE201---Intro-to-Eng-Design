###############################################################################
# main.py
#
# This script is one way to solve the 5th in-class exercise from MCHE201 in the
# spring semester of 2018.
# 
# That exercise was given as:
#   * Divide the flex sensor range into four
#   * Turn on the same number LEDs as the “range number” of the current state 
#     of the flex sensor.
#   * In other words, when the sensor is not bent, no LEDs should be on. When 
#     it's bent a little, one LED should turn on. When it's bent to its 
#     maximum, all 4 LEDs should be on.
#
# The pin connected to Pin X22 on the pyboard, should 
# have a pull-up resistor of 10K connected to it as well. The other pin of the
# flex sensor should be connected to ground.
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

# Set up the analog-to-digital converter
flex_adc = pyb.ADC(pyb.Pin("X22"))

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)

# Define some constants setting the range of the flex sensor
# These numbers will likely vary for your particular system. 
# So, they should be determined experimentally.
MIN_ADC = 2875
CENTER = 3275
MAX_ADC = 3850

# The pattern that the LEDs should follow is:
#
#   |   |   |   | Center |   |   |   |   
# 4 | 3 | 2 | 1 |   0    | 1 | 2 | 3 | 4
# 
# where the number represents the number of LEDs on. We can see from this
# chart that there are 4.5 "zones" on either side of the center. With the 
# middle, "0 LED on" zone split evenly between the two bend directions.
# 
# We'll assume that the flex sensor reading varies linearly with how far it 
# is bent to determine the numerical values for these ranges. Note: This is 
# generally *not* true. To improve the performance of this script, you would
# want to consult the specification sheet of the sensor or experimentally
# determine the relationship between flex and resistance. From that data, 
# you could better tune these ranges.

# Using the analysis above, we can define the size of each division
LOW_ADC_DIVIDER = (CENTER - MIN_ADC) / 4.5
HIGH_ADC_DIVIDER = (MAX_ADC - CENTER) / 4.5

# We'll create ranges both above and below the center
# This will account for the flex sensor being bent in either direction
ONE_ZONE_LOW = CENTER - LOW_ADC_DIVIDER * 0.5  
TWO_LED_LOW = CENTER - LOW_ADC_DIVIDER * 1.5
THREE_LED_LOW = CENTER - LOW_ADC_DIVIDER * 2.5
FOUR_LED_LOW = CENTER - LOW_ADC_DIVIDER * 3.5

ONE_ZONE_HIGH = CENTER + HIGH_ADC_DIVIDER * 0.5  
TWO_LED_HIGH = CENTER + HIGH_ADC_DIVIDER * 1.5
THREE_LED_HIGH = CENTER + HIGH_ADC_DIVIDER * 2.5
FOUR_LED_HIGH = CENTER + HIGH_ADC_DIVIDER * 3.5


# Now read the pot every 500ms, forever
while (True):
    # Read the value of the flex sensor. It should be in the range 0-4095
    flex_value = flex_adc.read()
    
    # I'll work directly with the ADC value 0-4095. You could also convert
    # to voltage and use that number to determine how bent the sensor is. 
    # The code below would do this conversion.
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    # voltage = 3.3 / 4095 * flex_value
    
    # print out the values, nicely formatted
    print("\nADC:     {:5d}".format(flex_value))
    
    # Now, we'll check the ADC value to determine which of the ranges it 
    # falls into.
    if flex_value < FOUR_LED_LOW or flex_value > FOUR_LED_HIGH:
        print("All LEDs on.")
        RED_LED.on()
        GREEN_LED.on()
        YELLOW_LED.on()
        BLUE_LED.on()
    elif flex_value < THREE_LED_LOW or flex_value > THREE_LED_HIGH:
        print("Three LEDs on.")
        RED_LED.on()
        GREEN_LED.on()
        YELLOW_LED.on()
        BLUE_LED.off()
    elif flex_value < TWO_LED_LOW or flex_value > TWO_LED_HIGH:
        print("Two LEDs on.")
        RED_LED.on()
        GREEN_LED.on()
        YELLOW_LED.off()
        BLUE_LED.off()
    elif flex_value < ONE_ZONE_LOW or flex_value > ONE_ZONE_HIGH:
        print("One LEDs on.")
        RED_LED.on()
        GREEN_LED.off()
        YELLOW_LED.off()
        BLUE_LED.off()
    else:
        print("No LEDs on.")
        RED_LED.off()
        GREEN_LED.off()
        YELLOW_LED.off()
        BLUE_LED.off()

    # sleep for 500ms
    time.sleep_ms(500)