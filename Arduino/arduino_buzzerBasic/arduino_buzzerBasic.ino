/* ----------------------------------------------------------------------------

arduino_buzzerBasic.ino

Example sketch showing the basic use of the buzzer included with the SparkFun Inventor’s Kit

Created: 09/29/16
   - Joshua Vaughan
   - joshua.vaughan@louisiana.edu
   - http://www.ucs.louisiana.edu/~jev9637

 Modified:
   *

---------------------------------------------------------------------------- */

// Define the pin number of the buzzer and LED
// We do so here rather than just typing the pin numbers directly to:
//  * Make the code more readable
//  * Make it easier to change the pin number later. We'd only have to change 
//    the number here.
const int BUZZER_PIN = 9;  
const int LED = 13;  

const int buzzer_freq = 262; // a C note  


void setup() {
  // put your setup code here, to run once:

  // define the buzzer pin as an output
  pinMode(BUZZER_PIN, OUTPUT);

  // Let's also set up the onboard LED as an output
  pinMode(LED, OUTPUT);

  // Now, let's beep once to let us know the set up function finished
  // We'll do it manually here, rather than use the beepNtimes() function
  tone(BUZZER_PIN, buzzer_freq, 250);   // output a tone for 250ms
  delay(250);                           // wait for the tone command to finish
  tone(BUZZER_PIN, buzzer_freq, 250);   // output a tone for 250ms
  delay(250);                           // wait for the tone command to finish
}

void loop() {
  // put your main code here, to run repeatedly:

  // Toggle the LED 3 times to let us know we're in the main loop
  for (int counter = 0; counter < 3; counter++) {
    digitalWrite(LED, HIGH);
    delay(100);
    digitalWrite(LED, LOW);
    delay(100);
  }

  // Add a 2s delay in place of some longer running code we might have in a 
  // "real" program
  delay(2000);

  // Now let's use the function we wrote below, called beepNtimes to beep 
  // 3 times, letting us know the loop funciton is now "looping" back to the 
  // beginning
  beepNtimes(BUZZER_PIN, buzzer_freq, 3);
}


void beepNtimes(int pin, int freq, int number_of_beeps) {
    // Function to beep the buzzer N times when called, with 100ms between beeps
    // Note that this is a "blocking" function. It takes a nonzero amount of time
    // to run, during which nothing else is happening.
    // 
    // Arguments:
    //    pin - the pin the buzzer is attached to
    //    freq - the frequency to buzz/beep at
    //    number_of_beeps - the number of times to beep

    for (int counter = 0; counter < number_of_beeps; counter++) {
        tone(pin, freq, 100);   // output a tone for 100ms
        delay(100);             // wait for the tone command to finish
    }
}

