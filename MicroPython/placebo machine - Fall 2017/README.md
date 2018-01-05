This is the code for the "Placebo" machine for the [fall 2017 MCHE 201 final
contest](http://www.ucs.louisiana.edu/~jev9637/MCHE201_StarWars.html).

The machine just releases two tennis balls onto the track once the start signal is sensed. Hobby-style servos are used as the release mechanism for the tennis balls, which are placed on two short ramps. As written, it is set up for the pyboard LITE servo pin assignments. See the comments in the script for changes necessary for the pyboard.


More information on external interrupts in MicroPython can be found at:

http://docs.micropython.org/en/latest/pyboard/library/pyb.ExtInt.html?highlight=interrupt

The hardware configuration is shown below.

![MCHE201 Fall 2017 Placebo Machine](placebo_Fall2017.png)
