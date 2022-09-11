This scripts reads the on-board accelerometer of the pyboard. Using the filtered values provided by the y-axis value of `pyb.Accel().filtered_xyz()` method, a combination of LEDs is turned on/off. In addition, a text-based meter showing the tilt in that direction is printed to the REPL.

For more information on the on-board accelerometer of the pyboard, see:
  http://docs.micropython.org/en/latest/pyboard/tutorial/accel.html