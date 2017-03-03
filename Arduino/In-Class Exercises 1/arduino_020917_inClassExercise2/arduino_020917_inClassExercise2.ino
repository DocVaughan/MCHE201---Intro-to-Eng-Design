/*------------------------------------------------------------------------------------
arduino_020917_inClassExercise2.ino

The exercise from class session on 02/09/17. It should print the odd numbers between
1 and 27, and Counter = 13 - Bad Luck! when counter is 13

Created: 09/22/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 03/03/17 - JEV - joshua.vaughan@louisiana.edu
    - modified name to match new semester's work
    - better spacing
------------------------------------------------------------------------------------*/

void setup() {
  // put your setup code here, to run once:
  
  // Start the serial monitor with a baudrate of 9600
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  // Loop from 1 to 27, incrementing the counter by 2 each time
  for (int counter = 1; counter <= 27; counter = counter + 2) {
    
    if (counter == 13 ) {
        Serial.println("Counter = 13 - Bad Luck!!");
    }
    else {
        Serial.println(counter);
    }
  }

  // Delay 1000ms (1s) and print an empty line before looping
  delay(1000);
  Serial.println("");
}
