# main.py -- put your code here!

###############################################################################
# main.py
#
# Script controlling the on-board LEDs of the pyboard
#
# Most adapted from:
#    http://docs.micropython.org/en/latest/pyboard/tutorial/leds.html
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

# use a list comprehension to give us all the on-board LEDs
leds = [pyb.LED(i) for i in range(1,5)]

# Loop through toggling each LED on/off 5 times
for _ in range(5):
    for led in leds:
        led.toggle()
        pyb.delay(100)
        led.toggle()

# vary the intensity of the blue LED (only this LED can do this)
intensity = 0
while intensity < 255*5: # complete the cycle 5 times
    intensity = (intensity + 1) % 255
    led.intensity(intensity)
    pyb.delay(20)

