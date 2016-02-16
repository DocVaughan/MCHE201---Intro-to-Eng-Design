
/*-----------------------------------------------------------------------------
arduino_servomotor_speedControl.ino

Demonstrates controlling the speed of a hobby-style servomotor

Adapted from the SparkFun Inventor's Kit example code, their orignal comments
are also provided below
  * https://www.sparkfun.com/products/12060

Uses the Servo Library, provided with base Arduino IDE install:
  * https://www.arduino.cc/en/reference/servo

Created: 02/11/16
   - Joshua Vaughan
   - joshua.vaughan@louisiana.edu
   - http://www.ucs.louisiana.edu/~jev9637

 Modified:
   *
-----------------------------------------------------------------------------*/

/*---- Original Premable from Sparkfun ----------------------------------------
SparkFun Inventor's Kit
Example sketch 08

SINGLE SERVO

  Sweep a servo back and forth through its full range of motion.

  A "servo", short for servomotor, is a motor that includes 
  feedback circuitry that allows it to be commanded to move to
  specific positions. This one is very small, but larger servos
  are used extensively in robotics to control mechanical arms,
  hands, etc. You could use it to make a (tiny) robot arm,
  aircraft control surface, or anywhere something needs to be
  moved to specific positions.

Hardware connections:

  The servo has a cable attached to it with three wires.
  Because the cable ends in a socket, you can use jumper wires
  to connect between the Arduino and the servo. Just plug the
  jumper wires directly into the socket.
  
  Connect the RED wire (power) to 5 Volts (5V)
  Connect the WHITE wire (signal) to digital pin 9
  Connect the BLACK wire (ground) to ground (GND)

  Note that servos can use a lot of power, which can cause your
  Arduino to reset or behave erratically. If you're using large
  servos or many of them, it's best to provide them with their
  own separate 5V supply. See this Arduino Forum thread for info:
  http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1239464763

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
------ Original Premable from Sparkfun --------------------------------------*/

// Once you "include" a library, you'll have access to those functions.
#include <Servo.h>          // include the servo library

const byte SERVO_PIN = 9;   // Define the pin teh servo is attached to

// Now we'll create a servo "object", called myservo. You should
// create one of these for each servo you want to control. 
// You can control a maximum of twelve servos on the Uno 
// using this library. (Other servo libraries may let you
// control more). Note that this library disables PWM on
// pins 9 and 10!

Servo servo_9;  // create the servo control object

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup()
{
  // Attach the servo_9 object to digital pin 9.
  // If you want to control more than one servo, attach more
  // servo objects to the desired digital pins.

  // Attach tells the Arduino to begin sending control signals
  // to the servo. Servos require a continuous stream of control
  // signals, even if you're not currently moving them.
  // While the servo is being controlled, it will hold its 
  // current position with some force. If you ever want to
  // release the servo (allowing it to be turned by hand),
  // you can call servo1.detach().

  servo_9.attach(SERVO_PIN);
}


void loop()
{
    int servo_angle;  // Define a variable to hold the desired servo angle

    servo_9.write(30);  // Move the servo to 30 deg to set up the code below
  
   // Change position at a slower speed:
  
    // To slow down the servo's motion, we'll use a for() loop
    // to give a series intermediate positions, with delays between them.
    // The step size and delay can be changed to make the servo slow down
    // or speed up. Note that the servo can't move faster than its full
    // speed, so you can't update it any faster than every 20ms.
  
    // Tell servo to go to 150 degrees, stepping by two degrees every 20ms
    for (servo_angle = 30; servo_angle <= 150; servo_angle += 2)
    {
        servo_9.write(servo_angle);  // Move to next position
        delay(20);                   // Short pause to allow it to move
    }
  
    // Tell servo to go to 30 degrees, stepping by one degree every 40ms
    for (servo_angle = 150; servo_angle >= 30; servo_angle -= 1)
    {
        servo_9.write(servo_angle);  // Move to next position
        delay(40);                   // Short pause to allow it to move
    }
}
