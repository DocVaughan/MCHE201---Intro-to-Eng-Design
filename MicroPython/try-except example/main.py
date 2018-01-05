# -----------------------------------------------------------------------------
# main.py
#
# Simple script demonstrating trial... except concept
#
# The use here closely mirrors that explained at:
#  https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions
#
# Created: 10/26/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * 11/08/17 - JEV - joshua.vaughan@louisiana.edu
#     - added raise to exception to push through what error caused the problem
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
    
    # If we call raise here, we'll still get the information on why the 
    # exception was raised in the first place. Without this, we do not.
    raise 
    
# This block will always run, whether the try finishes or if an exception occurs
finally:
    print("Always runs.")