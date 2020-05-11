# jQuery

jQuery streamlines interactions with the DOM that would typically be done with
vanilla js, such as extracting elements by id, tag, or class.

To include jQuery, use a `<script>` tag with `src` pointed at the jQuery download path. Bootstrap has one such example in their js bundle. Traditional wisdom (google) suggests placing all such `script` calls before the closing `body` tag.

### Selecting elements

```javascript
$("li")    // select all items having the li tag
$("#nice") // select all items having the "nice" id
$(".cool") // select all items having the class "cool"
```


### Altering CSS
```javascript
// make the text of ALL li pink
$("li").css("color", "pink")

// make the background color of all paragraphs red
var x = $("p")
x.css("background", "red")

// changes the above x variable's CSS in bulk
var newCSS = {
  'color': 'white',
  'background': 'blue',
  'border': '20px solid red'
}
x.css(newCSS)

// use indexing to change a particular elements -- eq(1) ~ array[1]
x.eq(1).css("background", "pink")

// grab the LAST element in x
x.eq(-1).css("background", "orange")
```

### Altering text and inner HTML
```javascript
// change the text of an element
$('p').eq(0).text() //returns current value
$('p').eq(0).text("This changes the current value")

// alter inner html
$('p').eq(0).html()
$('p').eq(0).html("<em>New, emphasized value</em>")

// alter attributes -- this changes every li id to "mike"
$("li").attr("id", "mike")

// this changes the second input to a checkbox
$('input').eq(1).attr("type", 'checkbox')


// change the value attribute
$('input').eq(1).val('new value')
```

### Classes (CSS)
These are useful for creating dynamic behavior, as changing the class for an element means that the styling reference also changes.
```javascript
$('h1').addClass("turnRed")
$("h1").removeClass("turnRed")

// use toggle to keep track of state
$("h1").toggleClass("turnRed")
```

### Events

The basics of events are all listed [here](https://api.jquery.com/category/events/).

#### On click actions
This example makes each `li` elements log its context to console if it get clicked.
```javascript
$("li").click(function() {
  console.log(this.innerText)
})
```

This example is used to change all list elements.
```javascript
$("li").dblclick(function() {
  $(this).text("The old text has been erased!")
})
```
#### Key Presses

This example toggles a class on and off for a heading based on keypresses inside of the first form (`eq(0)`).

```javascript
$("input").eq(0).keypress(function() {
  $("h3").toggleClass("turnBlue")
})
```

#### The `event` keyword
`event` is a default arg that can be passed leveraged in event functions. For example, the following code will log all of the event metadata associated with a keypress. Note the `which` field in the resulting logged object, which provides the index of the input keypress.

```javascript
$("input").eq(0).keypress(function(event) {
  console.log(event);
})
```

This allows code like the following, in which the toggle case is only activated when an `enter` keypress event is detected -- index 13 for the `which` field. The whole set of ascii indices can be found [here](http://www.asciitable.com/).
```javascript
$("input").eq(0).keypress(function(event) {
  console.log(event);
  if (event.which == 13) {
    $("h3").toggleClass("turnBlue")
  }
})
```

#### The `on` method

Essentially the same functionality as vanilla `addEventListener`. Use like:
```javascript
$("h1").on("dblclick", function(event) {
  $(this).toggleClass("turnBlue")
})
```

or, for hover,
```javascript
$("h1").on("mouseenter", function(event) {
  $(this).toggleClass("turnBlue")
})
```

### Animations
Warning: this section may not work with the slim version of jQuery. Evidence of this may include a message in console suggesting that function/method being called is undefined. See [here](https://api.jquery.com/category/effects/) for more info on effects and animations.

Example usage:

```javascript
// this selects the submit button, making the page fade on click
$("input").eq(1).click(function(event){
  console.log(event);
  $('.container').fadeOut(300);
});

```
