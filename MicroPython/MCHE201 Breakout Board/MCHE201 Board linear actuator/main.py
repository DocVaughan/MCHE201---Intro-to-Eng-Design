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
# This code requires the .py files from the MCHE201 Controller Board repository
# found at:
#    https://github.com/DocVaughan/MCHE201_Controller
#
# Created:03/26/19 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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

# We'll use the machine i2c implementation.
import machine 

# We also need to import the linear actuator code from the library
import actuator

# Initialize communication with the motor driver
i2c = machine.I2C(scl=machine.Pin("X9"), sda=machine.Pin("X10"))

# And, then initialize the linear actuator control object
linear_actuator = actuator.LinearActuator(i2c)


try:
    # To control the actuator, give it a speed between -100 and 100
    print("Moving at 1/2 speed in one direction")
    linear_actuator.set_speed(50)    # Go ~1/2 speed in one direction
    time.sleep(0.5)                  # Continue at this speed for 0.5s

    # ALWAYS STOP THE actuator BEFORE SWITCHING DIRECTIONS!!!!
    # To stop, issue a speed of 0
    print("Stopping.")
    linear_actuator.set_speed(0)
    time.sleep(1) # pause briefly to let the motor stop - 1s here

    # To move the actuator in the opposite direction, give a negative speed
    print("Moving at 1/2 speed in the other direction")
    linear_actuator.set_speed(-50)      # Go ~1/2 speed in the other direction
    time.sleep(0.5)                       # Continue at this speed for 0.5s

    # To stop, issue a speed of 0
    print("Stopping.")
    linear_actuator.set_speed(0)
    time.sleep(1) # pause briefly to let the motor stop

    # Move the actuator in one direction, ramping up to 1/2 speed
    print("Rampign up to 1/2 speed in one direction.")
    for speed in range(50):
        linear_actuator.set_speed(speed)
        time.sleep_ms(20)

    print("Ramping through to 1/2 speed in the other direction.")
    # Stop the actuator, then move it in the opposite direction, 
    # ramping up to 1/2 speed
    for speed in range(100):
        linear_actuator.set_speed(50 - speed)
        time.sleep_ms(20)
    
    print("Rampign down to zero speed.")
    # Ramp down from 1/2 speed to zero speed
    for speed in range(50):
        linear_actuator.set_speed(-50 + speed)
        time.sleep_ms(20)
    
    # Finally, set the speed to zero
    linear_actuator.set_speed(0)

except:
    print("Some problem occured. Stopping the actuator.")
    linear_actuator.set_speed(0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 