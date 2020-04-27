# Document Object Model (the DOM)

### Accessing DOM
```javascript
console.dir(document) // dumps DOM as a json object (JSON)
```
### Basic helper methods
```javascript
document.URL // url of the site
document.body // html in the body
document.head // everything in head of html
document.links // all links on a site
```
### Selectors
```javascript
document.getElementById()
document.getElementByClassName()
document.getElementsByTagName()

// Get first item having css style passed (# for id, . for class, etc)
document.querySelector()

// Get all items having css style passed
document.querySelectorAll()
```

### Extract info from tags
```javascript
// This would get the third list element on the page, and show its text context
document.getElementsByTagName("li")[2].innerHTML
```

### Manipulate a tag
```javascript
// change header to red
var myHeader = document.querySelector("h1")
myHeader.style.color = "red"

// run function on a timer (Alert "Hello" every 3000 milliseconds)
setInterval(function(){ alert("Hello"); }, 3000);
```

### Changing text
#### Use innerHTML to tag changes, textContent for text
```javascript
var par = document.querySelector("p")
par.textContent = "new stuff"
par.innerHTML = "<strong>new stuff</strong>"
```

### Getting nested content
```javascript
var special = document.querySelector("#special")
var nestedLink = special.querySelector("a")

nestedLink.getAttribute('href')
// "https://www.facebook.com"

nestedLink.setAttribute('href', "http://www.amazon.com")
nestedLink.getAttribute('href')
// "http://www.amazon.com"
```

### Events
Events include hover, click, double click, drags, and more. We handle them
with events listeners.
```javascript
// if youve written a changeColor function
var head = document.querySelector('h1');
head.addEventListener("click", changeColor);

// alternative example from mozilla docs
const btn = document.querySelector('button');

function random(number) {
  return Math.floor(Math.random() * (number+1));
}

btn.onclick = function() {
  const rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
  document.body.style.backgroundColor = rndCol;
}
```
