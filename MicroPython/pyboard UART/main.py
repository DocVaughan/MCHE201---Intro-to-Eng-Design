# -----------------------------------------------------------------------------
# main.py
#
# This script demonstrates functionality of reading information over serial. 
# We're using the same serial port as the REPL, so normal connection should 
# just work
#
# pyboard/MicroPython UART:
#  http://docs.micropython.org/en/latest/pyboard/library/pyb.UART.html
#
# Created: mm/dd/yy - Name - email@louisiana.edu
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

# Insert code here

# UART 1 is the one connected to the REPL
uart = pyb.UART(1, 115200)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1, timeout=1000) # init with given parameters



while (True):
    # To wait for a user input, we use the input() command. Its use matches
    # the full Python implementation: 
    #  http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
    user_input = input("Enter a number, then press return.\n")
    
    # The return will be string, so we need to conver to a number. We can use
    # that conversion to check that a number was actually entered
    try:
        user_number = int(user_input)
        print("You entered: {}\n\n".format(user_input))

    # We'll get a ValueError if the input can't be converted to an integer
    except ValueError: 
        print("Please enter a number.\n\n")
