###############################################################################
# main.py
#
# This script will control a single DC motor using a TB6612 motor driver board. 
# It should work with all Toshiba TB6612 driver breakouts, but has only been 
# tested with the Adafruit one:
#  https://www.adafruit.com/product/2448
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

# We need to set up two digital outputs that we will use to control the 
# direction of the motor.
A1_pin = pyb.Pin("X8", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
A2_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# We also need to set up a third pin to control the speed of the motor. This 
# output needs to have PWM capabilities, so it should be connected to a pin
# that has an associated timer on the pyboard
PWM_pin = pyb.Pin("X6")
PWM_TIMER = pyb.Timer(2, freq=20000)
PWM_CHANNEL = PWM_TIMER.channel(1, pyb.Timer.PWM, pin=PWM_pin)


try:
    # This for loop will run 5 times
    for counter in range(5):
        print("Turning on approx 1/2 speed")

        # to turn the motor in one direction, A1 should be high and A2 low
        A1_pin.value(1)
        A2_pin.value(0)
    
        # We set the speed by setting the duty cycle of the PWM command
        PWM_CHANNEL.pulse_width_percent(50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle to 0
        PWM_CHANNEL.pulse_width_percent(0)
        time.sleep_ms(100)         # Sleep briefly to let the motor stop
    
    
        print("Turning on approx 1/2 speed in the other direction")
        # to turn the motor in one direction, A0 should be high and A1 low
        A1_pin.value(0)
        A2_pin.value(1)
    
        # We set the speed by setting the duty cycle of the PWM command
        PWM_CHANNEL.pulse_width_percent(50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle to 0
        PWM_CHANNEL.pulse_width_percent(0)
        time.sleep_ms(100)         # Sleep briefly to let the motor stop
finally:
    print("Some Error Occurred. Stopping motor.")
    # To stop the motor, we should set the duty cycle to 0
    PWM_CHANNEL.pulse_width_percent(0)