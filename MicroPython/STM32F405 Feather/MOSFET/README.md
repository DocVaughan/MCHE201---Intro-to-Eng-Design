This script simply to toggles a digital output on/off. In this case, we are using it to control a MOSFET, which is acting like a on/off switch for controlling a 5V, spring-return solenoid. [This article](http://bildr.org/2012/03/rfp30n06le-arduino/) explains the concept in a straighforward way.

The hardware configuration to run this script without any modification is shown below. The ... of the mosfet to pin Y3 of the pyboard...

![pyboard transistor setup](pyboard_breadboard_transistor_LED.png)