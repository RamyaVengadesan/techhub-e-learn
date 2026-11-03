"""Printable cheat sheets. Items are written one per line as   code :: description"""


def _s(title, text):
    items = []
    for line in text.strip().splitlines():
        code, desc = [p.strip() for p in line.split(" :: ", 1)]
        items.append(dict(code=code, desc=desc))
    return dict(title=title, items=items)


CHEATSHEETS = [
    dict(slug="html-essentials", module="html", title="HTML Essentials", intro="The tags and attributes you will use in almost every page.", sections=[
        _s("Page skeleton", """
<!DOCTYPE html> :: Declare an HTML5 document
<html lang="en"> :: Root element with a language
<meta charset="UTF-8"> :: Character encoding
<meta name="viewport" content="width=device-width, initial-scale=1"> :: Responsive scaling on phones
<title>Page title</title> :: Tab and search result title
<link rel="stylesheet" href="style.css"> :: Attach a stylesheet
<script src="app.js" defer></script> :: Load a script after parsing
"""),
        _s("Text", """
<h1> to <h6> :: Headings, most to least important
<p> :: Paragraph
<br> / <hr> :: Line break / thematic break
<strong> / <em> :: Important / emphasised text
<blockquote> / <q> :: Block / inline quotation
<code> / <pre> :: Inline code / preformatted text
<span> :: Generic inline container
<div> :: Generic block container
"""),
        _s("Links and media", """
<a href="url"> :: Link
<a href="#id"> :: Link to a place on the same page
<a href="mailto:x@y.com"> :: Email link
<a target="_blank" rel="noopener"> :: Open in a new tab safely
<img src="a.jpg" alt="description"> :: Image with text alternative
<picture><source><img></picture> :: Responsive image sources
<video controls src="v.mp4"> :: Video player
<audio controls src="a.mp3"> :: Audio player
<iframe src="url" title="..."> :: Embed another page
"""),
        _s("Lists", """
<ul><li>Item</li></ul> :: Bulleted list
<ol><li>Item</li></ol> :: Numbered list
<dl><dt>Term</dt><dd>Meaning</dd></dl> :: Description list
<ol start="5" reversed> :: Start number / reverse order
"""),
        _s("Tables", """
<table> :: Table container
<tr> :: Row
<th scope="col"> :: Header cell
<td> :: Data cell
<caption> :: Table title
colspan="2" / rowspan="2" :: Span columns / rows
<thead> <tbody> <tfoot> :: Group rows
"""),
        _s("Forms", """
<form action="/send" method="post"> :: Form container
<label for="id"> :: Label tied to an input id
<input type="text" name="n"> :: Text field
type="email" / "password" / "number" / "date" :: Common input types
type="checkbox" / "radio" :: Choices
<select><option> :: Drop-down list
<textarea rows="4"> :: Multi-line text
<button type="submit"> :: Submit button
required, min, max, pattern :: Built-in validation
placeholder, autocomplete, disabled :: Helpful input attributes
"""),
        _s("Semantic layout", """
<header> :: Intro or top of page or section
<nav> :: Navigation links
<main> :: Main content, once per page
<section> :: Themed group of content
<article> :: Self-contained piece
<aside> :: Side content
<footer> :: Bottom of page or section
<figure><figcaption> :: Media with a caption
"""),
        _s("Global attributes", """
id="x" :: Unique identifier
class="a b" :: One or more class names
style="color: red" :: Inline CSS
title="tip" :: Tooltip text
hidden :: Hide an element
data-id="5" :: Custom data
tabindex="0" :: Make focusable
aria-label="Close" :: Accessible name
"""),
    ]),
    dict(slug="css-essentials", module="css", title="CSS Essentials", intro="Selectors, the box model, text and colours at a glance.", sections=[
        _s("Selectors", """
p :: Every paragraph
.card :: Class
#main :: Id
a[href^="https"] :: Attribute starts with
ul li :: Descendant
ul > li :: Direct child
h2 + p :: Next sibling
h2 ~ p :: Later siblings
a:hover :: Mouse over
li:nth-child(2n) :: Even items
p::first-line :: Pseudo-element
:is(h1, h2) :: Match any in the list
"""),
        _s("Box model", """
width / height :: Content size
padding: 10px 20px :: Space inside (vertical horizontal)
border: 1px solid #ccc :: Border shorthand
margin: 0 auto :: Centre a block horizontally
box-sizing: border-box :: Include padding and border in width
border-radius: 8px :: Rounded corners
box-shadow: 0 2px 6px rgba(0,0,0,.2) :: Drop shadow
outline: 2px solid blue :: Outline without taking space
"""),
        _s("Text and fonts", """
color: #1d4ed8 :: Text colour
font-family: system-ui, sans-serif :: Font stack
font-size: 1rem :: Text size
font-weight: 700 :: Boldness
line-height: 1.6 :: Line spacing
text-align: center :: Horizontal alignment
text-decoration: none :: Remove underline
text-transform: uppercase :: Change case
letter-spacing: .05em :: Space between letters
"""),
        _s("Backgrounds and colour", """
background: #fff url(a.png) no-repeat :: Background shorthand
background-size: cover :: Scale to fill
linear-gradient(to right, red, blue) :: Gradient image
opacity: .5 :: Transparency of the whole element
rgb(29 78 216 / 50%) :: Colour with alpha
hsl(220 80% 50%) :: Hue, saturation, lightness
"""),
        _s("Display and position", """
display: block | inline | inline-block | none :: How the box flows
position: relative | absolute | fixed | sticky :: Positioning scheme
top / right / bottom / left :: Offsets
z-index: 10 :: Stacking order
overflow: hidden | auto | scroll :: Clip or scroll extra content
visibility: hidden :: Hide but keep space
"""),
        _s("Units", """
px :: Pixels
rem :: Relative to the root font size
em :: Relative to the element's font size
% :: Percent of the parent
vw / vh :: 1% of viewport width / height
ch :: Width of the character 0
fr :: Fraction of free grid space
"""),
        _s("Effects", """
transition: all .2s ease :: Animate between states
transform: translateY(-4px) scale(1.05) :: Move, scale, rotate
@keyframes spin { to { rotate: 360deg } } :: Define an animation
animation: spin 1s linear infinite :: Run an animation
filter: blur(4px) grayscale(1) :: Visual filters
cursor: pointer :: Hand cursor
"""),
        _s("Responsive", """
@media (min-width: 768px) { ... } :: Rules for wider screens
@media (prefers-color-scheme: dark) :: Dark mode rules
max-width: 100% :: Keep media inside its box
clamp(1rem, 2.5vw, 2rem) :: Fluid size with limits
:root { --brand: #1d4ed8 } :: Define a custom property
color: var(--brand) :: Use a custom property
"""),
    ]),
    dict(slug="css-flexbox-grid", module="css", title="Flexbox and Grid", intro="The two modern layout systems side by side.", sections=[
        _s("Flex container", """
display: flex :: Start a flex layout
flex-direction: row | column :: Main axis direction
justify-content: space-between :: Align along the main axis
align-items: center :: Align along the cross axis
flex-wrap: wrap :: Allow items to wrap
gap: 16px :: Space between items
align-content: center :: Align wrapped lines
"""),
        _s("Flex items", """
flex: 1 :: Grow to share free space
flex-grow / flex-shrink / flex-basis :: The three parts of flex
align-self: flex-end :: Override alignment for one item
order: -1 :: Change visual order
margin-left: auto :: Push an item to the end
"""),
        _s("Flex patterns", """
display:flex; justify-content:center; align-items:center :: Centre anything
display:flex; gap:12px; flex-wrap:wrap :: Wrapping row of cards
nav { display:flex; justify-content:space-between } :: Logo left, links right
.sidebar{flex:0 0 240px} .main{flex:1} :: Fixed sidebar, flexible content
"""),
        _s("Grid container", """
display: grid :: Start a grid layout
grid-template-columns: 1fr 2fr 1fr :: Three columns
grid-template-columns: repeat(3, 1fr) :: Three equal columns
grid-template-rows: auto 1fr auto :: Header, content, footer rows
gap: 16px :: Row and column gap
place-items: center :: Centre items in their cells
grid-template-areas: "h h" "s m" :: Name regions
"""),
        _s("Grid items", """
grid-column: 1 / 3 :: Span from line 1 to line 3
grid-column: span 2 :: Span two columns
grid-row: 2 / 4 :: Span rows
grid-area: header :: Place in a named area
justify-self / align-self :: Align one item in its cell
"""),
        _s("Responsive grids", """
repeat(auto-fit, minmax(220px, 1fr)) :: As many columns as fit
repeat(auto-fill, 100px) :: Fixed tracks that fill the row
minmax(0, 1fr) :: Equal columns that cannot overflow
grid-auto-flow: dense :: Fill gaps automatically
subgrid :: Inherit parent tracks
"""),
        _s("Which one?", """
One direction (row or column) :: Use flexbox
Rows and columns together :: Use grid
Content decides the size :: Flexbox
Layout decides the size :: Grid
Both can nest inside each other :: Combine them
"""),
    ]),
    dict(slug="js-essentials", module="js", title="JavaScript Essentials", intro="Core syntax, control flow, functions and the DOM.", sections=[
        _s("Variables and types", """
const x = 1; :: Cannot be reassigned
let y = 2; :: Can be reassigned
typeof x :: "number", "string", "boolean", "object", "undefined", "function"
null / undefined :: Empty on purpose / not set
Number("42") / String(42) :: Convert types
`Hello ${name}` :: Template literal
"""),
        _s("Operators", """
+ - * / % ** :: Arithmetic
=== / !== :: Strict equality (prefer these)
&& || ! :: And, or, not
?? :: Use the right side only if left is null or undefined
a ? b : c :: Ternary
x?.y :: Optional chaining
"""),
        _s("Control flow", """
if (a) { } else if (b) { } else { } :: Conditions
switch (v) { case 1: ...; break; default: ... } :: Many branches
for (let i = 0; i < 5; i++) { } :: Counting loop
for (const x of list) { } :: Loop over values
for (const k in obj) { } :: Loop over keys
while (cond) { } :: Loop while true
break / continue :: Leave / skip an iteration
"""),
        _s("Functions", """
function add(a, b) { return a + b; } :: Declaration
const add = (a, b) => a + b; :: Arrow function
function f(a, b = 2) { } :: Default parameter
function f(...args) { } :: Rest parameters
setTimeout(fn, 500); :: Run once later
setInterval(fn, 1000); :: Run repeatedly
"""),
        _s("Objects and classes", """
const o = { a: 1, b: 2 }; :: Object literal
o.a / o["a"] :: Read a property
const { a, b } = o; :: Destructuring
const copy = { ...o, c: 3 }; :: Spread copy
Object.keys(o) / Object.entries(o) :: Keys / pairs
class A { constructor() { } method() { } } :: Class
JSON.stringify(o) / JSON.parse(s) :: To and from JSON text
"""),
        _s("DOM", """
document.querySelector(".a") :: First match
document.querySelectorAll("li") :: All matches
el.textContent = "Hi" :: Set text safely
el.classList.toggle("on") :: Add or remove a class
el.setAttribute("href", "#") :: Set an attribute
document.createElement("li") :: Make an element
parent.append(child) :: Add to the page
el.addEventListener("click", fn) :: Listen for events
"""),
        _s("Async", """
fetch(url).then(r => r.json()) :: Request JSON
async function f() { const r = await fetch(url); } :: Async function
try { } catch (e) { } finally { } :: Handle errors
new Promise((res, rej) => { }) :: Create a promise
Promise.all([a, b]) :: Wait for all
"""),
    ]),
    dict(slug="js-arrays-strings", module="js", title="Arrays and Strings", intro="The methods you will reach for every day.", sections=[
        _s("Array basics", """
arr.length :: Number of items
arr.push(x) / arr.pop() :: Add / remove at the end
arr.unshift(x) / arr.shift() :: Add / remove at the start
arr.slice(1, 3) :: Copy a part, original unchanged
arr.splice(1, 2) :: Remove items, changes original
arr.concat(b) / [...a, ...b] :: Join arrays
arr.includes(x) :: Is it in the array?
arr.indexOf(x) :: Position or -1
arr.join(", ") :: Array to string
Array.isArray(x) :: Is it an array?
"""),
        _s("Transform arrays", """
arr.map(x => x * 2) :: New array, same length
arr.filter(x => x > 2) :: Keep matching items
arr.reduce((sum, x) => sum + x, 0) :: Combine into one value
arr.find(x => x.id === 3) :: First match or undefined
arr.findIndex(fn) :: Index of first match
arr.some(fn) / arr.every(fn) :: Any / all match
arr.sort((a, b) => a - b) :: Sort numbers
arr.reverse() :: Reverse in place
arr.flat() :: Flatten one level
arr.forEach(fn) :: Run for each item
"""),
        _s("String basics", """
s.length :: Number of characters
s.toUpperCase() / s.toLowerCase() :: Change case
s.trim() :: Remove outer spaces
s.slice(0, 3) :: Part of a string
s.split(",") :: String to array
s.replace("a", "b") :: Replace first match
s.replaceAll("a", "b") :: Replace every match
s.includes("x") :: Contains?
s.startsWith("a") / s.endsWith("z") :: Check the ends
s.indexOf("x") :: Position or -1
s.padStart(5, "0") :: Pad to a length
s.repeat(3) :: Repeat text
s.at(-1) :: Last character
"""),
        _s("Numbers and Math", """
Math.round(2.5) / Math.floor(2.9) / Math.ceil(2.1) :: Rounding
Math.max(1, 5) / Math.min(1, 5) :: Largest / smallest
Math.random() :: 0 up to but not including 1
Math.floor(Math.random() * 10) :: Random whole number 0 to 9
Math.abs(-3) :: Absolute value
(3.14159).toFixed(2) :: Format decimals as text
parseInt("42px") / parseFloat("3.5") :: Read numbers from text
Number.isNaN(x) :: Is it NaN?
"""),
        _s("Dates", """
new Date() :: Now
new Date("2026-01-31") :: From a string
d.getFullYear() / d.getMonth() / d.getDate() :: Year, month (0-11), day
d.getTime() :: Milliseconds since 1970
d.toLocaleDateString("en-IN") :: Formatted date
"""),
    ]),
]
