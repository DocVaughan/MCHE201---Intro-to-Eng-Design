# -----------------------------------------------------------------------------
# main.py
#
# This script includes several ways to print the odd numbers between 1 and 27
# to the MicroPython REPL. It is typically the first example done by students
# in MCHE201: Introduction to Engineering Design
#
# Created: 03/01/18 - Joshua Vaughan - joshua.vaughan@louisiana.edu
#
# Modified:
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
#     - major change 2
#   * mm/dd/yy - Name (email if not same person as above)
#     - major change 1
#
# TODO:
#   * mm/dd/yy - Major bug to fix
#   # mm/dd/yy - Desired new feature
# -----------------------------------------------------------------------------

import pyb  # import the pyboard module
import time # import the time module (remove if not using)

# ----- Method 1 -----
# In this first method, we create a range of 14 numbers, then simply do the 
# math to convert 0-14 -> 1,3,..., 27
for counter in range(14):
    # We could just do this simple math in the print statement. I've left it 
    # outside to hopefully make the algorithm clearer.
    odd_number = 2 * counter + 1 
    
    print(odd_number)


# ----- Method 2 -----
# Here, we'll use a for loop with a properly defined range. Here, we use the 
# extra terms available in the range function. The order is 
#    range(start, stop, increment)
# We have to extend the range past 27 because the last number listed in not
# included in the range.
for counter in range(1, 29, 2):
    print(counter)


# ----- Method 3 -----
# In this method, we'll use a range(27), then use the modulo operator to test 
# for even/odd and print only the odd numbers. The modulo operator returns the 
# remainder from whole-number division of the two numbers. # ----- Method 1 -----
# In this first method, # If the modulo of a number with 2 is zero (meaning it 
# can exactly be divided by 2), it is positive.
for counter in range(29):
    if counter % 2 != 0: # if counter%2 is not 0, then the number is odd
        print(counter)


# ----- Method 4 -----
# Here, we'll use a while loop and increment the counter ourselves. 
# We'll increment it by 2 each time to only get the odd numbers. We could also
# increment by 1 and either do math on counter to create an odd number, as we 
# did in Method 1, or use one an if statement, like we did in Method 3
counter = 1  
while counter <= 27:
    print(counter)
    counter = counter + 2 # Increment by 2 to get to the next odd number


# ----- Method 5 -----
# Python also has a method called list comprehensions. I typically don't teach 
# them in MCHE201, as I think what is happening is tough for a real beginner to 
# follow. But, for operations liek this one, they can be a good tool. They 
# more-or-less allow writing for loops with embedded conditionals in one line.
# For more information, these two articles have a good overview:
#    http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
#    https://dbader.org/blog/list-dict-set-comprehensions-in-python

# Here, ListOfNones would actually be a list of Nones because the list 
# comprehension doens't really *return* anything. It just prints.
ListOfNones = [print(x) for x in range(1,29,2)]  

# We could change it slightly to save a list of the odd numbers, then print 
# that list

oddNumbers = [x for x in range(1,29,2)]
print(oddNumbers)


# ----- Method 6 -----
# Another list comprehension, this time with an included if statement
ListOfNones = [print(x) for x in range(29) if x%2 != 0]


# ----- Method 7 -----
# Another list comprehension, this time using the math like Method 1
ListOfNones = [print(2 * x + 1) for x in range(14)]