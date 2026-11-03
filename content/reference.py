"""Reference tables (W3Schools style): HTML tags, attributes and events, CSS properties, selectors and
functions, JavaScript and DOM reference.

Each page: slug, module, title, intro, cols, groups[{name, items[{name, desc, extra?, lesson?}]}].
To keep this file readable, items are written one per line as   name :: description :: extra :: lesson
(extra and lesson are optional; leave extra empty for two-column pages).
"""

import re


def _items(text):
    out = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in re.split(r"\s+::(?=\s|$)", line)]
        parts += [""] * (4 - len(parts))
        name, desc, extra, lesson = parts[:4]
        item = dict(name=name, desc=desc)
        if extra:
            item["extra"] = extra
        if lesson:
            item["lesson"] = lesson
        out.append(item)
    return out


def _groups(spec):
    return [dict(name=name, items=_items(text)) for name, text in spec]


# ============================================================================ HTML tags
HTML_TAGS = [
    ("Basic", """
<!DOCTYPE> :: Declares that the document is HTML5. :: :: structure
<html> :: The root element of an HTML page. :: :: structure
<head> :: Holds metadata about the page, such as the title and links to stylesheets. :: :: head-elements
<title> :: Sets the page title shown on the browser tab. :: :: head-elements
<body> :: Holds all the visible content of the page. :: :: structure
<h1> to <h6> :: Headings, from most important (`h1`) to least important (`h6`). :: :: headings
<p> :: Defines a paragraph. :: :: paragraphs
<br> :: Inserts a single line break. :: :: paragraphs
<hr> :: A thematic break between paragraph-level content, drawn as a horizontal line. :: :: paragraphs
<!--...--> :: A comment that the browser does not display. :: :: comments
"""),
    ("Formatting", """
<abbr> :: An abbreviation or acronym; `title` can give the full text. :: :: quotations
<address> :: Contact information for the author of a page or article. :: :: quotations
<b> :: Draws attention to text without adding extra importance. :: :: formatting
<bdi> :: Isolates text that may be formatted in a different direction from the text around it.
<bdo> :: Overrides the current text direction.
<blockquote> :: A section quoted from another source. :: :: quotations
<cite> :: The title of a creative work, such as a book or film. :: :: quotations
<code> :: A fragment of computer code. :: :: code-elements
<del> :: Text that was deleted from the document. :: :: formatting
<dfn> :: The term being defined.
<em> :: Emphasised text, usually shown in italics. :: :: formatting
<i> :: Text in an alternate voice or mood, usually shown in italics. :: :: formatting
<ins> :: Text that was inserted into the document. :: :: formatting
<kbd> :: Keyboard input. :: :: code-elements
<mark> :: Text highlighted for reference. :: :: formatting
<pre> :: Preformatted text that keeps spaces and line breaks. :: :: paragraphs
<q> :: A short inline quotation. :: :: quotations
<rp> :: Fallback parentheses for browsers that do not support ruby annotations.
<rt> :: The pronunciation or explanation of the characters in a ruby annotation.
<ruby> :: A ruby annotation, used for East Asian typography.
<s> :: Text that is no longer accurate or relevant. :: :: formatting
<samp> :: Sample output from a computer program. :: :: code-elements
<small> :: Side comments and small print. :: :: formatting
<strong> :: Text of strong importance, usually shown in bold. :: :: formatting
<sub> :: Subscript text. :: :: formatting
<sup> :: Superscript text. :: :: formatting
<time> :: A specific time or date in a machine-readable form.
<u> :: Text with an unarticulated annotation, usually shown underlined. :: :: formatting
<var> :: A variable in a mathematical expression or program. :: :: code-elements
<wbr> :: A position where the browser may break a long word.
"""),
    ("Forms and Input", """
<form> :: A form that collects input from the user. :: :: forms
<input> :: An input control; its `type` decides what it is. :: :: input-types
<textarea> :: A multi-line text input. :: :: form-elements
<button> :: A clickable button. :: :: form-elements
<select> :: A drop-down list. :: :: form-elements
<optgroup> :: A group of related options in a drop-down list. :: :: form-elements
<option> :: An option in a `select`, `optgroup` or `datalist`. :: :: form-elements
<label> :: A label for a form control. :: :: forms
<fieldset> :: Groups related controls inside a form. :: :: form-elements
<legend> :: A caption for a `fieldset`. :: :: form-elements
<datalist> :: A list of suggested values for an `input`. :: :: datalist
<output> :: The result of a calculation or user action.
"""),
    ("Frames", """
<iframe> :: Embeds another HTML page inside the current page. :: :: iframes
"""),
    ("Images", """
<img> :: Embeds an image. :: :: images
<map> :: An image map with clickable areas. :: :: image-maps
<area> :: A clickable area inside an image map. :: :: image-maps
<canvas> :: A drawing area that scripts can paint on. :: :: canvas
<figure> :: Self-contained content, such as an image with a caption. :: :: images
<figcaption> :: A caption for a `figure`. :: :: images
<picture> :: A container that offers several image sources for different conditions. :: :: picture
<svg> :: A container for scalable vector graphics. :: :: svg
"""),
    ("Audio and Video", """
<audio> :: Embeds sound content. :: :: audio
<video> :: Embeds a video. :: :: video
<source> :: A media resource for `audio`, `video` or `picture`. :: :: video
<track> :: Text tracks such as subtitles for `audio` and `video`. :: :: video
<embed> :: A container for external content, such as a plug-in. :: :: embedding
<object> :: An embedded object, such as a PDF or another page. :: :: embedding
<param> :: A parameter for an `object` element.
"""),
    ("Links", """
<a> :: A hyperlink to another page, file or location. :: :: links
<link> :: Links the page to an external resource, such as a stylesheet. :: :: head-elements
<nav> :: A set of navigation links. :: :: semantic
"""),
    ("Lists", """
<ul> :: An unordered (bulleted) list. :: :: lists
<ol> :: An ordered (numbered) list. :: :: lists
<li> :: A list item. :: :: lists
<dl> :: A description list. :: :: lists
<dt> :: A term in a description list. :: :: lists
<dd> :: The description of a term in a description list. :: :: lists
<menu> :: A list of commands; browsers treat it like an unordered list.
"""),
    ("Tables", """
<table> :: A table. :: :: tables
<caption> :: A table caption. :: :: table-styling
<th> :: A header cell in a table. :: :: tables
<tr> :: A row in a table. :: :: tables
<td> :: A data cell in a table. :: :: tables
<thead> :: Groups the header rows of a table. :: :: table-styling
<tbody> :: Groups the body rows of a table. :: :: table-styling
<tfoot> :: Groups the footer rows of a table. :: :: table-styling
<col> :: Column properties for a column inside a `colgroup`.
<colgroup> :: Groups one or more columns of a table for formatting.
"""),
    ("Styles and Semantics", """
<style> :: Holds style information (CSS) for the document. :: :: css
<div> :: A generic block container with no meaning of its own. :: :: div-span
<span> :: A generic inline container with no meaning of its own. :: :: div-span
<header> :: Introductory content for a page or section. :: :: semantic
<footer> :: A footer for a page or section. :: :: semantic
<main> :: The main content of the page. :: :: semantic
<section> :: A thematic section of content. :: :: semantic
<article> :: Self-contained content, such as a blog post. :: :: semantic
<aside> :: Content related to the surrounding content, such as a sidebar. :: :: semantic
<details> :: Extra details the user can show or hide. :: :: details-summary
<summary> :: The visible heading of a `details` element. :: :: details-summary
<dialog> :: A dialog box or window. :: :: dialog
<data> :: Links content to a machine-readable value.
<hgroup> :: Groups a heading with related content such as a subheading.
<search> :: Holds the controls of a search or filtering feature.
<progress> :: The progress of a task. :: :: progress-meter
<meter> :: A scalar measurement within a known range. :: :: progress-meter
"""),
    ("Meta Info", """
<head> :: A container for metadata. :: :: head-elements
<meta> :: Metadata about the page, such as the character set, description and viewport. :: :: head-elements
<base> :: The base URL and default target for all relative URLs in the page. :: :: head-elements
"""),
    ("Programming", """
<script> :: Embeds or links to a script. :: :: js-where-to
<noscript> :: Content shown when scripts are turned off.
<template> :: Holds HTML that is not rendered until a script uses it. :: :: web-components
<slot> :: A placeholder inside a web component that you fill with your own markup. :: :: web-components
"""),
    ("Obsolete and Deprecated", """
<acronym> :: Obsolete. Use `abbr` instead.
<applet> :: Obsolete. Use `object` or `embed` instead.
<basefont> :: Obsolete. Use CSS instead.
<big> :: Obsolete. Use CSS `font-size` instead.
<center> :: Obsolete. Use CSS `text-align` instead.
<dir> :: Obsolete. Use `ul` instead.
<font> :: Obsolete. Use CSS font properties instead.
<frame> :: Obsolete. Frames are no longer supported.
<frameset> :: Obsolete. Frames are no longer supported.
<noframes> :: Obsolete. Frames are no longer supported.
<strike> :: Obsolete. Use `del` or `s` instead.
<tt> :: Obsolete. Use `code` or CSS instead.
<marquee> :: Non-standard scrolling text. Use a CSS animation instead.
"""),
]

