// objects are just dictionaries
var carInfo = {make:"Toyota", year:1995, model:"4Runner"}
carInfo["make"] // Toyota

// these can be super nested

// show entire object
console.dir(carInfo)

// iteration
for (key in carInfo) {
  // no guarantee of order
  console.log(key);
  console.log(carInfo[key]);
}


// these dicts ARE objects in the traditional sense (self --> this)
var myObj = {
  age: 37,
  hairColor: "Blonde",
  reportProps: function() {
    return [this.age, this.hairColor];
  }
}

myObj.reportProps()
// Array [ 37, "Blonde" ]
