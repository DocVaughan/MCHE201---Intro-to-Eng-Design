/*------------------------------------------------------------------------------------
arduino_020917_inClassExercise5.ino

Code to get analog data and turn on an LED based on the value. This 
version using the calculated analog voltage to determine when to turn
the LED on/off.

http://arduino.cc/en/Tutorial/ReadAnalogVoltage

Created: 09/27/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 03/03/17 - JEV - joshua.vaughan@louisiana.edu
    - updated naming to match Spring 2017 assignment
    - better spacing
------------------------------------------------------------------------------------*/
const int LED = 13;  // Define the onboard LED pin

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  // set the LED pin as an output
  pinMode(LED, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);

  // Voltages on the analog input are 0-5V, so 2.5V is halfway
  if (voltage >= 2.5) {
    digitalWrite(LED, HIGH); // Turn LED on
    Serial.println("Voltage >=2.5V, LED On");
  }
  else {
    digitalWrite(LED, LOW); // Turn LED off
    Serial.println("Voltage <2.5V, LED Off");
  }
  
  // Pause 1s (1000ms) between readings
  delay(1000);
}
