// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function () {
    return this.name.length
  }
}

console.log("I am alive hahahaha");
var ans = employee["nameLength"]()
console.log("Answer is "+ans);
// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

console.log("Calling alert");
for (k in employee){
  console.log((k+" is "+employee[k]));
}
console.log("Alert end!!");
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////
console.log("Last name is:");
// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function(){
    lname = this.name.split(" ");
    return lname[lname.length-1]
  }
}
console.log(employee["lastName"]());
// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
