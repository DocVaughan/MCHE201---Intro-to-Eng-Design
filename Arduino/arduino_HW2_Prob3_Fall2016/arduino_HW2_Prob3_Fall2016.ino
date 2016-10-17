/*------------------------------------------------------------------------------------
arduino_HW2_Prob3_Fall2016.ino

Connect the potentiometer and the red, green, yellow, and blue LEDs. The LEDs track 
the position of the potentiometer. The potentiometer range should be divided into 
four ranges, so that when the potentiometer is at the minimum of its range 
(all the way “left”), the leftmost LED is lit, and similar for the right side. 
In the middle portion of the potentiometer range, the middle LEDs are lit according 
ranges defined.

This is done in an explicit way. We could also be more elegant by using an array 
to hold the LED pin numbers. It would be less code to write, but perhaps would be
less readable, especially by those new to coding.

http://arduino.cc/en/Tutorial/ReadAnalogVoltage
https://www.arduino.cc/en/Tutorial/BlinkWithoutDelay


Created: 10/17/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/

// Define the LED pin outputs
const int RED_LED = 8;
const int GREEN_LED = 9;
const int YELLOW_LED = 10;
const int BLUE_LED = 11;

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  
  // read the input on analog pin 0:
  int sensor_value = analogRead(A0);

  if (sensor_value <= 255) {
    // turn on the red LED
    digitalWrite(RED_LED, HIGH); 
    Serial.println("Red LED on.");

    // and turn off all others
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(BLUE_LED, LOW);
  }
  else if (sensor_value <= 512) {
    // turn on the green LED
    digitalWrite(GREEN_LED, HIGH); 
    Serial.println("Green LED on.");

    // and turn off all others
    digitalWrite(RED_LED, LOW);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(BLUE_LED, LOW);
  }
  else if (sensor_value <= 768) {
    // turn on the yellow LED
    digitalWrite(YELLOW_LED, HIGH); 
    Serial.println("Yellow LED on.");

    // and turn off all others
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(BLUE_LED, LOW);
  }
  else {
    // turn on the yellow LED
    digitalWrite(BLUE_LED, HIGH); 
    Serial.println("Blue LED on.");

    // and turn off all others
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, LOW);
  }
  
  // Pause 10ms between readings
  delay(10);
}