# ============================================================================ HTML attributes
HTML_ATTRS = [
    ("Global attributes", """
class :: One or more class names, used by CSS and JavaScript. :: All elements :: classes
id :: A unique identifier for the element. :: All elements :: id
style :: Inline CSS for the element. :: All elements :: styles
title :: Extra information, usually shown as a tooltip. :: All elements :: attributes
lang :: The language of the element's content. :: All elements :: attributes
dir :: The text direction: `ltr`, `rtl` or `auto`. :: All elements
hidden :: Hides the element from view. :: All elements
tabindex :: Sets the tab order, or makes an element focusable. :: All elements
accesskey :: A keyboard shortcut to activate or focus the element. :: All elements
contenteditable :: Whether the user can edit the content. :: All elements :: contenteditable
draggable :: Whether the element can be dragged. :: All elements :: drag-drop
spellcheck :: Whether the browser checks spelling and grammar. :: All elements :: contenteditable
translate :: Whether the content should be translated. :: All elements
data-* :: Custom data attributes for storing extra information. :: All elements :: data-attributes
role :: The ARIA role of the element. :: All elements :: aria
aria-* :: ARIA attributes that expose state and relationships to assistive technology. :: All elements :: aria
autofocus :: Focuses the element when the page loads. :: All elements
inert :: Makes the element and its children non-interactive. :: All elements
popover :: Turns the element into a popover. :: All elements :: popover
inputmode :: A hint for which on-screen keyboard to show. :: Editable elements
enterkeyhint :: A hint for the label of the Enter key on virtual keyboards. :: Editable elements
slot :: Assigns the element to a named slot in a web component. :: All elements :: web-components
"""),
    ("Links and media", """
href :: The URL of a link or resource. :: `a`, `area`, `link`, `base` :: links
target :: Where to open the linked document. :: `a`, `area`, `form`, `base` :: link-targets
rel :: The relationship between this page and the linked resource. :: `a`, `area`, `link`
download :: Downloads the target instead of navigating to it. :: `a`, `area`
hreflang :: The language of the linked document. :: `a`, `link`
type :: The media type (MIME type) of the resource. :: `a`, `link`, `script`, `source`
src :: The URL of an external file. :: `img`, `script`, `iframe`, `audio`, `video`, `source`, `track` :: images
alt :: Alternative text for an image. :: `img`, `area`, `input` :: images
width :: The width of the element in pixels. :: `img`, `canvas`, `video`, `iframe`, `input` :: images
height :: The height of the element in pixels. :: `img`, `canvas`, `video`, `iframe`, `input` :: images
srcset :: A list of image sources for different screen sizes. :: `img`, `source` :: responsive-lazy-images
sizes :: The display size of an image for different layouts. :: `img`, `source` :: responsive-lazy-images
loading :: Set to `lazy` to delay loading offscreen images and iframes. :: `img`, `iframe` :: responsive-lazy-images
decoding :: A hint for how the browser should decode an image. :: `img`
crossorigin :: How to handle cross-origin requests for the resource. :: `img`, `script`, `link`, `audio`, `video`
referrerpolicy :: Which referrer information to send when fetching. :: `a`, `img`, `iframe`, `link`, `script`
controls :: Shows playback controls. :: `audio`, `video` :: video
autoplay :: Starts playing as soon as it can. :: `audio`, `video` :: video
loop :: Plays again when it ends. :: `audio`, `video` :: video
muted :: Starts with the sound off. :: `audio`, `video` :: video
poster :: An image shown until the video plays. :: `video` :: video
preload :: How much of the media to load in advance. :: `audio`, `video`
playsinline :: Plays inline instead of full screen on some mobile browsers. :: `video`
usemap :: Connects an image to an image map. :: `img` :: image-maps
sandbox :: Restricts what an embedded page can do. :: `iframe` :: iframe-sandbox
allow :: A permissions policy for an embedded page. :: `iframe`
srcdoc :: HTML content to show inside the frame. :: `iframe` :: iframe-sandbox
"""),
    ("Forms", """
action :: Where to send the form data. :: `form` :: form-attributes
method :: The HTTP method used to send the form data (`get` or `post`). :: `form` :: form-attributes
enctype :: How form data is encoded when sent with `post`. :: `form` :: form-attributes
novalidate :: Skips built-in form validation on submit. :: `form` :: form-validation
name :: The name of the control, sent with the form data. :: `input`, `select`, `textarea`, `button`, `form`, `meta` :: form-attributes
value :: The value of the control. :: `input`, `button`, `option`, `li` :: input-attributes
placeholder :: A hint shown inside an empty field. :: `input`, `textarea` :: input-attributes
required :: The field must be filled in before the form is submitted. :: `input`, `select`, `textarea` :: form-validation
readonly :: The field cannot be edited, but is still submitted. :: `input`, `textarea` :: input-attributes
disabled :: Disables the control. :: `input`, `select`, `textarea`, `button`, `fieldset`, `option` :: input-attributes
checked :: Pre-selects a checkbox or radio button. :: `input` :: input-attributes
selected :: Pre-selects an option. :: `option` :: form-elements
multiple :: Allows more than one value. :: `input`, `select` :: input-attributes
min :: The minimum value. :: `input`, `meter`, `progress` :: input-attributes
max :: The maximum value. :: `input`, `meter`, `progress` :: input-attributes
step :: The allowed number intervals. :: `input` :: input-attributes
minlength :: The minimum number of characters. :: `input`, `textarea` :: form-validation
maxlength :: The maximum number of characters. :: `input`, `textarea` :: input-attributes
pattern :: A regular expression the value must match. :: `input` :: form-validation
autocomplete :: Whether the browser may autofill the field. :: `input`, `form`, `select`, `textarea` :: input-attributes
for :: Connects a label to a control by its `id`. :: `label`, `output` :: forms
form :: Associates the control with a form by its `id`. :: `input`, `button`, `select`, `textarea`, `fieldset`
list :: Connects an input to a `datalist` by its `id`. :: `input` :: datalist
accept :: The file types a file input accepts. :: `input` :: input-attributes
size :: The visible width in characters, or visible options. :: `input`, `select`
rows :: The visible number of lines. :: `textarea` :: form-elements
cols :: The visible width in characters. :: `textarea` :: form-elements
wrap :: How text is wrapped when the form is submitted. :: `textarea`
label :: A label for the option or group. :: `option`, `optgroup`, `track`
"""),
    ("Tables", """
colspan :: The number of columns a cell spans. :: `td`, `th` :: table-spans
rowspan :: The number of rows a cell spans. :: `td`, `th` :: table-spans
headers :: Links a cell to the header cells that describe it. :: `td`
scope :: Whether a header cell applies to a row or a column. :: `th`
span :: The number of columns a `col` spans. :: `col`, `colgroup`
"""),
    ("Other", """
charset :: The character encoding of the document. :: `meta`, `script` :: charset
content :: The value of a `meta` element. :: `meta` :: head-elements
http-equiv :: Provides an HTTP header for the information in `content`. :: `meta`
async :: Runs the script as soon as it is available. :: `script`
defer :: Runs the script after the page has been parsed. :: `script`
integrity :: A hash the browser uses to verify a fetched file. :: `link`, `script`
nonce :: A one-time token used with a Content Security Policy. :: `script`, `style`
open :: Whether the details or dialog is shown. :: `details`, `dialog` :: details-summary
start :: The first number of an ordered list. :: `ol` :: lists
reversed :: Counts an ordered list backwards. :: `ol` :: lists
datetime :: The date and time of the element. :: `time`, `del`, `ins`
cite :: The URL of the source of a quotation or change. :: `blockquote`, `q`, `del`, `ins` :: quotations
media :: The media or device the resource is for. :: `link`, `source`, `style`
nomodule :: Skips the script in browsers that support modules. :: `script`
"""),
]

# ============================================================================ HTML events
HTML_EVENTS = [
    ("Window events", """
onload :: Fires when an element or the page has finished loading.
onbeforeunload :: Fires just before the page is unloaded.
onunload :: Fires when the page is unloaded. Deprecated: use `pagehide` instead.
onpageshow :: Fires when the user navigates to the page.
onpagehide :: Fires when the user navigates away from the page.
onresize :: Fires when the window is resized.
onscroll :: Fires when an element's scrollbar is scrolled.
onhashchange :: Fires when the part of the URL after `#` changes.
onpopstate :: Fires when the history entry changes.
onerror :: Fires when an error occurs while loading a file.
ononline :: Fires when the browser starts to work online.
onoffline :: Fires when the browser starts to work offline.
"""),
    ("Form events", """
onchange :: Fires when the value of an element is committed.
oninput :: Fires when the value of an input changes as the user types.
onfocus :: Fires when an element gets focus.
onblur :: Fires when an element loses focus.
onsubmit :: Fires when a form is submitted.
onreset :: Fires when a form is reset.
onselect :: Fires when text is selected.
oninvalid :: Fires when a form control fails validation.
"""),
    ("Keyboard events", """
onkeydown :: Fires when a key is pressed down.
onkeyup :: Fires when a key is released.
onkeypress :: Fires when a key is pressed. Deprecated: use `keydown` instead.
"""),
    ("Mouse events", """
onclick :: Fires when the element is clicked.
ondblclick :: Fires when the element is double-clicked.
onmousedown :: Fires when a mouse button is pressed on the element.
onmouseup :: Fires when a mouse button is released over the element.
onmousemove :: Fires when the pointer moves over the element.
onmouseover :: Fires when the pointer moves onto the element or one of its children.
onmouseout :: Fires when the pointer moves out of the element or one of its children.
onmouseenter :: Fires when the pointer enters the element, without bubbling.
onmouseleave :: Fires when the pointer leaves the element, without bubbling.
oncontextmenu :: Fires when the right mouse button is clicked to open the context menu.
onwheel :: Fires when the mouse wheel rolls over the element.
"""),
    ("Pointer and touch events", """
onpointerdown :: Fires when a pointer (mouse, pen or touch) becomes active.
onpointerup :: Fires when a pointer is no longer active.
onpointermove :: Fires when a pointer moves.
ontouchstart :: Fires when a finger touches the screen.
ontouchmove :: Fires when a finger moves on the screen.
ontouchend :: Fires when a finger is lifted from the screen.
"""),
    ("Drag events", """
ondrag :: Fires while an element is being dragged. :: :: drag-drop
ondragstart :: Fires when the user starts to drag an element. :: :: drag-drop
ondragend :: Fires when the user has finished dragging an element. :: :: drag-drop
ondragenter :: Fires when a dragged element enters a drop target. :: :: drag-drop
ondragleave :: Fires when a dragged element leaves a drop target. :: :: drag-drop
ondragover :: Fires while a dragged element is over a drop target. :: :: drag-drop
ondrop :: Fires when a dragged element is dropped on a target. :: :: drag-drop
"""),
    ("Clipboard events", """
oncopy :: Fires when the user copies content.
oncut :: Fires when the user cuts content.
onpaste :: Fires when the user pastes content.
"""),
    ("Media events", """
onplay :: Fires when playback starts.
onpause :: Fires when playback is paused.
onended :: Fires when playback reaches the end.
onvolumechange :: Fires when the volume changes or the media is muted.
ontimeupdate :: Fires when the playback position changes.
onloadedmetadata :: Fires when the duration and dimensions are known.
onloadeddata :: Fires when the first frame of media has loaded.
oncanplay :: Fires when the browser can start playing.
onseeking :: Fires when the user starts moving to a new position.
onseeked :: Fires when the user has finished moving to a new position.
onwaiting :: Fires when playback stops while waiting for data.
onstalled :: Fires when the browser tries to load data but it is not arriving.
"""),
    ("Other events", """
ontoggle :: Fires when a `details` element is opened or closed. :: :: details-summary
onanimationend :: Fires when a CSS animation ends.
ontransitionend :: Fires when a CSS transition ends.
"""),
]

