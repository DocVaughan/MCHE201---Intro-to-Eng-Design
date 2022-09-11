This script demonstrates the use the timer-based interrupts on the the pyboard.

These provide a way to trigger a command after a set amount of time without requiring a `timer.sleep()`-type function which would prohibit us from doing other things. In this example, we'll just set up a timer to trigger at a fixed interval, then enter a loop printing a counter. The timer is used to trigger a separate print function at a regular interval. The script also demonstrates how to change this interval on the fly.

A similar construct could be used to set a motor after a set amount of time running, etc.

For more information on the timers in MicroPython see:
   http://docs.micropython.org/en/latest/pyboard/tutorial/timer.html
   
For more information on interrupts and interrupt handlers in MicroPython see:
* http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/switch.html#technical-details-of-interrupts
* http://docs.micropython.org/en/latest/pyboard/reference/isr_rules.html#isr-rules
