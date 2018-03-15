This script is one way to solve the 11th in-class exercise from MCHE201 in the 
spring semester of 2018. 

That exercise was given as:


This simple script to reads the value of an IR sensor every 500ms and prints 
its value to the REPL. The yellow cable from the sensor should be connected 
to Pin X22 on the pyboard, as shown below.

![IR Sensor Hardware Setup](pyboard_breadboard_IRsensor.png)

The sensor in the MCHE201 kit is a Sharp GP2Y0A41SK_E. It is designed to sense objects between 4 and 30cm, and outputs approximately 3.1V at 4cm and 0.3V at 30cm.
 
There is a nonlinear relationship between these values, which is given in the [Sensor datasheet](http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a41sk_e.pdf). The 
[Sensor Application Note](http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a_gp2y0d_series_appl_e.pdf) has additional information, as well.

