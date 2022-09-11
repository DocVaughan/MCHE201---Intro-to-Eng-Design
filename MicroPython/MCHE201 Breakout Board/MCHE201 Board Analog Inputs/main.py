###############################################################################
# main.py
#
# Simple script to read the value of all the analog inputs on the MCHE201 
# breakout board. It does this in the simplest way possible, by manually 
# polling the inputs.
#
# Created: 02/27/19
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 
#
# TODO:
#   * 
###############################################################################

import pyb      # import the pyboard module
import time     # import the time module

# Set up the analog-to-digital converter
pot_adc = pyb.ADC(pyb.Pin("Y11"))           # Potentiometer
fsr_adc = pyb.ADC(pyb.Pin("Y12"))           # Force Sensitive Resistor
touch_adc = pyb.ADC(pyb.Pin("X19"))         # Soft Potentiometer
IR_adc = pyb.ADC(pyb.Pin("X20"))            # IR distance sensor
linearAct_adc = pyb.ADC(pyb.Pin("X21"))     # Linear Actuator Potentiometer
flex_adc = pyb.ADC(pyb.Pin("X22"))          # Flex sensor

# We'll also read the internal information of the pyboard
core_adc = pyb.ADCAll(12, 0x70000) # 12 bit resolution, internal channels

# Now read the pot every 500ms, forever
while (True):
    # Read the value of each analog sensors. All should be in the range 0-4095
    pot_value = pot_adc.read()
    fsr_value = fsr_adc.read()
    touch_value = touch_adc.read()
    IR_value = IR_adc.read()
    linearAct_value = linearAct_adc.read()
    flex_value = flex_adc.read()
    
    # We can convert the value to the voltage we are reading. 
    # 0=0V and 4095=3.3V
    pot_voltage = 3.3 / 4095 * pot_value
    fsr_voltage = 3.3 / 4095 * fsr_value
    touch_voltage = 3.3 / 4095 * touch_value
    IR_voltage = 3.3 / 4095 * IR_value
    linearAct_voltage = 3.3 / 4095 * linearAct_value
    flex_voltage = 3.3 / 4095 * flex_value
    
    # print out the values, nicely formatted
    #print("\033[2J\033[;H") # This should clear the terminal, but you may want to remove to use CoolTerm
    print("Sensor                 ADC Value : Voltage")
    print("------                 --------- : -------")
    print("Pontentiometer              {:04d} : {:4.2f}".format(pot_value, pot_voltage))
    print("Force Sens. Resistor        {:04d} : {:4.2f}".format(fsr_value, fsr_voltage))
    print("Soft Pontentiometer         {:04d} : {:4.2f}".format(touch_value, touch_voltage))
    print("IR Sensor                   {:04d} : {:4.2f}".format(IR_value, IR_voltage))
    print("Linear Actuator             {:04d} : {:4.2f}".format(linearAct_value, linearAct_voltage))
    print("Flex Sensor                 {:04d} : {:4.2f}".format(flex_value, flex_voltage))
    print("")

    # read the internal board information
    core_temp = core_adc.read_core_temp()          # read MCU temperature
    core_vbat = core_adc.read_core_vbat()          # read MCU VBAT
    core_vref = core_adc.read_core_vref()          # read MCU VREF
    vref = core_adc.read_vref()                    # read MCU supply voltage
    
    print("Core Properties")
    print("---------------")
    print("Core Temperature:              {:5.2f} C".format(core_temp))
    print("Backup Battery Voltage:        {:5.2f} V".format(core_vbat))
    print("Core Reference Voltage:        {:5.2f} V".format(core_vref))
    print("Reference Voltage:             {:5.2f} V\n\n".format(vref))

    # sleep for 250ms
    time.sleep_ms(250)