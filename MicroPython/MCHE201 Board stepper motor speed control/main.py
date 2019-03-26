# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate a simple way to vary the speed of a stepper motor 
# using the pyboard connected over i2c to a Adafruit Motor Driver Shield. It
# also demonstrates the different step types.
#
# See the pyboard stepper motor folder in this repository for basic control:
#  https://git.io/vFCw1
#
# This code requires the .py files from the MCHE201 Controller Board repository
# found at:
#  https://github.com/DocVaughan/MCHE201_Controller
#
# For more information on the different step types, see:
#  https://en.wikipedia.org/wiki/Stepper_motor#Phase_current_waveforms
#
# Created: 03/26/19 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
i2c = machine.I2C(scl=machine.Pin("X9"), sda=machine.Pin("X10"))

# Now, we can initialize the stepper motor object
steppers = stepper.Steppers(i2c)

# Then, create an instance for the connected stepper motor
# Use index 0 if the motor is connected to M1 & M2
# Use index 1 if the motor is connected to M3 & M4
STEPPER_MOTOR_NUM = 0
stepper0 = steppers.get_stepper(STEPPER_MOTOR_NUM)

# To make the motor move more than one step, we need to repeatedly call
# the one-step function. 
#
# To control the speed of the rotation, but still use single steps,
# we can insert a short delay into the for loop. This will result in a short
# delay between each step of the motor, slowing its overall rotation. However,
# if we slow the rotation too much, the motion will not be smooth.
#
# The motors in the MCHE201 kit have 200 step/rev, so the for loop below should
# cause the motor to turn one full revolution.
print("Moving 1 revolution forward in SINGLE step mode.")
for index in range(200):
    stepper0.onestep(stepper.FORWARD, stepper.SINGLE)
    
    # Pause 10ms (0.01s) between each step
    # This means the motor will take about 2seconds to make a full revolution.
    time.sleep_ms(10) 


# If we wanted to step up the torque, we can use use DOUBLE step mode. We 
# still insert a short delay into the for loop to tune the speed. In DOUBLE
# step mode, the torque of the motor is increased by energizing two of the 
# motor coils at each step. The cost of this is increased current/energy
# usage.
#
# For the 200 step/rev motors in the MCHE201, 200 steps results in one
# complete revolution of the motor.
print("Moving 1 revolution backward in DOUBLE step mode.")
for index in range(200):
    stepper0.onestep(stepper.BACKWARD, stepper.DOUBLE)

    # Pause 10ms (0.01s) between each step
    time.sleep_ms(10) 


# We can also control the motors in INTERLEAVE mode. This alternates between
# SINGLE and DOUBLE mode from one step to the next. This increases the 
# resolution of the move, but reduces the torque.
#
# For the 200 step/rev motors in the MCHE201, 400 interleaved steps results in 
# one complete revolution of the motor.
print("Moving 1 revolution forward in INTERLEAVE mode.")
start_time = time.ticks_ms()
for index in range(400):
    stepper0.onestep(stepper.FORWARD, stepper.INTERLEAVE)
    
    # Pause 1ms (0.001s) between each step
    time.sleep_ms(1) 


# There is also a MICROSTEP mode. In microstep mode, each physical step is 
# divided into 16 microsteps. This is done by energizing combinations of coils.
# This results in higher torque and smoother motion, at the expense of drawing 
# more current. Because there are more steps per rotation of the motor.
print("Moving 1 revolution backward in MICROSTEP MODE.")
for index in range(3200):
    stepper0.onestep(stepper.BACKWARD, stepper.MICROSTEP)
    
    # Sleep 1ms (0.001s) between steps
    time.sleep_ms(1)
