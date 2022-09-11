###############################################################################
# main.py
#
# Script to read and print the status of a Wii Nunchuk in MicroPython on 
# the pyboard
#
# It has been tested with:
#  * The Wii Nunchucky adapter - https://www.adafruit.com/product/345
#  * WiiChuck adapter - https://www.dfrobot.com/product-91.html
#
# The hardware connctions between the pyboard and the Wii Nunchucky board are:
# 
#  pyboard    | Nunchucky
#  ---------- | ---------
#  Y9 - scl   | Clk
#  Y10 - sda  | Data
#  3V3        | 3.3V
#  GND        | Gnd
#
# The nunchuck.py file in this folder must be on the pyboard. It is a copy of 
# the one at:
#  https://github.com/kfricke/micropython-nunchuck/
#
# Created: 11/11/17
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

import machine
import time

# We need to import the nunchuk file to use its functions
import nunchuck 

# Set up the i2c communication for the controller
# We slow down the comm. speed with the freq=10000 parameter
i2c_nun = machine.I2C(scl=machine.Pin("Y9"), sda=machine.Pin("Y10"), freq=10000)

# Pass the i2c setup to create an instance of the nunchuk controller
nun = nunchuck.Nunchuck(i2c_nun)

while(True):
    # Read joystick, accelerometer, and button states of the Nunchuk and save
    # the current state in the corresponding variable
    joystick = nun.joystick()
    accel = nun.accelerator()
    button = nun.buttons()

    # printing this should clear the REPL
    # We can fake a screen where only the values update
    print("\033[2J\033[;H") 
    
    # Now, we"ll print out the status of the controller
    print(" Reading a Wii Nunchuk with MicroPython on the pyboard")
    print("-------------------------------------------------------")
    print(" Joystick: X={0: <3} Y={1: <3} \r\n Accel:    X={2: <3} Y={3: <3} Z={4: <3} \r\n Buttons:  C={5:<9} Z={6:<6}".format(
            joystick[0], joystick[1],
            accel[0], accel[1], accel[2],
            str(button[0]), str(button[1])
            ))
    
    # Sleep 100ms between readings
    time.sleep_ms(100)
