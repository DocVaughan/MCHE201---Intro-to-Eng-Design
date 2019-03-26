# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate a simple way to determine the actual speed of a 
# stepper motor. To do this, we assume that the stepper is able to properly 
# execute each step. So, we simply time the execution of a known number of 
# steps. Knowing that we have 200 physical steps/rev motors and the type of 
# step command we are using, we can get an estimate of the speed of the motor.
# 
# NOTE: By assuming that the motor can execute every step that we request 
# perfectly, we are not considering the tradeoff between speed and torque *or*
# any other physical properties of the motor in these calculations. We are 
# essentially only looking at the "software speed limit" for the motors. In 
# other words, how quickly can we issue step commands to the motor.
#
#
# See the pyboard stepper motor folder in this repository for basic control:
#  https://git.io/vFCw1
#
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

# We'll first define a start time
start_time = time.ticks_ms()

# Now, we'll move the motor
for index in range(200):
    stepper0.onestep(stepper.FORWARD, stepper.SINGLE)
    
    # Pause 1ms (0.001s) between each step
    # This means the motor will take about 0.2seconds to make a full revolution.
    time.sleep_ms(1) 

# Now that the loop has ended, we get the time again, then compare it to the
# start time. To do so, we use the time.ticks_diff() method as documented at:
#  http://docs.micropython.org/en/v1.9.2/pyboard/library/utime.html#utime.ticks_diff
end_time = time.ticks_ms()
elapsed_time = time.ticks_diff(end_time, start_time)
print('The elapsed time for SINGLE was {}ms.\n'.format(elapsed_time))


# Let's do the same in DOUBLE step mode
print("Moving 1 revolution backward in DOUBLE step mode.")
start_time = time.ticks_ms() # Define a start time
for index in range(200):
    stepper0.onestep(stepper.BACKWARD, stepper.DOUBLE)

    # Pause 1ms (0.01s) between each step
    time.sleep_ms(1) 

# Now that the loop has ended, we get the time again, then compare it to the
# start time. To do so, we use the time.ticks_diff() method as documented at:
#  http://docs.micropython.org/en/v1.9.2/pyboard/library/utime.html#utime.ticks_diff
end_time = time.ticks_ms()
elapsed_time = time.ticks_diff(end_time, start_time)
print('The elapsed time for DOUBLE was {}ms.\n'.format(elapsed_time))

# The result of these two moves with the 1ms delay will be an elapsed time 
# around 400ms. This means that the motor took ~400ms to complete on revolution
# in both modes. However, if the onestep() function took zero time, we should
# be able to move 1 revolution in half that (200 steps * 1ms per step = 200ms).
# This seems to suggest that that one_step() function call takes approximately
# 1ms to execute.
#
# Let's test that by removing the sleep command and measuring the time again.
# Let's do the same in DOUBLE step mode
print("Moving 1 revolution forward in DOUBLE step mode.")
start_time = time.ticks_ms() # Define a start time
for index in range(200):
    stepper0.onestep(stepper.FORWARD, stepper.DOUBLE)

# Now that the loop has ended, we get the time again, then compare it to the
# start time. To do so, we use the time.ticks_diff() method as documented at:
#  http://docs.micropython.org/en/v1.9.2/pyboard/library/utime.html#utime.ticks_diff
end_time = time.ticks_ms()
elapsed_time = time.ticks_diff(end_time, start_time)
print('The elapsed time for DOUBLE without a delay was {}ms.\n'.format(elapsed_time))

# In this case, you should see a move time of approximately 300ms. So, we can't
# really say that that onestep() command takes 1ms after all. This also 
# suggests that the fastest we can move the motor in SINGLE or DOBULE STEP 
# mode is 1 rev/300ms or 3.3 rev/s (~200rpm)

# Let's test that theory by rotating the motor for multiple revolutions and 
# seeing if we can maintain this speed. The for loop below should rotate the 
# motor for 10 revolutions
print("Moving 10 revolutions backward in DOUBLE step mode.")
start_time = time.ticks_ms() # Define a start time
for index in range(10*200):
    stepper0.onestep(stepper.BACKWARD, stepper.DOUBLE)

# Now that the loop has ended, we get the time again, then compare it to the
# start time. To do so, we use the time.ticks_diff() method as documented at:
#  http://docs.micropython.org/en/v1.9.2/pyboard/library/utime.html#utime.ticks_diff
end_time = time.ticks_ms()
elapsed_time = time.ticks_diff(end_time, start_time)
print('The elapsed time for 10 revolutions was {}ms.\n'.format(elapsed_time))

# You should see that the 10 revolutions took approximately 3000ms. This 
# confirms our maximum speed achievable.


# Finally, let's look at MICROSTEP mode. We'll just directly to the 10 
# revolution case to calculate the maximum speed in this mode.
print("Moving 10 revolutions forward in MICROSTEP mode.")
start_time = time.ticks_ms() # Define a start time

for index in range(10 * 3200):
    stepper0.onestep(stepper.FORWARD, stepper.MICROSTEP)

# Now that the loop has ended, we get the time again, then compare it to the
# start time. To do so, we use the time.ticks_diff() method as documented at:
#  http://docs.micropython.org/en/v1.9.2/pyboard/library/utime.html#utime.ticks_diff
end_time = time.ticks_ms()
elapsed_time = time.ticks_diff(end_time, start_time)
print('The elapsed time for 10 MICROSTEP revolutions was {}ms.\n'.format(elapsed_time))


# These 10 revoluations should take approximately 53000ms. This means that each
# revoluation took approximately 5300ms. This suggests that the maximum speed
# the motor can move in MICROSTEP mode is 1 rev/5300 ms or ~0.19 rev/s (~11rpm).