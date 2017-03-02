/*------------------------------------------------------------------------------------
arduino_solenoidSwitch_transistor.ino

Retract a solenoid if a switch is pressed, solenoid triggered via transistor

Created: 03/02/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * mm/dd/yy - Name (email if not same person as above)
    - major change 1
------------------------------------------------------------------------------------*/

// the control output will be digital pin 8
const int solenoid_transistor = 8;

// Attach the switch to pin 3 - make it a constant so it can't be changed
const int solenoid_switch = 3;

void setup() {
  Serial.begin(9600);        // set up Serial library at 9600 bps
 
  //configure the motor_switch as an input and enable the internal pull-up resistor
  pinMode(solenoid_transistor, OUTPUT);
  pinMode(solenoid_switch, INPUT_PULLUP);  
}


void loop() {    
  // If the button is pressed, retrac the solenoid
  if(!digitalRead(solenoid_switch))
  {
      Serial.println("Button Pressed. Retracting solenoid...");
      // full speed forward just passes maximum current to enable solenoid
      digitalWrite(solenoid_transistor, HIGH);
      
      // pause 100ms
      delay(100);
      
      // Stop the solenoid 
      digitalWrite(solenoid_transistor, LOW);
          
      // Delay for 1000 ms before continuing (avoiding solenoid burnout)
      delay(1000);
  }
    
  // Delay for 10 ms before looping and checking the swtich again
  delay(10);
}