# ============================================================================ CSS properties
CSS_PROPS = [
    ("Align and Flexbox", """
align-content :: Aligns the lines of a flex or grid container along the cross axis. :: `stretch`, `center`, `flex-start`, `flex-end`, `space-between`, `space-around` :: css-flexbox
align-items :: Aligns items along the cross axis. :: `stretch`, `center`, `flex-start`, `flex-end`, `baseline` :: css-flexbox
align-self :: Overrides `align-items` for one item. :: `auto`, `center`, `flex-start`, `flex-end`, `stretch` :: css-flex-items
justify-content :: Aligns items along the main axis. :: `flex-start`, `center`, `space-between`, `space-around`, `space-evenly` :: css-flexbox
justify-items :: Aligns grid items along the row axis. :: `start`, `end`, `center`, `stretch` :: css-grid
justify-self :: Aligns one grid item along the row axis. :: `auto`, `start`, `end`, `center`, `stretch` :: css-grid
place-content :: Shorthand for `align-content` and `justify-content`. :: `center`, `start`, `space-between` :: css-flexbox
place-items :: Shorthand for `align-items` and `justify-items`. :: `center`, `start`, `stretch` :: css-grid
place-self :: Shorthand for `align-self` and `justify-self`. :: `auto`, `center`
flex :: Shorthand for `flex-grow`, `flex-shrink` and `flex-basis`. :: `1`, `0 0 200px`, `auto`, `none` :: css-flex-items
flex-basis :: The initial size of a flex item. :: `auto`, length, percentage :: css-flex-items
flex-direction :: The direction of the main axis. :: `row`, `row-reverse`, `column`, `column-reverse` :: css-flexbox
flex-flow :: Shorthand for `flex-direction` and `flex-wrap`. :: `row wrap`, `column nowrap` :: css-flexbox
flex-grow :: How much an item grows to fill free space. :: number :: css-flex-items
flex-shrink :: How much an item shrinks when space is short. :: number :: css-flex-items
flex-wrap :: Whether items wrap onto new lines. :: `nowrap`, `wrap`, `wrap-reverse` :: css-flexbox
gap :: Shorthand for `row-gap` and `column-gap`. :: length :: css-flexbox
row-gap :: The space between rows. :: length
column-gap :: The space between columns. :: length
order :: The order of an item in a flex or grid container. :: integer :: css-flex-items
"""),
    ("Animation", """
animation :: Shorthand for all animation properties. :: `name duration timing-function delay count direction fill-mode` :: css-animations
animation-name :: The name of the `@keyframes` rule to use. :: name, `none` :: css-animations
animation-duration :: How long one cycle takes. :: time :: css-animations
animation-timing-function :: The speed curve of the animation. :: `ease`, `linear`, `ease-in`, `ease-out`, `cubic-bezier()` :: css-animations
animation-delay :: A delay before the animation starts. :: time :: css-animations
animation-iteration-count :: How many times the animation runs. :: number, `infinite` :: css-animations
animation-direction :: Whether the animation plays forwards, backwards or alternates. :: `normal`, `reverse`, `alternate`, `alternate-reverse` :: css-animations
animation-fill-mode :: The styles applied before and after the animation. :: `none`, `forwards`, `backwards`, `both` :: css-animations
animation-play-state :: Whether the animation is running or paused. :: `running`, `paused` :: css-animations
"""),
    ("Background", """
background :: Shorthand for the background properties. :: color, image, position, size, repeat :: css-backgrounds
background-attachment :: Whether the background scrolls with the page. :: `scroll`, `fixed`, `local` :: css-backgrounds
background-blend-mode :: How background layers blend with each other. :: `multiply`, `screen`, `overlay` :: css-blend-backdrop
background-clip :: How far the background extends. :: `border-box`, `padding-box`, `content-box`, `text` :: css-backgrounds
background-color :: The background colour. :: colour, `transparent` :: css-backgrounds
background-image :: One or more background images. :: `url()`, gradient, `none` :: css-backgrounds
background-origin :: The positioning area of the background image. :: `padding-box`, `border-box`, `content-box` :: css-backgrounds
background-position :: The starting position of the background image. :: `center`, `top left`, length, percentage :: css-backgrounds
background-repeat :: Whether the background image repeats. :: `repeat`, `no-repeat`, `repeat-x`, `repeat-y` :: css-backgrounds
background-size :: The size of the background image. :: `auto`, `cover`, `contain`, length :: css-backgrounds
"""),
    ("Border", """
border :: Shorthand for width, style and colour of all four borders. :: `1px solid #ccc` :: css-borders
border-top :: Shorthand for the top border. :: width style colour :: css-borders
border-right :: Shorthand for the right border. :: width style colour :: css-borders
border-bottom :: Shorthand for the bottom border. :: width style colour :: css-borders
border-left :: Shorthand for the left border. :: width style colour :: css-borders
border-color :: The colour of the borders. :: colour :: css-borders
border-style :: The style of the borders. :: `solid`, `dashed`, `dotted`, `double`, `none` :: css-borders
border-width :: The width of the borders. :: length, `thin`, `medium`, `thick` :: css-borders
border-radius :: Rounds the corners of an element. :: length, percentage :: css-border-radius
border-top-left-radius :: Rounds the top-left corner. :: length, percentage :: css-border-radius
border-top-right-radius :: Rounds the top-right corner. :: length, percentage :: css-border-radius
border-bottom-right-radius :: Rounds the bottom-right corner. :: length, percentage :: css-border-radius
border-bottom-left-radius :: Rounds the bottom-left corner. :: length, percentage :: css-border-radius
border-image :: Uses an image as the border. :: `url()` slice width repeat
border-block :: Shorthand for the borders at the block start and end. :: width style colour :: css-logical-properties
border-inline :: Shorthand for the borders at the inline start and end. :: width style colour :: css-logical-properties
"""),
    ("Box model and sizing", """
box-shadow :: Adds one or more shadows to an element. :: `offset-x offset-y blur spread colour` :: css-box-shadow
box-sizing :: What the `width` and `height` include. :: `content-box`, `border-box` :: css-box-sizing
width :: The width of an element. :: `auto`, length, percentage :: css-height-width
height :: The height of an element. :: `auto`, length, percentage :: css-height-width
min-width :: The minimum width. :: length, percentage :: css-height-width
max-width :: The maximum width. :: length, percentage, `none` :: css-height-width
min-height :: The minimum height. :: length, percentage :: css-height-width
max-height :: The maximum height. :: length, percentage, `none` :: css-height-width
inline-size :: The size in the inline direction (the logical version of `width`). :: length, percentage :: css-logical-properties
block-size :: The size in the block direction (the logical version of `height`). :: length, percentage :: css-logical-properties
aspect-ratio :: The preferred width-to-height ratio. :: `16 / 9`, `1`, `auto` :: css-aspect-ratio
overflow :: What happens to content that does not fit. :: `visible`, `hidden`, `scroll`, `auto` :: css-overflow
overflow-x :: Overflow behaviour in the horizontal direction. :: `visible`, `hidden`, `scroll`, `auto` :: css-overflow
overflow-y :: Overflow behaviour in the vertical direction. :: `visible`, `hidden`, `scroll`, `auto` :: css-overflow
overscroll-behavior :: What happens when you scroll past the edge of a scroll area. :: `auto`, `contain`, `none`
resize :: Whether the user can resize the element. :: `none`, `both`, `horizontal`, `vertical`
object-fit :: How an image or video fits its box. :: `fill`, `contain`, `cover`, `none` :: css-gallery
object-position :: The position of an image or video inside its box. :: `center`, `top`, length :: css-gallery
"""),
    ("Margin and padding", """
margin :: Shorthand for all four margins. :: length, percentage, `auto` :: css-margins
margin-top :: The top margin. :: length, percentage, `auto` :: css-margins
margin-right :: The right margin. :: length, percentage, `auto` :: css-margins
margin-bottom :: The bottom margin. :: length, percentage, `auto` :: css-margins
margin-left :: The left margin. :: length, percentage, `auto` :: css-margins
margin-block :: The margins at the block start and end. :: length, `auto` :: css-logical-properties
margin-inline :: The margins at the inline start and end. :: length, `auto` :: css-logical-properties
padding :: Shorthand for all four paddings. :: length, percentage :: css-padding
padding-top :: The top padding. :: length, percentage :: css-padding
padding-right :: The right padding. :: length, percentage :: css-padding
padding-bottom :: The bottom padding. :: length, percentage :: css-padding
padding-left :: The left padding. :: length, percentage :: css-padding
padding-block :: The paddings at the block start and end. :: length :: css-logical-properties
padding-inline :: The paddings at the inline start and end. :: length :: css-logical-properties
scroll-margin :: The margin around a scroll snap area. :: length :: css-scroll-snap
scroll-padding :: The padding of a scroll container's snapport. :: length :: css-scroll-snap
"""),
    ("Outline", """
outline :: Shorthand for outline width, style and colour. :: `2px solid blue` :: css-outline
outline-color :: The colour of the outline. :: colour :: css-outline
outline-offset :: The space between the outline and the border edge. :: length :: css-outline
outline-style :: The style of the outline. :: `solid`, `dashed`, `dotted`, `none` :: css-outline
outline-width :: The width of the outline. :: length, `thin`, `medium`, `thick` :: css-outline
"""),
    ("Color and opacity", """
color :: The text colour. :: colour :: css-colors
opacity :: How transparent an element is. :: `0` to `1` :: css-opacity
accent-color :: The accent colour of form controls such as checkboxes. :: colour, `auto` :: css-accent-appearance
caret-color :: The colour of the text cursor. :: colour, `auto`
color-scheme :: The colour schemes an element supports. :: `light`, `dark`, `light dark` :: css-dark-mode
"""),
    ("Columns", """
columns :: Shorthand for `column-width` and `column-count`. :: width count
column-count :: The number of columns. :: number, `auto`
column-width :: The ideal column width. :: length, `auto`
column-rule :: Shorthand for the rule drawn between columns. :: width style colour
column-span :: Whether an element spans all columns. :: `none`, `all`
column-fill :: How content is balanced between columns. :: `balance`, `auto`
"""),
    ("Display and position", """
display :: How an element is displayed. :: `block`, `inline`, `inline-block`, `flex`, `grid`, `none` :: css-display
visibility :: Whether an element is visible, while still taking up space. :: `visible`, `hidden`, `collapse` :: css-visibility
position :: How an element is positioned. :: `static`, `relative`, `absolute`, `fixed`, `sticky` :: css-position
top :: The offset from the top edge. :: length, percentage, `auto` :: css-position
right :: The offset from the right edge. :: length, percentage, `auto` :: css-position
bottom :: The offset from the bottom edge. :: length, percentage, `auto` :: css-position
left :: The offset from the left edge. :: length, percentage, `auto` :: css-position
inset :: Shorthand for `top`, `right`, `bottom` and `left`. :: length, `auto` :: css-position
z-index :: The stack order of a positioned element. :: integer, `auto` :: css-z-index
float :: Floats an element to the left or right. :: `left`, `right`, `none` :: css-float
clear :: Which sides of an element may not touch floats. :: `left`, `right`, `both`, `none` :: css-float
vertical-align :: The vertical alignment of an inline or table-cell element. :: `baseline`, `top`, `middle`, `bottom` :: css-align
contain :: Tells the browser an element is independent of the rest of the page. :: `layout`, `paint`, `size`, `content` :: css-performance
content-visibility :: Skips rendering work for offscreen content. :: `visible`, `auto`, `hidden` :: css-performance
"""),
    ("Font", """
font :: Shorthand for the font properties. :: `italic bold 16px/1.5 Arial, sans-serif` :: css-fonts
font-family :: The typeface, with fallbacks. :: font names, generic family :: css-font-stacks
font-size :: The size of the text. :: length, percentage, `small`, `large` :: css-fonts
font-size-adjust :: Adjusts the font size to keep a consistent x-height. :: number, `none`
font-style :: Normal, italic or oblique text. :: `normal`, `italic`, `oblique` :: css-fonts
font-variant :: Small-caps and other variants. :: `normal`, `small-caps` :: css-fonts
font-weight :: How bold the text is. :: `normal`, `bold`, `100` to `900` :: css-fonts
font-stretch :: A normal, condensed or expanded face. :: `condensed`, `normal`, `expanded`, percentage :: css-font-face
font-feature-settings :: Controls OpenType features. :: `"liga" 1`
font-variation-settings :: Controls the axes of a variable font. :: `"wght" 600` :: css-font-face
font-kerning :: Controls the use of kerning. :: `auto`, `normal`, `none`
"""),
    ("Grid", """
grid :: Shorthand for the explicit and implicit grid properties. :: template, auto-flow :: css-grid
grid-template :: Shorthand for the rows, columns and areas. :: rows / columns :: css-grid-areas
grid-template-columns :: The column tracks of a grid. :: `1fr 1fr`, `repeat(3, 1fr)`, `200px auto` :: css-grid
grid-template-rows :: The row tracks of a grid. :: `auto`, `100px 1fr` :: css-grid
grid-template-areas :: Names areas of the grid. :: quoted strings :: css-grid-areas
grid-area :: Places an item in a named area, or sets its lines. :: name, `row-start / col-start / row-end / col-end` :: css-grid-areas
grid-column :: Shorthand for `grid-column-start` and `grid-column-end`. :: `1 / 3`, `span 2` :: css-grid-areas
grid-column-start :: The column line where an item starts. :: number, `span n`, `auto` :: css-grid-areas
grid-column-end :: The column line where an item ends. :: number, `span n`, `auto` :: css-grid-areas
grid-row :: Shorthand for `grid-row-start` and `grid-row-end`. :: `1 / 3`, `span 2` :: css-grid-areas
grid-row-start :: The row line where an item starts. :: number, `span n`, `auto` :: css-grid-areas
grid-row-end :: The row line where an item ends. :: number, `span n`, `auto` :: css-grid-areas
grid-auto-columns :: The size of implicitly created columns. :: length, `auto`, `minmax()`
grid-auto-rows :: The size of implicitly created rows. :: length, `auto`, `minmax()`
grid-auto-flow :: How auto-placed items fill the grid. :: `row`, `column`, `dense`
"""),
    ("List and counters", """
list-style :: Shorthand for the list-style properties. :: type position image :: css-lists
list-style-image :: An image used as the list marker. :: `url()`, `none` :: css-lists
list-style-position :: Whether the marker is inside or outside the item. :: `inside`, `outside` :: css-lists
list-style-type :: The type of list marker. :: `disc`, `circle`, `square`, `decimal`, `none` :: css-lists
counter-reset :: Creates or resets a counter. :: name, number :: css-counters
counter-increment :: Increases a counter. :: name, number :: css-counters
counter-set :: Sets a counter to a value. :: name, number
"""),
    ("Table", """
border-collapse :: Whether table borders are collapsed into one. :: `collapse`, `separate` :: css-tables
border-spacing :: The distance between cell borders when they are separate. :: length :: css-tables
caption-side :: The placement of a table caption. :: `top`, `bottom`
empty-cells :: Whether to show borders of empty cells. :: `show`, `hide`
table-layout :: The algorithm used to lay out a table. :: `auto`, `fixed` :: css-tables
"""),
    ("Text", """
direction :: The text direction. :: `ltr`, `rtl` :: css-writing-mode
hyphens :: Controls hyphenation. :: `none`, `manual`, `auto`
letter-spacing :: The space between characters. :: length, `normal` :: css-text-effects
line-break :: How lines break in text, mainly for CJK scripts. :: `auto`, `loose`, `normal`, `strict`
line-height :: The height of a line of text. :: number, length, `normal` :: css-text
overflow-wrap :: Whether a long word may break to prevent overflow. :: `normal`, `break-word`, `anywhere` :: css-text-effects
tab-size :: The width of a tab character. :: number, length
text-align :: The horizontal alignment of text. :: `left`, `right`, `center`, `justify` :: css-text
text-align-last :: The alignment of the last line of a block. :: `auto`, `left`, `center`, `justify`
text-decoration :: Shorthand for the text decoration properties. :: `underline`, `none`, `line-through` :: css-text
text-decoration-color :: The colour of the decoration line. :: colour
text-decoration-line :: The kind of decoration line. :: `underline`, `overline`, `line-through`
text-decoration-style :: The style of the decoration line. :: `solid`, `dotted`, `dashed`, `wavy`
text-decoration-thickness :: The thickness of the decoration line. :: length, `auto`
text-indent :: The indent of the first line of text. :: length, percentage :: css-text
text-justify :: The justification method used with `text-align: justify`. :: `auto`, `inter-word`, `inter-character`
text-overflow :: How clipped text is shown. :: `clip`, `ellipsis` :: css-text-effects
text-shadow :: Adds a shadow to text. :: `offset-x offset-y blur colour` :: css-text-effects
text-transform :: Capitalisation of text. :: `none`, `uppercase`, `lowercase`, `capitalize` :: css-text
text-underline-offset :: The distance of an underline from the text. :: length, `auto`
text-wrap :: How text wraps. :: `wrap`, `nowrap`, `balance`, `pretty` :: css-text-wrap-clamp
-webkit-line-clamp :: Limits a block of text to a number of lines (used with `display: -webkit-box`). :: number :: css-text-wrap-clamp
unicode-bidi :: Works with `direction` for bidirectional text. :: `normal`, `embed`, `bidi-override`
white-space :: How white space and line breaks are handled. :: `normal`, `nowrap`, `pre`, `pre-wrap` :: css-text-effects
word-break :: Where lines may break inside words. :: `normal`, `break-all`, `keep-all` :: css-text-effects
word-spacing :: The space between words. :: length, `normal` :: css-text-effects
writing-mode :: Whether lines run horizontally or vertically. :: `horizontal-tb`, `vertical-rl`, `vertical-lr` :: css-writing-mode
"""),
    ("Transform", """
transform :: Applies a 2D or 3D transformation. :: `translate()`, `rotate()`, `scale()`, `skew()` :: css-transforms
transform-origin :: The origin point of a transformation. :: `center`, `top left`, length :: css-transforms
transform-style :: Whether children are placed in 3D space. :: `flat`, `preserve-3d`
perspective :: The distance between the viewer and the z=0 plane. :: length, `none`
perspective-origin :: The vanishing point of the perspective. :: `center`, length
backface-visibility :: Whether the back of an element is visible when turned. :: `visible`, `hidden`
translate :: Moves an element, as an individual property. :: length :: css-transforms
rotate :: Rotates an element, as an individual property. :: angle :: css-transforms
scale :: Scales an element, as an individual property. :: number :: css-transforms
"""),
    ("Transition", """
transition :: Shorthand for all transition properties. :: `property duration timing-function delay` :: css-transitions
transition-property :: Which properties transition. :: `all`, property name :: css-transitions
transition-duration :: How long a transition takes. :: time :: css-transitions
transition-timing-function :: The speed curve of a transition. :: `ease`, `linear`, `ease-in-out`, `cubic-bezier()` :: css-transitions
transition-delay :: A delay before a transition starts. :: time :: css-transitions
"""),
    ("Visual effects and misc", """
cursor :: The mouse cursor shown over an element. :: `pointer`, `default`, `text`, `not-allowed`, `grab` :: css-cursor
pointer-events :: Whether an element reacts to the pointer. :: `auto`, `none`
user-select :: Whether the user can select text. :: `auto`, `none`, `text`, `all`
filter :: Applies graphical effects such as blur or grayscale. :: `blur()`, `brightness()`, `grayscale()` :: css-filters
backdrop-filter :: Applies effects to the area behind an element. :: `blur()`, `saturate()` :: css-blend-backdrop
mix-blend-mode :: How an element blends with what is behind it. :: `multiply`, `screen`, `difference` :: css-blend-backdrop
isolation :: Whether an element creates a new stacking context. :: `auto`, `isolate`
clip-path :: Clips an element to a shape. :: `circle()`, `polygon()`, `inset()` :: css-clip-path-mask
mask :: Hides parts of an element using an image or gradient. :: `url()`, gradient :: css-clip-path-mask
will-change :: Hints which properties are about to change. :: property name, `auto` :: css-performance
scroll-behavior :: Whether scrolling is smooth or instant. :: `auto`, `smooth`
scroll-snap-type :: How strictly a container snaps to snap points. :: `x mandatory`, `y proximity` :: css-scroll-snap
scroll-snap-align :: Where an item aligns when snapping. :: `start`, `center`, `end` :: css-scroll-snap
touch-action :: Which touch gestures the browser handles. :: `auto`, `none`, `pan-x`, `pan-y`
appearance :: Removes or restores the native look of a form control. :: `none`, `auto` :: css-accent-appearance
content :: Generated content for `::before` and `::after`. :: string, `attr()`, `counter()`, `none` :: css-pseudo-elements
quotes :: The quotation marks used by `q` and `blockquote`. :: `none`, string pairs
all :: Resets all properties. :: `initial`, `inherit`, `unset`, `revert`
"""),
]

