var firstName = prompt("What's your first name?")
var lastName = prompt("What's your last name?")
var age = prompt("How old are you?")
var height = prompt("How tall are you? (centimeters)")
var petName = prompt("What's your pet's name?")

var correctName = firstName[0] === lastName[0]
var correctAge = (age > 20) && (age < 30)
var correctHeight = height >= 170
var correctPet = "y" === petName[petName.length - 1]

var fullCondition = correctName && correctAge
                    && correctHeight && correctPet

if (fullCondition) {
  console.log("Welcome Comrade!");
} else {
  console.log("Nothing to see here... :^))))");
}
