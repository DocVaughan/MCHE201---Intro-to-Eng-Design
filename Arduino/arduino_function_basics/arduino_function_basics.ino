/*------------------------------------------------------------------------------------
function_basics.ino

Demonstrating making functions

Copied from: http://arduino.cc/en/Reference/FunctionDeclaration

Created: 09/02/13 - Joshua Vaughan - joshua.vaughan@louisiana.edu

Modified:
------------------------------------------------------------------------------------*/

void setup(){
  Serial.begin(9600);
}

void loop() {
  int i = 2;
  int j = 3;
  int k;

  k = myMultiplyFunction(i, j); // k now contains 6
  Serial.println(k);
  delay(500);
}

int myMultiplyFunction(int x, int y){
  int result;
  result = x * y;
  return result;
}