# ============================================================================ CSS selectors
CSS_SELECTORS = [
    ("Basic selectors", """
* :: Selects all elements. :: `* { margin: 0 }` :: css-selectors-basic
element :: Selects all elements of that type. :: `p { color: blue }` :: css-selectors-basic
.class :: Selects all elements with that class. :: `.note { color: red }` :: css-selectors-basic
#id :: Selects the element with that id. :: `#header { height: 80px }` :: css-selectors-basic
selector, selector :: Selects all of the listed selectors. :: `h1, h2, h3 { margin: 0 }` :: css-selectors-basic
"""),
    ("Combinators", """
A B :: Descendant: selects every B inside A. :: `div p` :: css-combinators
A > B :: Child: selects every B that is a direct child of A. :: `ul > li` :: css-combinators
A + B :: Adjacent sibling: selects the B directly after A. :: `h2 + p` :: css-combinators
A ~ B :: General sibling: selects every B after A with the same parent. :: `h2 ~ p` :: css-combinators
"""),
    ("Attribute selectors", """
[attr] :: Elements that have the attribute. :: `a[target]` :: css-attribute-selectors
[attr=value] :: Elements whose attribute equals the value. :: `input[type="text"]` :: css-attribute-selectors
[attr~=value] :: The attribute contains the word in a space-separated list. :: `[class~="card"]` :: css-attribute-selectors
[attr|=value] :: The attribute equals the value or starts with it followed by a hyphen. :: `[lang|="en"]` :: css-attribute-selectors
[attr^=value] :: The attribute starts with the value. :: `a[href^="https"]` :: css-attribute-selectors
[attr$=value] :: The attribute ends with the value. :: `a[href$=".pdf"]` :: css-attribute-selectors
[attr*=value] :: The attribute contains the value anywhere. :: `a[href*="example"]` :: css-attribute-selectors
[attr=value i] :: Matches the value without regard to case. :: `[type="TEXT" i]` :: css-attribute-selectors
"""),
    ("Pseudo-classes", """
:hover :: An element the pointer is over. :: `a:hover` :: css-pseudo-classes
:active :: An element being activated, for example while clicked. :: `button:active` :: css-pseudo-classes
:focus :: An element that has focus. :: `input:focus` :: css-pseudo-classes
:focus-visible :: An element focused in a way that should show a focus ring, such as by keyboard. :: `button:focus-visible` :: css-pseudo-classes
:focus-within :: An element that contains a focused element. :: `form:focus-within` :: css-pseudo-classes
:link :: Links that have not been visited. :: `a:link` :: css-links
:visited :: Links that have been visited. :: `a:visited` :: css-links
:first-child :: An element that is the first child of its parent. :: `li:first-child` :: css-pseudo-classes
:last-child :: An element that is the last child of its parent. :: `li:last-child` :: css-pseudo-classes
:only-child :: An element that is the only child of its parent. :: `p:only-child` :: css-pseudo-classes
:nth-child(n) :: Elements by their position among siblings. :: `li:nth-child(odd)` :: css-pseudo-classes
:nth-last-child(n) :: Elements by their position counting from the end. :: `li:nth-last-child(2)` :: css-pseudo-classes
:first-of-type :: The first sibling of its type. :: `p:first-of-type` :: css-pseudo-classes
:last-of-type :: The last sibling of its type. :: `p:last-of-type` :: css-pseudo-classes
:nth-of-type(n) :: Elements by their position among siblings of the same type. :: `p:nth-of-type(2)` :: css-pseudo-classes
:only-of-type :: An element with no siblings of the same type. :: `img:only-of-type`
:not(selector) :: Elements that do not match the selector. :: `p:not(.intro)` :: css-has-is-where
:is(list) :: Elements matching any selector in the list. :: `:is(h1, h2) a` :: css-has-is-where
:where(list) :: Like `:is()`, but with zero specificity. :: `:where(h1, h2) a` :: css-has-is-where
:has(selector) :: An element that contains a match for the selector. :: `a:has(img)` :: css-has-is-where
:empty :: An element with no children and no text. :: `p:empty`
:root :: The root element of the document. :: `:root { --brand: blue }` :: css-variables
:target :: The element whose id matches the URL fragment. :: `:target { background: yellow }`
:checked :: A checked checkbox, radio button or selected option. :: `input:checked` :: css-forms
:disabled :: A disabled form control. :: `input:disabled` :: css-forms
:enabled :: An enabled form control. :: `input:enabled`
:required :: A form control with the `required` attribute. :: `input:required` :: css-forms
:optional :: A form control without the `required` attribute. :: `input:optional`
:valid :: A form control whose value passes validation. :: `input:valid` :: css-forms
:invalid :: A form control whose value fails validation. :: `input:invalid` :: css-forms
:placeholder-shown :: An input that is currently showing its placeholder. :: `input:placeholder-shown`
:read-only :: An element the user cannot edit. :: `input:read-only`
:lang(code) :: Elements with a given language. :: `p:lang(fr)`
"""),
    ("Pseudo-elements", """
::before :: Inserts generated content before an element's content. :: `p::before { content: "Note: " }` :: css-pseudo-elements
::after :: Inserts generated content after an element's content. :: `p::after { content: "!" }` :: css-pseudo-elements
::first-letter :: The first letter of a block. :: `p::first-letter { font-size: 2em }` :: css-pseudo-elements
::first-line :: The first line of a block. :: `p::first-line { font-weight: bold }` :: css-pseudo-elements
::selection :: The part of the text the user has selected. :: `::selection { background: yellow }` :: css-pseudo-elements
::placeholder :: The placeholder text of an input. :: `input::placeholder { color: gray }`
::marker :: The marker box of a list item. :: `li::marker { color: red }`
::backdrop :: The backdrop behind a full-screen element or modal dialog. :: `dialog::backdrop { background: rgba(0,0,0,.5) }` :: dialog
"""),
    ("Nesting", """
& :: In nested CSS, refers to the parent selector. :: `.card { &:hover { color: red } }` :: css-nesting
"""),
]

