# SLIDE 38
a = 2 # Define the value of a

if (a > 5):
    print("Tell me something, girl")

elif (a == 2):
    print("Are you happy in this modern world")

else:
    print("Or do you need more?")


# SLIDE 39
a = 2 # Define the value of a
b = 3 # Define the value of b

if (a + b > 5):
    print("Kiki, do you love me?")

elif (b - a == 2):
    print("Are you riding?")

else:
    print("Say you'll never ever leave...")


# SLIDE 40
sensedStartSignal = True # Start was sensed

if (sensedStartSignal):
    print("Sensed start signal. Starting robot.")
    # Code to run once the start signal was sensed 

else:
    print("Checking start signal...")
    # Code to check the start signal


# SLIDE 42
list_of_pies = ["apple", "cherry", "pumpkin"]

for pie in list_of_pies:
    print("I think {} pies are delicious!".format(pie))


# SLIDE 43
list_of_pies = ["apple", "cherry", "pumpkin"]

for index, pie in enumerate(list_of_pies):
    print("The number {:d} pie in the list is {}.".format(index, pie))


# SLIDE 45
# ----- while loop example ---------------------
index = 0

while (index < 10):
    print("Index = {:d}".format(index))
    index = index + 2


# SLIDE 46
# ----- while loop example ---------------------
index = 0

while (index < 10):
    if (index == 3):
        print("Index = {:d}".format(index))

    index = index + 1


# SLIDE 47
# ----- while loop example -----------------------
keepRunning = True
index = 0

while(keepRunning):
    print("Running.")

    if (index >= 10):
        keepRunning = False

    time.sleep(.1) # sleep 100ms

    index = index + 1

print("Stopped.")