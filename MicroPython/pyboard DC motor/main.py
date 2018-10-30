# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of a DC motor using the
# pyboard connected over i2c to a Adafruit Motor Driver Shield
#
# This code requires the .mpy files from the Dr. Vaughan's fork of the 
# Adafruit repository to be on the pyboard. Be sure to get the files from the 
# release corresponding to the version of MicroPython that you are using.
#  https://github.com/DocVaughan/micropython-adafruit-pca9685 
#
# For more information see:
#  https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver
#  The circuit on the shield is identical to the Feather board shown in that
#  tutorial.
#
#
# Created: 10/20/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
    # To control the motor, give it a speed between -4095 and 4095
    print("Moving 1/2 speed in one direction.")
    motors.speed(MOTOR_NUMBER, 2048)    # Go ~1/2 speed in one direction
    time.sleep(1)                       # Continue at this speed for 1s

    # ALWAYS STOP THE MOTOR BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    print("Stopping.")
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To turn the motor in the opposite direction, give a negative speed
    print("Moving 1/2 speed in the other direction.")
    motors.speed(MOTOR_NUMBER, -2048)   # Go ~1/2 speed in the other direction
    time.sleep(1)                       # Continue at this speed for 1s

    # To stop, issue a speed of 0
    print("Stopping.")
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep_ms(10) # pause briefly to let the motor stop

    print("Varying speed from 0 to half-speed, then back to zero.")
    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, speed)
        time.sleep_ms(1)

    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, 2048 - speed)
        time.sleep_ms(1)

except:
    print("Error. Stopping motors.")
    motors.speed(MOTOR_NUMBER, 0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 