# ============================================================================ CSS functions and at-rules
CSS_FUNCS = [
    ("Math functions", """
calc() :: Calculates a value from an expression. :: `width: calc(100% - 40px)` :: css-calc-min-max-clamp
min() :: Uses the smallest of the given values. :: `width: min(90%, 600px)` :: css-calc-min-max-clamp
max() :: Uses the largest of the given values. :: `width: max(50%, 300px)` :: css-calc-min-max-clamp
clamp() :: Keeps a value between a minimum and maximum. :: `font-size: clamp(1rem, 2.5vw, 2rem)` :: css-calc-min-max-clamp
var() :: Inserts the value of a custom property. :: `color: var(--brand, blue)` :: css-variables
attr() :: Inserts the value of an HTML attribute, mostly in `content`. :: `content: attr(title)` :: css-pseudo-elements
"""),
    ("Colour functions", """
rgb() :: A colour from red, green and blue values. :: `rgb(29 78 216)` :: css-colors
hsl() :: A colour from hue, saturation and lightness. :: `hsl(220 80% 48%)` :: css-colors
oklch() :: A colour in the perceptual OKLCH space. :: `oklch(55% 0.2 260)` :: css-modern-colors
color-mix() :: Mixes two colours. :: `color-mix(in srgb, blue 30%, white)` :: css-modern-colors
"""),
    ("Gradient functions", """
linear-gradient() :: A gradient along a line. :: `linear-gradient(to right, red, blue)` :: css-gradients
radial-gradient() :: A gradient radiating from a centre point. :: `radial-gradient(circle, white, blue)` :: css-gradients
conic-gradient() :: A gradient rotated around a centre point. :: `conic-gradient(red, yellow, green)` :: css-gradients
repeating-linear-gradient() :: A repeating linear gradient. :: `repeating-linear-gradient(45deg, #eee 0 10px, #fff 10px 20px)` :: css-gradients
"""),
    ("Grid functions", """
repeat() :: Repeats a track definition. :: `grid-template-columns: repeat(3, 1fr)` :: css-grid
minmax() :: A size range for a grid track. :: `minmax(200px, 1fr)` :: css-grid-responsive
fit-content() :: Sizes a track to its content up to a limit. :: `fit-content(300px)`
"""),
    ("Transform and filter functions", """
translate() :: Moves an element. :: `transform: translate(20px, 10px)` :: css-transforms
rotate() :: Rotates an element. :: `transform: rotate(45deg)` :: css-transforms
scale() :: Resizes an element. :: `transform: scale(1.2)` :: css-transforms
skew() :: Skews an element along the x and y axes. :: `transform: skew(10deg, 5deg)` :: css-transforms
blur() :: Applies a blur filter. :: `filter: blur(4px)` :: css-filters
grayscale() :: Converts the element to grayscale. :: `filter: grayscale(100%)` :: css-filters
drop-shadow() :: Adds a shadow that follows the shape of the content. :: `filter: drop-shadow(2px 4px 6px gray)` :: css-filters
"""),
    ("At-rules", """
@media :: Applies styles when a media condition is true. :: `@media (min-width: 768px) { ... }` :: css-media-queries
@supports :: Applies styles only if the browser supports a feature. :: `@supports (display: grid) { ... }` :: css-supports
@layer :: Declares cascade layers. :: `@layer base, components;` :: css-layers
@container :: Applies styles based on the size of a container. :: `@container (min-width: 400px) { ... }` :: css-container-queries
@keyframes :: Defines the steps of an animation. :: `@keyframes fade { from { opacity: 0 } to { opacity: 1 } }` :: css-animations
@font-face :: Defines a custom font to load. :: `@font-face { font-family: "My Font"; src: url(...) }` :: css-font-face
@import :: Imports another stylesheet. :: `@import url("theme.css");`
@property :: Registers a typed custom property. :: `@property --angle { syntax: "<angle>"; ... }` :: css-property-rule
@charset :: Declares the character encoding of the stylesheet. :: `@charset "UTF-8";`
@page :: Sets styles for printed pages. :: `@page { margin: 2cm }` :: css-print
"""),
]

