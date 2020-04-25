// docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
var countries = ["USA", "Germany", "China"]

countries[0] === "USA"

// arrays are mutable (strings are not mutable in js)
countries[0] = "Mike"
countries[0] === "Mike"

// js supports mixed data types
var mixed = [true, "Mike", 400]
mixed.length


// push, pop
var myArray = ["one", "two", "three"]
myArray.pop()  // "three"

myArray.push("new")
// ["one", "two", "new"]


// iterations
var arr = ["a", "b", "c"]

for (var i=0; i< arr.length; i++){
  console.log(arr[i])
}

for (entry of arr){
  console.log(entry)
}

// apply function to array -- MAP
arr.forEach(alert);
