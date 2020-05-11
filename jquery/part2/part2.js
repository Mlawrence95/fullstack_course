$("li").click(function() {
  console.log(this.innerText)
})

$("li").dblclick(function() {
  $(this).text("The old text has been erased!")
})

$("input").eq(0).keypress(function(event) {
  console.log(event);
  if (event.which == 13) {
    $("h3").toggleClass("turnBlue")
  }
})

$("h1").on("dblclick", function(event) {
  $(this).toggleClass("turnBlue")
})
