###############################################################################
# main.py
#
# This script will control a single DC motor using a Texas Instruments DRV8871 
# motor driver. It should work with all DRV8871 driver breakouts, but has only 
# been tested with the Adafruit one:
#  https://www.adafruit.com/product/3190
#  
#
# Motor driver shec sheet - https://cdn-shop.adafruit.com/product-files/3190/drv8871.pdf
# Adafruit Overview - https://learn.adafruit.com/adafruit-drv8871-brushed-dc-motor-driver-breakout
#
# Created: 11/06/17
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

# We need to set up two digital outputs that we will use to control the 
# direction of the motor. Both outputs need to have PWM capabilities, so both 
# should be connected to a pin that has an associated timer on the pyboard. 
# The pins usd below should work on both the pyboard and pyboard LITE. In this
# case we are using timer 4.
PWM_TIMER = pyb.Timer(4, freq=20000)

IN1_pin = pyb.Pin('X9')
IN1_PWM = PWM_TIMER.channel(1, pyb.Timer.PWM, pin=IN1_pin)

IN2_pin = pyb.Pin('X10')
IN2_PWM = PWM_TIMER.channel(2, pyb.Timer.PWM, pin=IN2_pin)


try:
    # This for loop will run 5 times
    for counter in range(5):
        print("Turning on approx 3/4 speed")

        # To turn the motor in one direction, we need to set IN2 low and 
        # control the speed using PWM on IN 1
        IN2_PWM.pulse_width_percent(0)
    
        # We set the speed by setting the duty cycle of the PWM command
        IN1_PWM.pulse_width_percent(75)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle to 0
        IN1_PWM.pulse_width_percent(0)
        time.sleep_ms(100)         # Sleep briefly to let the motor stop
    
    
        print("Turning on approx 3/4 speed in the other direction")
        # to turn the motor in one direction, A0 should be high and A1 low
        # To turn the motor in the other direction, we need to set IN2 low and 
        # control the speed using PWM on IN2
        IN1_PWM.pulse_width_percent(0)
    
        # We set the speed by setting the duty cycle of the PWM command
        IN2_PWM.pulse_width_percent(75)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle of both IN1 and IN2 to 0
        IN1_PWM.pulse_width_percent(0)
        IN2_PWM.pulse_width_percent(0)
        time.sleep_ms(100)         # Sleep briefly to let the motor stop

except:
    print("Some Error Occurred. Stopping motor.")
    # To stop the motor, we should set the duty cycle to 0
    IN1_PWM.pulse_width_percent(0)
    IN2_PWM.pulse_width_percent(0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 