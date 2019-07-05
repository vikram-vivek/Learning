var fname = prompt("Enter your First Name:");
var lname = prompt("Enter your Last Name:");
var age = prompt("Enter your age:");
var height = prompt("Enter your height in cms:");
var petname = prompt("Enter your pet name:");

if ((fname[0] == lname[0])&(age>=20 & age<=30)&(height>=170)&(petname=="Sammy")){
  console.log("Welcome Spy!");
} else {
  console.log("Nothing to see here.");
}
