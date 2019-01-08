This script is one way to solve the 8th in-class exercise from MCHE201 in the fall semester of 2018.

That exercise was given as:
* Connect a pushbutton
* Turn on the green LED
* When the pushbutton is pressed
    - Turn on the red LED
    - Turn off the green LED
* When the button is pressed again
    - Turn off the red LED
    - Turn on the green LED
    - Print the time elapsed between button pressed to the REPL
    
In this version of the solution, we use nested loops check for the status of the button. To prevent multiple readings of the same button press, we have to be careful with the timing. Even with some trial-and-error tuning of the timing in the various `time.sleep_ms()` calls, this solution is *very* fragile to how fast/long the user presses the button for each transition change. There will be a limit, but you could perhaps tune this solution to be more robust by changing the values in the various `time.sleep_ms()` function calls.

The hardware to run this script without modification is shown below. 

![Pushbutton Hardware Setup](pyboard_breadboard_pushButton.png)