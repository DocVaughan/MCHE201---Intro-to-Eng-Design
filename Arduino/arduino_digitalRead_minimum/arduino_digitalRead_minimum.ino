
/*------------------------------------------------------------------------------------
arduino_digitalRead_minimum.ino

Reads the status of a switch attached to pin 2

From: http://arduino.cc/en/Tutorial/DigitalReadSerial
      This example code is in the public domain.

Modified:
  * 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - added our class boilerplate header
    - updated commenting to make consistent with our earlier examples
------------------------------------------------------------------------------------*/

// digital pin 2 has a pushbutton attached to it. 
// It's good practice to assign a name, to make your code easier to read
int pushButton = 2;    // This is now global in scope

// This is always run once when the sketch starts
void setup() {
  // initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  
  // Remember that the digital pins can be in or out, so... 
  // We need to definte the digital pin as an INPUT
  pinMode(pushButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the value of the pin
  int buttonState = digitalRead(pushButton);
  
  // print out the state of the button
  Serial.println(buttonState);
  
  delay(1);        // delay 1ms between reads for stability
}
