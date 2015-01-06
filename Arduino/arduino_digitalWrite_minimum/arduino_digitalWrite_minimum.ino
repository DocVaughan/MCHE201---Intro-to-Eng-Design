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
// name it led to make your code easier to read
int led = 13;

// This is always run once when the sketch starts
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// This runs immediately after setup, looping indefinitely
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  
  delay(1000);               // wait for a second
  
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  
  delay(1000);               // wait for a second
}
