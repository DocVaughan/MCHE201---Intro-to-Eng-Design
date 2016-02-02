/*-----------------------------------------------------------------------------
arduino_SimpleForLoop.ino

Demonstrating a simple for loop just printing the value of the loop counter

For loop reference: https://www.arduino.cc/en/Reference/For

Created: 02/02/16
   - Joshua Vaughan
   - joshua.vaughan@louisiana.edu
   - http://www.ucs.louisiana.edu/~jev9637

 Modified:
   *
-----------------------------------------------------------------------------*/

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup() {
  // Set up the Serial Monitor
  Serial.begin(9600);
}

// This runs immediately after setup, looping indefinitely
void loop() {
  
  // Create the for loop
  // This will start at 0,        int counter = 0
  //       increment by 1,        counter++
  //       run while counter < 0, counter < 10
  for (int counter = 0; counter < 10; counter++) {
    // Everything between the for loops {} will run each time it loops
    // Here, we just print the value of the counter (with some formatting)
    Serial.print("Counter = ");
    Serial.println(counter);
  }
  
  // Code here will run once the the for loop is finished
  Serial.println(""); // A blank line for readability
  Serial.println("Finished the for loop... ");
  Serial.println(""); // A blank line for readability
  delay(1000); // Pause one second (1000ms) for repeating
}

