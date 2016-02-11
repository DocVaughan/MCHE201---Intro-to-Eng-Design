/*------------------------------------------------------------------------------------
arduino_analogWrite_minimum.ino

Basic setup for analog writing. It acutally uses PWM.

From: http://arduino.cc/en/Reference/AnalogWrite
      This example code is in the public domain.

Modified:
  * 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - added our class boilerplate header
    - updated commenting to make consistent with our earlier examples
  * 02/11/16 - Joshua Vaughan - ulamil
    - updated commenting
    - renamed variables for consistency with other examples
------------------------------------------------------------------------------------*/

// Assume Pin 9 has an LED connected 
// name it led to make your code easier to read
const int LED_PIN = 5;      // an LED connected to digital pin 5


// This is always run once when the sketch starts
void setup()
{
  pinMode(LED_PIN, OUTPUT);   // sets the pin as output
}


// This runs immediately after setup, looping indefinitely
void loop()
{
  byte duty_cycle = 15;            // the duty cycle, between 0-255 (0-100%)

  // analogWrite duty_cycle values from 0 to 255 correspond to duty cycles 0-100%
  analogWrite(LED_PIN, duty_cycle);  
}
