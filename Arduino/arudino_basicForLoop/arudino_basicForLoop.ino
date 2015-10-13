/*------------------------------------------------------------------------------------
arduino_basicForLoopm.ino

Demontrates a basic for loop.

See: https://www.arduino.cc/en/Reference/For

Created: 10/13/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 
------------------------------------------------------------------------------------*/

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("For... loop starting");
  
  for (int counter = 0; counter < 10; counter++)
    {
    Serial.print("Counter = ");
    Serial.println(counter);
    delay(100);
    }

  Serial.println("For... loop finished");
  Serial.println(""); 
  delay(500);
}
