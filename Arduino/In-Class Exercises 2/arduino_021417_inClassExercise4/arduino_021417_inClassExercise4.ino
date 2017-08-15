/*------------------------------------------------------------------------------------
arduino_021417_inClassExercise4.ino

Connect the photo resistor and the piezo buzzer. When light is blocked from the photo 
resistor, sound the buzzer. When light is seen by the sensor, the buzzer should be 
silent. See Circuit #6 from the SIK for help with the photo resistor and Circuit #11 
for help with the piezo buzzer.

http://arduino.cc/en/Tutorial/ReadAnalogVoltage

Created: 10/17/16 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 03/03/17 - JEV - joshua.vaughan@louisiana.edu
    - Updated naming to match Spring 2017 assignment
------------------------------------------------------------------------------------*/

// Define the buzzer pin
const int BUZZER_PIN = 9; 
const int BUZZER_FREQ = 262; // a C note  

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  // define the buzzer pin as an output
  pinMode(BUZZER_PIN, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  
  // read the input on analog pin 0:
  int sensor_value = analogRead(A0);

  // if the sensor sees light, turn on the buzzer, else turn it off
  if (sensor_value > 512 ) {
    // turn on the buzzer
    tone(BUZZER_PIN, BUZZER_FREQ);

    // output to serial monitor for debugging
    Serial.println("I see the light!");
  }
  else {
    // turn off the buzzer
    noTone(BUZZER_PIN);

    // output to serial monitor for debugging
    Serial.println("Darkness surrounds me.");
  }

  // Pause 10ms between readings
  delay(10);
}
