This simple script to reads the value of a Force Sensitive Resistor (FSR) every 500ms and print  its value to the REPL. The sensor is connected to Pin Y12 on the pyboard and should have a pull-down resistor of 10K connected to it as well. The other pin of the FSR flex sensor should be connected to 3.3V, as shown in the figure below.

![FSR Hardware Setup](pyboard_breadboard_FSR.png)

This script will also work as is with the MCHE201 controller board with the hardware configuration shown in the figure below.

![MCHE201 Controller Board FSR Hardware Setup](MCHE201board_FSR.png)