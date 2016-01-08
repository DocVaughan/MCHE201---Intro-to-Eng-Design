/*------------------------------------------------------------------------------------
arduino_MotorShieldBasic.ino

Indefinitely cycles motor connected to M3 full speed forward, off, then full speed reverse

For use with the Adafruit Motor Shield v2 
http://www.adafruit.com/products/1438

Adapted from the example code in the Adafruit library

Get the library at: 
https://github.com/ladyada/Adafruit_Motor_Shield_V2_Library/archive/master.zip

Created: 10/23/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu

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
#include "utility/Adafruit_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Select which 'port' M1, M2, M3 or M4. In this case, M3
Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);

// You can also make another motor on port M2
//Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(2);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Adafruit Motorshield v2 - DC Motor test");

  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
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

   Serial.println("Running reverse at full speed...");
  // Set the direction of the motor to BACKWARD
  Motor3->run(BACKWARD);

  // Delay for 2 seconds
  // Here, the motor will continue to run while the Arduino is "sleeping"
  delay(2000);
  
  Serial.println("Stopping...");
  Motor3->run(RELEASE);
  // Delay for 2 seconds

  // Pause 5000ms before repeating the loop
  // The motor will stay off during this delay
  delay(5000);
}
