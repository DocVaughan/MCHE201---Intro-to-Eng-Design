Script to read and print the status of a Wii Nunchuk in MicroPython on 
the pyboard.

It has been tested with:
 * [The Wii Nunchucky adapter](https://www.adafruit.com/product/345)
 * [WiiChuck adapter](https://www.dfrobot.com/product-91.html)

The hardware connctions between the pyboard and the Wii Nunchucky board are:

**pyboard**    | **Nunchucky**
-------------- | ---------
Y9 - scl       | Clk
Y10 - sda      | Data
3V3            | 3.3V
GND            | Gnd

The nunchuck.py file in this folder must be on the pyboard. It is a copy of 
the one at:
  https://github.com/kfricke/micropython-nunchuck/
