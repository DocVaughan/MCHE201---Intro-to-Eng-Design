/*-----------------------------------------------------------------------------
arduino_020216_LectureExercise1.ino

Exercise from MCHE201 Lecture on 02/02/16
This shows two ways do complete the task. There are many.

Optional Link to relevant documentation

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

  Serial.println("Beginning Loop option 1...");
  // OPTION 1: This for loop increments by 2 each loop
  // Create the for loop
  // This will start at 0,        int counter = 0
  //       increment by 2,        counter = counter + 2
  //       run while counter < 0, counter < 10
  for (int counter = 1; counter <= 27; counter = counter + 2) {
    // Everything between the for loops {} will run each time it loops
    // Here, we just print the value of the counter (with some formatting)
    Serial.print("Counter = ");
    Serial.println(counter);
  }

  delay(1000); // Pause one second (1000ms)
  
  Serial.println(""); // A blank line for readability
  Serial.println("Beginning Loop option 2...");
  // OPTION 2: This for loop increments by 1 each loop
  // It requires some math inside the loop
  // Create the for loop
  // This will start at 0,        int counter = 0
  //       increment by 1,        counter = counter++
  //       run while counter < 30, counter < 30
  for (int counter = 1; counter <= 14; counter++) {
    // Everything between the for loops {} will run each time it loops
    // Here, we just print the value of the counter (with some formatting)
    Serial.print("Counter = ");
    Serial.println(2 * counter - 1);
  }
  
  // Code here will run once the both loops are finished
  Serial.println(""); // A blank line for readability
  Serial.println("Finished both options... ");
  Serial.println(""); // A blank line for readability
  delay(1000); // Pause one second (1000ms) for repeating
}

