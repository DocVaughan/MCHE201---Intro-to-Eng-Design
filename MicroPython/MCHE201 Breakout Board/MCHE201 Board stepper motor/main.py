# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of a stepper motor using the
# pyboard connected the MCHE201 controller board
#
# This code requires the .py files from the MCHE201 Controller Board repository
# found at:
#  https://github.com/DocVaughan/MCHE201_Controller
#
# The motors in the MCHE 201 kits have 200 steps/rev.
#  https://www.adafruit.com/product/324
#
# For more information on the different step types, see:
#  https://en.wikipedia.org/wiki/Stepper_motor#Phase_current_waveforms
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

# We'll use the machine i2c implementation.
import machine 

# We also need to import the stepper motor code from the library
import stepper

# Initialize communication with the motor driver
i2c = machine.I2C(scl=machine.Pin("X9"), sda=machine.Pin("X10"))

# Now, we can initialize the stepper motor object
stepper_motor = stepper.StepperMotor(i2c)

# Now, we can control the motor. To make it move one step in SINGLE step mode
# Note that the onestep() function is blocking. Nothing else will run while the
# step is being performed.
# 
# In SINGLE mode, only one coil of the motor is energized at each step. This 
# exactly matches the simple explanation that we walked through in MCHE201
# lecture.
print("Moving one step backward in SINGLE mode")
stepper_motor.onestep(stepper.FORWARD, stepper.SINGLE)

# We can also move in DOUBLE step mode. This time in reverse.
# In DOUBLE step mode, the torque of the motor is increased by energizing two 
# of the motor coils at each step. The cost of this is increased current/energy
# usage.
#
# The section titled "Full-step drive (two phases on)" on the wikipedia page
# has a nice explanation of this mode:
#  https://en.wikipedia.org/wiki/Stepper_motor#Full-step_drive_.28two_phases_on.29
print("Moving one step backward in DOUBLE mode")
stepper_motor.onestep(stepper.BACKWARD, stepper.DOUBLE)

# To make the motor move more than one step, we need to repeatedly call
# the one-step function. The motors in the MCHE201 kit have 200 step/rev
# so the for loop below should cause the motor to turn one full revolution. We
# need to insert a short delay between onestep() function calls to allow the 
# motor time to move.
print("Moving one revolution forward in SINGLE mode")
for index in range(200):
    stepper_motor.onestep(stepper.FORWARD, stepper.SINGLE)

    # Sleep 1ms (0.01s) between steps
    # At this delay, the motor will spin at 30rpm
    time.sleep_ms(10)   
    

# There is also a MICROSTEP mode. In microstep mode, each physical step is 
# divided into 16 microsteps. Here, we'll move 3200 microsteps using a 
# for loop, so this for loop should cause the motor in the MCHE201 kit
# to rotate 1 full revolution. The MICROSTEP mode will also have higher torque
# and smoother motion, at the expense of drawing more current.
print("Moving one revolution backward in MICROSTEP mode")
for index in range(3200):
    stepper_motor.onestep(stepper.BACKWARD, stepper.MICROSTEP)
    
    # Sleep 1ms (0.001s) between steps
    # At this delay, the motor will spin at 18.75rpm
    time.sleep_ms(1)   


