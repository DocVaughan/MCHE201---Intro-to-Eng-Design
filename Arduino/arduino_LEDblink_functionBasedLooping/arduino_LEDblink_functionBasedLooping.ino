/*------------------------------------------------------------------------------------
arduino_LEDblink_functionBasedLooping.ino

Uses a function on an LED on for one second, then off for one second, repeatedly.
It repeats this five times using three different looping methods

From: http://arduino.cc/en/Tutorial/Blink
      This example code is in the public domain.

Created: 02/10/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu
------------------------------------------------------------------------------------*/
 
// Pin 13 has an LED connected on most Arduino boards, including the RedBoard we have
// name it led to make your code easier to read
int led = 13;

// This is always run once when the sketch starts
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT); 

  // initialize serial communication at 9600 bits per second
  Serial.begin(9600);  
}


// This runs immediately after setup, looping indefinitely
void loop() {
  
  // Loop 5 times, printing the counter blinking the LED each time
  for (int counter = 0; counter < 5; counter++) {
    
    // Print the current loop counter to the serial monitor
    Serial.print("For loop counter = ");
    Serial.println(counter);
    
    blink_LED();
  }
  
   // Loop 5 times, printing the counter blinking the LED each time
  int counter = 1;
  while ( counter <=5 ) {
    // Print the current loop counter to the serial monitor
    Serial.print("While loop counter = ");
    Serial.println(counter);
    
    // increment the counter
    counter = counter + 1;
    
    blink_LED();
  }
  
  // Loop 5 times, printing the counter blinking the LED each time
  counter = 1;
  do {
    // Print the current loop counter to the serial monitor
    Serial.print("DO loop counter = ");
    Serial.println(counter);
    
    // increment the counter
    counter = counter + 1;
    
    blink_LED();
    
  } while( counter <= 5);
  
  
  // This is a dirty way to cause loop() to only run once
  // This while loop repeats forever, until the power is cut or the board is reset
  while(true){}
}


void blink_LED(){
  // Blink the LED
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  
  delay(1000);               // wait for a second
  
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  
  delay(1000);               // wait for a second
}
