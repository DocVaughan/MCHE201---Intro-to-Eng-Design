# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of a stepper motor using the
# pyboard connected over i2c to a Adafruit Motor Driver Shield
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
#
# Created: 10/20/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
MOTOR_NUMBER = 0 # DC motor M1

try:
    # To control the motor, give it a speed between -4095 and 4095
    motors.speed(MOTOR_NUMBER, 2048)    # Go ~1/2 speed in one direction
    time.sleep(1)                       # Continue at this speed for 1s

    # ALWAYS STOP THE MOTOR BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To turn the motor in the opposite direction, give a negative speed
    motors.speed(MOTOR_NUMBER, -2048)   # Go ~1/2 speed in the other direction
    time.sleep(1)                       # Continue at this speed for 1s

    # To stop, issue a speed of 0
    motors.speed(MOTOR_NUMBER, 0)
    time.sleep_ms(10) # pause briefly to let the motor stop


    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, speed)
        time.sleep_ms(1)

    for speed in range(2048):
        motors.speed(MOTOR_NUMBER, 2048 - speed)
        time.sleep_ms(1)

except:
    motors.speed(MOTOR_NUMBER, 0)