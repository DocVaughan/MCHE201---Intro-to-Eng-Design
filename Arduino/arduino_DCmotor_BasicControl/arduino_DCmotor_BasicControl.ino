/*------------------------------------------------------------------------------------
arduino_DCmotor_BasicControl.ino

Makes a DC motor run for 2s, pause for 2s, run for 2s, pause for 2s, ...

For use with the Adafruit Motor Shield v2 
http://www.adafruit.com/products/1438

Adapted from the example code in the Adafruit library

Get the library at: 
https://github.com/ladyada/Adafruit_Motor_Shield_V2_Library/archive/master.zip

Created: 03/17/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * mm/dd/yy - Name (email if not same person as above)
    - major change 1
    - major change 2
  * mm/dd/yy - Name (email if not same person as above)
    - major change 1
------------------------------------------------------------------------------------*/

// Include the necessary libraries for the motor shield
// You should include all three below anytime you're using the motor-driver shield
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Select which 'port' M1, M2, M3 or M4. In this case, M3
Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps

  AFMS.begin();  // create with the default frequency 1.6KHz
}

void loop() {
  // Set the speed to maximum
  Motor3->setSpeed(255);
  
  Serial.println("Running forward at full speed...");
  // Set the direction of the motor to FORWARD
  Motor3->run(FORWARD);

  // Delay for 2 seconds
  // Here, the motor will continue to run while the Arduino is "sleeping"
  delay(2000);

  // Always stop before switch directions
  Serial.println("Stopping...");
  Motor3->run(RELEASE); // Stop the motor
  // Delay for 2 seconds
  // Here, the motor will be stopped while the Arduino is "sleeping"
  delay(2000);
}
