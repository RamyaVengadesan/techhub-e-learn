"""Glossary. One term per line:  term :: definition :: module :: lesson-slug (lesson optional)"""

_RAW = """
Accessibility :: Designing pages so everyone can use them, including people who use screen readers, keyboards or zoom. :: general :: accessibility
Alt text :: A short text description of an image, read aloud by screen readers and shown if the image fails to load. :: html :: images
Animation :: Changing styles gradually over time, in CSS with `@keyframes` and the `animation` property. :: css :: css-animations
API :: A set of rules that lets one program talk to another, for example a server sending data to your page. :: general :: js-fetch
Argument :: A value you pass to a function when you call it. :: js :: js-parameters
Array :: An ordered list of values, written with square brackets. :: js :: js-arrays
Arrow function :: A short way to write a function using `=>`. :: js :: js-arrow-functions
Asynchronous :: Code that starts now and finishes later, so the rest of the program does not wait. :: js :: js-async-await
Attribute :: Extra information inside an HTML opening tag, such as `href` or `class`. :: html :: attributes
Async/await :: Syntax that lets asynchronous code read like normal top-to-bottom code. :: js :: js-async-await
Background :: The colour or image behind an element's content, set with the CSS `background` properties. :: css :: css-backgrounds
Block element :: An element that starts on a new line and takes the full available width, such as a paragraph. :: html :: block-inline
Boolean :: A value that is either `true` or `false`. :: js :: js-data-types
Border :: A line drawn around an element's padding. :: css :: css-borders
Box model :: The way CSS sizes every element as content, padding, border and margin. :: css :: css-box-model
Breakpoint :: A screen width at which a responsive layout changes, usually set in a media query. :: css :: css-media-queries
Browser :: The program that downloads web pages and displays them, such as Chrome, Firefox or Safari. :: general
Cache :: A stored copy of a file so it loads faster the next time. :: general
Callback :: A function passed to another function to be called later. :: js :: js-callbacks
Cascade :: The rules CSS uses to decide which style wins when several rules apply. :: css :: css-inheritance-cascade
Class :: In HTML, a label you can reuse on many elements and style in CSS. In JavaScript, a blueprint for making objects. :: general :: classes
Client :: The device and browser a visitor uses, as opposed to the server. :: general
Closure :: A function that remembers the variables from the place where it was created. :: js :: js-closures
Comment :: Text in code that the computer ignores, written for people. :: general :: comments
Compiler :: A tool that translates code into another form. Browsers do not need one for plain HTML, CSS and JavaScript. :: general
Component :: A reusable piece of an interface, such as a button or card. :: general
Console :: The developer tool where JavaScript prints messages and errors. :: js :: js-debugging
Constant :: A variable declared with `const` that cannot be reassigned. :: js :: js-variables
Cookie :: A small piece of data a website stores in your browser. :: general
CSS :: Cascading Style Sheets, the language that controls how HTML looks. :: css :: css-intro
Custom property :: A CSS variable written with two dashes, such as `--brand`, and read with `var()`. :: css :: css-variables
Data attribute :: A custom HTML attribute starting with `data-` that stores extra information on an element. :: html :: data-attributes
Debugging :: Finding and fixing mistakes in code. :: general :: js-debugging
Declaration :: One CSS instruction made of a property and a value, such as `color: red`. :: css :: css-syntax
Deploy :: To publish your website so other people can visit it. :: general
Destructuring :: A short way to pull values out of arrays or objects into variables. :: js :: js-destructuring
DevTools :: Tools built into the browser to inspect HTML, edit CSS, run JavaScript and find problems. :: general :: js-debugging
DOCTYPE :: The first line of an HTML page that tells the browser it is a modern HTML document. :: html :: structure
DOM :: The Document Object Model, the browser's live tree of elements that JavaScript can read and change. :: js :: js-dom-intro
Domain name :: The human-friendly address of a website, such as `example.com`. :: general
Element :: A part of an HTML page made of a start tag, content and an end tag. :: html :: elements
Em :: A CSS unit relative to the font size of the element. :: css :: css-units
Entity :: A code such as `&amp;` that displays a special character in HTML. :: html :: entities
Event :: Something that happens on a page, such as a click or a key press, that JavaScript can react to. :: js :: js-events
Event listener :: A function that waits for a specific event and runs when it happens. :: js :: js-event-listener
Favicon :: The small icon shown on a browser tab. :: html :: favicon
Fetch :: The browser feature for requesting data from a server. :: js :: js-fetch
Flexbox :: A CSS layout system for arranging items in a row or column. :: css :: css-flexbox
Float :: An older CSS property that pushes an element to the left or right so text wraps around it. :: css :: css-float
Font stack :: A list of fonts in order of preference, so the browser can fall back if one is missing. :: css :: css-font-stacks
Form :: A group of inputs that lets visitors send information. :: html :: forms
Framework :: A large toolkit that decides how you structure an application, for example React. :: general
Front end :: The part of a website that people see and use in the browser. :: general
Function :: A reusable block of code that you can run by calling its name. :: js :: js-functions
Git :: A tool that records the history of your code so you can undo changes and collaborate. :: general
GitHub :: A website for storing Git projects online and sharing them. :: general
Grid :: A CSS layout system for arranging items in rows and columns together. :: css :: css-grid
Head :: The part of an HTML page holding information about the page, such as its title. :: html :: head-elements
Heading :: A title element from `<h1>` to `<h6>` that outlines the page. :: html :: headings
Hosting :: A service that stores your website files and serves them to visitors. :: general
Hover :: When the mouse pointer is over an element, which CSS can style with `:hover`. :: css :: css-pseudo-classes
HTML :: HyperText Markup Language, the language that gives web pages their structure. :: html :: intro
HTTP :: The set of rules browsers and servers use to exchange web pages. HTTPS is the secure version. :: general
Hyperlink :: A clickable element that takes you to another page or place, made with `<a>`. :: html :: links
Id :: A unique name for one element in a page. :: html :: id
Inheritance :: When an element receives some style values, such as colour and font, from its parent. :: css :: css-inheritance-cascade
Inline element :: An element that stays inside a line of text, such as a link. :: html :: block-inline
Input :: A form control where visitors type or choose information. :: html :: input-types
JavaScript :: The programming language that makes web pages interactive. :: js :: js-intro
JSON :: A text format for sending structured data, written like JavaScript objects. :: js :: js-json
Keyframes :: The `@keyframes` rule that defines the steps of a CSS animation. :: css :: css-animations
Label :: Text linked to a form input so that clicking it focuses the input and screen readers can announce it. :: html :: form-elements
Layout :: How elements are arranged on the page. :: general :: layout
Library :: A collection of ready-made code you can use in your own project. :: general
Lazy loading :: Waiting to load an image until the visitor scrolls near it. :: html :: responsive-lazy-images
Loop :: Code that repeats while a condition is true. :: js :: js-loops
Margin :: The empty space outside an element's border. :: css :: css-margins
Markup :: Text with tags that describe the structure of content, as in HTML. :: html
Media query :: A CSS rule that applies styles only when conditions such as screen width are met. :: css :: css-media-queries
Meta tag :: A tag in the head that describes the page to browsers and search engines. :: html :: head-elements
Method :: A function that belongs to an object, such as `array.push()`. :: js :: js-object-methods
Mobile first :: Designing for small screens first, then adding styles for larger ones. :: css :: css-mobile-first
Module :: A JavaScript file that exports code for other files to import. :: js :: js-modules
Nesting :: Placing one element, list or rule inside another. :: general :: nested-lists
Node :: Any item in the DOM tree, such as an element or a piece of text. :: js :: js-dom-intro
Null :: A value that means "nothing" on purpose. :: js :: js-data-types
Object :: A collection of named values called properties. :: js :: js-objects
Open Graph :: Meta tags that control how a page looks when shared on social networks. :: html :: open-graph-json-ld
Padding :: The space between an element's content and its border. :: css :: css-padding
Parameter :: A named variable in a function definition that receives an argument. :: js :: js-parameters
Placeholder :: Hint text shown inside an empty input. :: html :: input-attributes
Position :: The CSS property that controls how an element is placed: static, relative, absolute, fixed or sticky. :: css :: css-position
Promise :: An object that represents a result that will arrive later. :: js :: js-promises
Property :: In CSS, the name of a style such as `color`. In JavaScript, a named value on an object. :: general
Pseudo-class :: A keyword added to a selector for a special state, such as `:hover`. :: css :: css-pseudo-classes
Pseudo-element :: A keyword that styles part of an element, such as `::before`. :: css :: css-pseudo-elements
Rem :: A CSS unit relative to the font size of the root element. :: css :: css-units
Repository :: A project folder tracked by Git. :: general
Responsive design :: Building pages that adapt to any screen size. :: css :: css-media-queries
Root :: The top-level element of a document, `<html>`. :: html :: structure
Scope :: The part of a program where a variable can be used. :: js :: js-scope
Selector :: The part of a CSS rule that chooses which elements to style. :: css :: css-selectors-basic
Semantic HTML :: Using elements that describe their meaning, such as `<nav>` and `<article>`. :: html :: semantic
SEO :: Search engine optimisation, improving a page so search engines can find and understand it. :: general :: seo
Server :: A computer that stores website files and sends them to browsers on request. :: general
Specificity :: The scoring CSS uses to decide which selector wins when rules conflict. :: css :: css-specificity
String :: Text in JavaScript, written in quotes. :: js :: js-strings
Tag :: The code in angle brackets that starts or ends an HTML element, such as `<p>`. :: html :: elements
Template literal :: A string written with backticks that can contain `${values}`. :: js :: js-template-literals
Transition :: A smooth change between two CSS states over a short time. :: css :: css-transitions
URL :: The address of a page or file on the web. :: general :: url-encoding
Variable :: A named container for a value. :: js :: js-variables
Viewport :: The visible area of a web page in the browser window. :: html :: responsive
Z-index :: A CSS property that controls which overlapping element appears on top. :: css :: css-z-index
"""


def _build():
    out = []
    for line in _RAW.strip().splitlines():
        parts = [p.strip() for p in line.split(" :: ")]
        parts += [""] * (4 - len(parts))
        term, definition, module, lesson = parts[:4]
        item = dict(term=term, definition=definition, module=module or "general")
        if lesson:
            item["lesson"] = lesson
        out.append(item)
    return sorted(out, key=lambda t: t["term"].lower())


GLOSSARY = _build()
