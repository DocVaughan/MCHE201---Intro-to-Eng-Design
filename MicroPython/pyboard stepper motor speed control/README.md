This script demonstrates basic speed control of a stepper motor using the pyboard connected over i2c to a Adafruit Motor Driver Shield, showing the various step modes available.

For more information on the step modes, and the pros/cons of each, the [wikipedia article on stepper motors](https://en.wikipedia.org/wiki/Stepper_motor#Phase_current_waveforms) provides a good high-level overview.

This code requires the .mpy files from the [Adafruit repository](https://github.com/adafruit/micropython-adafruit-pca9685) to be on the pyboard. If you are running on the pyboard LITE, you will need the `.py` files found within that repository; the `.mpy` files will not work.

For more information see:
https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver

The circuit on the shield is identical to the Feather board shown in that tutorial.

The [motors in the MCHE 201 kits](https://www.adafruit.com/product/324) have 200 steps per revolution.

The hardware configuration to run this script without modification is shown below:

![Stepper Motor Hardware Configuration](pyboard_breadboard_motorShield_stepperMotor.png)
