This script demonstrates a simple way to determine the actual speed of a stepper motor. To do this, we assume that the stepper is able to perfectly execute each step. So, we simply time the execution of a known number of steps. Knowing that we have 200 physical steps/rev motors and the type of step command we are using, we can get an estimate of the speed of the motor. The comments within `main.py` explain the method.

***IMPORTANT:*** By assuming that the motor can execute every step that we request perfectly, we are not considering the tradeoff between speed and torque *or* any other physical properties of the motor in these calculations. We are essentially only looking at the "software speed limit" for the motors. In  other words, how quickly can we issue step commands to the motor.

For more information on the step modes, and the pros/cons of each, the [wikipedia article on stepper motors](https://en.wikipedia.org/wiki/Stepper_motor#Phase_current_waveforms) provides a good high-level overview.

This code requires the `.py` files from the [MCHE201 Controller Board repository](https://github.com/DocVaughan/MCHE201_Controller) to be on the pyboard.

The [motors in the MCHE 201 kits](https://www.adafruit.com/product/324) have 200 steps per revolution.

The hardware configuration to run this script without modification is shown below:

![Stepper Motor Hardware Configuration](MCHE201board_stepperMotor.png)
