# -----------------------------------------------------------------------------
# main.py
#
# Simple script demonstrating trial... except concept
#
# Optional Link to relevant documentation
#
# Created: 10/26/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
import time # import the time module

counter = 0 # Set the initial value of the counter

try:
    while (True):
        value = 1 / (10 - counter)

        print("Things are running smoothly...")
        print("Value = {:.4f}\n".format(value))

        # Sleep 1s
        time.sleep(1)
        
        # increment the counter by 1
        counter = counter + 1

# When counter=10, we'll have "ZeroDivisionError: division by zero",
# which this except will "catch"
except:
    print("Not so smooth any more.")
    
# This block will always run, whether the try finishes or if an exception occurs
finally:
    print("Always runs.")