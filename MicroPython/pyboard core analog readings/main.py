###############################################################################
# main.py
#
# simple script to read the value of all the  the ADCall information on the 
# pyboard
# 
# See:
#   https://docs.micropython.org/en/latest/library/pyb.ADC.html#the-adcall-object
#
# Created: 04/03/19
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

# We'll also read the internal information of the pyboard
core_adc = pyb.ADCAll(12, 0x70000) # 12 bit resolution, internal channels

# Now read the pot every 250ms, forever
while (True):
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
    print("Reference Voltage:             {:5.2f} V".format(vref))

    # sleep for 250ms
    time.sleep_ms(250)