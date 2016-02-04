
/*------------------------------------------------------------------------------------
arduino_Pushbutton_ActiveLow.ino

Reads the status of a switch attached to pin 2 and lights the onbaord LED 
according to its state.

This assumes that the pushbutton is wired in an active low configuration.
  For more info, see https://learn.sparkfun.com/tutorials/pull-up-resistors

From: http://arduino.cc/en/Tutorial/DigitalReadSerial
      This example code is in the public domain.

Modified:
  * 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - added our class boilerplate header
    - updated commenting to make consistent with our earlier examples
  * 02/04/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - Added LED code
    - Made pin definition a const
------------------------------------------------------------------------------------*/

// digital pin 2 has the pushbutton attached to it. 
// It's good practice to assign a name, to make your code easier to read
const int pushButton = 2;    // This is now global in scope

// Pin 13 has an LED connected on most Arduino boards, including the RedBoard we have
// Name it LED to make your code easier to read
// Adding the const in front will protect you from accidentally changing its value
const int LED = 13;

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
  // declare a value to store the state of the pin
  // the button only has two states so a boolean is the best choice
  boolean buttonState = true;    

  // Now, read the current state of the button
  buttonState = digitalRead(pushButton);

  if (buttonState) {
      // print out the state of the button
      Serial.println("The button is not pressed");

      // Turn the LED off. If it is already off this command has no effect
      digitalWrite(LED, LOW);
  }
  else {
      // print out the state of the button
      Serial.println("The button is pressed");

      // Turn the LED off. If it is already on this command has no effect
      digitalWrite(LED, HIGH);
  }

  
  // delay 100ms between reads for stability
  delay(100);        
}
