#! /usr/bin/env python

###############################################################################
# MCHE201_ControlBox.py
#
# Code to control the MCHE201 competition
#  1. Listens for switch to be pressed
#  2. When pressed, closes all 8 relays for 30sec
#
#
# Created: 11/03/15
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 03/31/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#       - updated for Python 3 
#       - Replaced PiFace with Ocean Control USB relays
#
###############################################################################

# import from __future__ for Python 2 people
from __future__ import division, print_function, unicode_literals


import numpy as np
import serial
import time


class oceanControls(object):
    """ Class to wrap the ASCII protocol for controlling the Ocean Controls
    Relay module"""
    
    def __init__(self, port, baudrate = 9600, address = 00):
        self.ser = serial.Serial(port, baudrate, 
                                 bytesize=8, parity='N', 
                                 stopbits=1, timeout=0.1)
        
        self.address = address
        
                                 
    def turnRelayOn(self, relay_number):
        """ Method to turn on an individual relay 
        
        Input arguments:
            relay_number = The relay number to control
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.ser.write('@{:02d} ON {}\r'.format(self.address, relay_number).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
        
    def turnRelayOff(self, relay_number):
        """ Method to turn off an individual relay 
        
        Input arguments:
            relay_number = The relay number to control
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.ser.write('@{:02d} OFF {}\r'.format(self.address, relay_number).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    
    def timedRelayOn(self, relay_number, time_on):
        """ Method to turn on an individual relay for a set time
        
        Input arguments:
            relay_number = The relay number to control
            time_on = the time the relay should remain on (s)
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            # Convert the time input (s) to the number of ms the relay should be on
            time_tenths = int(time_on * 10)
        
            if time_tenths < 1 or time_tenths > 255:
                raise ValueError('The time must be between 0.1s and 25.5s')
            
            if not np.isclose((time_on / 0.1) % 1, 0):
                raise ValueError('The resolution of this command is only 0.1s.\n\
                Please enter a value that is a multiple of 0.1s.')
        
            self.ser.write('@{:02d} TR {} {:03d}\r'.format(self.address, relay_number, time_tenths).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
        
    
    def turnAllOn(self):
        """ Method to turn on all relays 
        
        Input arguments:
            nothing
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        self.ser.write('@{:02d} ON {}\r'.format(self.address, 0).encode('utf-8'))
    
    
    def turnAllOff(self):
        """ Method to turn off all relays 
        
        Input arguments:
            nothing
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        self.ser.write('@{:02d} OFF {}\r'.format(self.address, 0).encode('utf-8'))

    def isDigitalInputOn(self, digital_input_number):
        """ Method that checks the status of an individual digital input 
        
        Input Arugments:
            digital_input_number = The input number to check
        
        Returns:
            Boolean indicating if input is High/On (True) or Low/Ooff (False)
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/16/16
        """
        
        if digital_input_number in [1, 2, 3, 4]:
            self.ser.flushInput()
            # May need to change to below in versions of PySerial >= 3.0
            # self.ser.reset_input_buffer()
        
            self.ser.write('@{:02d} IS {:02d}\r'.format(self.address, digital_input_number).encode('utf-8'))
        
            # TODO: Be more elegant about this
            status_string = self.ser.readlines()[-1]
        
            status = int(status_string.split()[-1])
        
            if status:
                return True
            else:
                return False
        else:
            raise ValueError('Please enter a digital input number between 1 and 4.')
    
    def isRelayOn(self, relay_number):
        """ Method that checks the status of an individual relay 
        
        Input Arugments:
            relay_number = The relay number to control
        
        Returns:
            Boolean indicating if relay is on (True) or off (False)
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            # self.ser.flushInput()
            # May need to change to below in versions of PySerial >= 3.0
            # self.ser.reset_input_buffer()
        
            self.ser.write('@{:02d} RS {:02d}\r'.format(self.address, relay_number).encode('utf-8'))
            
            # TODO: Be more elegant about this
            status_string = self.ser.readlines()[-1]
        
            status = int(status_string.split()[-1])
        
            if status:
                return True
            else:
                return False
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    def printRelayStatus(self, relay_number):
        """ Method to print the status of an individual relay 
        
        Input Arugments:
            relay_number = The relay number to control
        
        Returns:
            nothing
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            if controller.isRelayOn(relay_number):
                print('Relay {} is on.'.format(relay_number))
            else:
                print('Relay {} is off.'.format(relay_number))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    def printDigitalInputStatus(self, digital_input_number):
        """ Method to print the status of an individual digital input 
        
        Input Arugments:
            relay_number = The digital input number to check
        
        Returns:
            nothing
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/16/16
        """
        
        if digital_input_number in [1, 2, 3, 4]:
            if controller.isDigitalInputOn(digital_input_number):
                print('Input {} is High/On.'.format(digital_input_number))
            else:
                print('Input {} is Low/Off.'.format(digital_input_number))
        else:
            raise ValueError('Please enter a digital input number between 1 and 4.')


if __name__ == "__main__":
    
    # Define an instance of the oceanControls class
    controller = oceanControls('/dev/tty.usbserial-AL01H195')
    
    # Now the relationship between the Ocean Controller outputs and the track
    # Define the values for red then increment around the track CW
    # Red - Blue - Black - Yellow
    # Should allow easier changing in the future
    red_relay = 1
    red_LED = 5
    
    blue_relay = red_relay + 1    
    blue_LED = red_LED + 1
    
    black_relay = blue_relay + 1
    black_LED = blue_LED + 1
    
    yellow_relay = black_relay + 1
    yellow_LED = black_LED + 1
    
    # Define the digital input position of the hardware switch
    hardware_start_switch = 4
    
    try:
        while True:
            if controller.isDigitalInputOn(hardware_start_switch):
                # Close all the relays
                controller.turnAllOn()
            
                # Get the current time
                start_time = time.time()
            
                # Keep the relays closed for 30 seconds
                while (time.time() - start_time < 30):
                    time.sleep(0.1)
            
                # Open all the relays
                controller.turnAllOff()
            
            # sleep 0.1s between checks of the start switch
            time.sleep(0.1)

    except(KeyboardInterrupt, SystemExit):
        controller.turnAllOff()
        controller.ser.close()