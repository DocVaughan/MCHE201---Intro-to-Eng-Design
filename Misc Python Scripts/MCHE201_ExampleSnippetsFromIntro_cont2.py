## Slide 13
import pyb  # import the pyboard module

# Assign the names to the onboard LEDs
RED_LED = pyb.LED(1)
GREEN_LED = pyb.LED(2)
YELLOW_LED = pyb.LED(3)
BLUE_LED = pyb.LED(4)



## Slide 15
# Assign the 4th LED to variable BLUE_LED
BLUE_LED = pyb.LED(4)

BLUE_LED.on()               # Turn fully on
time.sleep(1)               # Sleep 1 second

BLUE_LED.intensity(128)     # Set to ~1/2 intensity
time.sleep(1)               # Sleep 1 second

BLUE_LED.intensity(64)      # Set to ~1/4 intensity
time.sleep(1)               # Sleep 1 second

BLUE_LED.intensity(1)       # Set to min. intensity
time.sleep(1)               # Sleep 1 second

BLUE_LED.off()              # Turn it off


## Slide 16
# Assign the 4th LED to variable BLUE_LED
BLUE_LED = pyb.LED(4)

print("Turning on LED")
BLUE_LED.on()               # Turn on at full brightness
time.sleep(1)               # Sleep 1 second

print("Setting to 1/2 intensity")
BLUE_LED.intensity(128)     # Set to ~1/2 intensity
time.sleep(1)               # Sleep 1 second

print("Setting to 1/4 intensity")
BLUE_LED.intensity(64)      # Set to ~1/4 intensity
time.sleep(1)               # Sleep 1 second

print("Setting to min. intensity")
BLUE_LED.intensity(1)       # Set to minimum intensity
time.sleep(1)               # Sleep 1 second

print("Turning off LED")
BLUE_LED.off()              # Turn it off


## Slide 22

import pyb      # import the pyboard module
import time     # import the time module

# Assign the Switch object for the onboard button 
# to variable button
button = pyb.Switch()

# The condition for this while is always true, so 
# it runs forever
while (True):
    # button() is True if the button is pressed
    if (button()): 
        print("Button Pressed!")
    
    time.sleep_ms(100) # Sleep 100ms between reading
    
    