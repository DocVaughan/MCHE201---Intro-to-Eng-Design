# main.py -- put your code here!

#! /usr/bin/env python

###############################################################################
# main.py
#
# Script for basic logging to the micro-SD card
#
# Most adapted from:
#  https://github.com/micropython/micropython/blob/master/examples/accellog.py
#
#  Main edit from the example is using safer "with open..." syntax for the file
#
# Created: 08/07/15
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   *
#
###############################################################################

# log the accelerometer values to a .csv-file on the SD-card

import pyb

accel = pyb.Accel()                                 # create object of accelerometer
blue = pyb.LED(4)                                   # create object of blue LED

blue.on()                                           # turn on blue LED

# open file to write data - /sd/ is the SD-card, /flash/ is the internal memory
with open('/sd/log.csv', 'w') as log:
    log.write('Time (ms),X,Y,Z\n')                      # write heading to file

    start_time = pyb.millis()

    for i in range(100):                                # do 100 times
            t = pyb.elapsed_millis(start_time)          # get time since reset
            x, y, z = accel.filtered_xyz()              # get acceleration data
            log.write('{},{},{},{}\n'.format(t,x,y,z))  # write data to file
            pyb.delay(100)                              # Delay for 100ms

blue.off()                                          # turn off LED
