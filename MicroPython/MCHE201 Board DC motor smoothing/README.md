This script to demonstrates one method to smoothly start and stop a DC motor using the pyboard connected to the MCHE201 controller board. An Exponential Moving Average (EMA) is used to smooth sudden changes in desired
motor speed.

We set the current speed command `speed` by:

`speed = alpha * last_speed + (1-alpha) * desired_speed`

where `0 < alpha < 1`. For larger values of `alpha` past inputs are valued more, meaning the response is smoothed more aggressively. So, the speed of the response can be tuned by changing alpha. For example, to respond to a step change of speed, reaching 90% of the desired value in `N` time steps, `alpha` can be chosen according to:

` alpha = 1 - 2 / (N+1) `

For more information on the [Exponential Moving Average (EMA) wikipedia page](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average).
 
*Note:* The `alpha` in the Wikipedia entry is actually the `(1-alpha)` term of the formulation shown here.

This code requires the .py files from the [MCHE201 Controller Board repository](https://github.com/DocVaughan/MCHE201_Controller) to be on the pyboard.

![DC Motor Setup](MCHE201Board_DCmotor.png)