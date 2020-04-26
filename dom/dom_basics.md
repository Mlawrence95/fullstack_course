# document object model

### accessing DOM
```javascript
console.dir(document) // dumps DOM as a json object (JSON)
```
### basic helper methods
```javascript
document.URL = url of the site
document.body = html in the body
document.head = everything in head of html
document.links = all links on a site
```
### selectors
```javascript
document.getElementById()
document.getElementByClassName()
document.getElementsByTagName()

// Get first item having css style passed (# for id, . for class, etc)
document.querySelector()

// Get all items having css style passed
document.querySelectorAll()
```

### extract info from tags
```javascript
// This would get the third list element on the page, and show its text context
document.getElementsByTagName("li")[2].innerHTML
```

### manipulate a tag
```javascript
// change header to red
var myHeader = document.querySelector("h1")
myHeader.style.color = "red"

// run function on a timer (Alert "Hello" every 3000 milliseconds)
setInterval(function(){ alert("Hello"); }, 3000);
```

### changing text
#### use innerHTML to tag changes, textContent for text
```javascript
var par = document.querySelector("p")
par.textContent = "new stuff"
par.innerHTML = "<strong>new stuff</strong>"
```

### getting nested content
```javascript
var special = document.querySelector("#special")
var nestedLink = special.querySelector("a")

nestedLink.getAttribute('href')
"https://www.facebook.com"

nestedLink.setAttribute('href', "http://www.amazon.com")
nestedLink.getAttribute('href')
"http://www.amazon.com"
```

### Events
Events include hover, click, double click, drags, and more. We handle them
with events listeners.
```javascript
var head = document.querySelector('h1');
head.addEventListener("click", changeColor);
```
