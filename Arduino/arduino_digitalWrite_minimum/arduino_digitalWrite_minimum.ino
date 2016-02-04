/*------------------------------------------------------------------------------------
arduino_digitalWrite_minimum.ino

Turns on an LED on for one second, then off for one second, repeatedly.

From: http://arduino.cc/en/Tutorial/Blink
      This example code is in the public domain.

Modified:
  * 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - added our class boilerplate header
    - updated commenting to make consistent with our earlier examples
------------------------------------------------------------------------------------*/
 
// Pin 13 has an LED connected on most Arduino boards, including the RedBoard we have
// Name it LED to make your code easier to read
// Adding the const in front will protect you from accidentally changing its value
const int LED = 13;


// This is always run once when the sketch starts
void setup() {                
  pinMode(LED, OUTPUT);      // initialize the digital pin as an output
}


// This runs immediately after setup, looping indefinitely
void loop() {
  digitalWrite(LED, HIGH);   // turn the LED on
  
  delay(1000);               // wait for 1000ms = 1 second
  
  digitalWrite(LED, LOW);    // turn the LED off
  
  delay(1000);               // wait for 1000ms = 1 second
}
