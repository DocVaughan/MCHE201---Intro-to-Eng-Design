/*------------------------------------------------------------------------------------
arduino_solenoidBasic_transistor.ino

Retract a solenoid if a switch is pressed, solenoid triggered via transistor

Created: 03/02/17 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * mm/dd/yy - Name (email if not same person as above)
    - major change 1
------------------------------------------------------------------------------------*/

// the control output will be digital pin 8
const int solenoid_transistor = 8;

void setup() {
  Serial.begin(9600);        // set up Serial library at 9600 bps
 
  //configure the motor_switch as an input and enable the internal pull-up resistor
  pinMode(solenoid_transistor, OUTPUT);
}


void loop() {    
      // Retract the solenoid   
      Serial.println("Retracting solenoid...");
      digitalWrite(solenoid_transistor, HIGH);
      
      // pause 50ms
      delay(100);
      
      // Release the solenoid 
      Serial.println("Retracting solenoid...");
      digitalWrite(solenoid_transistor, LOW);
      
          
      // Delay for 1000 ms before continuing (avoiding solenoid burnout)
      delay(1000);
}
