/*------------------------------------------------------------------------------------
arduino_analogRead_minimum.ino

Bare minimum to get analog data and print to serial monitor

http://arduino.cc/en/Tutorial/ReadAnalogVoltage

Created: 09/03/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 02/11/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu
    - improved commenting
    - updated variable names for consistency with other examples
------------------------------------------------------------------------------------*/

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  
  // print out the value calculated from the sensor reading, formatting nicely
  Serial.print("The input voltage was ");
  Serial.print(voltage);
  Serial.println(" VDC.");
  Serial.println("");        // Print a blank line to make output easier to read
  
  // Pause 1s (1000ms) between readings
  delay(1000);
}
