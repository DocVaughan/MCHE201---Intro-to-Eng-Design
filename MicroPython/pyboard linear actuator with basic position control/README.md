***NOTE: As of 10/28/17, this script is not complete.***
Script to demonstrate the using the potentiometer of the linear actuator in a feedback controller on its length. We use a simple on/off controller based on a deadzone around the desired length. The pyboard connected over i2c to a Adafruit Motor Driver Shield. 

The linear actuator actually has a DC motor inside, so we control it using the same commands that we would issue to a DC motor connected to the board. It also a potentiometer that can give us information about the position of the actuator. Its value will be near Vcc (3.3VDC in this case) when fully retracted and near 0VDC when fully extended. You should test your linear actuator to determine the ADC values corresponding to its limits. They will vary slightly, so you may need to change the values of `ACT_MAX_ADC` and `ACT_MIN_ADC` to reflect those at the maximum and minimum lengths of the actuator you have. 

This script reads the value of the potentiometer, then uses a mapping of its value to the actuator length to determine the current position of the actuator. This value is then used to generate the command to drive the actuator to a desired length. The command represents a simple on/off controller. If the actuator is outside a tolerable range around the desired length, it is moved at ~1/2 speed in the direction needed. Once within that tolerable range of length, it is stopped.

This code requires the .mpy files from the [Adafruit repository](https://github.com/adafruit/micropython-adafruit-pca9685) to be on the pyboard.
 
For more information see:
https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver

The circuit on the shield is identical to the Feather board shown in that tutorial.

The hardware setup to use this script is shown below.

![Linear Actuator Hardware Setup](pyboard_breadboard_motorShield_linearActuator.png)
