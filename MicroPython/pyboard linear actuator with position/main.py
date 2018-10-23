# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of the linear actuator using 
# the pyboard connected over i2c to a Adafruit Motor Driver Shield.
#
# The linear actuator actually has a DC motor inside, so we control it 
# using the same commands that we would issue to a DC motor connected to the
# board.
#
# It also a potentiometer that can give us information about the position of 
# the actuator. This script reads the value of the potentiometer, then 
# estimates the length of the actuator from this value.
#
# The linear actuators in the MCHE 201 kits are:
#  https://www.servocity.com/hda4-2
#
# This code requires the .mpy files from the repository linked below to be
# on the pyboard.
#  https://github.com/adafruit/micropython-adafruit-pca9685
#
# For more information see:
#  https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver
#  The circuit on the shield is identical to the Feather board shown in that
#  tutorial.
#
# Created: 10/29/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 11/08/17 - JEV - joshua.vaughan@louisiana.edu
#     - added raise to exception to push through what error caused the problem
#
# TODO:
#   * mm/dd/yy - Major bug to fix
#   # mm/dd/yy - Desired new feature
# -----------------------------------------------------------------------------

import pyb  # import the pyboard module
import time # import the time module (remove if not using)

# We'll use the machine i2c implementation. It's what the Adafruit library expects
import machine 

# We also need to import the DC motor code from the library
import motor

# Initialize communication with the motor driver
i2c = machine.I2C(scl=machine.Pin('Y9'), sda=machine.Pin('Y10'))

# And, then initialize the DC motor control object
motors = motor.DCMotors(i2c)

# Now, we can initialize the DC motor object. The number should match the
# motor number = (number on the motor driver board - 1)
# For example, M1 on the board is motor 0, M2 on the board is motor 1, etc
MOTOR_NUMBER = 0 # M1

# Set up the analog-to-digital converter to read the linear actuator 
# potentiometer that gives us information on its current length
linear_adc = pyb.ADC(pyb.Pin("X21"))

# We'll also define some constants for use in this code
# Change these two values to match those at the limits of your actuator.
ACT_MAX_ADC = 185  # ADC value at actuator maximum length
ACT_MIN_ADC = 4065 # ADC value at actuator minimum length
ACT_MAX_LEN = 3.93 # maximum stroke length (in)
ACT_MIN_LEN = 0.0  # minimum stroke length (in)

# We'll now define a function that will convert a ADC value to actuator length
def calculate_length(adc_value):
    """ 
    This function uses a simple linear interpolation (y=mx+b) to estimate
    the current length of the linear actuator. It assumes a 4-inch stroke, like 
    those used in the MCHE201 kits
    
    Arguments:
      adc_value : the adc value (0-4095) to calculate the length for
      
    Returns:
      length : the calculated length
    """
    
    # calculate the slope and y-intercept for the linear fit
    slope = (ACT_MAX_LEN - ACT_MIN_LEN) / (ACT_MAX_ADC - ACT_MIN_ADC)
    intercept = ACT_MIN_LEN - slope * ACT_MIN_ADC
    
    # Now, calculate the length for the current ADC value
    length = slope * adc_value + intercept
    return length

# Now we'll run the main part of the script, which moves the actuator around,
# while printing out the current ADC value and calculated length
try:
    # Move the actuator in one direction, ramping up to 1/2 speed
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        linear_length = calculate_length(linear_pot)
        print("Length:     {:.2f}in".format(linear_length))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)

    # Stop the actuator, then move it in the opposite direction, 
    # ramping up to 1/2 speed in that direction
    for speed in range(4095):
        motors.speed(MOTOR_NUMBER, 2048 - speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        linear_length = calculate_length(linear_pot)
        print("Length:     {:.2f}in".format(linear_length))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)
        
    # Ramp down from 1/2 speed to zero speed
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, -2048 + speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        linear_length = calculate_length(linear_pot)
        print("Length:     {:.2f}in\n".format(linear_length))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)

except: # If any error occurs, then stop
    print("Some error occured. Stopping.")
    motors.speed(MOTOR_NUMBER, 0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 