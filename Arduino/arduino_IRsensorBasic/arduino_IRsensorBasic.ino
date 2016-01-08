/*------------------------------------------------------------------------------------
arduino_IRsensorBasic.ino

Bare minimum to read the IR sensor and print to serial monitor

For the MCHE201 IR sensor:
 * Rad - +5VDC
 * Black - Ground
 * Yellow - Analog pin 0

The sensor outputs approximately:
  * 3.1V at 4cm
  * 0.3V at 30cm
  * There is a nonlinear relationship between these values

For wiring: http://bildr.org/2011/03/various-proximity-sensors-arduino/
For analog: http://arduino.cc/en/Tutorial/ReadAnalogVoltage

Created: 10/27/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  *
------------------------------------------------------------------------------------*/

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input from the IR sensor on analog pin 0:
  int sensorValue = analogRead(A0);

  // print out the raw value that was read:
  Serial.print("The raw analog reading was ");
  Serial.println(sensorValue);

  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("This corresponds to an analog votlage of ");
  Serial.print(voltage);
  Serial.println("V");

  // TODO: Complete curve fit for voltage -> distance
  // Convert voltage to approx distance based on curve fit found at:
  //   https://acroname.com/articles/linearizing-sharp-ranger-data
//  float distance = 1 / voltage - 0.42;
//
//  if ((distance > 30) || (distance < 4))
//  {
//    // If the caculated value is outside the sensor specs warn the user
//    Serial.println("Calculated distance was outside of sensor range. Do NOT trust.");
//  }
//  else // we got a reasonable value
//  {
//      // print out the raw value you read
//      Serial.print("The approximate distance is ");
//      Serial.print(distance);
//      Serial.println(" cm.");
//  }
//
  Serial.println("");
  
  // Pause 1s (1000ms) between readings
  delay(1000);
}
