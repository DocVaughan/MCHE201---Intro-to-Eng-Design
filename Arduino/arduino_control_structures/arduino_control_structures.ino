/* NOTE: This will NOT compile and run. 
 *  
 * It's for demonstration ONLY!
 * 
 * Created: 10/08/15 - Joshua Vaughan - joshua.vaughan@louisiana.edu
 * 
 */


// ----- if... else if... else syntax ------------------------------------------
if (condition1 == true)
{
  // do Thing A
}
else if (condition2 == true) // if condition1 isn't true, check condition2
{
  // do Thing B
}
else // if neither condition1 or condition2 are true, do this
{
  // do Thing C
}



// ----- switch case syntax ----------------------------------------------------
switch (var) {
    case 1:
      // do something when var equals 1
      break; // stop evaluating the switch...case
      
    case 2:
      // do something when var equals 2
      break; // stop evaluating the switch...case
    
    default: 
      // if nothing else matches, do the default
      // default is optional
}



// ----- for-loop syntax -------------------------------------------------------
for (initialization; condition; increment) {
  // do something;
}



// ----- while-loop syntax -----------------------------------------------------
while(condition == true) {
  // do something;
}



// ----- do-while syntax -------------------------------------------------------
do {
    // do something;
} while (condition == true);





// ----- comparison syntax -----------------------------------------------------
// these evaluate to true (1) or false (0), a boolean
 x == y (x is equal to y)
 x != y (x is not equal to y
 x <  y (x is less than y)  
 x >  y (x is greater than y) 
 x <= y (x is less than or equal to y) 
 x >= y (x is greater than or equal to y)
