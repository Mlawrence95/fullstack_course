var defaultColor = "#bbb";

var blue = prompt("Player one, please enter your name. You are blue!")
var red  = prompt("Player two, please enter your name. You are red!")

var blueTurn  = true;
var game_over = false;
var nPlaced   = 0;

// check if game has been won yet
function gameOver() {
  return true;
}

// return the element at specified row, column
// alter like
// > x = elementAt(0, 0)
// > x.css('background', 'red')
function elementAt(row, column) {
  row_tag    = `row${row}`;
  var rowDiv = $(`#${row_tag} .circle`);
  return rowDiv.eq(column);
}

function makeMove(column) {
  index = getRowIndex(column)
  if (index == -1) {
    console.log("oh shit this wasnt supposed to happen")
  } else {
    var target = elementAt(index, column)
    var playerColor = blueTurn ? "blue": "red"
    target.css("background-color", playerColor)
    target.addClass("activated")
    nPlaced += 1;
  }
}

function getRowIndex(column) {
  // column in [0, 1, 2...6]
  // returns row index for placement of piece, or -1 if full
  columnID = `column${column}`
  for (var row=0; row<4; row++) {
    var target = elementAt(row, column)
    if (!target.hasClass("activated")) {
      return row;
    }
  }
  return -1;
}


// attach make move event to each column
for (var column=0; column<=6; column++) {
  $(`#column${column}`).click(makeMove(column))
}


function playGame() {
  // Main game loop
  while (!game_over) {
    if (blueTurn) {
      $("h3").text(`${blue}, it's your turn!`)
    } else {
      $("h3").text(`${red}, it's your turn!`)
    }
    var currentNPlaced = nPlaced;
    while (nPlaced == currentNPlaced) {
      setTimeout(playGame, 5 * 1000)
      console.log("Waiting for next move...")
    }
    // wait for user input before advancing
    // blueTurn = !blueTurn
    game_over = true;
  }
}


playGame();

var winner = "sky";
$("h3").text(`Game over. ${winner} has won! :^)`)
