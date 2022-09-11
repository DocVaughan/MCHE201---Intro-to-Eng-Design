###############################################################################
# main.py
#
# Main script to read a quadrature encoder. It just prints the current angle 
# to the REPL.
#
# This script requires the file encoder.py to be on the pyboard as well.
# It is included in the repository along with this example script and based
# on code found at:
#  https://github.com/peterhinch/micropython-samples/blob/master/encoders/encoder_portable.py 
#
# Created: 11/10/18
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

import pyb      
import time     
from encoder import Encoder  # from encoder.py, which must be on the pyboard
# 
# Define the physical counts per revolution of the encoder
ENC_COUNTS_PER_REV = 1024

# Scale by 1/(4 * encoder counts) since it's a quadrature signal
SCALE = 1 / (4 * ENC_COUNTS_PER_REV) 

# Define the encoder pins
# encA = pyb.Pin("X1", pyb.Pin.IN) 
# encB = pyb.Pin("X2", pyb.Pin.IN)

# Then the encoder instance
# quad_enc = Encoder(encA, encB, 0, SCALE)


################################# Encoder Setup ################################
pin_a = pyb.Pin('X1', pyb.Pin.AF_PP, pull=pyb.Pin.PULL_UP, af=pyb.Pin.AF1_TIM2)
pin_b = pyb.Pin('X2', pyb.Pin.AF_PP, pull=pyb.Pin.PULL_UP, af=pyb.Pin.AF1_TIM2)

# The prescaler is ignored. When incrementing, the counter will count up-to
# and including the period value, and then reset to 0.
enc_timer = pyb.Timer(2, prescaler=0, period=65535)

# ENC_AB will increment/decrement on the rising edge of either the A channel or
# the B channel.
enc_channel = enc_timer.channel(1, pyb.Timer.ENC_AB)


# This will loop forever, checking the button every 100ms
while (True):
    # get the encoder position, then convert to degrees
    # What is returned by the encoder.position() methods is the number of 
    # revolutions
#     angle = quad_enc.position * 360 
    angle = enc_timer.counter() #* 360*SCALE 
    
    print("Anglular change since startup: {}".format(angle))
    
    time.sleep_ms(100)          # Sleep 100 milliseconds (0.1s)