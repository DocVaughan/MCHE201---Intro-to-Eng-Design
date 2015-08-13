/*------------------------------------------------------------------------------------
arduino_digitalWrite_functionBased.ino

Uses function on an LED on for one second, then off for one second, repeatedly.

From: http://arduino.cc/en/Tutorial/Blink
      This example code is in the public domain.

Created: 02/03/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu
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
  blink_LED();
}


void blink_LED(){
  // Blink the LED
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  
  delay(1000);               // wait for a second
  
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  
  delay(1000);               // wait for a second
}
