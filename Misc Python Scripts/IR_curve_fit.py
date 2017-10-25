#! /usr/bin/env python

###############################################################################
# IR_curve_fit.py
#
# Script to calculate the relationship between distance and analog output voltage for a Sharp gp2y0a41sk_e IR sensor
#
# NOTE: Any plotting is set up for output, not viewing on screen.
#       So, it will likely be ugly on screen. The saved PDFs should look
#       better.
#
# Created: 10/25/17
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

# For curve fit
import scipy.optimize as optimize


distance = np.array([4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40])
voltage = np.array([2.75, 2.35, 2, 1.75, 1.55, 1.4, 1.25, 1.05, 0.95, 0.8, 0.75, 0.65, 0.55, 0.42, 0.375, 0.35])


# Now, we'll try to fit a curve to the data
def fit_function(t, a, b, c):
    # the data looks like an exponential
    return a * np.exp(-b * t) + c

fitParams, fitCovariances = optimize.curve_fit(fit_function, voltage, distance)

curve = fit_function(voltage, fitParams[0], fitParams[1], fitParams[2])

curve_eq_text = 'Distance = {:.4f} exp(-{:.4f} Voltage) + {:.4f}'.format(fitParams[0], fitParams[1], fitParams[2])

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
plt.xlabel('Analog Output (V)', fontsize=22, weight='bold', labelpad=5)
plt.ylabel('Distance (cm)', fontsize=22, weight='bold', labelpad=10)
 
plt.plot(voltage, distance, linewidth=2, linestyle='', marker='d', label=r'Data')
plt.plot(voltage, curve, linewidth=2, linestyle='-', label=r'Fit')

plt.text(1.0, 0.67,
         curve_eq_text,
         fontsize=14,
         horizontalalignment='right',
         verticalalignment='center',
         transform=ax.transAxes)

# uncomment below and set limits if needed
# plt.xlim(0,40)
# plt.ylim(0,3.2)

# Create the legend, then fix the fontsize
leg = plt.legend(loc='upper right', ncol = 1, fancybox=True)
ltext  = leg.get_texts()
plt.setp(ltext,fontsize=18)

# Adjust the page layout filling the page using the new tight_layout command
plt.tight_layout(pad=0.5)

# save the figure as a high-res pdf in the current folder
plt.savefig('IRsensor_curveFit.pdf')

# show the figure
plt.show()