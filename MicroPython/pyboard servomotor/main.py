###############################################################################
# main.py
#
# Script to run a servo motor connected to pin X1
#
# Code adapted from: 
#  http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/servo.html
#
# Created: 10/06/17
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

# Define the servo object. 
# Servo 1 is connected to X1, Servo 2 to X2, Servo 3 to X3, and Servo 2 to X4
# Here, we'll use the first position
servo1 = pyb.Servo(1)

# Now, we can control the angle of the servo
# The range of possible angles is -90 < angle < 90, but many servos can't move
# over that entire range. A safer range is -60 < angle < 60 or even 
# -45 < angle < 45
servo1.angle(45)

# Sleep 1s to let it move to that angle
time.sleep(1)

# Move to -60degrees
servo1.angle(-45)

# Sleep 1s to let it move to that angle
time.sleep(1)

# We can also get the current angle of the servo. Note that this is based
# on the current servo command, not the actual physical angle of the servo
# In many cases, the servo should nearly-exactly track the angle command.
# However, it is possible that the servo does not track the command.
#
# To get the angle, call the .angle() method without an argument
current_angle = servo1.angle()
print("The current servo angle is {:+5.2f} degrees.".format(current_angle))

# Finally, we can also specify how long it should take the servo to move to the 
# commanded angle by adding a second argument to the .angle() call. The 
# argument should be the time to move in milliseconds (1000 = 1s)

# Move to 45 degrees, taking 2seconds to get there
servo1.angle(45, 2000)

# Let's monitor the angle as it moves
current_angle = servo1.angle()

# While we're more than 1 degree away from the target, print the current angle
while ((current_angle-45)**2 > 1.0): 
    current_angle = servo1.angle()
    print("The current servo angle is {:+5.2f} degrees.".format(current_angle))
    time.sleep_ms(100)

current_angle = servo1.angle()
print("Arrived at a final angle of {:+5.2f} degrees.".format(current_angle))
