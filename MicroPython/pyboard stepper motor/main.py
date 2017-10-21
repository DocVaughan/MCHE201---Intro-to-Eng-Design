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
# The motors in the MCHE 201 kits have 200 steps/rev.
#  https://www.adafruit.com/product/324
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

# We also need to import the stepper motor code from the library
import stepper

# Initialize communication with the motor driver
i2c = machine.I2C(scl=machine.Pin('Y9'), sda=machine.Pin('Y10'))

# Now, we can initialize the stepper motor object
steppers = stepper.Steppers(i2c)

# Then, create an instance for the connected stepper motor
# Use index 0 if the motor is connected to M1 & M2
# Use index 1 if the motor is connected to M3 & M4
STEPPER_MOTOR_NUM = 0

stepper0 = steppers.get_stepper(STEPPER_MOTOR_NUM)

# Now, we can control the motor. To make it move one step in SINGLE step mode
# Note that the onestep() function is blocking. Nothing else will run while the
# step is being performed
stepper0.onestep(stepper.FORWARD, stepper.SINGLE)

# We can also move in DOUBLE step mode. This time in reverse
stepper0.onestep(stepper.BACKWARD, stepper.DOUBLE)

# To make the motor move more than one step, we need to repeatedly call
# the one-step function. The motors in the MCHE201 kit have 200 step/rev
# so the for loop below should cause the motor to turn one full revolution
for index in range(200):
    stepper0.onestep(stepper.FORWARD, stepper.SINGLE)

# There is also a MICROSTEP mode is good. Here, we'll move 3200 microsteps
# using a for loop. In microstep mode, each physical step is divided into 16
# microsteps, so this for loop should cause the motor in the MCHE201 kit
# to rotate 1 full revolution. The MICROSTEP mode will also have higher torque,
# at the expense of drawing more current.
for index in range(3200):
    stepper0.onestep(stepper.REVERSE, stepper.MICROSTEP)


