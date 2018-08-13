#! /usr/bin/env python

###############################################################################
# MCHE201_qualifyingRoundScheduling.py
#
# script to generate combinations of teams for MCHE201 Qualifying round
#
# NOTE: Any plotting is set up for output, not viewing on screen.
#       So, it will likely be ugly on screen. The saved PDFs should look
#       better.
#
# Created: 04/12/18
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

# A Python program to print all combinations 
# of given length with duplicates in input
from itertools import combinations, permutations
 
NUMBER_OF_TEAMS = 19

teams_round1 = [100+i+1 for i in range(19)]
teams_round2 = [200+i+1 for i in range(19)]

teams = teams_round1 + teams_round2

# and length 4
comb = combinations(teams, 4)
 
# Print the obtained combinations
for i in list(comb):
    print(i)