# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of a DC motor using the
# pyboard connected to the MCHE201 Controller board
#
# This code requires the .py files from the MCHE201 Controller Board repository
# found at:
#  https://github.com/DocVaughan/MCHE201_Controller
#
#
# Created: 03/26/19 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 
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
i2c = machine.I2C(scl=machine.Pin("X9"), sda=machine.Pin("X10"))

# And, then initialize the DC motor control object
motors = motor.DCMotors(i2c)

# Now, we can initialize the DC motor object. The number should match the
# motor number on the motor driver board
MOTOR_NUMBER = 1 # DC motor 1

try:
    # To control the motor, give it a speed between -100 and 100
    print("Moving 1/2 speed in one direction.")
    motors.set_speed(MOTOR_NUMBER, 50)    # Go ~1/2 speed in one direction
    time.sleep(1)                       # Continue at this speed for 1s

    # ALWAYS STOP THE MOTOR BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    print("Stopping.")
    motors.set_speed(MOTOR_NUMBER, 0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To turn the motor in the opposite direction, give a negative speed
    print("Moving 1/2 speed in the other direction.")
    motors.set_speed(MOTOR_NUMBER, -50)     # Go ~1/2 speed in the other direction
    time.sleep(1)                       # Continue at this speed for 1s

    # To stop, issue a speed of 0
    print("Stopping.")
    motors.set_speed(MOTOR_NUMBER, 0)
    time.sleep_ms(10) # pause briefly to let the motor stop

    print("Varying speed from 0 to half-speed, then back to zero.")
    for speed in range(50):
        motors.set_speed(MOTOR_NUMBER, speed)
        time.sleep_ms(250)

    for speed in range(50):
        motors.set_speed(MOTOR_NUMBER, 50 - speed)
        time.sleep_ms(250)

except:
    print("Error. Stopping motors.")
    motors.set_speed(MOTOR_NUMBER, 0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 