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
  
//  for (int counter = 0; counter < 10; counter++)
//    {
//    Serial.print("Counter = ");
//    Serial.println(counter);
//    delay(100);
//    }

  // This while loop is equivalent to the for loop above
//  int counter = 0;  
//  while (counter < 10)
//    {
//    Serial.print("Counter = ");
//    Serial.println(counter);
//    delay(100);
//    counter++; // equivalent to counter = counter + 1; 
//    }

// This do... while loop is equivalent to the for loop above
  int counter = 0;  
  do
    {
    Serial.print("Counter = ");
    Serial.println(counter);
    delay(100);
    counter++; // equivalent to counter = counter + 1; 
    } while (counter < 10); 


  Serial.println("For... loop finished");
  Serial.println(""); 
  delay(500);

// Uncomment below to only run the loop once
// The code will get stuck in this infinite while loop
//  while(true)
//  {
//    delay(100);
//  }
}
