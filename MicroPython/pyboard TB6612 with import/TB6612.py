#! /usr/bin/env python

###############################################################################
# 
# Class to handle the basic functionality of running a DC motor with a TB6612
# motor driver. Basic usage is explained in the main.py script in this folder.
#
# Created: 11/01/17
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
#
###############################################################################

import pyb
import time

class motor(object):
    """ Convenience class for controlling a motor

    Arguments
      IN1pin : the IN1 pin
      IN2pin : the IN2 pin
      PWMpin : the PWM pin
      timer_number : number of the timer to use. 
                     Needs to correspond to pin used for the PWM
      channel_number : number of the channel to use on the timer
                       Needs to correspond to pin used for the PWM

    Other atributes
      isRunning : Boolean describing if motor is running or not
      speed : current speed of the motor
      direction : current direction the motor is running
                  =None if the motor is not currently moving
    """
    
    def __init__(self, PWMpin, IN1pin, IN2pin, timer_number, channel_number):
        self.isRunning = False
        self.currentDirection = None
        self.currentSpeed = 0

        # We need to set up two digital outputs that we will use to control the 
        # direction of the motor.
        self.IN1pin = pyb.Pin(IN1pin, pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
        self.IN2pin = pyb.Pin(IN2pin, pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)

        # We also need to set up a third pin to control the speed of the motor. This 
        # output needs to have PWM capabilities, so it should be connected to a pin
        # that has an associated timer on the pyboard
        self.PWMpin = pyb.Pin(PWMpin)
        self.PWM_TIMER = pyb.Timer(timer_number, freq=20000)
        self.ch = self.PWM_TIMER.channel(channel_number, pyb.Timer.PWM, pin=self.PWMpin)


    def set_speed(self, speed):
        """ method to set the speed and direction of a motor
        Arguments:
          speed : speed of the motor -100 to 100 (as percentage of max)
        """
        
        if speed == 0:
            direction = None
            self.stop()
        
        elif speed * self.currentSpeed < 0:
            # if this product is negative, the current speed and desired newSpeed
            # are in different directions. We always want to stop the motor
            # before changing directions, so we raise an error saying so.
            raise ValueError("Motors should be stopped before switching direction")

        # Based on the speed input, select the direction and duty-cycle
        elif speed >= 0 and speed < 100:
            self.IN1pin.value(1)
            self.IN2pin.value(0)
            direction = "Positive"
            self.ch.pulse_width_percent(speed)

        elif speed < 0 and speed > -100:
            self.IN1pin.value(0)
            self.IN2pin.value(1)
            direction = "Negative"
            # negative sign need to correct for negative dir. It maps only to 
            # duty cycle
            self.ch.pulse_width_percent(-speed) 

        else:
            raise ValueError("Please enter speed between -100 and 100")

        # set the status attributes
        self.isRunning = True
        self.currentDirection = direction
        self.currentSpeed = speed

    def stop(self):
        """ redirects to a soft stop """
        self.soft_stop()


    def hard_stop(self):
        """ Method to hard stop an individual motor"""

        self.ch.pulse_width_percent(0)

        # set the status attributes
        self.isRunning = False
        self.currentDirection = None
        self.currentSpeed = 0


    def soft_stop(self):
        """ Method to soft stop (coast to stop) an individual motor"""
        if self.currentSpeed > 0:
            for i in range(self.currentSpeed):
                self.ch.pulse_width_percent(self.currentSpeed-i)
                time.sleep(0.01)
        elif self.currentSpeed < 0:
            for i in range(-self.currentSpeed):
                self.ch.pulse_width_percent(self.currentSpeed+i)
                time.sleep(0.01)
        
        self.ch.pulse_width_percent(0)

        # set the status attributes
        self.isRunning = False
        self.currentDirection = None
        self.currentSpeed = 0.0
