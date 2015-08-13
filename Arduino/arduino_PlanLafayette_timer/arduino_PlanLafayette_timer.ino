/*------------------------------------------------------------------------------------
 arduino_MasterPlan_timer.ino
 
 Basic timer for the PlanLafayette MCHE201 contest - Spring 2015
 1. Reads the "start" switch
 2. Keep two pins high for one minute, which close two relays
 3. Keeps pins high for indicator LEDs while "on"
 4. Checks reset switch during each "timing" loop
 
 Created: 11/10/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
 
 Modified:
 * 11/15/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
   - changed to triggering relays (little change to code, actually)
 * 11/17/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu
   - added status LEDs
   - added reset button and LED
   - reduced delay time in timing loop to allow quicker reset button
 * 03/29/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu
   - modified from old MCHE470 timer
   - decreased runtime to 30s
 
 ------------------------------------------------------------------------------------*/

// Variables declared here are global
// Pin declarations (const makes them immutable)
const int startButton = 2;          // pin 2 has the start button attached to it 
const int resetButton = 3;          // pin 3 has the timer reset button attached to it

const int LEDreset = 4;             // pin for reset button LED

const int outTeam1 = 5;             // pin to trigger start for Team 1
const int LEDteam1 = 6;             // pin to light LED for Team 1
const int outTeam2 = 7;             // pin to trigger start for Team 2
const int LEDteam2 = 8;             // pin to light LED for Team 2

const int testPin = 12;             // pin to test reading the output

// define the system parameters
int count = 0;          // counter for timer

// This is always run once when the sketch starts
// Use to initialize variables, pin modes, libraries, communication, etc
void setup()
{
  // initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  Serial.println("Starting...");
  Serial.println(" ");

  // define the start and reset buttons' digital pin as an INPUT_PULLUP
  // http://www.arduino.cc/en/Tutorial/InputPullupSerial
  pinMode(startButton, INPUT_PULLUP);
  pinMode(resetButton, INPUT_PULLUP);

  // define the test digital pin as an INPUT
  pinMode(testPin, INPUT_PULLUP);

  // define the output digital pins
  pinMode(LEDreset, OUTPUT);
  pinMode(outTeam1, OUTPUT);
  pinMode(LEDteam1, OUTPUT);
  pinMode(outTeam2, OUTPUT);
  pinMode(LEDteam2, OUTPUT);
}


// This runs immediately after setup, looping indefinitely
void loop()
{
  int outputState;
  int timeRemaining;
  int resetButtonState;

  // read the value of the startButton, invert to align with intuitive logic
  int startButtonState = !digitalRead(startButton);

  // This switch is wired as active-low, but the reading is inverted when read. 
  // This way, the logic matches our intution of HIGH = on
  if (startButtonState){
    Serial.println(" ");
    Serial.println("Starting 30s Timer... ");

    while(count < 300){

      // read the reset button each time through the timer loop
      resetButtonState = digitalRead(resetButton);

      // if the reset button is pressed, then break from the timer loop
      if (resetButtonState == 0){
        break;
      }

      // set the output pins to high to close relay for the teams to sense
      digitalWrite(outTeam1, HIGH);
      digitalWrite(outTeam2, HIGH);

      // set the indicator LEDs to high for the teams to see
      digitalWrite(LEDteam1, HIGH);
      digitalWrite(LEDteam2, HIGH);

      // set the reset button LED to high
      digitalWrite(LEDreset, HIGH);

      // We assume all other processing time is negligible compared to this pause
      delay(100);

      // increment the counter
      count++;

      // Print the current state to serial monitor once per second (every 100 loops)
      if (count % 10 == 0){
        timeRemaining = 30 - count/10;

        // read the state of the test pin
        outputState = digitalRead(testPin);

        Serial.print("ON: ");
        Serial.print(timeRemaining);
        Serial.print("s Remaining ");
        Serial.print("  \t");
        Serial.print("Test Pin = ");
        Serial.println(outputState);
      }
    }
  }
  else
  {
    // set the pins low after timer loop is done or reset button is pushed
    digitalWrite(outTeam1, LOW);
    digitalWrite(LEDteam1, LOW);
    digitalWrite(outTeam2, LOW);
    digitalWrite(LEDteam2, LOW);
    digitalWrite(LEDreset, LOW);

    // If we had been in timer-countdown mode, print finished to the Serial Monitor
    if (count != 0){
      Serial.println(" ");
      Serial.println("Count finished... ");
    }

    // reset the counter
    count = 0;
  }
}

