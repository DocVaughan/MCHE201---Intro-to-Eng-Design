This is a template script showing how to start a device based on the start signal closing. It assumes that the external digital input connected to pin X6. The internal pull-down resistor is used. In this version, we manually poll the status of the digital input connected to pin X6. 

The hardware configuration is shown below.

![MCHE201 Start Signal Hardware Configuration](pyboard_breadboard_startCables.png)

This script will also work as is with the MCHE201 controller board with the hardware configuration shown in the figure below.

![MCHE201 Controller Board Start Signal Hardware Configuration](MCHE201board_startCables.png)

Alternately, the banana cables from the track can be connected directly to the MCHE201 controller board, as shown below.

![MCHE201 Controller Board Start Signal Hardware Configuration - Option 2](MCHE201board_startCables_Option2.png)