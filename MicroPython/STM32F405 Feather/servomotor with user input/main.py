###############################################################################
# main.py
#
# Script to take a user command on servo angle then, move a servo motor 
# connected to the pyb.Servo(1) pin on the board.
#
# See note in script for what physical pin this corresponds to on the version
# of the pyboard that you have.
#
# Code adapted from: 
#  http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/servo.html
#
# Created: 11/17/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 
#
# TODO:
#   * 
###############################################################################

import pyb  # import the pyboard module
import time # import the time module

# Define the servo object. The numbering scheme differs between the pyboard and
# the pyboard LITE.
# 
# For the pyboard:
#  Servo 1 is connected to X1, Servo 2 to X2, Servo 3 to X3, and Servo 2 to X4
#
# For the pyboard LITE:
#  Servo 1 is connected to X3, Servo 2 to X4, Servo 3 to X1, and Servo 2 to X2

# Here, we'll use the first position on the pyboard
servo1 = pyb.Servo(1)

# Define the minimum and maximum angles that we'll allow motion to
SERVO_MAX_ANGLE = 75
SERVO_MIN_ANGLE = -75

# Now we'll run the main part of the script, which asks the user for an input, 
# processes it, checking its validity, then moves the servo to the resulting
# desired angle.

while(True):
    # Read the potentiometer of the linear actuator, calculate initial length,
    # then print out its value
    current_angle = servo1.angle()
    print("Current Angle:    {:.2d}deg".format(current_angle))

    # Now, we'll ask the user for their input
    print("Enter the desired angle in degrees, then press return.")
    print("The range of allowed angles is {:+d}deg to {:+d}deg.".format(SERVO_MIN_ANGLE, SERVO_MAX_ANGLE))
    desired_angle_input = input()

    # We can us a try...except block to make sure the user actually input a 
    # number. If not, we'll use the current angle as the desired.
    try:
        # convert to an integer
        desired_angle = int(desired_angle_input) 
    except ValueError:
        print("Please enter a valid number.")
        print("Remaining at current angle.")
        desired_angle = current_angle

    # Check that the desired length is within the bounds of the actuator
    if desired_angle > SERVO_MAX_ANGLE:
        desired_angle = SERVO_MAX_ANGLE
        print("The servo cannot move to that angle.")
        print("Moving to maximum angle of {:+2d}deg instead.\n".format(desired_angle))
    elif desired_angle < SERVO_MIN_ANGLE:
        desired_angle = SERVO_MIN_ANGLE
        print("The servo cannot move to that angle.")
        print("Moving to minimum angle of {:+2d}deg instead.\n".format(desired_angle))
    else:
        print("Moving to desired angle of {:+2d}deg.\n".format(desired_angle))

    servo1.angle(desired_angle)

    # sleep 1s to give the servo time to move
    time.sleep(1)