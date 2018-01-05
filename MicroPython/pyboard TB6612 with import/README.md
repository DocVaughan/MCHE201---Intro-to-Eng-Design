This simple script demonstrates basic control of a brushed DC motor using a [Toshiba TB6612 motor driver](https://cdn-shop.adafruit.com/datasheets/TB6612FNG_datasheet_en_20121101.pdf). The [Adafruit breakout board](https://www.adafruit.com/product/2448) for this chip is used. In this script, the motor should spin one direction at ~1/2 speed for two seconds, stop briefly, then spin at ~1/2 speed in the opposite direction for two seconds.

This version uses the file `TB6612.py` to establish a class with some convenience functions for controlling a motor. It needs to be copied to the pyboard in order for this to work.

Like we do in this code, always stop the motor before reversing directions.

The standby pin, labeled STBY on the Adafruit breakout needs to be pulled up to VCC (3V3 from the pyboard in this case) via a 10K resistor.

The hardware configuration to run this script without any modification is shown below. The selection of pins in the example should work on both the pyboard and pyboard LITE.

![Single DC Motor Hardware Setup](pyboard_breadboard_TB6612_DCmotor.png)