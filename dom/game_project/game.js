// these help reference squares on the board
var dim = ["zero", "one", "two"];

// "" - > X -> O -> "" on click
function cycleMarker() {
  var current = this.textContent;
  var next;
  if (current == "") {
    next = "X"
  } else if (current == "X") {
    next = "O"
  } else if (current == "O") {
    next = ""
  } else {
    console.log("No match found for marker with current state: " + current)
  }
  this.innerHTML = `<strong>${next}</strong>`
}

function resetBoard() {
  for (row of dim) {
    for (column of dim) {
      var boxID = `#${row}${column}`
      var box = document.querySelector(boxID)
      box.innerHTML = `<strong></strong>`
    }
  }
}


// Add reset functionality
var restartButton = document.querySelector('#restart')
restartButton.addEventListener("click", resetBoard)

// add on-click functionality to game board
// this  can be done with querySelectorAll in a more clean way
for (row of dim) {
  for (column of dim) {
    var boxID = `#${row}${column}`
    var box = document.querySelector(boxID)
    box.addEventListener('click', cycleMarker)
    console.log(boxID)
  }
}
