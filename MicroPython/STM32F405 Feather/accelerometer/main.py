###############################################################################
# main.py
#
# Script reading the on-board accelerometer of the pyboard and lighting LEDs
# according to tilt in the Y-direction. In addition, a text-based meter showing 
# the tilt in that direction is printed to the REPL.
#
# The orientation of the axes is:
#
#      Y
#      ^
#      | USB
# +---------+
# |         |
# |         |
# |    Z    | ---> X
# |         |
# |         |
# +---------+
#
#
# Created: 11/17/18
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   *
#
###############################################################################

import pyb
import time

# create the accelerometer instance
accel = pyb.Accel()

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)

# TODO: This should probably be in a try..except 
while True:
    # The raw values are signed integers with values between around -32 and 31,
    # but typical values tend to be between -20 and 20.
    # 
    # On a completely flat surface, the values should be (0, 0, g)
    # print("Raw values are: ({}, {}, {})".
    #       format(accel.x(), accel.y(), accel.z()))

    # The filtered version sums the last 4 values, you can keep a running
    # average by dividing by 4
    filtered = accel.filtered_xyz()
    x_scaled = filtered[0] / 4
    y_scaled = filtered[1] / 4
    z_scaled = filtered[2] / 4
    filtered_scaled = (x_scaled, y_scaled, z_scaled)

    # print("Filtered values are {}\n".format(filtered_scaled))
    
    # Scaled the y value from +/-20 to 0-20
    y_print = round((y_scaled + 20)/2)
    
    # print("y_print = {}".format(y_print))
    
    # Clear the terminal screen so that it looks like just the bar of the 
    # meter is updating
    print("\033[2J\033[;H") 
    
    # Now, print a "meter" showing the tilt
    print("Min         0         Max")
    print(" <", end="") # The end="" part of this statement prevent a new line
    
    for index in range(21):
        if index == y_print:   # At the value of the tilt, print a vertical bar
            print("|", end="")
        else:   
            print("-", end="") # elsewhere, print a dash
    
    print(">")

    # Based on the filtered values of the y-direction accelerometer reading,
    # we'll also light various combinations of LEDs to indicated the degree of 
    # tilt
    #
    # Note: There are more elegant and efficient ways to do this. 
    #       This way is very crude, but easy to understand.
    if y_scaled > 8:   # Full forward, only blue on
        BLUE_LED.on()
        YELLOW_LED.off()
        GREEN_LED.off()
        RED_LED.off()
    elif y_scaled > 6: # Almost full forward, blue and yellow on
        BLUE_LED.on()
        YELLOW_LED.on()
        GREEN_LED.off()
        RED_LED.off()
    elif y_scaled > 4: # Slightly forward, only yellow on
        BLUE_LED.off()
        YELLOW_LED.on()
        GREEN_LED.off()
        RED_LED.off()
    elif y_scaled < -8: # Full backward, only red on
        BLUE_LED.off()
        YELLOW_LED.off()
        GREEN_LED.off()
        RED_LED.on()
    elif y_scaled < -6: # Almost full backward, red and green on
        BLUE_LED.off()
        YELLOW_LED.off()
        GREEN_LED.on()
        RED_LED.on()
    elif y_scaled < -4: # Slightly backward, only green on
        BLUE_LED.off()
        YELLOW_LED.off()
        GREEN_LED.on()
        RED_LED.off()
    else:               # Almost level, no leds on
        BLUE_LED.off()
        YELLOW_LED.off()
        GREEN_LED.off()
        RED_LED.off()

    # Pause 100ms between readings
    pyb.delay(100)