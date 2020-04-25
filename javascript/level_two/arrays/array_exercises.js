var isLive = true;
var roster = [];

function add() {
  var name = prompt("What name would you like to add?")
  roster.push(name)
}

function remove() {
  var rem = prompt("Which name would you like to remove?")
  if (!roster.includes(rem)) {
    console.log("Name not found in roster.")
  } else {
    var newRoster = []
    for (name of roster) {
      if (name !== rem) {
        newRoster.push(name)
      }
    }
  }
  roster = newRoster;
}

function display() {
  alert("Dumping roster to console.")
  console.log(roster)
}

function quit() {
  isLive = false;
  alert("Thanks for using the app! Your final roster is in console.")
  display();
}

while (isLive){
  var action = prompt("Would you like to add, remove, display, or quit?")
  if (action === "add") {
    add()
  } else if (action === "display") {
    display()
  } else if (action === "remove") {
    remove();
  } else if (action === "quit") {
    quit()
  } else {
    alert("Command not recognized. Please use add, display, remove, or quit.")
  }
}
