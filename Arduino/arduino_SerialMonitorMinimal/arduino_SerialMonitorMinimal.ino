/*-----------------------------------------------------------------------------
arduino_SerialMonitor_minimum.ino

Minimal required for Serial Monitor

Optional Link to relevant documentation

Created: 02/02/16
   - Joshua Vaughan
   - joshua.vaughan@louisiana.edu
   - http://www.ucs.louisiana.edu/~jev9637

 Modified:
   *
-----------------------------------------------------------------------------*/


void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Looping...");
  
  delay(1000); // Pause for one second
}
