#! /usr/bin/env python

###############################################################################
# motor_soft_start_test.py
#
# script to test a simple averaging algorithm for smoothing motor starts and stops
#
# NOTE: Any plotting is set up for output, not viewing on screen.
#       So, it will likely be ugly on screen. The saved PDFs should look
#       better.
#
# Created: 11/11/17
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

import numpy as np
import matplotlib.pyplot as plt



time = np.linspace(0,10,1001)
desired_speed = 100 * np.ones_like(time) * ((time < 1) + (time > 2))
# desired_speed = 2000 + 2000 * np.sin(0.25 * 2 * np.pi * time)
speed = np.zeros_like(time)

last_speed = 0 # The initial speed is 0

# The variable alpha defines how quickly we track changes. A higher value slows
# our response by favoring previous inputs more heavily. Our speed will be:
#  speed = alpha * last_speed + beta * desired_speed
# For the choices below, we should have a rise time to a step input in speed
# of about 20 time steps to reach 90% of the desired value
alpha = 0.9
beta = 1 - alpha

for index, desired in enumerate(desired_speed):
    
        speed[index] = alpha * last_speed + beta * desired
        last_speed = speed[index]
    
#         print("Deired speed:    {}".format(desired_speed))
#         print("Current commadn: {}".format(speed))
#         print("Last speed:      {}".format(last_speed))
        # motors.speed(MOTOR_NUMBER, speed)
    
        # Sleep 100ms (0.1s)
#         time.sleep_ms(100)



# Set the plot size - 3x2 aspect ratio is best
fig = plt.figure(figsize=(6,4))
ax = plt.gca()
plt.subplots_adjust(bottom=0.17, left=0.17, top=0.96, right=0.96)

# Change the axis units font
plt.setp(ax.get_ymajorticklabels(),fontsize=18)
plt.setp(ax.get_xmajorticklabels(),fontsize=18)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Turn on the plot grid and set appropriate linestyle and color
ax.grid(True,linestyle=':', color='0.75')
ax.set_axisbelow(True)

# Define the X and Y axis labels
plt.xlabel('Time (s)', fontsize=22, weight='bold', labelpad=5)
plt.ylabel('Duty Cycle Command', fontsize=22, weight='bold', labelpad=10)
 
plt.plot(time, desired_speed, linewidth=2, linestyle='-', label=r'Desired')
plt.plot(time, speed, linewidth=2, linestyle='--', label=r'Actual')

# uncomment below and set limits if needed
# plt.xlim(0,5)
plt.ylim(0,5000)

# Create the legend, then fix the fontsize
leg = plt.legend(loc='upper right', ncol = 2, fancybox=True)
ltext  = leg.get_texts()
plt.setp(ltext,fontsize=18)

# Adjust the page layout filling the page using the new tight_layout command
plt.tight_layout(pad=0.5)

# save the figure as a high-res pdf in the current folder
# plt.savefig('plot_filename.pdf')

# show the figure
plt.show()