This script is one way to solve the 11th in-class exercise from MCHE201 in the 
spring semester of 2018. 

That exercise was given as:
* Connect:
    - the IR sensor 
    - a pushbutton
* Wait for the pushbutton to be pressed
* Once it is pressed:
    - Read the IR sensor every 100ms for 30 seconds
    - Print its value to the REPL
    - If objects are closer than 6 inches, turn on the RED LED
    - Otherwise, turn on the Green LED
* After 30 seconds, turn off all the LEDs
 


The hardware configuration to run this script without modification is shown below.

![IR Sensor Hardware Setup](pyboard_breadboard_IRsensor.png)

The sensor in the MCHE201 kit is a Sharp GP2Y0A41SK_E. It is designed to sense objects between 4 and 30cm, and outputs approximately 3.1V at 4cm and 0.3V at 30cm.
 
There is a nonlinear relationship between these values, which is given in the [Sensor datasheet](http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a41sk_e.pdf). The 
[Sensor Application Note](http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/gp2y0a_gp2y0d_series_appl_e.pdf) has additional information, as well.

