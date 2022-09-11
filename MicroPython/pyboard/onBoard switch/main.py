# main.py -- put your code here!

#! /usr/bin/env python

###############################################################################
# main.py
#
# Script using the on-board switch
#
# Most adapted from:
#    http://docs.micropython.org/en/latest/pyboard/tutorial/switch.html
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

def march_LED():
    """ function increments to the next LED in the sequence
    
    use as a callback from the usr switch being pressed
    """
    global curr_LED
    global last_LED
    
    leds[curr_LED].toggle()
    leds[last_LED].toggle()
    
    last_LED = curr_LED
    curr_LED = (curr_LED + 1) % 4


# use a list comprehension to give us all the on-board LEDs
leds = [pyb.LED(i) for i in range(1,5)]

curr_LED = 1    # LED to turn on at next press of the button
last_LED = 0    # LED to turn off at netxt press of the button

# Turn on LED 1 to start - matching curr_LED and last_LED above
leds[0].toggle()

# define the switch object and point its callback to our march_LED function
usr_switch = pyb.Switch()
usr_switch.callback(march_LED)

while True:
    # loop through a short delay just waiting for the switch callback
    pyb.delay(20)