# ============================================================================ JavaScript reference
JS_REF = [
    ("Global functions", """
parseInt() :: Parses a string and returns an integer. :: `parseInt("42px")` :: js-numbers
parseFloat() :: Parses a string and returns a floating-point number. :: `parseFloat("3.14")` :: js-numbers
isNaN() :: Tells whether a value is `NaN` after conversion to a number. :: `isNaN("abc")` :: js-numbers
isFinite() :: Tells whether a value is a finite number after conversion. :: `isFinite(10)`
Number() :: Converts a value to a number. :: `Number("12")` :: js-type-conversion
String() :: Converts a value to a string. :: `String(42)` :: js-type-conversion
Boolean() :: Converts a value to a boolean. :: `Boolean("")` :: js-type-conversion
encodeURIComponent() :: Encodes a string for use in a URL component. :: `encodeURIComponent("a b&c")`
decodeURIComponent() :: Decodes a URL component. :: `decodeURIComponent("a%20b")`
encodeURI() :: Encodes a complete URI. :: `encodeURI("https://x.com/a b")`
decodeURI() :: Decodes a complete URI. :: `decodeURI("https://x.com/a%20b")`
structuredClone() :: Makes a deep copy of a value. :: `structuredClone(obj)`
queueMicrotask() :: Queues a function to run after the current task. :: `queueMicrotask(fn)` :: js-event-loop
"""),
    ("String", """
length :: The number of UTF-16 code units in the string. :: `"abc".length` :: js-strings
at() :: The character at an index; negative indexes count from the end. :: `"abc".at(-1)` :: js-string-methods
charAt() :: The character at an index. :: `"abc".charAt(1)` :: js-string-methods
charCodeAt() :: The UTF-16 code unit at an index. :: `"A".charCodeAt(0)`
codePointAt() :: The Unicode code point at an index. :: `"A".codePointAt(0)`
concat() :: Joins strings and returns a new string. :: `"a".concat("b")` :: js-string-methods
includes() :: Whether the string contains a substring. :: `"hello".includes("ell")` :: js-string-methods
startsWith() :: Whether the string starts with a substring. :: `"hello".startsWith("he")` :: js-string-methods
endsWith() :: Whether the string ends with a substring. :: `"hello".endsWith("lo")` :: js-string-methods
indexOf() :: The first index of a substring, or `-1`. :: `"hello".indexOf("l")` :: js-string-methods
lastIndexOf() :: The last index of a substring, or `-1`. :: `"hello".lastIndexOf("l")`
match() :: Matches the string against a regular expression. :: `"a1b2".match(/\\d/g)` :: js-regexp
matchAll() :: An iterator of all matches of a regular expression. :: `"a1b2".matchAll(/\\d/g)`
replace() :: Replaces the first match of a string or pattern. :: `"a-b".replace("-", "+")` :: js-string-methods
replaceAll() :: Replaces every match of a string or pattern. :: `"a-b-c".replaceAll("-", "+")` :: js-string-methods
search() :: The index of the first match of a regular expression, or `-1`. :: `"abc".search(/c/)`
slice() :: Extracts part of a string; negative indexes count from the end. :: `"hello".slice(1, 3)` :: js-string-methods
substring() :: Extracts part of a string between two indexes. :: `"hello".substring(1, 3)` :: js-string-methods
split() :: Splits a string into an array. :: `"a,b".split(",")` :: js-string-methods
toLowerCase() :: Converts to lower case. :: `"ABC".toLowerCase()` :: js-string-methods
toUpperCase() :: Converts to upper case. :: `"abc".toUpperCase()` :: js-string-methods
trim() :: Removes white space from both ends. :: `"  a ".trim()` :: js-string-methods
trimStart() :: Removes white space from the start. :: `"  a".trimStart()`
trimEnd() :: Removes white space from the end. :: `"a  ".trimEnd()`
padStart() :: Pads the start to a target length. :: `"5".padStart(3, "0")` :: js-string-methods
padEnd() :: Pads the end to a target length. :: `"5".padEnd(3, "0")` :: js-string-methods
repeat() :: Repeats the string a number of times. :: `"ab".repeat(3)` :: js-string-methods
localeCompare() :: Compares two strings in the current locale. :: `"a".localeCompare("b")`
normalize() :: Returns the Unicode normalisation form of the string. :: `"é".normalize("NFD")`
String.fromCharCode() :: Creates a string from UTF-16 code units. :: `String.fromCharCode(72, 105)`
String.raw :: A tag function that returns a template string without processing escapes. :: `String.raw`\\n``
substr() :: Deprecated. Use `slice()` or `substring()` instead. :: `"hello".substr(1, 3)`
"""),
    ("Number", """
Number.isInteger() :: Whether a value is an integer. :: `Number.isInteger(5)` :: js-numbers
Number.isFinite() :: Whether a value is a finite number, without conversion. :: `Number.isFinite(5)`
Number.isNaN() :: Whether a value is `NaN`, without conversion. :: `Number.isNaN(NaN)` :: js-numbers
Number.isSafeInteger() :: Whether a value is an integer in the safe range. :: `Number.isSafeInteger(2 ** 53)`
Number.parseFloat() :: Same as the global `parseFloat()`. :: `Number.parseFloat("1.5")`
Number.parseInt() :: Same as the global `parseInt()`. :: `Number.parseInt("10", 10)`
Number.MAX_SAFE_INTEGER :: The largest integer that can be represented exactly (2^53 - 1). :: `9007199254740991` :: js-numbers
Number.MIN_SAFE_INTEGER :: The smallest integer that can be represented exactly. :: `-9007199254740991`
Number.EPSILON :: The difference between 1 and the next larger number. :: `Number.EPSILON`
Number.MAX_VALUE :: The largest positive number that can be represented. :: `Number.MAX_VALUE`
Number.MIN_VALUE :: The smallest positive number that can be represented. :: `Number.MIN_VALUE`
Number.POSITIVE_INFINITY :: Positive infinity. :: `Infinity`
Number.NEGATIVE_INFINITY :: Negative infinity. :: `-Infinity`
Number.NaN :: The "not a number" value. :: `NaN`
toFixed() :: Formats a number with a fixed number of decimals, as a string. :: `(3.14159).toFixed(2)` :: js-numbers
toPrecision() :: Formats a number to a number of significant digits. :: `(123.456).toPrecision(4)`
toString() :: Converts a number to a string, optionally in another base. :: `(255).toString(16)`
toLocaleString() :: Formats a number using the locale's conventions. :: `(1234.5).toLocaleString("en-US")`
valueOf() :: The primitive value of a number object. :: `new Number(5).valueOf()`
"""),
    ("Math", """
Math.PI :: The value of pi. :: `3.14159...` :: js-math
Math.E :: Euler's number. :: `2.71828...`
Math.abs() :: The absolute value. :: `Math.abs(-5)` :: js-math
Math.ceil() :: Rounds up to the nearest integer. :: `Math.ceil(4.2)` :: js-math
Math.floor() :: Rounds down to the nearest integer. :: `Math.floor(4.9)` :: js-math
Math.round() :: Rounds to the nearest integer. :: `Math.round(4.5)` :: js-math
Math.trunc() :: Removes the fractional part. :: `Math.trunc(-4.7)` :: js-math
Math.sign() :: Returns `1`, `-1` or `0` for the sign of a number. :: `Math.sign(-3)`
Math.sqrt() :: The square root. :: `Math.sqrt(16)` :: js-math
Math.cbrt() :: The cube root. :: `Math.cbrt(27)`
Math.pow() :: A base raised to a power. :: `Math.pow(2, 3)` :: js-math
Math.exp() :: e raised to a power. :: `Math.exp(1)`
Math.log() :: The natural logarithm. :: `Math.log(Math.E)`
Math.log2() :: The base-2 logarithm. :: `Math.log2(8)`
Math.log10() :: The base-10 logarithm. :: `Math.log10(1000)`
Math.max() :: The largest of the given numbers. :: `Math.max(1, 5, 3)` :: js-math
Math.min() :: The smallest of the given numbers. :: `Math.min(1, 5, 3)` :: js-math
Math.random() :: A random number from 0 up to, but not including, 1. :: `Math.random()` :: js-math
Math.sin() :: The sine of an angle in radians. :: `Math.sin(Math.PI / 2)`
Math.cos() :: The cosine of an angle in radians. :: `Math.cos(0)`
Math.tan() :: The tangent of an angle in radians. :: `Math.tan(0)`
Math.atan2() :: The angle from the x-axis to the point (x, y). :: `Math.atan2(1, 1)`
Math.hypot() :: The square root of the sum of squares. :: `Math.hypot(3, 4)`
"""),
    ("Date", """
new Date() :: Creates a date object. :: `new Date("2026-10-30")` :: js-dates
Date.now() :: The number of milliseconds since 1 January 1970 UTC. :: `Date.now()` :: js-dates
Date.parse() :: Parses a date string into milliseconds since 1 January 1970 UTC. :: `Date.parse("2026-10-30")`
Date.UTC() :: Milliseconds since 1 January 1970 UTC for the given UTC date. :: `Date.UTC(2026, 9, 30)`
getFullYear() :: The four-digit year. :: `d.getFullYear()` :: js-dates
getMonth() :: The month, from 0 (January) to 11 (December). :: `d.getMonth()` :: js-dates
getDate() :: The day of the month, from 1 to 31. :: `d.getDate()` :: js-dates
getDay() :: The day of the week, from 0 (Sunday) to 6 (Saturday). :: `d.getDay()` :: js-dates
getHours() :: The hour, from 0 to 23. :: `d.getHours()`
getMinutes() :: The minutes, from 0 to 59. :: `d.getMinutes()`
getSeconds() :: The seconds, from 0 to 59. :: `d.getSeconds()`
getMilliseconds() :: The milliseconds, from 0 to 999. :: `d.getMilliseconds()`
getTime() :: The milliseconds since 1 January 1970 UTC. :: `d.getTime()` :: js-dates
getTimezoneOffset() :: The difference in minutes between UTC and local time. :: `d.getTimezoneOffset()`
setFullYear() :: Sets the year. :: `d.setFullYear(2030)`
setMonth() :: Sets the month (0 to 11). :: `d.setMonth(0)`
setDate() :: Sets the day of the month. :: `d.setDate(15)` :: js-dates
setHours() :: Sets the hours. :: `d.setHours(9)`
setMinutes() :: Sets the minutes. :: `d.setMinutes(30)`
setSeconds() :: Sets the seconds. :: `d.setSeconds(0)`
setTime() :: Sets the date from milliseconds since 1 January 1970 UTC. :: `d.setTime(0)`
toISOString() :: The date as an ISO 8601 string in UTC. :: `d.toISOString()` :: js-dates
toDateString() :: The date part as a readable string. :: `d.toDateString()`
toLocaleDateString() :: The date part formatted for a locale. :: `d.toLocaleDateString("en-GB")`
toLocaleTimeString() :: The time part formatted for a locale. :: `d.toLocaleTimeString("en-US")`
toLocaleString() :: The date and time formatted for a locale. :: `d.toLocaleString()`
toString() :: The date as a readable string. :: `d.toString()`
toJSON() :: The date as a string for JSON, same as `toISOString()`. :: `d.toJSON()`
"""),
    ("Array", """
length :: The number of elements in the array. :: `arr.length` :: js-arrays
Array.isArray() :: Whether a value is an array. :: `Array.isArray([])` :: js-arrays
Array.from() :: Creates an array from an iterable or array-like object. :: `Array.from("abc")` :: js-arrays
Array.of() :: Creates an array from its arguments. :: `Array.of(1, 2, 3)`
at() :: The element at an index; negative indexes count from the end. :: `arr.at(-1)`
concat() :: Joins arrays and returns a new array. :: `a.concat(b)` :: js-array-methods
entries() :: An iterator of `[index, value]` pairs. :: `arr.entries()`
every() :: Whether every element passes a test. :: `arr.every(x => x > 0)` :: js-array-iteration
fill() :: Fills elements with a value. :: `new Array(3).fill(0)`
filter() :: A new array of the elements that pass a test. :: `arr.filter(x => x > 1)` :: js-array-iteration
find() :: The first element that passes a test. :: `arr.find(x => x > 1)` :: js-array-iteration
findIndex() :: The index of the first element that passes a test. :: `arr.findIndex(x => x > 1)` :: js-array-iteration
findLast() :: The last element that passes a test. :: `arr.findLast(x => x > 1)`
findLastIndex() :: The index of the last element that passes a test. :: `arr.findLastIndex(x => x > 1)`
flat() :: Flattens nested arrays to a given depth. :: `[[1], [2]].flat()`
flatMap() :: Maps each element, then flattens the result by one level. :: `arr.flatMap(x => [x, x])`
forEach() :: Runs a function for each element. :: `arr.forEach(x => console.log(x))` :: js-array-iteration
includes() :: Whether the array contains a value. :: `arr.includes(2)` :: js-array-methods
indexOf() :: The first index of a value, or `-1`. :: `arr.indexOf(2)` :: js-array-methods
join() :: Joins the elements into a string. :: `arr.join("-")` :: js-array-methods
keys() :: An iterator of the indexes. :: `arr.keys()`
lastIndexOf() :: The last index of a value, or `-1`. :: `arr.lastIndexOf(2)`
map() :: A new array with the result of a function for each element. :: `arr.map(x => x * 2)` :: js-array-iteration
pop() :: Removes and returns the last element. :: `arr.pop()` :: js-array-methods
push() :: Adds elements to the end and returns the new length. :: `arr.push(4)` :: js-array-methods
reduce() :: Reduces the array to a single value, left to right. :: `arr.reduce((a, b) => a + b, 0)` :: js-array-iteration
reduceRight() :: Reduces the array to a single value, right to left. :: `arr.reduceRight((a, b) => a + b)`
reverse() :: Reverses the array in place. :: `arr.reverse()` :: js-array-methods
shift() :: Removes and returns the first element. :: `arr.shift()` :: js-array-methods
slice() :: A copy of part of the array. :: `arr.slice(1, 3)` :: js-array-methods
some() :: Whether at least one element passes a test. :: `arr.some(x => x > 2)` :: js-array-iteration
sort() :: Sorts the array in place. :: `arr.sort((a, b) => a - b)` :: js-array-methods
splice() :: Adds or removes elements in place. :: `arr.splice(1, 1)` :: js-array-methods
toString() :: Converts the array to a comma-separated string. :: `arr.toString()`
unshift() :: Adds elements to the start and returns the new length. :: `arr.unshift(0)` :: js-array-methods
values() :: An iterator of the values. :: `arr.values()`
toSorted() :: A sorted copy, leaving the original unchanged. :: `arr.toSorted()`
toReversed() :: A reversed copy, leaving the original unchanged. :: `arr.toReversed()`
toSpliced() :: A copy with elements removed or added, leaving the original unchanged. :: `arr.toSpliced(1, 1)`
with() :: A copy with one element replaced. :: `arr.with(0, "x")`
"""),
    ("Object", """
Object.keys() :: An array of an object's own enumerable property names. :: `Object.keys(obj)` :: js-object-methods
Object.values() :: An array of an object's own enumerable property values. :: `Object.values(obj)` :: js-object-methods
Object.entries() :: An array of `[key, value]` pairs. :: `Object.entries(obj)` :: js-object-methods
Object.fromEntries() :: Creates an object from `[key, value]` pairs. :: `Object.fromEntries([["a", 1]])` :: js-object-methods
Object.assign() :: Copies properties from source objects to a target. :: `Object.assign({}, a, b)` :: js-object-methods
Object.create() :: Creates an object with a given prototype. :: `Object.create(proto)` :: js-inheritance
Object.freeze() :: Prevents changes to an object. :: `Object.freeze(obj)` :: js-object-methods
Object.isFrozen() :: Whether an object is frozen. :: `Object.isFrozen(obj)`
Object.seal() :: Prevents adding or removing properties. :: `Object.seal(obj)`
Object.isSealed() :: Whether an object is sealed. :: `Object.isSealed(obj)`
Object.getPrototypeOf() :: The prototype of an object. :: `Object.getPrototypeOf(obj)` :: js-inheritance
Object.setPrototypeOf() :: Sets the prototype of an object. :: `Object.setPrototypeOf(obj, proto)`
Object.defineProperty() :: Defines or changes a property with a descriptor. :: `Object.defineProperty(obj, "x", { value: 1 })` :: js-getters-setters
Object.defineProperties() :: Defines several properties at once. :: `Object.defineProperties(obj, props)`
Object.getOwnPropertyNames() :: All own property names, including non-enumerable ones. :: `Object.getOwnPropertyNames(obj)`
Object.getOwnPropertyDescriptor() :: The descriptor of an own property. :: `Object.getOwnPropertyDescriptor(obj, "x")`
Object.hasOwn() :: Whether an object has an own property. :: `Object.hasOwn(obj, "x")`
Object.is() :: Whether two values are the same value. :: `Object.is(NaN, NaN)`
Object.groupBy() :: Groups the items of an iterable by a key function. :: `Object.groupBy(items, x => x.type)`
hasOwnProperty() :: Whether the object has the property as its own. :: `obj.hasOwnProperty("x")`
toString() :: A string representation of the object. :: `obj.toString()`
valueOf() :: The primitive value of the object. :: `obj.valueOf()`
"""),
    ("JSON", """
JSON.parse() :: Converts a JSON string into a JavaScript value. :: `JSON.parse('{"a":1}')` :: js-json
JSON.stringify() :: Converts a JavaScript value into a JSON string. :: `JSON.stringify({ a: 1 })` :: js-json
JSON.stringify() with space :: The third argument adds indentation to the output. :: `JSON.stringify(obj, null, 2)` :: js-json
JSON.parse() with reviver :: The second argument transforms values while parsing. :: `JSON.parse(text, (k, v) => v)`
"""),
    ("Promise", """
new Promise() :: Creates a promise from an executor function. :: `new Promise((resolve, reject) => { ... })` :: js-promises
then() :: Adds handlers for when the promise is fulfilled or rejected. :: `p.then(value => ...)` :: js-promises
catch() :: Adds a handler for when the promise is rejected. :: `p.catch(err => ...)` :: js-promises
finally() :: Adds a handler that runs whether the promise is fulfilled or rejected. :: `p.finally(() => ...)` :: js-promises
Promise.all() :: Waits for all promises, or rejects on the first rejection. :: `Promise.all([p1, p2])` :: js-promises
Promise.allSettled() :: Waits for all promises to settle, whatever the outcome. :: `Promise.allSettled([p1, p2])`
Promise.any() :: Fulfils with the first fulfilled promise. :: `Promise.any([p1, p2])`
Promise.race() :: Settles with the first promise to settle. :: `Promise.race([p1, p2])` :: js-promises
Promise.resolve() :: Creates a promise fulfilled with a value. :: `Promise.resolve(1)`
Promise.reject() :: Creates a promise rejected with a reason. :: `Promise.reject(new Error("no"))`
async function :: A function that always returns a promise and can use `await`. :: `async function f() { ... }` :: js-async-await
await :: Pauses an async function until a promise settles. :: `const x = await p;` :: js-async-await
"""),
    ("Set", """
new Set() :: Creates a collection of unique values. :: `new Set([1, 2, 2])` :: js-set-map
add() :: Adds a value. :: `set.add(3)` :: js-set-map
delete() :: Removes a value. :: `set.delete(3)` :: js-set-map
has() :: Whether the set contains a value. :: `set.has(3)` :: js-set-map
clear() :: Removes all values. :: `set.clear()`
size :: The number of values. :: `set.size` :: js-set-map
forEach() :: Runs a function for each value. :: `set.forEach(v => ...)`
values() :: An iterator of the values. :: `set.values()`
"""),
    ("Map", """
new Map() :: Creates a collection of key-value pairs where keys can be any type. :: `new Map([["a", 1]])` :: js-set-map
set() :: Sets the value for a key. :: `map.set("a", 1)` :: js-set-map
get() :: The value for a key. :: `map.get("a")` :: js-set-map
has() :: Whether the map has a key. :: `map.has("a")` :: js-set-map
delete() :: Removes a key and its value. :: `map.delete("a")`
clear() :: Removes all entries. :: `map.clear()`
size :: The number of entries. :: `map.size` :: js-set-map
keys() :: An iterator of the keys. :: `map.keys()`
values() :: An iterator of the values. :: `map.values()`
entries() :: An iterator of `[key, value]` pairs. :: `map.entries()`
forEach() :: Runs a function for each entry. :: `map.forEach((v, k) => ...)`
"""),
    ("RegExp", """
test() :: Whether the pattern matches a string. :: `/a+/.test("caat")` :: js-regexp
exec() :: Runs a search and returns the match details, or `null`. :: `/(\\d+)/.exec("a12")` :: js-regexp
source :: The pattern text of the regular expression. :: `/ab/.source`
flags :: The flags of the regular expression. :: `/ab/gi.flags`
lastIndex :: The index where the next match starts, for `g` and `y` flags. :: `re.lastIndex`
g :: Global flag: find all matches. :: `/a/g` :: js-regexp
i :: Ignore-case flag. :: `/a/i` :: js-regexp
m :: Multiline flag: `^` and `$` match at line breaks. :: `/^a/m`
s :: Dot-all flag: `.` also matches line breaks. :: `/a.b/s`
u :: Unicode flag: treats the pattern as Unicode code points. :: `/\\u{1F600}/u`
\\d :: Matches a digit. :: `/\\d+/` :: js-regexp
\\w :: Matches a letter, digit or underscore. :: `/\\w+/` :: js-regexp
\\s :: Matches a white space character. :: `/\\s/` :: js-regexp
. :: Matches any character except a line break. :: `/a.c/`
^ :: Matches the start of the input. :: `/^abc/`
$ :: Matches the end of the input. :: `/abc$/`
* :: Matches zero or more of the previous item. :: `/ab*/`
+ :: Matches one or more of the previous item. :: `/ab+/`
? :: Matches zero or one of the previous item. :: `/colou?r/`
{n,m} :: Matches between n and m of the previous item. :: `/\\d{2,4}/`
[abc] :: Matches any one of the listed characters. :: `/[aeiou]/`
(abc) :: A capturing group. :: `/(\\d+)-(\\d+)/`
"""),
    ("console", """
console.log() :: Writes a message to the console. :: `console.log("Hi")` :: js-output
console.info() :: Writes an informational message. :: `console.info("Note")`
console.warn() :: Writes a warning. :: `console.warn("Careful")`
console.error() :: Writes an error message. :: `console.error("Failed")` :: js-debugging
console.table() :: Shows an array or object as a table. :: `console.table(rows)` :: js-debugging
console.group() :: Starts an indented group of messages. :: `console.group("Label")`
console.groupEnd() :: Ends the current group. :: `console.groupEnd()`
console.time() :: Starts a timer. :: `console.time("t")` :: js-debugging
console.timeEnd() :: Stops a timer and logs the elapsed time. :: `console.timeEnd("t")`
console.count() :: Logs how many times it has been called with a label. :: `console.count("clicks")`
console.assert() :: Logs a message if a condition is false. :: `console.assert(x > 0, "x must be positive")`
console.dir() :: Shows an interactive listing of an object. :: `console.dir(obj)`
console.clear() :: Clears the console. :: `console.clear()`
"""),
]

