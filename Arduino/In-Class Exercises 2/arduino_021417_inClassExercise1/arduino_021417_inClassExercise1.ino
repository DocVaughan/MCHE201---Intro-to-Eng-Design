
/*------------------------------------------------------------------------------------
arduino_021417_inClassExercise1.ino

Reads the position of a pontentiometer and aligns a servo to the same angle

Created: 9/13/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 03/03/17 - JEV - joshua.vaughan@louisiana.edu
    - updated from MCHE470 version to MCHE201
    - updated naming to Spring 2017 assignment
------------------------------------------------------------------------------------*/

// include the servo libary
#include <Servo.h> 

// create servo object to control a servo
Servo myServo;   

// Pin declarations
const int POTENTIOMETER_PIN = 5;      // the potentiometer is connected to A5 
const int SERVO_PIN = 9;              // the servo is connected to pin 9
                              
// This is always run once when the sketch starts
void setup() {
  // initialize serial communication at 9600 bits per second - for debugging
  Serial.begin(9600);
  
  // Enable control of a servo on pin 3:
  myServo.attach(SERVO_PIN);
}

// the loop routine runs over and over again forever:
void loop() {
  int servoAngle;    // The desired angle of the servo
  
  // read the analog input
  int potValue = analogRead(POTENTIOMETER_PIN);
  
  // Map the potentiomoter output range to the servo angle range
  // The relatively cheap potentiometer in the kit acts strange near 0
  //   the servo will too as a result
  servoAngle= map(potValue, 0, 1023, 30, 150);
  
  // ensure the position is within an acceptable range
  // Here, we limit the servo to between 30 and 150 degrees rotation
  servoAngle = constrain(servoAngle, 30, 150);
  
  // Move the servo to the desired angle
  myServo.write(servoAngle);
  
  // Uncomment for debugging 
  Serial.print("Potentiometer Value: ");   
  Serial.print(potValue);              // print the value of the pot
  Serial.print("  \t");                // prints a tab, for pretty, readable output
  Serial.print("Desired Servo Angle: "); 
  Serial.println(servoAngle);          // print the desired servo angle
}
