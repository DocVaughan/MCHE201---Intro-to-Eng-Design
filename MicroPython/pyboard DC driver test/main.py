# -----------------------------------------------------------------------------
# main.py
#
# script to loop through each output of the motor shield to test functionality
# To test, have motors plugged into each output and/or rotate a motor through 
# the outputs (while powered down, then power up and run)
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
# Created: 11/03/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
# 
# Here, we make a list of motor numbers to iterate over
MOTOR_NUMBERS = [0,1,2,3] 

try:
    for motor_number in MOTOR_NUMBERS:
        print("Testing M{}...".format((motor_number+1)))
        # To control the motor, give it a speed between -4095 and 4095
        print("Forward...")
        motors.speed(motor_number, 2048)    # Go ~1/2 speed in one direction
        time.sleep(1)                       # Continue at this speed for 1s

        # ALWAYS STOP THE MOTOR BEFORE SWITCHING DIRECTIONS!!!!
        # To stop, issue a speed of 0
        print("Stop...")
        motors.speed(motor_number, 0)
        time.sleep(1) # pause briefly to let the motor stop - 1s here

        # To turn the motor in the opposite direction, give a negative speed
        print("Reverse...")
        motors.speed(motor_number, -2048)   # Go ~1/2 speed in the other direction
        time.sleep(1)                       # Continue at this speed for 1s

        # To stop, issue a speed of 0
        print("Stop...")
        motors.speed(motor_number, 0)
        time.sleep_ms(10) # pause briefly to let the motor stop
        
        if motor_number < 3:
            print("Waiting 10 seeconds before moving on to M{}".format((motor_number+2)))
        
            for seconds in range(10):
                print("{}".format(10-seconds))
                time.sleep(1)

finally:
    print("Stopping all motors.")
    for motor_number in MOTOR_NUMBERS:
        motors.speed(motor_number, 0)