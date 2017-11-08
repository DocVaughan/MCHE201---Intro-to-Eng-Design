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
# the actuator. This script does not utilize that information.
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
# Created: 10/23/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 11/08/17 - JEV - joshua.vaughan@louisiana.edu
#     - added print statements for REPL status of movements
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
MOTOR_NUMBER = 0 # DC motor M1

try:
    # To control the actuator, give it a speed between -4095 and 4095
    print("Moving at 1/2 speed in one direction")
    motors.speed(MOTOR_NUMBER, 2048)    # Go ~1/2 speed in one direction
    time.sleep(1)                       # Continue at this speed for 1s

    # ALWAYS STOP THE actuator BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    print("Stopping.")
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To move the actuator in the opposite direction, give a negative speed
    print("Moving at 1/2 speed in the other direction")
    motors.speed(MOTOR_NUMBER, -2048)   # Go ~1/2 speed in the other direction
    time.sleep(1)                       # Continue at this speed for 1s

    # To stop, issue a speed of 0
    print("Stopping.")
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep_ms(10) # pause briefly to let the motor stop

    # Move the actuator in one direction, ramping up to 1/2 speed
    print("Rampign up to 1/2 speed in one direction.")
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, speed)
        time.sleep_ms(1)

    print("Ramping throuhg to 1/2 speed in the other direction.")
    # Stop the actuator, then move it in the opposite direction, 
    # ramping up to 1/2 speed
    for speed in range(4095):
        motors.speed(MOTOR_NUMBER, 2048 - speed)
        time.sleep_ms(1)
    
    print("Rampign down to zero speed.")
    # Ramp down from 1/2 speed to zero speed
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, -2048 + speed)
        time.sleep_ms(1)

except:
    print("Some problem occured. Stopping the actuator.")
    motors.speed(MOTOR_NUMBER, 0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raise in the first place. Without this, we do not.
    raise 