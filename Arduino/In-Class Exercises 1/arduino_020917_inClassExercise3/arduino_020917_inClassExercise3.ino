/*------------------------------------------------------------------------------------
arduino_020917_inClassExercise3.ino

Uses a function on an LED on for one second, then off for one second, repeatedly.

From: http://arduino.cc/en/Tutorial/Blink
      This example code is in the public domain.

Created: 02/03/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified: 
  * 02/04/16 - JEV - joshua.vaughan@louisiana.edu
    - made the LED declaration constant
    - updated formatting to match other examples
  * 03/03/17 - JEV - joshua.vaughan@louisiana.edu
    - updated naming to match Spring 2017 assignment
------------------------------------------------------------------------------------*/
 
// Pin 13 has an LED connected on most Arduino boards, including the RedBoard we have
// Name it LED to make your code easier to read
// Adding the const in front will protect you from accidentally changing its value
const int LED = 13;

// This is always run once when the sketch starts
void setup() {                
  pinMode(LED, OUTPUT);     // initialize the digital pin as an output.
}


// This runs immediately after setup, looping indefinitely
void loop() {
  blinkLED();               // Call the blinkLED function
}


void blinkLED() {
  // Blink the LED
  digitalWrite(LED, HIGH);   // turn the LED on
  
  delay(1000);               // wait for 1000ms = 1 second
  
  digitalWrite(LED, LOW);    // turn the LED off
  
  delay(1000);               // wait for 1000ms = 1 second
}