# ============================================================================ DOM reference
JS_DOM = [
    ("Document", """
document.getElementById() :: The element with the given id. :: `document.getElementById("app")` :: js-dom-selecting
document.getElementsByClassName() :: A live collection of elements with a class name. :: `document.getElementsByClassName("note")` :: js-dom-selecting
document.getElementsByTagName() :: A live collection of elements with a tag name. :: `document.getElementsByTagName("p")` :: js-dom-selecting
document.querySelector() :: The first element that matches a CSS selector. :: `document.querySelector(".card")` :: js-dom-selecting
document.querySelectorAll() :: All elements that match a CSS selector. :: `document.querySelectorAll("li")` :: js-dom-selecting
document.createElement() :: Creates an element. :: `document.createElement("div")` :: js-dom-elements
document.createTextNode() :: Creates a text node. :: `document.createTextNode("Hi")`
document.createDocumentFragment() :: Creates a lightweight container for nodes. :: `document.createDocumentFragment()`
document.body :: The `body` element. :: `document.body`
document.head :: The `head` element. :: `document.head`
document.documentElement :: The root `html` element. :: `document.documentElement`
document.title :: The title of the document. :: `document.title = "New"`
document.URL :: The full URL of the document. :: `document.URL`
document.readyState :: The loading state: `loading`, `interactive` or `complete`. :: `document.readyState`
document.activeElement :: The element that currently has focus. :: `document.activeElement`
document.forms :: A collection of all forms in the document. :: `document.forms[0]` :: js-dom-forms
"""),
    ("Element", """
innerHTML :: Gets or sets the HTML inside an element. :: `el.innerHTML = "<b>Hi</b>"` :: js-dom-content
textContent :: Gets or sets the text of an element. :: `el.textContent = "Hi"` :: js-dom-content
innerText :: Gets or sets the rendered text of an element. :: `el.innerText`
outerHTML :: The HTML of an element, including the element itself. :: `el.outerHTML`
id :: Gets or sets the id. :: `el.id = "main"`
className :: Gets or sets the class attribute as a string. :: `el.className = "a b"`
getAttribute() :: The value of an attribute. :: `el.getAttribute("href")` :: js-dom-content
setAttribute() :: Sets the value of an attribute. :: `el.setAttribute("title", "Hi")` :: js-dom-content
removeAttribute() :: Removes an attribute. :: `el.removeAttribute("hidden")`
hasAttribute() :: Whether the element has an attribute. :: `el.hasAttribute("disabled")`
dataset :: Access to `data-*` attributes. :: `el.dataset.userId` :: data-attributes
children :: The child elements. :: `el.children`
firstElementChild :: The first child element. :: `el.firstElementChild`
lastElementChild :: The last child element. :: `el.lastElementChild`
nextElementSibling :: The next sibling element. :: `el.nextElementSibling`
previousElementSibling :: The previous sibling element. :: `el.previousElementSibling`
parentElement :: The parent element. :: `el.parentElement`
closest() :: The nearest ancestor (or the element itself) that matches a selector. :: `el.closest(".card")` :: js-event-delegation
matches() :: Whether the element matches a selector. :: `el.matches(".active")` :: js-event-delegation
append() :: Adds nodes or text after the last child. :: `el.append(child)` :: js-dom-elements
prepend() :: Adds nodes or text before the first child. :: `el.prepend(child)`
before() :: Inserts nodes before the element. :: `el.before(node)`
after() :: Inserts nodes after the element. :: `el.after(node)`
remove() :: Removes the element from the page. :: `el.remove()` :: js-dom-elements
replaceWith() :: Replaces the element with other nodes. :: `el.replaceWith(node)`
insertAdjacentHTML() :: Inserts HTML at a position relative to the element. :: `el.insertAdjacentHTML("beforeend", "<li>x</li>")`
cloneNode() :: Copies the element; pass `true` to copy its children too. :: `el.cloneNode(true)`
scrollIntoView() :: Scrolls the element into view. :: `el.scrollIntoView({ behavior: "smooth" })`
getBoundingClientRect() :: The size and position of the element relative to the viewport. :: `el.getBoundingClientRect()`
focus() :: Gives the element focus. :: `el.focus()`
click() :: Simulates a click on the element. :: `el.click()`
"""),
    ("Node and classList", """
appendChild() :: Adds a node as the last child. :: `parent.appendChild(child)` :: js-dom-elements
removeChild() :: Removes a child node. :: `parent.removeChild(child)`
insertBefore() :: Inserts a node before a reference child. :: `parent.insertBefore(node, ref)`
replaceChild() :: Replaces a child node. :: `parent.replaceChild(newNode, oldNode)`
contains() :: Whether a node is a descendant of another. :: `parent.contains(node)`
childNodes :: All child nodes, including text and comments. :: `el.childNodes`
parentNode :: The parent node. :: `el.parentNode`
nodeType :: A number for the kind of node, such as `1` for an element. :: `el.nodeType`
classList.add() :: Adds one or more classes. :: `el.classList.add("active")` :: js-dom-styles
classList.remove() :: Removes one or more classes. :: `el.classList.remove("active")` :: js-dom-styles
classList.toggle() :: Adds the class if missing, removes it if present. :: `el.classList.toggle("open")` :: js-dom-styles
classList.contains() :: Whether the element has a class. :: `el.classList.contains("open")` :: js-dom-styles
classList.replace() :: Replaces one class with another. :: `el.classList.replace("a", "b")`
"""),
    ("Style", """
element.style :: The inline styles of an element. :: `el.style.color = "red"` :: js-dom-styles
style.cssText :: All inline styles as one string. :: `el.style.cssText = "color: red"`
style.setProperty() :: Sets a CSS property, including custom properties. :: `el.style.setProperty("--size", "20px")` :: js-dom-styles
style.getPropertyValue() :: Reads a CSS property from the inline style. :: `el.style.getPropertyValue("--size")`
style.removeProperty() :: Removes an inline CSS property. :: `el.style.removeProperty("color")`
getComputedStyle() :: The final computed styles of an element. :: `getComputedStyle(el).fontSize` :: js-dom-styles
"""),
    ("Events", """
addEventListener() :: Attaches an event handler to a target. :: `el.addEventListener("click", fn)` :: js-event-listener
removeEventListener() :: Removes an event handler. :: `el.removeEventListener("click", fn)` :: js-event-listener
dispatchEvent() :: Sends an event to a target. :: `el.dispatchEvent(new Event("change"))`
new CustomEvent() :: Creates an event with custom data in `detail`. :: `new CustomEvent("saved", { detail: 1 })`
event.target :: The element that triggered the event. :: `event.target` :: js-event-delegation
event.currentTarget :: The element the handler is attached to. :: `event.currentTarget` :: js-event-listener
event.type :: The name of the event. :: `event.type`
event.preventDefault() :: Cancels the default action of the event. :: `event.preventDefault()` :: js-event-listener
event.stopPropagation() :: Stops the event from bubbling up. :: `event.stopPropagation()` :: js-event-listener
event.key :: The key that was pressed, in a keyboard event. :: `event.key === "Enter"` :: js-events
event.clientX :: The horizontal mouse position in the viewport. :: `event.clientX`
event.clientY :: The vertical mouse position in the viewport. :: `event.clientY`
"""),
    ("Window and browser", """
setTimeout() :: Runs a function once after a delay in milliseconds. :: `setTimeout(fn, 1000)` :: js-timers
clearTimeout() :: Cancels a timeout. :: `clearTimeout(id)` :: js-timers
setInterval() :: Runs a function repeatedly at an interval. :: `setInterval(fn, 1000)` :: js-timers
clearInterval() :: Cancels an interval. :: `clearInterval(id)` :: js-timers
requestAnimationFrame() :: Runs a function before the next repaint. :: `requestAnimationFrame(draw)`
window.innerWidth :: The width of the viewport in pixels. :: `window.innerWidth`
window.innerHeight :: The height of the viewport in pixels. :: `window.innerHeight`
window.scrollTo() :: Scrolls the window to a position. :: `window.scrollTo(0, 0)`
window.scrollY :: How far the page is scrolled vertically. :: `window.scrollY`
window.matchMedia() :: Tests a media query from JavaScript. :: `matchMedia("(max-width: 600px)").matches`
location.href :: The full URL; set it to navigate. :: `location.href`
location.pathname :: The path part of the URL. :: `location.pathname`
location.search :: The query string of the URL. :: `location.search`
location.hash :: The fragment part of the URL. :: `location.hash`
location.reload() :: Reloads the page. :: `location.reload()`
location.assign() :: Navigates to a new URL. :: `location.assign("/home")`
history.back() :: Goes back one page. :: `history.back()`
history.forward() :: Goes forward one page. :: `history.forward()`
history.pushState() :: Adds an entry to the history without reloading. :: `history.pushState({}, "", "/page")`
navigator.language :: The browser's preferred language. :: `navigator.language`
navigator.onLine :: Whether the browser is online. :: `navigator.onLine`
navigator.clipboard.writeText() :: Copies text to the clipboard. :: `navigator.clipboard.writeText("Hi")`
localStorage.setItem() :: Saves a value that stays after the browser closes. :: `localStorage.setItem("k", "v")` :: js-web-storage
localStorage.getItem() :: Reads a saved value. :: `localStorage.getItem("k")` :: js-web-storage
localStorage.removeItem() :: Removes a saved value. :: `localStorage.removeItem("k")` :: js-web-storage
sessionStorage :: Storage that lasts only for the browser tab session. :: `sessionStorage.setItem("k", "v")` :: js-web-storage
fetch() :: Makes a network request and returns a promise. :: `fetch("/api").then(r => r.json())` :: js-fetch
alert() :: Shows a message dialog. :: `alert("Hi")`
confirm() :: Shows an OK/Cancel dialog and returns a boolean. :: `confirm("Sure?")`
prompt() :: Shows a dialog that asks for text input. :: `prompt("Name?")`
"""),
    ("Forms", """
form.elements :: The controls of a form. :: `form.elements.email` :: js-dom-forms
form.submit() :: Submits the form. :: `form.submit()`
form.reset() :: Resets the form to its initial values. :: `form.reset()`
form.checkValidity() :: Whether all controls pass validation. :: `form.checkValidity()` :: form-validation
form.reportValidity() :: Checks validity and shows the browser's messages. :: `form.reportValidity()`
input.value :: The current value of a control. :: `input.value` :: js-dom-forms
input.checked :: Whether a checkbox or radio button is checked. :: `checkbox.checked` :: js-dom-forms
input.disabled :: Whether the control is disabled. :: `input.disabled = true`
input.files :: The files chosen in a file input. :: `input.files[0]`
select.selectedIndex :: The index of the selected option. :: `select.selectedIndex`
setCustomValidity() :: Sets a custom validation message. :: `input.setCustomValidity("Too short")` :: form-validation
validity :: The validity state of a control. :: `input.validity.valueMissing` :: form-validation
new FormData() :: Collects the values of a form's controls. :: `new FormData(form)`
"""),
]

