/*------------------------------------------------------------------------------------
arduino_stepperBasic.ino

Demonstrate basic use of a stepper motor using the Adafruit Motor Shield v2 
http://www.adafruit.com/products/1438 

Currently set up for using a motor connected to M3 and M4.

Adapted from the example code in the Adafruit library

Get the library at: 
https://github.com/ladyada/Adafruit_Motor_Shield_V2_Library/archive/master.zip

or use the Manage Libraries functionality in the Arduino IDE

Created: 03/02/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * mm/dd/yy - Name (email if not same person as above)
    - major change 1
    - major change 2
------------------------------------------------------------------------------------*/

// Include the necessary libraries for the motor shield
// Include all three below anytime you're using the motor-driver shield
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Specify the steps/rev and select which port the stepper is connected to
// if M1 & M2 = 1, if M3 & M4 = 2
Adafruit_StepperMotor *stepper1 = AFMS.getStepper(200, 2);

void setup() {
 // set up Serial library at 9600 bps
  Serial.begin(9600);          

 // create with the default frequency 1.6KHz
 AFMS.begin();

// Set the motor speed, the argument is rpm
stepper1->setSpeed(10);
}


void loop() {
  Serial.println("Single coil steps");
  stepper1->step(100, FORWARD, SINGLE); 
  stepper1->step(100, BACKWARD, SINGLE); 

  Serial.println("Double coil steps");
  stepper1->step(100, FORWARD, DOUBLE); 
  stepper1->step(100, BACKWARD, DOUBLE);
  
  Serial.println("Interleave coil steps");
  stepper1->step(100, FORWARD, INTERLEAVE); 
  stepper1->step(100, BACKWARD, INTERLEAVE); 
  
  Serial.println("Microstep steps");
  stepper1->step(50, FORWARD, MICROSTEP); 
  stepper1->step(50, BACKWARD, MICROSTEP);
}

