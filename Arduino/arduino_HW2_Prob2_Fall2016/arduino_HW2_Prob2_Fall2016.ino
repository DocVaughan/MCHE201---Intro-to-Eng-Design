
/*------------------------------------------------------------------------------------
arduino_HW2_Prob2_Fall2016.ino

Connect the two pushbutton switches and the multicolor LED. If no buttons are being 
pressed, the LED should display green. If either button is pressed alone, it should 
be yellow. If both buttons are pressed, it should run red. See Circuit #3 from the 
SIK for help with the multicolor LED and Circuit #5 for the pushbutton switches.

The trick is to realize how light combines. See:
  https://en.wikipedia.org/wiki/RGB_color_model


This assumes that the pushbutton is wired in an active low configuration.
  For more info, see https://learn.sparkfun.com/tutorials/pull-up-resistors

Created: 10/17/16
  - Joshua Vaughan
  - joshua.vaughan@louisiana.edu
  - http://www.ucs.louisiana.edu/~jev9637/

Modified:
  * 
------------------------------------------------------------------------------------*/

// digital pin 2 has the pushbutton attached to it. 
// It's good practice to assign a name, to make your code easier to read
const int BUTTON_1 = 2;    // This is now global in scope
const int BUTTON_2 = 3;    // This is now global in scope

// Define the pins to which the LED is connected
const int RED_PIN = 9;
const int GREEN_PIN = 10;
const int BLUE_PIN = 11;

// declare a value to store the state of the pin
// the button only has two states so a boolean is the best choice
boolean button1_state = true; 
boolean button2_state = true; 

// This is always run once when the sketch starts
void setup() {
  // initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  
  // Remember that the digital pins can be in or out, so... 
  // We need to define the button pins as an INPUTs
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);

  // Define the pins of the LEDs as OUTPUTs
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // Now, read the current state of the buttons
  button1_state = digitalRead(BUTTON_1);
  button2_state = digitalRead(BUTTON_2);

  int number_of_buttons = button1_state + button2_state;

  if (number_of_buttons == 0) {
      // print out the state of the button
      Serial.println("No buttons were pressed. Turning green LED on.");
    
      // Turn the green LED on
      digitalWrite(GREEN_LED, HIGH);
    
      // Turn the red and blue LEDs off
      digitalWrite(RED_LED, LOW);
      digitalWrite(BLUE_LED, LOW);  
  }
  else if (number_of_buttons == 1) {
      // print out the state of the button
      Serial.println("One button was pressed. Turning yellow light on.");
    
      // Turn the red and green LEDs on, combingin light is different than pigments
      // https://en.wikipedia.org/wiki/RGB_color_model
      digitalWrite(RED_LED, HIGH);
      digitalWrite(GREEN_LED, HIGH);
      
      // Turn the blue LED off
      digitalWrite(BLUE_LED, LOW);
  }
  else {
      // print out the state of the button
      Serial.println("Two buttons were pressed. Turning red LED on.");
    
      // Turn the red LED on
      digitalWrite(RED_LED, HIGH);

      // Turn the green and blue LEDs off
      digitalWrite(GREEN_LED, HIGH);
      digitalWrite(BLUE_LED, LOW);
  }
  
  // delay 10ms between reads for stability
  delay(10);        
}