REFS = [
    dict(slug="html-tags", module="html", title="HTML Tag Reference", cols=["Tag", "Description"],
         intro="Every HTML tag, grouped by purpose, with the obsolete ones marked.", groups=_groups(HTML_TAGS)),
    dict(slug="html-attributes", module="html", title="HTML Attribute Reference", cols=["Attribute", "Description", "Used on"],
         intro="Global attributes and the attributes that belong to particular elements.", groups=_groups(HTML_ATTRS)),
    dict(slug="html-events", module="html", title="HTML Event Reference", cols=["Event", "Description"],
         intro="Event attributes you can use to run JavaScript when something happens.", groups=_groups(HTML_EVENTS)),
    dict(slug="css-properties", module="css", title="CSS Property Reference", cols=["Property", "Description", "Values"],
         intro="CSS properties grouped by category, with the values you will use most.", groups=_groups(CSS_PROPS)),
    dict(slug="css-selectors", module="css", title="CSS Selector Reference", cols=["Selector", "Description", "Example"],
         intro="Basic, attribute and modern selectors, pseudo-classes and pseudo-elements.", groups=_groups(CSS_SELECTORS)),
    dict(slug="css-functions", module="css", title="CSS Function Reference", cols=["Function", "Description", "Example"],
         intro="CSS functions and at-rules with short examples.", groups=_groups(CSS_FUNCS)),
    dict(slug="js-reference", module="js", title="JavaScript Reference", cols=["Method / Property", "Description", "Syntax or example"],
         intro="Built-in JavaScript objects, methods and properties.", groups=_groups(JS_REF)),
    dict(slug="js-dom", module="js", title="JavaScript DOM Reference", cols=["Method / Property", "Description", "Example"],
         intro="Methods and properties for working with the page, events, the browser and forms.", groups=_groups(JS_DOM)),
]
