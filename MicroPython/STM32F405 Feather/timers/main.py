# main.py -- put your code here!

###############################################################################
# main.py
#
# Script demonstrating using the timers of the pyboard
#
# Most adapted from:
#    http://docs.micropython.org/en/latest/pyboard/tutorial/timer.html
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

# Pause for 1s
pyb.delay(1000)

# Create the timer instance
timer = pyb.Timer(4)

# Set it up to trigger at 10Hz
timer.init(freq=10)

# Create an LED instance and use the timer to toggle the LED on/off
timer.callback(lambda t:pyb.LED(1).toggle())

# Let it run for 5s
pyb.delay(5000)

# To disable to the callback, pass it None
timer.callback(None)

# Pause for 1s
pyb.delay(1000)

# We can set up and use multiple timers - here to toggle two LEDS
timer4 = pyb.Timer(4, freq=10)
timer7 = pyb.Timer(7, freq=20)
timer4.callback(lambda t: pyb.LED(1).toggle())
timer7.callback(lambda t: pyb.LED(2).toggle())

# Let it run for 5s
pyb.delay(5000)

# To disable to the callbacks, pass them None
timer4.callback(None)
timer7.callback(None)

# Pause for 1s
pyb.delay(1000)


# We use timer 2 to create a microsecond counter
micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)

# Set it to zero to start use
micros.counter(0)

# Now we can time something. Let's just time a delay command
start_microTimer = micros.counter()

# Pause 500ms
pyb.delay(500)

end_microTimer = micros.counter()

elapsed_time = end_microTimer - start_microTimer

print('The 500 ms pause took {} microseconds.'.format(elapsed_time))