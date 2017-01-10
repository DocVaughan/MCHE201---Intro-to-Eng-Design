/*------------------------------------------------------------------------------------
arduino_HW2_Prob1_Fall2016.ino

Reads a flex sensor value every 500ms and print it to the Serial Monitor. 
At the same time, move the servo within its range based on the curvature 
of the flex sensor.

http://arduino.cc/en/Tutorial/ReadAnalogVoltage
https://learn.sparkfun.com/tutorials/flex-sensor-hookup-guide

Code modified from the Circuit 9 code included with the SIK guide.

Created: 10/17/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/

#include <Servo.h> 

// Now, create the servo object and define the pin it's connected to
Servo servo1;
const int SERVO_PIN = 9;

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  // Enable control of a servo on pin SERVO_PIN
  servo1.attach(SERVO_PIN);
}

// the loop routine runs over and over again forever:
void loop() {
  
  // read the input on analog pin 0:
  int flex_value = analogRead(A0);
  
  // Below is copied from SIK Guide Circuit 9, with only variable name changes
  // Because the voltage divider circuit only returns a portion
  // of the 0-1023 range of analogRead(), we'll map() that range
  // to the servo's range of 0 to 180 degrees. The flex sensors
  // we use are usually in the 600-900 range:
  
  int servo_position = map(flex_value, 600, 900, 30, 150);
  servo_position = constrain(servo_position, 30, 150);

  // Now we'll command the servo to move to that position:
  servo1.write(servo_position);
  // End code copied directly from SIK guide
  
  // print out the value calculated from the sensor reading, formatting nicely
  Serial.print("The flex sensor value was ");
  Serial.print(flex_value);
  Serial.println(".");
  Serial.println("");        // Print a blank line to make output easier to read
  
  // Pause 500ms between readings
  delay(500);
}
