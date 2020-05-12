var blue = prompt("Player one, please enter your name. You are blue!")
var red  = prompt("Player two, please enter your name. You are red!")

$("h3").text(`${blue}, it's your turn!`)

var blueTurn  = true;

/* Helper Methods First!*/
function inBounds(row, column) {
  var rowGood = (row >=0) & (row <= 4)
  var colGood = (column >= 0) & (column <= 6)
  return rowGood & colGood
}

// return the element at specified row, column
function elementAt(row, column) {

  if (inBounds(row, column)) {
    row_tag    = `row${row}`;
    var rowDiv = $(`#${row_tag} .circle`);
    return rowDiv.eq(column);
  }
  return -1;
}

function getRowIndex(column) {
  // column in [0, 1, 2...6]
  // returns row index for placement of piece, or -1 if full
  for (var row=0; row<=4; row++) {
    var target = $(elementAt(row, column))
    if (!target.hasClass("blue") & !target.hasClass("red")) {
      return row;
    }
  }
  return -1;
}

function isColor(row, column, color) {
  return $(elementAt(row, column)).hasClass(color);
}

// check the x based at row, col to check for victory
function wonDiagonal(row, column, color) {
  // up => row += 1
  // right => column += 1
  // check how many in an x are same color. true if >= 4
  var nPiecesDecline = 0;
  var nPiecesIncline = 0;

  var currentColumn = column;
  var currentRow    = row;

  //check decline
  // up, left
  while (inBounds(currentRow, currentColumn)
         & isColor(currentRow, currentColumn, color)) {
      nPiecesDecline += 1;
      currentColumn  -= 1;  // left
      currentRow     += 1;  // up
  }

  currentRow =    row - 1;  // start, down one
  currentColumn = column + 1;  // start, right one
  // down, right
  while (inBounds(currentRow, currentColumn)
         & isColor(currentRow, currentColumn, color)) {
      nPiecesDecline += 1;
      currentColumn  += 1;  // right
      currentRow     -= 1;  // down
  }

  if (nPiecesDecline >= 4) {
    return true;
  }

  /* #### reset for incline  #### */
  currentColumn = column;
  currentRow    = row;

  // up, right
  while (inBounds(currentRow, currentColumn)
         & isColor(currentRow, currentColumn, color)) {
      nPiecesIncline += 1;
      currentColumn  += 1;  // right
      currentRow     += 1;  // up
  }

  currentRow =    row - 1;  // start, down one
  currentColumn = column - 1;  // start, left one

  // down, left
  while (inBounds(currentRow, currentColumn)
         & isColor(currentRow, currentColumn, color)) {
      nPiecesIncline += 1;
      currentColumn  -= 1;  // left
      currentRow     -= 1;  // down
  }

  if (nPiecesIncline >= 4) {
    return true;
  } else {
    return false;
  }
}

// check left, right of row, col to check for victory
function wonVertical(row, column, color) {
  // check how many left/right are same color. true if >= 4
  var nPieces = 0

  var currentRow = row;
  //check left
  while (inBounds(currentRow, column)
         & isColor(currentRow, column, color)) {
      nPieces += 1;
      currentRow -= 1;
  }

  // reset
  currentRow = row + 1;

  // check right
  while (inBounds(currentRow, column)
         & isColor(currentRow, column, color)) {
      nPieces += 1;
      currentRow += 1;
  }

  return nPieces >= 4;
}

// check up, down of row, col to check for victory
function wonHorizontal(row, column, color) {
  var nPieces = 0;

  var currentColumn = column;

  //check left
  while (inBounds(row, currentColumn)
         & isColor(row, currentColumn, color)) {
      nPieces += 1;
      currentColumn -= 1;
  }

  // reset, dont doublecount
  currentColumn = column + 1;

  // check above
  while (inBounds(row, currentColumn)
         & isColor(row, currentColumn, color)) {
      nPieces += 1;
      currentColumn += 1;
  }
  return nPieces >= 4;
}

// check if game has been won yet
function gameOver(row, column, color) {
  var hor = wonHorizontal(row, column, color);
  var vert = wonVertical(row, column, color);
  var diag = wonDiagonal(row, column, color);

  return hor || vert || diag;
}

function makeMove() {
  var column = -1;
  console.log("this is: " + this)

  for (var col=0; col<=6; col++){
    if ($(this).hasClass(`column${col}`)) {
      column = col;
      console.log("found column: " + col);
    }
  }
  var availableRow = getRowIndex(column);
  console.log("making move at " + availableRow + ", " + column)


  if ((availableRow == -1) || (column == -1)) {
    console.log("oh shit this wasnt supposed to happen")
  } else {
    var target = $(elementAt(availableRow, column))
    var playerColor = blueTurn ? "blue": "red"
    target.addClass(playerColor)

    if (gameOver(availableRow, column, playerColor)) {
      var winner = blueTurn ? blue: red
      $("h3").text(`Game over. ${winner} has won! :^)`)
      alert("Refresh to start over :^)")
    }
  }

  blueTurn = !blueTurn;
  if (blueTurn) {
    $("h3").text(`${blue}, it's your turn!`)
  } else {
    $("h3").text(`${red}, it's your turn!`)
  }
}

/* Set up the game board*/
$(".circle").on("click", makeMove);

  // $(".circle").click(function() {
  //   console.log($(this).closest(".circle").attr("class"))
  // })
