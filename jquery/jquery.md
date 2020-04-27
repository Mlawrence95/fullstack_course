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
```

### Form data
```javascript
$('input') // get all elements having an input tag
```
