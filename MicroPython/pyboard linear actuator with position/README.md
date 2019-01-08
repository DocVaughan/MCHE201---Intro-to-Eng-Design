This script to demonstrates the basic functionality of the linear actuator included in the MCHE201 kit using the pyboard connected over i2c to an Adafruit Motor Driver Shield. It includes an estimate of the actuator length based on its internal potentiometer.

The linear actuator actually has a DC motor inside, so we control it using the same commands that we would issue to a DC motor.

The linear actuator also has a potentiometer that can give us information about the position of the actuator. This script reads its value, then uses it to estimate the length of the actuator based on a simple linear approximation. In other words, we simply fit a straight line between the two ADC values at the extremes of the actuator stroke and assume the ADC value varies linearly with length. The [actuator spec sheet](https://www.servocity.com/hda4-2) states that the potentiometer should vary at a rate of 2.5K/inch. However, this script uses experimentally determined values. You may need to change the values of `ACT_MAX_ADC` and `ACT_MIN_ADC` to reflect those at the maximum and minimum lengths of the actuator.

This code requires the .mpy files from the [Dr. Vaughan's fork of the Adafruit repository](https://github.com/DocVaughan/micropython-adafruit-pca9685) to be on the pyboard. Be sure to get the files from the release corresponding to the version of MicroPython that you are using.
 
For more information see:
https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver

The circuit on the shield is identical to the Feather board shown in that tutorial.

The hardware setup to use this script is shown below.

![Linear Actuator Hardware Setup](pyboard_breadboard_motorShield_linearActuator.png)
