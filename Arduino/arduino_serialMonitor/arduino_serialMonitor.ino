/*------------------------------------------------------------------------------------
arduino_serialMonitor.ino

Prints a random number to the serial monitor

https://learn.sparkfun.com/tutorials/serial-communication
http://arduino.cc/en/Reference/Serial
http://arduino.cc/en/Reference/Random
http://arduino.cc/en/Reference/Delay

Created: 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever
void loop() {
  long randomNumber;  // the random() function returns a long
  
  // assign a random value between 0 and 100
  randomNumber = random(0,100);
  
  // print a random number to the serial monitor
  Serial.println(randomNumber);
  
  delay(500);          // pause for 500ms
}
