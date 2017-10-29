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
# the actuator. This script reads the value of the potentiometer, but does
# not do any mapping of is value to the length of the actuator.
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
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
#     - major change 2
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
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
linear_adc = pyb.ADC(pyb.Pin("X22"))

try:
    # To control the actuator, give it a speed between -4095 and 4095
    motors.speed(MOTOR_NUMBER, 2048)    # Go ~1/2 speed in one direction
    time.sleep(1)                       # Continue at this speed for 1s

    # ALWAYS STOP THE actuator BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To move the actuator in the opposite direction, give a negative speed
    motors.speed(MOTOR_NUMBER, -2048)   # Go ~1/2 speed in the other direction
    time.sleep(1)                       # Continue at this speed for 1s

    # To stop, issue a speed of 0
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep_ms(10) # pause briefly to let the motor stop

    # Move the actuator in one direction, ramping up to 1/2 speed
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        # We're not attempting to map this to a length
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)

    # Stop the actuator, then move it in the opposite direction, 
    # ramping up to 1/2 speed in that direction
    for speed in range(4095):
        motors.speed(MOTOR_NUMBER, 2048 - speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        # We're not attempting to map this to a length
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)
        
    # Ramp down from 1/2 speed to zero speed
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, -2048 + speed)
        
        # Read the potentiometer of the linear actuator and print out its value
        # We're not attempting to map this to a length
        linear_pot = linear_adc.read()
        print("Linear ADC: {}".format(linear_pot))
        
        # Sleep 1ms during each loop
        time.sleep_ms(1)

except: # If any error occurs, then stop the motors
    motors.speed(MOTOR_NUMBER, 0)