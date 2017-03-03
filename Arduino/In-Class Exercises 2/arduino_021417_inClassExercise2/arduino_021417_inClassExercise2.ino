
/*------------------------------------------------------------------------------------
arduino_021417_inClassExercise2.ino

Wire three pushbutton switches. Control the servo based on the state of the switches. 
Starting at 30deg., each button pressed adds 30 degrees to the current servo position. 
In other words, holding down 1 button moves the servo to 60deg, holding down any 2 
buttons moves the servo to 90deg, and holding down all three rotates the servo 120deg.

Note: This code assumes that the buttons are wired as active low, as outlined in the 
      SIK guide Circuit 5

Created: 03/03/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/

// include the servo libary
#include <Servo.h> 

// create servo object to control a servo
Servo myServo;   

// Pin declarations
const int BUTTON1_PIN = 2;          // pushbutton connected to pin 2
const int BUTTON2_PIN = 3;          // pushbutton connected to pin 3
const int BUTTON3_PIN = 4;          // pushbutton connected to pin 4   
const int SERVO_PIN = 9;            // the servo is connected to pin 9
                              
// This is always run once when the sketch starts
void setup() {
  // initialize serial communication at 9600 bits per second - for debugging
  Serial.begin(9600);

  // Set up the pushbuttons as inputs
  pinMode(BUTTON1_PIN, INPUT);
  pinMode(BUTTON2_PIN, INPUT);
  pinMode(BUTTON3_PIN, INPUT);
  
  // Enable control of a servo:
  myServo.attach(SERVO_PIN);
}

// the loop routine runs over and over again forever:
void loop() {

  // Read the state of 3 pushbuttons. Because the buttons are wired as active low, 
  // these values will be 1 if the button is *not* pushed and 0 if it is pressed.
  int button1_state = digitalRead(BUTTON1_PIN);
  int button2_state = digitalRead(BUTTON2_PIN);
  int button3_state = digitalRead(BUTTON3_PIN);

  // Keep track of the number of buttons pressed
  int numberButtonsPressed = 3 - (button1_state + button2_state + button3_state);

  // Solve for the servo angle based on the number of buttons pressed
  // We want to start at 30deg and move 30deg for each button pressed
  int servoAngle = 30 + 30 * numberButtonsPressed;
  
  // ensure the position is within an acceptable range
  // Here, we limit the servo to between 30 and 150 degrees rotation
  // It's generally a good idea to manually cehck and contrain variables that could  
  // cause damage if they are outside of an acceptable range. 
  servoAngle = constrain(servoAngle, 30, 150);
  
  // Move the servo to the desired angle
  myServo.write(servoAngle);
  
  // Uncomment for debugging 
  Serial.print("Number of Buttons Pressed: ");   
  Serial.print(numberButtonsPressed);  // print the number of buttons pressed
  Serial.print("  \t");                // prints a tab, for pretty, readable output
  Serial.print("Desired Servo Angle: "); 
  Serial.println(servoAngle);          // print the desired servo angle

  // Sleep for 10ms between loops
  delay(10);
}
