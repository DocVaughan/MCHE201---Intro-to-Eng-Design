/*------------------------------------------------------------------------------------
arduino_031716_DCmotor_LectureExercise2.ino

Make a DC motor run one direction for 2s, pause for 1s, then run the opposite 
direction for 5s and pause for 1s. Repeat this 5 times only.

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

// You can also make another motor on port M2
//Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(2);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps

  AFMS.begin();  // create with the default frequency 1.6KHz
}

void loop() {

  for (int counter = 1; counter <=5; counter ++) {
    String print_string = String("Starting loop number ") + String(counter, DEC);
    Serial.println(print_string);
    
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
    // Delay for 1 seconds
    // Here, the motor will be stopped while the Arduino is "sleeping"
    delay(1000);
  
     Serial.println("Running reverse at full speed...");
    // Set the direction of the motor to BACKWARD
    Motor3->run(BACKWARD);
  
    // Delay for 5 seconds
    // Here, the motor will continue to run while the Arduino is "sleeping"
    delay(5000);
    
    Serial.println("Stopping...\n");
    Motor3->run(RELEASE);
    // Delay for 2 seconds
  
    // Pause 1000ms before repeating the loop
    // The motor will stay off during this delay
    delay(1000);
  }

  Serial.println("Finished looping.");
  
  while(1) {
    delay(100);
  }
}
