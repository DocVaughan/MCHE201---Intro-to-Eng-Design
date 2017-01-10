/*------------------------------------------------------------------------------------
arduino_092716_inClassExercise1Alternate.ino

Code to get analog data and turn on an LED based on the value. This 
version using the raw analog sensor reading to determine when to turn
the LED on/off.

http://arduino.cc/en/Tutorial/ReadAnalogVoltage

Created: 09/27/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/
const int LED = 13; // Define the onboard LED pin

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
  
  if (sensorValue >= 512) {
    digitalWrite(LED, HIGH); // Turn LED on
    Serial.println("sensorValue >= 512, LED On");
  }
  else {
    digitalWrite(LED, LOW); // Turn LED off
    Serial.println("sensorValue < 512, LED Off");
  }
  
  // Pause 1s (1000ms) between readings
  delay(1000);
}
