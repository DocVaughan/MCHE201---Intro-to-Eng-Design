This simple script to reads the value of a potentiometer every 500ms and print its value to the REPL. The "middle" pin of the potentiometer should be 
connected to Pin Y11 on the pyboard. One of the outer pins should be connected to A3V3 (Pin X23) and the other to AGND (PIN X24), as shown below.

![Potentiometer Hardware Setup](pyboard_breadboard_potentiometer.png)

This script will also work as is with the MCHE201 controller board with the hardware configuration shown in the figure below.

![MCHE201 Controller Board Potentiometer Hardware Setup](MCHE201board_potentiometer.png)