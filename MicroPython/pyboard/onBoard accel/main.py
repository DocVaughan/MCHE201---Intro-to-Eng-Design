###############################################################################
# main.py
#
# Script reading the on-board accelerometer of the pyboard
#
# Most adapted from:
#    http://docs.micropython.org/en/latest/pyboard/tutorial/accel.html
#    http://test-ergun.readthedocs.org/en/latest/library/pyb.Accel.html
#
# Created: 08/07/15
#   - Joshua Vaughan
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   *
#
###############################################################################

# The orientation of the axes is:
#
#      Y
#      ^
#      | USB
# +---------+
# |         |
# |         |
# |    Z    | ---> X
# |         |
# |         |
# +---------+
# 
# Keep in mind that these mems-type accelerometers can also measure "tilt"


# create the accelerometer instance
accel = pyb.Accel()

# TODO: This should probably be in a try..except 
while True:
    # The raw values are signed integers with values between around -32 and 31
    # On a completely flat surface, the values should be (0, 0, g)
    print('Raw values are: ({}, {}, {})'.
           format(accel.x(), accel.y(), accel.z()))

    # The filtered version sums the last 4 values, you can keep a running
    # average by dividing by 4
    filtered = accel.filtered_xyz()
    x_scaled = filtered[0] / 4
    y_scaled = filtered[1] / 4
    z_scaled = filtered[2] / 4
    filtered_scaled = (x_scaled, y_scaled, z_scaled)

    print('Filtered values are {}'.format(filtered_scaled))

    # There is also a tilt reading. For what is measures, see p15 of:
    #   http://micropython.org/resources/datasheets/MMA7660FC.pdf
    print('Tilt is {0:#010b}\n'.format(accel.tilt()))

    # Pause 100ms between readings
    pyb.delay(100)