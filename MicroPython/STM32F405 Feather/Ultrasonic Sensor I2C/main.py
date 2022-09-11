# -----------------------------------------------------------------------------
# main.py
#
# script to demonstrate the basic functionality of the a Zio Ultrasonic 
# Distance sensor with the pyboard connected over i2c via the SparkFun Qwiic 
# connector
#
# You may need to check the address of your sensor and change the 
# SENSOR_ADDRESS variable to match. To do so, you can issue the i2c.scan()
# method once you have initialized the i2c communication
#
# The sensor is:
#    https://www.sparkfun.com/products/15171
#
#
# Created: 04/05/19 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
import machine 

# Initialize communication with the sensor
i2c = machine.I2C(scl=machine.Pin("Y9"), sda=machine.Pin("Y10"))

# You can uncomment this block to scan for the i2c address. SENSOR_ADDRESS 
# below should match what it returns
# i2c.scan()

SENSOR_ADDRESS = 24

# This is the command the sensor expects to request a measurement
MEASURE_COMMAND = 0x01 

# Create a data array to hold the results returned
ultrasonic_data = bytearray(2)

while(True):
    # Request a measurement
    i2c.writeto(SENSOR_ADDRESS, bytearray([MEASURE_COMMAND]))

    # Get the two byte response and store it in the data bytearray we defined
    # earlier
    i2c.readfrom_into(SENSOR_ADDRESS, ultrasonic_data)

    print('The high byte was 0x{:02x}, 0b{:08b}'.format(ultrasonic_data[0], ultrasonic_data[0]))
    print('The low byte was 0x{:02x}, 0b{:08b}'.format(ultrasonic_data[1], ultrasonic_data[1]))
    
    # The data comes in two bytes. We byte shift the first we receive and 
    # do a bitwise or to get the distance value as a result
    # The distance returned is in mm
    distance = ultrasonic_data[0]<<8 | ultrasonic_data[1]
    
    print('The resulting distance is {:d}mm\n\n'.format(distance))
    
    time.sleep_ms(200)