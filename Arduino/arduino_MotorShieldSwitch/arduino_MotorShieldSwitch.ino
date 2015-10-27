/*------------------------------------------------------------------------------------
arduino_MotorShieldSwitch.ino

Runs a motor at full speed while a switch is pressed 

For use with the Adafruit Motor Shield v2 
http://www.adafruit.com/products/1438

Adapted from the example code in the Adafruit library

Get the library at: 
https://github.com/ladyada/Adafruit_Motor_Shield_V2_Library/archive/master.zip

Created: 10/27/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu

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

// Select which 'port' M1, M2, M3 or M4. In this case, M3
Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);

// Attach the switch to pin 3 - make it a constant so it can't be changed
const int motor_switch = 3;

void setup() {
  Serial.begin(9600);        // set up Serial library at 9600 bps
  Serial.println("Motor Running via Switch Input");

  AFMS.begin();  // create with the default frequency 1.6KHz
 
  //configure the motor_switch as an input and enable the internal pull-up resistor
  pinMode(motor_switch, INPUT_PULLUP);

  // Set the speed to maximum
  // The speed won't change, so we can define it in setup
  Motor3->setSpeed(255);
  
}


void loop() {    
  // While the button is held down, run the motor
  while(!digitalRead(motor_switch))
  {
      Serial.println("Button Pressed. Running motor...");
      // Set the direction of the motor to FORWARD
      // The direction won't change, so we can define it in setup
      Motor3->run(FORWARD);
      
      // Delay for 10 ms before checking the swtich again
      delay(10);
  }

  // if the button is not pressed, stop the motor
  Motor3->run(RELEASE); // Stop the motor
  
  // Delay for 10 ms before looping and checking the swtich again
  delay(10);
}
