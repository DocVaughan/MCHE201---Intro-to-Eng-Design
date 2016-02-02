/*-----------------------------------------------------------------------------
arduino_020216_LectureExercise2.ino

Exercise 2 from MCHE201 Lecture on 02/02/16

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
  Serial.println("Beginning For loop...");
  
  // Create the for loop
  // This will start at 0,        int counter = 0
  //       increment by 2,        counter = counter + 2
  //       run while counter < 0, counter < 10
  for (int counter = 1; counter <= 27; counter = counter + 2) {
    // Everything between the for loops {} will run each time it loops
    
    // Check if counter is 13
    if (counter == 13) { 
      // if so print that it's unlucky
      Serial.println("Counter = 13... Bad Luck!!!");
    }
    else { // Just print the value of the counter
      Serial.print("Counter = ");
      Serial.println(counter);
    }
  }
  
  // Code here will run once the the for loops is finished
  Serial.println(""); // A blank line for readability
  Serial.println("Finished the for loop... ");
  Serial.println(""); // A blank line for readability
  delay(1000); // Pause one second (1000ms) for repeating
}

