/*------------------------------------------------------------------------------------
function_basics.ino

Demonstrating making functions

Copied from: http://arduino.cc/en/Reference/FunctionDeclaration

Created: 09/02/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
  * 02/02/16 - JEV - joshua.vaughan@louisiana.edu
    - Better commenting
------------------------------------------------------------------------------------*/

void setup(){
  // Set up the Serial Monitor
  Serial.begin(9600);
}

void loop() {
  int i = 2;
  int j = 3;
  int m = 10;
  int k;

  // Call the myMutiplyFunction, sending the values of i and j as inputs
  k = myMultiplyFunction(i, j); // k now contains 6
  Serial.println(k);

  // Pause for 500ms
  delay(500);

  // Call the myMutiplyFunction, sending the values of i and m as inputs
  k = myMultiplyFunction(i, m); // k should be 20
  Serial.println(k);
  
  // Pause for 500ms
  delay(500);
}

int myMultiplyFunction(int x, int y) {
  int result;

  // Multiply the two input integers
  result = x * y;

  // Return the value of result
  return result;
}
