## STM32F405 Feather, by Adafruit

This folder contains the [MicroPython](https://micropython.org) code, originally written for the [pyboard](https://docs.micropython.org/en/latest/pyboard/quickref.html), ported to work on the [Adafruit STM32F405 Feather](https://www.adafruit.com/product/4382). Most scripts only require updating the pins used, as the pyboard 1.1 and the Feather both using the same chip, the [STM32F405](https://www.st.com/en/microcontrollers-microprocessors/stm32f405-415.html) from STMicroelectronics.

Some scripts were not able to be ported and/or are unique to the Feather, due to different onboard hardware. For example, the Feather only has one traditional LED that is user addressable, while the pyboard has four. It does, however, have a [NeoPixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels) onboard[^1].

[^1]: NeoPixel is Adafruit's nomenclature for "smart" LEDS, and are often WS2812s.


### Updated to STM32F405 Feather?
As the port is ongoing, folders might contain code that has not been ported yet. Please use the list below as a reference for what has. Once all scripts have been updated, this list will be removed from the README.

-[ ] accelerometer    
-[ ] buzzer    
-[ ] core analog readings    
-[ ] default files    
-[ ] digital input - mag swtich    
-[ ] digital input    
-[ ] digital output    
-[ ] DRV8871    
-[x] first script    
-[ ] flex sensor    
-[ ] FSR    
-[ ] IR sensor Distance Calculation    
-[ ] IR sensor with Filtering    
-[ ] IR sensor  
-[ ] LED intensity - Moved to offboard LED
-[ ] LED - multiLED from one GPIO      
-[ ] LED relay    
-[ ] MOSFET      
-[ ] onBoard micro-SD    
-[ ] potentiometer    
-[ ] quadrature encoder    
-[x] RED toggle - Renamed to *RED LED toggle*    
-[ ] servomotor - multiple    
-[ ] servomotor with user input    
-[ ] servomotor    
-[ ] soft potentiometer    
-[ ] SSD1306 Display    
-[ ] start button interrupt    
-[ ] start button template    
-[ ] TB6612 linear actuator    
-[ ] TB6612 two motors    
-[ ] TB6612 with import two motors    
-[ ] TB6612 with import    
-[ ] TB6612    
-[ ] timer interrupts    
-[ ] timers    
-[ ] transistor    
-[ ] try-except example    
-[ ] UART    
-[ ] Ultrasonic Sensor I2C    
-[ ] Wii Nunchuk    
-[ ] WS2812

### Unavailable for STM32F405 Feather
This list contains the scripts that are not able to be run on the Feather, along with the reason why. 

-[ ] LED cycle - only one onboard LED
-[ ] LED Knight Rider - only one onboard LED
-[ ] onBoard accel - no onboard accelerometer
-[ ] onboard button  - no onboard button (except reset)
-[ ] onBoard LEDs - only one onboard LED
-[ ] onBoard switch - no onboard button (except reset)

### Added for STM32F405 Feather?
This list of scripts are available only on this port.

-[ ] 