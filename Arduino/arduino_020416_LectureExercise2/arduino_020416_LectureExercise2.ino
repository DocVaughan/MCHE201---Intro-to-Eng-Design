
/*------------------------------------------------------------------------------------
arduino_020416_LectureExercise2.ino

Reads the status of a switch attached to pin 2 and toogles the state of onboard LED
with each press

This assumes that the pushbutton is wired in an active low configuration.
  For more info, see https://learn.sparkfun.com/tutorials/pull-up-resistors

Created: 02/04/16
  - Joshua Vaughan
  - joshua.vaughan@louisiana.edu
  - http://www.ucs.louisiana.edu/~jev9637/

Modified:
  * 
------------------------------------------------------------------------------------*/

// digital pin 2 has the pushbutton attached to it. 
// It's good practice to assign a name, to make your code easier to read
const int pushButton = 2;    // This is now global in scope

// Pin 13 has an LED connected on most Arduino boards, including the RedBoard we have
// Name it LED to make your code easier to read
// Adding the const in front will protect you from accidentally changing its value
const int LED = 13;

// declare a value to store the state of the pin
// the button only has two states so a boolean is the best choice
boolean buttonState = true; 

// declare a variable that keeps track of the LED state
boolean LEDisOn = false;

// This is always run once when the sketch starts
void setup() {
  // initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  
  // Remember that the digital pins can be in or out, so... 
  // We need to define the digital pin as an INPUT
  pinMode(pushButton, INPUT);

  // Define the pin of the LED as an ouput
  pinMode(LED, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // Now, read the current state of the button
  buttonState = digitalRead(pushButton);

  if (!buttonState) {
      // print out the state of the button
      Serial.println("The button was pressed...");
      
      if (LEDisOn) {
        Serial.println("LED was on. Turning it off.");
        LEDisOn = false;           // Update the variable tracking the LED state
        digitalWrite(LED, LOW);    // Turn the LED off.
      }
      else {
        Serial.println("LED was off. Turning it on.");
        LEDisOn = true;            // Update the variable tracking the LED state
        digitalWrite(LED, HIGH);   // Turn the LED on.
      }
      delay(1000); // delay 1000ms
      
      Serial.println("");          // print a blank line to improve readability
  }

  
  // delay 10ms between reads for stability
  delay(10);        
}
