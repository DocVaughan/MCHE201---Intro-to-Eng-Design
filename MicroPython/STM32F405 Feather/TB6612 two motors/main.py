###############################################################################
# main.py
#
# This script will control a two DC motors using a TB6612 motor driver board. 
# It should work with all Toshiba TB6612 driver breakouts, but has only been 
# tested with the Adafruit and SparkFun version:
#  * https://www.adafruit.com/product/2448
#  * https://www.sparkfun.com/products/14451
#
# Hardware Connection
# pyboard | TB6612 Breakout 
# ------- | ----------------------------
# X6      | PWMA 
# X7      | AIN2
# X8      | AIN1
# Y4      | PWMB
# Y5      | BIN2
# Y6      | BIN1
# 3V3     | Vcc
# GND     | GND
# -       | STBY to VCC via 10K resistor
#
# Motor driver shec sheet - https://cdn-shop.adafruit.com/datasheets/TB6612FNG_datasheet_en_20121101.pdf
# Adafruit Overview - https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout
# SparkFun Overview - https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide
#
# Created: 03/30/18
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

# We need to set up the digital outputs that we will use to control the 
# direction of the motor.
A1_pin = pyb.Pin("X8", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
A2_pin = pyb.Pin("X7", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
B1_pin = pyb.Pin("Y6", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
B2_pin = pyb.Pin("Y5", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

# We also need to set up a third pin for each motor to control its speed. This 
# output needs to have PWM capabilities, so it should be connected to a pin
# that has an associated timer on the pyboard
PWMA_pin = pyb.Pin("X6")
PWMA_TIMER = pyb.Timer(2, freq=20000)
PWMA_CHANNEL = PWMA_TIMER.channel(1, pyb.Timer.PWM, pin=PWMA_pin)

PWMB_pin = pyb.Pin("Y4")
PWMB_TIMER = pyb.Timer(4, freq=20000)
PWMB_CHANNEL = PWMB_TIMER.channel(4, pyb.Timer.PWM, pin=PWMB_pin)

try:
    # This for loop will run 5 times
    for counter in range(5):
        print("Turning on approx 1/2 speed")

        # to turn the motor in one direction, IN1 should be high and IN2 low
        # Set Motor A
        A1_pin.value(1)
        A2_pin.value(0)
        
        # Set Motor B
        B1_pin.value(1)
        B2_pin.value(0)
    
        # We set the speed by setting the duty cycle of the PWM command
        PWMA_CHANNEL.pulse_width_percent(50)
        PWMB_CHANNEL.pulse_width_percent(50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle to 0
        PWMA_CHANNEL.pulse_width_percent(0)
        PWMB_CHANNEL.pulse_width_percent(0)
        time.sleep_ms(100)         # Sleep briefly to let the motor stop
    
    
        print("Turning on approx 1/2 speed in the other direction")
        # to turn the motor in one direction, A0 should be high and A1 low
        # Set Motor A
        A1_pin.value(0)
        A2_pin.value(1)
        
        # Set Motor B
        B1_pin.value(0)
        B2_pin.value(1)
    
        # We set the speed by setting the duty cycle of the PWM command
        PWMA_CHANNEL.pulse_width_percent(50)
        PWMB_CHANNEL.pulse_width_percent(50)
    
        # Sleep 2 seconds. The motor should keep running
        time.sleep(2)
    
        print("Stopping...")
        # To stop the motor, we should set the duty cycle to 0
        PWMA_CHANNEL.pulse_width_percent(0)
        PWMB_CHANNEL.pulse_width_percent(0)
                
        time.sleep_ms(100)         # Sleep briefly to let the motor stop

except:
    print("\n\nSome Error Occurred. Stopping motors.\n\n")
    # To stop the motor, we should set the duty cycle to 0
    PWMA_CHANNEL.pulse_width_percent(0)
    PWMB_CHANNEL.pulse_width_percent(0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 