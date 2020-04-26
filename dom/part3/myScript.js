var headings = document.querySelectorAll('h1')
console.log("connected!")

var hover = headings[0];
var click = headings[1];
var doubleClick = headings[2];

// on hover - change for hover and then again when mouse moves off
hover.addEventListener("mouseover", function() {
  hover.textContent = "Hello there :^)"
  hover.style.color = "blue";
})

hover.addEventListener("mouseout", function(){
  hover.textContent = "HOVER OVER ME!";
  hover.style.color = 'black';
})

// on click
click.addEventListener('click', function(){
  click.textContent += ' redrum '
  click.style.color = "red";
})


// double click... pretty straightforward
doubleClick.addEventListener("dblclick", function(){
  doubleClick.innerHTML = "<strong>W H O A</strong>"
  doubleClick.style.color = "green"
})
