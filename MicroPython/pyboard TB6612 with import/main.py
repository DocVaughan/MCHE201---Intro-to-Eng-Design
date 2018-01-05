###############################################################################
# main.py
#
# This script will control a single DC motor using a TB6612 motor driver board. 
# It should work with all Toshiba TB6612 driver breakouts, but has only been 
# tested with the Adafruit one:
#  https://www.adafruit.com/product/2448
#
# In this version, we use a class developed specifically for interfacing with
# and controlling the TB6612. It provides several convenience functions. To
# use this class, you need to copy the TB6612.py file to the pyboard.
#
# Motor driver shec sheet - https://cdn-shop.adafruit.com/datasheets/TB6612FNG_datasheet_en_20121101.pdf
# Adafruit Overview - https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout
#
# Created: 11/01/17
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

import pyb  # import the pyboard module
import time # import the time module
import TB6612 # import the file containing our TB6612 motor code

# We need to set up two digital outputs that we will use to control the 
# direction of the motor. In this case, the TB6612 class file will handle the
# low-level settings for the pins
A1_PIN = 'X8'
A2_PIN = 'X7'

# We also need to set up a third pin to control the speed of the motor. This 
# output needs to have PWM capabilities, so it should be connected to a pin
# that has an associated timer on the pyboard. IF these are defined correctly
# here, then the TB6612 class file will handle the low-level set up
PWM_PIN = 'X6'
PWM_TIMER = 2
PWM_CHANNEL = 1

# Now, we can create a motor instance, calling upon the TB6612 class
motorA = TB6612.motor(PWM_PIN, A1_PIN, A2_PIN, PWM_TIMER, PWM_CHANNEL)


try:
    # This for loop will run 5 times
    for counter in range(5):
        print("Turning on approx 1/2 speed")

        # To start the motor, issue the .set_speed() command with a speed 
        # between -100 and 100
        motorA.set_speed(50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set tell it to stop
        motorA.stop()
        time.sleep_ms(100)         # Sleep briefly to let the motor stop
    
        print("Turning on approx 1/2 speed in the other direction")
        # To move in the opposite direction, issue a negative speed       
        motorA.set_speed(-50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        motorA.stop()
        time.sleep_ms(100)         # Sleep briefly to let the motor stop

except:
    print("Some Error Occurred. Stopping motor.")
    # To stop the motor, we should set the duty cycle to 0
    motorA.stop()
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 