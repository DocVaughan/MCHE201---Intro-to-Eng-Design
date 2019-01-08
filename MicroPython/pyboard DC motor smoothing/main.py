# -----------------------------------------------------------------------------
# main.py
#
# Script to demonstrate one method to smoothly start and stop a DC motor using
# the pyboard connected over i2c to a Adafruit Motor Driver Shield. An 
# Exponential Moving Average (EMA) is used to smooth sudden changes in desired
# motor speed.
#
# For mor information on the Exponential Moving Average (EMA), see:
#  https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
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
# Created: 11/11/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
# It's what the Adafruit library expects
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

# We'll define a variable to hold a running average of our prior speed commands
last_speed = 0

# Define a start time
start_time = time.ticks_ms() 

# The variable alpha defines how quickly we track changes. A higher value slows
# our response by favoring previous inputs more heavily. Our speed will be:
#
#  speed = alpha * last_speed + beta * desired_speed
#
# For the choices below, we should have a rise time to a step input in speed
# of about 20 time steps to reach 90% of the desired value. (See README.md for 
# a simple explanation on how to choose this value.) In this script, we're 
# looping at approximately 0.01s (due to the sleep command), so we should reach
# 90% of the desired speed in 20*0.01 = 0.2s.
alpha = 0.9
beta = 1 - alpha

try:
    while (True):
        elapsed_time = time.ticks_diff(time.ticks_ms(), start_time)
        
        # If the elapsed time is less than 3 seconds, then the desired duty
        # cycle is 1000/4095
        if (elapsed_time < 3000):
            desired_speed = 1000
        
        # else if the time is less than 6s (In other words, between 3 and 6s),
        # then the desired duty cycle is 2000/4095
        elif (elapsed_time < 6000):
            desired_speed = 2000
        
        # If the elapsed time is both greater than 3s and greater than 6s
        # then the desired duty cycle is 0
        else:
            desired_speed = 0

        # This is a simple implementation of a Exponential Moving Average (EMA)
        # For more information see: 
        #  https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
        speed = alpha * last_speed + beta * desired_speed
        last_speed = speed # Save the current speed for use in the next loop
        
        # printing this should clear the REPL
        # We can fake a screen where only the values update
        # print("\033[2J\033[;H") 
        
        print("\nDesired speed:    {:+6d}".format(desired_speed))
        print("Current command:  {:+6d}".format(int(speed)))
        
        motors.speed(MOTOR_NUMBER, int(speed))
    
        # Sleep 10ms (0.01s)
        time.sleep_ms(10)

except:
    print("Error. Stopping motors.")
    motors.speed(MOTOR_NUMBER, 0)
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 