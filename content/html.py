"""HTML module lessons for TechHub.

Same schema as the original lessons.py: slug, title, group, intro, sections[{h, p, code?}],
example, tip (optional), exercise [{q, options, answer}].
In intro/p/tip text, <tag> mentions and `backtick spans` are shown as inline code.
"""

GROUPS = ["Getting Started", "Text & Style", "Links & Media", "Lists & Tables",
          "Forms", "Layout & Semantics", "Advanced"]

LESSONS = [
    # ---------------------------------------------------------------- Getting Started
    dict(slug="intro", title="HTML Introduction", group="Getting Started",
         intro="HTML is the language that gives every web page its structure. This chapter explains what it is and how it works.",
         sections=[
             dict(h="What is HTML?", p="HTML stands for HyperText Markup Language. It is the standard language for creating web pages. HTML describes the structure of a page using elements, and the browser turns those elements into what you see."),
             dict(h="A simple page", p="Every HTML page follows the same pattern. The browser reads the file from top to bottom and displays the content inside <body>.",
                  code='<!DOCTYPE html>\n<html>\n  <head>\n    <title>My first page</title>\n  </head>\n  <body>\n    <h1>Hello, world!</h1>\n    <p>This is my first web page.</p>\n  </body>\n</html>'),
             dict(h="HTML, CSS and JavaScript", p="HTML is the structure (the skeleton). CSS controls the look (colours, spacing, fonts). JavaScript adds behaviour (clicks, animation, updates). You learn HTML first because the other two build on it."),
         ],
         example='<!DOCTYPE html>\n<html>\n  <head>\n    <title>My first page</title>\n  </head>\n  <body>\n    <h1>Hello, world!</h1>\n    <p>This is my first web page.</p>\n  </body>\n</html>',
         tip="You do not need to install anything. Every example in this tutorial runs in your browser.",
         exercise=[
             dict(q="What does HTML stand for?", options=["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Making Language"], answer=0),
             dict(q="Which language controls the colours and spacing of a page?", options=["HTML", "CSS", "Python", "SQL"], answer=1),
         ]),
    dict(slug="structure", title="HTML Page Structure", group="Getting Started",
         intro="Every page is built from the same few parts. Learn them once and you can read any HTML file.",
         sections=[
             dict(h="The main parts", p="<!DOCTYPE html> tells the browser this is a modern HTML page. <html> wraps everything. <head> holds information about the page. <body> holds everything people see."),
             dict(h="Inside the head", p="The head is not shown on the page. It sets the tab title with <title>, the character set with <meta charset>, and links to stylesheets with <link>.",
                  code='<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>My page</title>\n  <link rel="stylesheet" href="style.css">\n</head>'),
             dict(h="The lang attribute", p='Add lang="en" to <html> so screen readers and search engines know the language of your page.'),
         ],
         example='<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8">\n    <title>Page structure</title>\n  </head>\n  <body>\n    <h1>Visible content goes in the body</h1>\n  </body>\n</html>',
         tip="Only the content inside <body> is displayed. Change the <title> and look at the browser tab to see where it appears.",
         exercise=[
             dict(q="Which element contains everything the visitor sees?", options=["<head>", "<body>", "<title>", "<meta>"], answer=1),
             dict(q="Which element sets the text shown on the browser tab?", options=["<title>", "<h1>", "<header>", "<tab>"], answer=0),
         ]),
    dict(slug="elements", title="HTML Elements", group="Getting Started",
         intro="An HTML element is the basic building block of every page: a start tag, some content and an end tag.",
         sections=[
             dict(h="Anatomy of an element", p="An element has an opening tag, content, and a closing tag. The closing tag has a forward slash.",
                  code='<p>This is a paragraph.</p>\n<!-- <p> opening tag, text content, </p> closing tag -->'),
             dict(h="Empty elements", p="Some elements have no content and no closing tag, such as <br> (line break), <hr> (horizontal line) and <img>. They are called void or empty elements."),
             dict(h="Nested elements", p="Elements can live inside other elements. Close the inner element before the outer one.",
                  code='<body>\n  <p>I am <strong>very</strong> happy.</p>\n</body>'),
         ],
         example='<p>This is a <strong>bold</strong> word inside a paragraph.</p>\n<p>Line one<br>Line two after a break.</p>\n<hr>',
         tip="Tag names are not case sensitive, but lowercase is the convention and is easier to read.",
         exercise=[
             dict(q="Which of these is an empty (void) element?", options=["<p>", "<br>", "<h1>", "<strong>"], answer=1),
             dict(q="What marks the end of an element?", options=["A closing tag with a slash", "A semicolon", "A blank line", "A comment"], answer=0),
         ]),
    dict(slug="attributes", title="HTML Attributes", group="Getting Started",
         intro="Attributes give elements extra information. They always sit inside the opening tag.",
         sections=[
             dict(h="Name and value", p='Attributes come as name="value" pairs. For example, href tells a link where to go and src tells an image where its file is.',
                  code='<a href="https://example.com">Visit</a>\n<img src="photo.jpg" alt="A photo">'),
             dict(h="Common attributes", p="id gives an element a unique name. class groups elements for styling. style adds quick CSS. title shows a tooltip. lang sets the language.",
                  code='<p id="intro" class="note" title="Hello!" style="color: blue;">Hover over me.</p>'),
             dict(h="Always use quotes", p="Write attribute values in double quotes. It is required when a value contains spaces and it keeps your code consistent."),
         ],
         example='<h1 style="color: royalblue;">A blue heading</h1>\n<p title="This is a tooltip">Hover over this paragraph.</p>\n<a href="https://www.wikipedia.org" target="_blank">Open Wikipedia</a>',
         tip="Try changing royalblue to another colour name such as tomato or seagreen.",
         exercise=[
             dict(q="Which attribute gives a link its destination?", options=["src", "href", "alt", "link"], answer=1),
             dict(q="Where do attributes go?", options=["In the opening tag", "In the closing tag", "After the closing tag", "In the head only"], answer=0),
         ]),

    # ---------------------------------------------------------------- Text
    dict(slug="headings", title="HTML Headings", group="Text & Style",
         intro="Headings give your page an outline. HTML has six levels, from <h1> (most important) to <h6> (least).",
         sections=[
             dict(h="Six levels", p="Use <h1> for the main title of the page, <h2> for main sections, <h3> for subsections, and so on.",
                  code='<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>'),
             dict(h="Meaning, not size", p="Browsers make <h1> large and <h6> small, but pick a level for its meaning. If you only want bigger text, use CSS. Search engines and screen readers use headings to understand your page."),
             dict(h="Use one h1", p="A page normally has a single <h1>. Do not skip levels, for example going from <h1> straight to <h4>."),
         ],
         example='<h1>Heading level 1</h1>\n<h2>Heading level 2</h2>\n<h3>Heading level 3</h3>\n<h4>Heading level 4</h4>\n<h5>Heading level 5</h5>\n<h6>Heading level 6</h6>',
         tip="Headings are for structure. Never use a heading just to make text bold or big.",
         exercise=[
             dict(q="Which is the most important heading?", options=["<h6>", "<h3>", "<h1>", "<head>"], answer=2),
             dict(q="How many heading levels does HTML have?", options=["3", "4", "6", "10"], answer=2),
         ]),
    dict(slug="paragraphs", title="HTML Paragraphs", group="Text & Style",
         intro="The <p> element holds a block of text. Browsers add space above and below each paragraph.",
         sections=[
             dict(h="Paragraphs", p="Wrap each paragraph in its own <p> element.", code="<p>This is a paragraph.</p>\n<p>This is another paragraph.</p>"),
             dict(h="Extra spaces are ignored", p="The browser collapses extra spaces and line breaks in your code into a single space. To start a new line inside a paragraph, use <br>. To draw a dividing line, use <hr>.",
                  code="<p>Roses are red,<br>Violets are blue.</p>\n<hr>\n<p>The line above is an hr.</p>"),
             dict(h="Preformatted text", p="Use <pre> when spaces and line breaks must be kept exactly as typed, such as for code or poems."),
         ],
         example="<p>This paragraph\n   has extra     spaces and line breaks\n   in the code, but the browser ignores them.</p>\n\n<p>Use br to break<br>a line.</p>\n\n<pre>This text\n   keeps its\n      spacing.</pre>",
         tip="Do not press Enter twice to make space between paragraphs. Use separate <p> elements and style the gap with CSS.",
         exercise=[
             dict(q="Which tag starts a new line without starting a new paragraph?", options=["<p>", "<br>", "<hr>", "<pre>"], answer=1),
             dict(q="Which element keeps spaces and line breaks exactly as typed?", options=["<pre>", "<p>", "<span>", "<em>"], answer=0),
         ]),
    dict(slug="formatting", title="HTML Text Formatting", group="Text & Style",
         intro="HTML has elements that change how text looks and, more importantly, what it means.",
         sections=[
             dict(h="Meaning vs. looks", p="<strong> means important text and <em> means emphasised text. Browsers show them as bold and italic. <b> and <i> look the same but add no extra meaning.",
                  code="<strong>Important</strong>\n<em>Emphasised</em>\n<b>Bold</b>\n<i>Italic</i>"),
             dict(h="Other useful elements", p="<mark> highlights text. <small> makes smaller print. <del> shows deleted text and <ins> shows inserted text. <sub> and <sup> make subscript and superscript."),
             dict(h="Code", p="Use <code> for a piece of computer code, shown in a monospace font.", code="<p>Use the <code>console.log()</code> function.</p>"),
         ],
         example="<p>This is <strong>important</strong> and this is <em>emphasised</em>.</p>\n<p>Water is H<sub>2</sub>O and 3<sup>2</sup> = 9.</p>\n<p>Price: <del>$20</del> <ins>$15</ins></p>\n<p>Please <mark>remember this</mark>.</p>\n<p>Type <code>print('hi')</code> to say hi.</p>",
         tip="Prefer <strong> and <em> over <b> and <i> when the text really is important or emphasised.",
         exercise=[
             dict(q="Which element marks text as important?", options=["<strong>", "<small>", "<sub>", "<hr>"], answer=0),
             dict(q="Which element highlights text like a marker pen?", options=["<mark>", "<em>", "<code>", "<ins>"], answer=0),
         ]),
    dict(slug="comments", title="HTML Comments", group="Text & Style",
         intro="Comments are notes in your code. The browser ignores them, so visitors never see them.",
         sections=[
             dict(h="Writing a comment", p="A comment starts with <!-- and ends with -->.", code="<!-- This is a comment -->\n<p>This is visible.</p>"),
             dict(h="Why use comments?", p="Use them to explain tricky code, to leave reminders for yourself, or to switch off a piece of code temporarily without deleting it.",
                  code="<!-- <p>This paragraph is hidden for now.</p> -->"),
         ],
         example="<!-- This comment is not shown -->\n<p>You can see this paragraph.</p>\n<!-- <p>You cannot see this one.</p> -->",
         tip="Comments are still visible to anyone who views the page source, so never put passwords in them.",
         exercise=[
             dict(q="Which is the correct HTML comment?", options=["<!-- comment -->", "// comment", "/* comment */", "# comment"], answer=0),
             dict(q="Can a visitor see an HTML comment in the rendered page?", options=["Yes, in a tooltip", "No, but it is visible in the page source", "Yes, in small print", "No, and it cannot be found anywhere"], answer=1),
         ]),

    # ---------------------------------------------------------------- Links & Media
    dict(slug="links", title="HTML Links", group="Links & Media",
         intro="Links connect web pages together. They are created with the <a> (anchor) element.",
         sections=[
             dict(h="Creating a link", p="The href attribute holds the destination. The text between the tags is what people click.",
                  code='<a href="https://www.wikipedia.org">Go to Wikipedia</a>'),
             dict(h="Open in a new tab", p='Add target="_blank" to open the link in a new tab. Pair it with rel="noopener" for safety.',
                  code='<a href="https://www.wikipedia.org" target="_blank" rel="noopener">New tab</a>'),
             dict(h="Links inside a page", p="Give an element an id, then link to it with a # sign.",
                  code='<a href="#bottom">Jump to the bottom</a>\n...\n<h2 id="bottom">Bottom</h2>'),
             dict(h="Email links", p='Use mailto: to open the visitor\'s email app.', code='<a href="mailto:hello@example.com">Email us</a>'),
         ],
         example='<p><a href="https://www.wikipedia.org" target="_blank">Visit Wikipedia</a></p>\n<p><a href="#end">Jump to the end</a></p>\n<div style="height:300px"></div>\n<h3 id="end">You reached the end</h3>',
         tip="Write link text that makes sense on its own. Prefer \"Read the pricing guide\" over \"Click here\".",
         exercise=[
             dict(q="Which attribute holds the address a link points to?", options=["src", "href", "target", "url"], answer=1),
             dict(q="Which target value opens a link in a new tab?", options=["_self", "_blank", "_new", "_top"], answer=1),
         ]),
    dict(slug="images", title="HTML Images", group="Links & Media",
         intro="The <img> element puts a picture on the page. It is an empty element, so it has no closing tag.",
         sections=[
             dict(h="Adding an image", p="src is the image address. alt is text that describes the image.",
                  code='<img src="cat.jpg" alt="A grey cat on a sofa">'),
             dict(h="Why alt matters", p="Screen readers read the alt text aloud, and it is shown if the image fails to load. Describe what the image shows. Use alt=\"\" for pure decoration."),
             dict(h="Size", p="Use width and height to set the size. Giving both stops the page jumping while images load.",
                  code='<img src="cat.jpg" alt="A cat" width="300" height="200">'),
         ],
         example='<img src="data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'300\' height=\'120\'><rect width=\'300\' height=\'120\' fill=\'%231e5eff\'/><text x=\'150\' y=\'68\' fill=\'white\' font-size=\'22\' text-anchor=\'middle\'>My image</text></svg>" alt="A blue banner that says My image" width="300" height="120">',
         tip="Every <img> needs an alt attribute. It helps blind visitors, and search engines use it too.",
         exercise=[
             dict(q="Which attribute gives the text alternative for an image?", options=["title", "alt", "src", "name"], answer=1),
             dict(q="How do you close an <img> element?", options=["</img>", "You do not, it is an empty element", "<img/> only", "With </image>"], answer=1),
         ]),

    # ---------------------------------------------------------------- Lists & Tables
    dict(slug="lists", title="HTML Lists", group="Lists & Tables",
         intro="Lists group related items. HTML has bulleted, numbered and description lists.",
         sections=[
             dict(h="Unordered list", p="<ul> makes a bulleted list. Each item is an <li>.", code="<ul>\n  <li>Coffee</li>\n  <li>Tea</li>\n</ul>"),
             dict(h="Ordered list", p="<ol> makes a numbered list. Use it when the order matters.", code="<ol>\n  <li>Boil water</li>\n  <li>Add tea</li>\n</ol>"),
             dict(h="Description list", p="<dl> pairs terms (<dt>) with descriptions (<dd>).", code="<dl>\n  <dt>HTML</dt>\n  <dd>The structure of a web page</dd>\n</dl>"),
         ],
         example="<h3>Shopping</h3>\n<ul>\n  <li>Milk</li>\n  <li>Bread</li>\n</ul>\n\n<h3>Steps</h3>\n<ol>\n  <li>Open the editor</li>\n  <li>Write HTML</li>\n  <li>Run it</li>\n</ol>\n\n<dl>\n  <dt>HTML</dt>\n  <dd>The structure of a page</dd>\n</dl>",
         tip="To nest a list, put the inner <ul> or <ol> inside an <li>.",
         exercise=[
             dict(q="Which element creates a numbered list?", options=["<ul>", "<ol>", "<dl>", "<li>"], answer=1),
             dict(q="Which element holds a single list item?", options=["<item>", "<li>", "<dd>", "<ul>"], answer=1),
         ]),
    dict(slug="tables", title="HTML Tables", group="Lists & Tables",
         intro="Tables show data in rows and columns. Use them for data, not for page layout.",
         sections=[
             dict(h="The building blocks", p="<table> wraps the table. <tr> is a row. <th> is a header cell and <td> is a data cell.",
                  code="<table>\n  <tr><th>Name</th><th>Age</th></tr>\n  <tr><td>Asha</td><td>21</td></tr>\n</table>"),
             dict(h="Grouping", p="<thead>, <tbody> and <tfoot> group the header, body and footer rows. <caption> gives the table a title."),
             dict(h="Spanning cells", p="colspan makes a cell stretch across columns and rowspan across rows."),
         ],
         example='<table border="1" cellpadding="6">\n  <caption>Marks</caption>\n  <thead>\n    <tr><th>Name</th><th>Maths</th><th>Science</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Asha</td><td>92</td><td>88</td></tr>\n    <tr><td>Ravi</td><td>85</td><td>90</td></tr>\n  </tbody>\n</table>',
         tip="The border attribute is old. Real sites add borders with CSS, which you will learn next.",
         exercise=[
             dict(q="Which element is a table row?", options=["<td>", "<tr>", "<th>", "<row>"], answer=1),
             dict(q="Which element is a header cell?", options=["<th>", "<td>", "<thead>", "<caption>"], answer=0),
         ]),

    # ---------------------------------------------------------------- Forms and layout
    dict(slug="forms", title="HTML Forms", group="Forms",
         intro="Forms collect information from visitors, like a name, an email or a choice.",
         sections=[
             dict(h="The form element", p="<form> wraps all the controls. action says where to send the data and method says how.",
                  code='<form action="/signup" method="post">\n  ...\n</form>'),
             dict(h="Inputs and labels", p="<input> is a field. Its type decides what it is: text, email, password, checkbox, radio, number, date and more. Connect a <label> to an input with matching for and id so clicking the label focuses the field.",
                  code='<label for="email">Email</label>\n<input type="email" id="email" name="email" required>'),
             dict(h="Other controls", p="<textarea> is for long text, <select> with <option> makes a drop-down, and <button> submits the form."),
         ],
         example='<form>\n  <p><label for="n">Name</label><br>\n  <input type="text" id="n" name="name" placeholder="Your name"></p>\n  <p><label for="e">Email</label><br>\n  <input type="email" id="e" name="email" required></p>\n  <p><label for="c">Course</label><br>\n  <select id="c" name="course">\n    <option>HTML</option>\n    <option>CSS</option>\n  </select></p>\n  <p><label><input type="checkbox"> I agree</label></p>\n  <button type="button">Send</button>\n</form>',
         tip="Every input needs a label. It makes forms usable with a screen reader and gives a bigger click area.",
         exercise=[
             dict(q="Which input type is meant for email addresses?", options=['type="mail"', 'type="email"', 'type="text-email"', 'type="at"'], answer=1),
             dict(q="Which element makes a drop-down list?", options=["<select>", "<dropdown>", "<list>", "<input>"], answer=0),
         ]),
    dict(slug="semantic", title="HTML Semantic Layout", group="Layout & Semantics",
         intro="Semantic elements describe their purpose, so both people and browsers understand your page layout.",
         sections=[
             dict(h="Layout elements", p="<header> is the top of a page or section. <nav> holds navigation links. <main> is the main content. <section> groups related content. <article> is a self-contained piece. <aside> is side content. <footer> is the bottom.",
                  code="<header>...</header>\n<nav>...</nav>\n<main>\n  <article>...</article>\n  <aside>...</aside>\n</main>\n<footer>...</footer>"),
             dict(h="div and span", p="<div> is a generic block container and <span> a generic inline one. Use them when no semantic element fits, mostly to attach CSS classes."),
         ],
         example='<header>\n  <h1>My Blog</h1>\n  <nav><a href="#">Home</a> | <a href="#">About</a></nav>\n</header>\n<main>\n  <article>\n    <h2>First post</h2>\n    <p>Hello from my blog.</p>\n  </article>\n</main>\n<footer><p>&copy; 2026 My Blog</p></footer>',
         tip="Prefer semantic elements over a pile of <div> tags. The page becomes easier to read and to navigate.",
         exercise=[
             dict(q="Which element should hold the main navigation links?", options=["<nav>", "<aside>", "<footer>", "<span>"], answer=0),
             dict(q="Which element is a generic block container with no meaning?", options=["<div>", "<article>", "<main>", "<header>"], answer=0),
         ]),
]

LESSONS += [
    # ============================================================ Getting Started
    dict(slug="editors", title="HTML Editors", group="Getting Started",
         intro="All you need to write HTML is a text editor and a web browser. This chapter shows how to create your first page and open it.",
         sections=[
             dict(h="Choose an editor", p="Any plain-text editor works, including Notepad and TextEdit. A code editor such as Visual Studio Code is more comfortable because it colours your code, closes tags for you and suggests names as you type."),
             dict(h="Create your first page", p="Follow these four steps: create a file called `index.html`, type the code below, save it with UTF-8 encoding, then double-click the file to open it in your browser.",
                  code='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My first page</title>
</head>
<body>
  <h1>It works!</h1>
</body>
</html>'''),
             dict(h="See your changes", p="After every edit, save the file and refresh the browser (F5 or Ctrl+R). The page always shows the last saved version of the file."),
         ],
         example='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My first page</title>
</head>
<body>
  <h1>It works!</h1>
  <p>I wrote this page in a text editor.</p>
</body>
</html>''',
         tip="When you save a word-processor document as `.docx` the file is not plain text. Always save HTML as a plain text file ending in `.html`.",
         exercise=[
             dict(q="Which file extension do HTML files normally use?", options=[".txt", ".html", ".docx", ".exe"], answer=1),
             dict(q="What do you need at minimum to write and view an HTML page?", options=["A text editor and a web browser", "A paid compiler", "A database server", "A graphics tablet"], answer=0),
             dict(q="After editing an HTML file, what must you do to see the change in the browser?", options=["Restart the computer", "Save the file and refresh the page", "Rename the file", "Delete the old tab history"], answer=1),
         ]),
    dict(slug="basic", title="HTML Basic Examples", group="Getting Started",
         intro="Before the details, here is a quick tour of the elements you will use on almost every page: headings, paragraphs, links, images and lists.",
         sections=[
             dict(h="A page with the basics", p="Read this page from top to bottom. Each line is explained in the lessons that follow.",
                  code='''<h1>My Website</h1>
<p>Welcome to my first website.</p>
<a href="about.html">About me</a>
<img src="me.jpg" alt="A photo of me" width="120">
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>'''),
             dict(h="Documents and elements", p="An HTML document is a tree of elements. Elements sit inside other elements, and the browser shows them in the order they appear in the file."),
             dict(h="What to learn next", p="Start with page structure, then elements and attributes. After that, headings, text and links will feel familiar."),
         ],
         example='''<h1>My Website</h1>
<p>Welcome to my first website.</p>
<p><a href="#about">About me</a></p>
<img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='60'><rect width='120' height='60' fill='royalblue'/><text x='60' y='36' fill='white' font-size='16' text-anchor='middle'>Photo</text></svg>" alt="A blue placeholder photo" width="120" height="60">
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>''',
         tip="Do not worry about memorising everything now. Come back to this page whenever you need a quick reminder.",
         exercise=[
             dict(q="In a basic page, which element is the usual choice for the main title?", options=["<p>", "<h1>", "<li>", "<img>"], answer=1),
             dict(q="Which basic element shows a bulleted list of items?", options=["<ol>", "<table>", "<ul>", "<a>"], answer=2),
         ]),
    dict(slug="head-elements", title="HTML Head Elements", group="Getting Started",
         intro="The <head> holds information about the page. Visitors do not see it, but browsers and search engines depend on it.",
         sections=[
             dict(h="The elements you can use", p="<title> sets the tab title. <meta> gives page information. <link> loads outside files such as stylesheets. <style> holds CSS. <script> holds or loads JavaScript. <base> sets a default address for relative links.",
                  code='''<head>
  <title>My page</title>
  <meta charset="UTF-8">
  <meta name="description" content="A short summary of this page">
  <meta name="author" content="Asha">
  <link rel="stylesheet" href="style.css">
  <style>
    body { background: white; }
  </style>
  <script src="app.js" defer></script>
  <base href="https://example.com/docs/">
</head>'''),
             dict(h="The base element", p="`<base href>` makes every relative link on the page start from one address. A page can only have one <base>, and it must come before any link that uses it."),
             dict(h="Metadata", p="Use `name` and `content` on <meta> for descriptions and authors. Use `charset` for the character set and `name=\"viewport\"` to make the page work on phones."),
         ],
         example='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Head elements</title>
  <style>
    body { font-family: sans-serif; background: aliceblue; color: navy; }
  </style>
</head>
<body>
  <h1>Styled from the head</h1>
  <p>The colours on this page come from the style element in the head.</p>
</body>
</html>''',
         tip="Only the content of <title> and the effects of the other head elements are visible. The head itself is never drawn on the page.",
         exercise=[
             dict(q="Which head element sets a default address for all relative links?", options=["<link>", "<meta>", "<base>", "<style>"], answer=2),
             dict(q="Which head element puts CSS rules directly inside the page?", options=["<style>", "<css>", "<script>", "<font>"], answer=0),
             dict(q="Where does the <meta> element belong?", options=["Inside <body>", "Inside <head>", "After </html>", "Inside <footer>"], answer=1),
         ]),

    # ============================================================ Text & Style
    dict(slug="styles", title="HTML Styles", group="Text & Style",
         intro="The `style` attribute changes how an element looks by adding CSS directly to it.",
         sections=[
             dict(h="The style attribute", p="Write CSS as `property: value;` pairs inside the attribute. Separate several pairs with semicolons.",
                  code='<p style="color: blue; font-size: 20px;">Blue text, 20 pixels tall</p>'),
             dict(h="Common properties", p="`color` sets text colour. `background-color` sets the background. `font-size` and `font-family` control the text. `text-align` aligns it left, right, centre or justify. `border` draws a line around an element.",
                  code='<h1 style="text-align: center; color: navy;">Centred heading</h1>\n<p style="background-color: lightyellow; border: 1px solid orange;">A boxed paragraph</p>'),
             dict(h="Use sparingly", p="Inline styles are fine for quick tests, but real sites keep CSS in a stylesheet so one change updates every page."),
         ],
         example='''<h1 style="text-align: center; color: royalblue;">Styled heading</h1>
<p style="font-family: Georgia, serif; font-size: 20px;">This paragraph uses a serif font at 20 pixels.</p>
<p style="background-color: lightyellow; border: 2px solid orange; padding: 8px;">A highlighted box.</p>''',
         tip="Change `royalblue` to another colour name and press Run to see the heading change at once.",
         exercise=[
             dict(q="Which attribute adds CSS directly to a single element?", options=["class", "css", "style", "format"], answer=2),
             dict(q="Which CSS property changes the colour of text?", options=["background-color", "font-style", "text-decoration", "color"], answer=3),
             dict(q="Which declaration centres text horizontally?", options=["align: middle", "text-align: center", "text-center: on", "font-align: centre"], answer=1),
         ]),
    dict(slug="quotations", title="HTML Quotations", group="Text & Style",
         intro="HTML has special elements for quotes, citations, abbreviations and contact details. They add meaning as well as style.",
         sections=[
             dict(h="Block and inline quotes", p="`<blockquote>` holds a long quotation and is usually indented. `<q>` holds a short quotation inside a sentence, and browsers add quotation marks for you.",
                  code='<blockquote cite="https://example.com/speech">\n  The only way to learn is by doing.\n</blockquote>\n<p>She said <q>practice every day</q> and smiled.</p>'),
             dict(h="Citation and abbreviation", p="`<cite>` marks the title of a work, such as a book or film. `<abbr>` marks an abbreviation, and its `title` attribute shows the full form when you hover.",
                  code='<p>I read <cite>The Hobbit</cite> last week.</p>\n<p>The <abbr title="World Health Organization">WHO</abbr> published a report.</p>'),
             dict(h="Contact details", p="`<address>` is for the contact details of the author or owner of the page. `<bdo dir=\"rtl\">` overrides the text direction."),
         ],
         example='''<blockquote>Learning never exhausts the mind.</blockquote>
<p>As the saying goes, <q>practice makes progress</q>.</p>
<p>I love <cite>The Little Prince</cite>.</p>
<p><abbr title="HyperText Markup Language">HTML</abbr> is easy to learn.</p>
<address>Written by Asha<br>asha@example.com</address>''',
         tip="Never use <blockquote> just to indent text. Use it only when the content really is a quotation.",
         exercise=[
             dict(q="Which element marks a short quotation inside a sentence and adds quote marks automatically?", options=["<q>", "<blockquote>", "<cite>", "<quote>"], answer=0),
             dict(q="Which element marks an abbreviation and can show its full form on hover?", options=["<dfn>", "<short>", "<abbr>", "<i>"], answer=2),
             dict(q="Which element is meant for the contact details of a page author?", options=["<cite>", "<contact>", "<address>", "<small>"], answer=2),
         ]),
    dict(slug="code-elements", title="HTML Computer Code", group="Text & Style",
         intro="HTML includes elements that display code, keyboard keys and program output in a clear, monospace style.",
         sections=[
             dict(h="The code family", p="`<code>` is a piece of code. `<kbd>` is keyboard input. `<samp>` is sample output from a program. `<var>` is a variable name. All of them use a monospace font by default.",
                  code='<p>Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.</p>\n<p>The program prints <samp>Hello, world!</samp></p>\n<p>Let <var>x</var> be a number.</p>'),
             dict(h="Keeping the layout", p="`<code>` collapses whitespace like normal text. To keep line breaks and indentation, wrap it in `<pre>`.",
                  code='<pre><code>for (let i = 0; i &lt; 3; i++) {\n  console.log(i);\n}</code></pre>'),
         ],
         example='''<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>
<p>Run <code>python app.py</code> in the terminal.</p>
<p>The program prints <samp>Hello, world!</samp></p>
<p>If <var>x</var> = 3, then <var>x</var> + 2 = 5.</p>
<pre><code>if (a &lt; b) {
  go();
}</code></pre>''',
         tip="Inside code samples, write `&lt;` instead of `<` so the browser shows the character instead of reading it as a tag.",
         exercise=[
             dict(q="Which element shows keyboard input such as Ctrl + C?", options=["<samp>", "<kbd>", "<var>", "<key>"], answer=1),
             dict(q="Which element displays sample output from a program?", options=["<var>", "<code>", "<kbd>", "<samp>"], answer=3),
             dict(q="Which element keeps the line breaks and spaces of a code block?", options=["<pre>", "<br>", "<span>", "<hr>"], answer=0),
         ]),
    dict(slug="colors", title="HTML Colors", group="Text & Style",
         intro="Colours are set with CSS. You can write them as names, HEX codes, RGB, HSL, or with transparency.",
         sections=[
             dict(h="Colour names", p="HTML supports 140 colour names such as `tomato`, `royalblue`, `seagreen` and `gold`.",
                  code='<div style="background-color: tomato;">Tomato</div>'),
             dict(h="HEX and RGB", p="A HEX colour is `#RRGGBB`, where each pair is a hexadecimal number from 00 to FF. `rgb(255, 0, 0)` gives the same red using numbers from 0 to 255.",
                  code='<div style="background-color: #1D5BD8;">HEX blue</div>\n<div style="background-color: rgb(29, 91, 216);">RGB blue</div>'),
             dict(h="HSL and transparency", p="`hsl(220, 80%, 48%)` sets hue (0 to 360), saturation and lightness. Add a fourth value for transparency with `rgba()` or `hsla()`: 0 is fully clear and 1 is solid.",
                  code='<div style="background-color: rgba(29, 91, 216, 0.4);">Semi-transparent</div>'),
         ],
         example='''<div style="background-color: tomato; padding: 8px; color: white;">tomato (name)</div>
<div style="background-color: #1D5BD8; padding: 8px; color: white;">#1D5BD8 (HEX)</div>
<div style="background-color: rgb(46, 139, 87); padding: 8px; color: white;">rgb(46, 139, 87)</div>
<div style="background-color: hsl(45, 100%, 50%); padding: 8px;">hsl(45, 100%, 50%)</div>
<div style="background-color: rgba(29, 91, 216, 0.3); padding: 8px;">rgba(29, 91, 216, 0.3)</div>''',
         tip="Check that text and background colours have enough contrast. Light grey on white is hard to read for many people.",
         exercise=[
             dict(q="Which value is the HEX code for pure red?", options=["#00FF00", "#0000FF", "#FFFF00", "#FF0000"], answer=3),
             dict(q="Which colour does rgb(0, 0, 255) show?", options=["Red", "Green", "Blue", "Black"], answer=2),
             dict(q="What does the fourth value in rgba(255, 0, 0, 0.5) control?", options=["Opacity (alpha)", "Red amount", "Border width", "Brightness of the screen"], answer=0),
         ]),
    dict(slug="css", title="HTML and CSS", group="Text & Style",
         intro="CSS (Cascading Style Sheets) controls how HTML looks. There are three ways to add it to a page.",
         sections=[
             dict(h="Inline CSS", p="Use the `style` attribute on one element. It affects only that element.",
                  code='<h1 style="color: blue;">Blue heading</h1>'),
             dict(h="Internal CSS", p="Put rules inside a `<style>` element in the `<head>`. They apply to the whole page.",
                  code='<head>\n  <style>\n    h1 { color: blue; }\n    p  { font-size: 18px; }\n  </style>\n</head>'),
             dict(h="External CSS", p="Save the rules in a file ending in `.css` and link it from the head. One file can style every page of a site, so this is the usual choice.",
                  code='<head>\n  <link rel="stylesheet" href="styles.css">\n</head>'),
             dict(h="Which rule wins?", p="When rules clash, an inline style normally beats a rule in a stylesheet. If two stylesheet rules are equally specific, the one that comes last wins."),
         ],
         example='''<!DOCTYPE html>
<html>
<head>
  <style>
    h1 { color: royalblue; }
    p { font-size: 18px; color: #333; }
    .big { font-size: 28px; }
  </style>
</head>
<body>
  <h1>Internal CSS</h1>
  <p>This paragraph is styled by a rule in the head.</p>
  <p class="big">This one also uses a class.</p>
</body>
</html>''',
         tip="Use external CSS for real projects. Changing one file then updates the look of every page.",
         exercise=[
             dict(q="Which way of adding CSS uses a separate .css file?", options=["Inline", "Internal", "External", "Embedded"], answer=2),
             dict(q="Where does an internal stylesheet go?", options=["After </html>", "In a <style> element inside <head>", "Inside <footer>", "In a <css> element in <body>"], answer=1),
             dict(q="When an inline style and a normal stylesheet rule set the same property, which one wins?", options=["The inline style", "The stylesheet rule", "The longer one", "The browser picks at random"], answer=0),
         ]),
    dict(slug="entities", title="HTML Entities", group="Text & Style",
         intro="Some characters have a special meaning in HTML. To show them as text, write an entity instead.",
         sections=[
             dict(h="Reserved characters", p="The browser reads `<` as the start of a tag. To display it, write `&lt;`. Other common entities are `&gt;` for >, `&amp;` for & and `&quot;` for a double quote.",
                  code='<p>Use &lt;p&gt; to start a paragraph.</p>\n<p>Tom &amp; Jerry</p>'),
             dict(h="Entity syntax", p="An entity starts with `&` and ends with `;`. You can use a name such as `&copy;` or a number such as `&#169;`. Names are easier to read, numbers cover every character.",
                  code='&copy; 2026   &#169; 2026'),
             dict(h="Non-breaking space", p="The browser collapses several spaces into one. `&nbsp;` is a space that is not collapsed and never lets a line break between two words.",
                  code='<p>Price: 5&nbsp;&nbsp;&nbsp;dollars</p>'),
         ],
         example='''<p>To write a paragraph, use &lt;p&gt; and &lt;/p&gt;.</p>
<p>Fish &amp; chips</p>
<p>She said &quot;hello&quot;.</p>
<p>Spaced&nbsp;&nbsp;&nbsp;&nbsp;out&nbsp;text</p>
<p>&copy; 2026 My Site</p>''',
         tip="Always write `&amp;` for an ampersand in text, even though most browsers forgive a bare &.",
         exercise=[
             dict(q="Which entity displays a less-than sign?", options=["&gt;", "&lt;", "&amp;", "&less;"], answer=1),
             dict(q="Which entity displays an ampersand?", options=["&and;", "&amp;", "&apos;", "&ampersand;"], answer=1),
             dict(q="What does &nbsp; produce?", options=["A new line", "A non-breaking space", "A bold word", "A tab"], answer=1),
         ]),
    dict(slug="symbols", title="HTML Symbols", group="Text & Style",
         intro="Entities can also show symbols that are not on your keyboard, such as currency signs, maths signs and arrows.",
         sections=[
             dict(h="Common symbols", p="`&copy;` shows ©, `&reg;` shows ®, `&trade;` shows ™, `&euro;` shows €, `&pound;` shows £, `&deg;` shows °, `&times;` shows ×, `&divide;` shows ÷ and `&rarr;` shows →.",
                  code='<p>&copy; 2026 &reg; &trade;</p>\n<p>&euro;20 &pound;15 &yen;300</p>\n<p>25&deg;C &times; 2 &divide; 5 &rarr;</p>'),
             dict(h="Numeric references", p="Every character has a number. Use `&#8364;` (decimal) or `&#x20AC;` (hexadecimal) for the euro sign.",
                  code='<p>&#8364; &#x20AC;</p>'),
         ],
         example='''<p>Copyright &copy; 2026</p>
<p>Registered &reg; and trademark &trade;</p>
<p>Prices: &euro;20, &pound;15, &yen;300</p>
<p>Temperature: 25&deg;C</p>
<p>Maths: 6 &times; 3 = 18, 18 &divide; 3 = 6</p>
<p>Arrow: &rarr; &larr; &hearts;</p>''',
         tip="Use UTF-8 and you can also type most symbols directly. Entities are handy when your keyboard does not have the symbol.",
         exercise=[
             dict(q="Which entity name shows the copyright symbol?", options=["&cp;", "&copy;", "&cright;", "&c;"], answer=1),
             dict(q="Which entity name shows the euro sign?", options=["&eur;", "&euros;", "&euro;", "&e;"], answer=2),
             dict(q="Which format is a hexadecimal character reference?", options=["&#x20AC;", "&#20AC;", "&x20AC;", "&hex20AC;"], answer=0),
         ]),
    dict(slug="emojis", title="HTML Emojis", group="Text & Style",
         intro="Emojis are characters, just like letters. With UTF-8 you can use them anywhere in an HTML page.",
         sections=[
             dict(h="Emojis are characters", p="Each emoji has a number in the Unicode standard. The browser draws it with an emoji font, so the look differs between devices.",
                  code='<p style="font-size: 48px;">&#128512; &#128077; &#128640;</p>'),
             dict(h="Set the charset", p="Make sure the page declares `<meta charset=\"UTF-8\">`. Without it, emojis may appear as strange symbols."),
             dict(h="Decimal and hexadecimal", p="You can write an emoji as a decimal reference such as `&#128512;` or a hexadecimal reference such as `&#x1F600;`. Both give the same grinning face. You can also paste the emoji directly into a UTF-8 file."),
         ],
         example='''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
  <p style="font-size: 48px;">&#128512; &#128077; &#128640; &#10084;</p>
  <p>Hex form: &#x1F60D; &#x1F389;</p>
</body>
</html>''',
         tip="Emojis are sized with `font-size`, the same as normal text.",
         exercise=[
             dict(q="Which meta tag helps emojis display correctly?", options=['<meta name="emoji">', '<meta charset="UTF-8">', '<meta lang="emoji">', '<meta type="unicode">'], answer=1),
             dict(q="How is the hexadecimal reference for the grinning face written?", options=["&#x1F600;", "&#1F600;", "&emoji;", "&x1F600"], answer=0),
             dict(q="How do you make an emoji larger on the page?", options=["Add a size attribute", "Use the font-size CSS property", "Use the <big> element", "Use width and height"], answer=1),
         ]),

    # ============================================================ Links & Media
    dict(slug="link-targets", title="HTML Link Targets and Colours", group="Links & Media",
         intro="Links can open in different places and can be styled for every state: unvisited, visited, hovered and pressed.",
         sections=[
             dict(h="The target attribute", p="`_self` opens in the same tab (the default). `_blank` opens in a new tab. `_parent` and `_top` are used with frames.",
                  code='<a href="https://example.com" target="_blank" rel="noopener">New tab</a>'),
             dict(h="Download and title", p="`download` tells the browser to save the file instead of opening it. `title` shows a tooltip.",
                  code='<a href="report.pdf" download title="Get the report">Download the report</a>'),
             dict(h="Styling link states", p="Use the pseudo-classes `a:link`, `a:visited`, `a:hover` and `a:active`, in that order, to style each state.",
                  code='a:link    { color: royalblue; }\na:visited { color: purple; }\na:hover   { color: tomato; }\na:active  { color: red; }'),
             dict(h="Links that look like buttons", p="Style the link with padding, a background colour and `text-decoration: none` to turn it into a button."),
         ],
         example='''<style>
  a.btn { display: inline-block; padding: 10px 18px; background: royalblue; color: white; text-decoration: none; border-radius: 6px; }
  a.btn:hover { background: navy; }
  a.plain:hover { color: tomato; }
</style>
<p><a class="plain" href="#a" title="A plain link">Hover over this link</a></p>
<p><a class="btn" href="#b">A link styled as a button</a></p>''',
         tip="When you use `target=\"_blank\"`, add `rel=\"noopener\"` so the new page cannot control the old one.",
         exercise=[
             dict(q="Which target value opens a link in the same tab or window?", options=["_blank", "_new", "_self", "_tab"], answer=2),
             dict(q="Which attribute tells the browser to save a linked file instead of opening it?", options=["save", "download", "target", "get"], answer=1),
             dict(q="Which pseudo-class styles a link while the mouse pointer is over it?", options=["a:visited", "a:active", "a:link", "a:hover"], answer=3),
         ]),
    dict(slug="file-paths", title="HTML File Paths", group="Links & Media",
         intro="A file path tells the browser where to find a file such as an image, a stylesheet or another page.",
         sections=[
             dict(h="Absolute and relative paths", p="An absolute path is a full web address such as `https://example.com/img/logo.png`. A relative path starts from the current page, such as `img/logo.png`.",
                  code='<img src="https://example.com/img/logo.png" alt="Logo">\n<img src="img/logo.png" alt="Logo">'),
             dict(h="Moving between folders", p="`folder/file.png` goes into a folder. `../file.png` goes up one folder. `/file.png` starts from the root folder of the website.",
                  code='<img src="../img/logo.png" alt="Logo">\n<img src="/img/logo.png" alt="Logo">'),
             dict(h="Good habits", p="Use lowercase file names, no spaces, and keep images in an `img` folder. Relative paths keep working when you move the whole site to a new server."),
         ],
         example='''<p>This image path does not exist, so the browser shows the alt text instead:</p>
<img src="img/missing.png" alt="[Missing picture: the file path is wrong]">
<p>Fixing the path is the first thing to check when a picture does not appear.</p>''',
         tip="If an image does not load, check the spelling, the folder and the capital letters of the path. Many servers treat `Logo.png` and `logo.png` as different files.",
         exercise=[
             dict(q="What does ../ mean at the start of a file path?", options=["Go to the website root", "Go up one folder", "Go into a folder named dots", "Open a new tab"], answer=1),
             dict(q="Which src value is a relative path?", options=["https://example.com/a.png", "//cdn.example.com/a.png", "file:///C:/a.png", "images/a.png"], answer=3),
             dict(q="What does a path that starts with a single / refer to?", options=["The current folder", "The root folder of the website", "The parent folder", "A web address on another site"], answer=1),
         ]),
    dict(slug="image-maps", title="HTML Image Maps", group="Links & Media",
         intro="An image map makes parts of a single image clickable, each leading to a different place.",
         sections=[
             dict(h="How it works", p="Add `usemap=\"#name\"` to the <img>. Then create a `<map name=\"name\">` with one `<area>` for each clickable region.",
                  code='<img src="shapes.png" alt="Shapes" usemap="#shapes">\n<map name="shapes">\n  <area shape="rect" coords="0,0,100,100" href="square.html" alt="Square">\n  <area shape="circle" coords="150,50,40" href="circle.html" alt="Circle">\n</map>'),
             dict(h="Shapes and coordinates", p="`rect` uses `x1,y1,x2,y2`. `circle` uses `x,y,radius`. `poly` uses a list of `x,y` points. Coordinates count in pixels from the top-left corner of the image."),
             dict(h="Always add alt", p="Each <area> needs an `alt` attribute so people using screen readers know where the link goes."),
         ],
         example='''<img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='100'><rect width='100' height='100' fill='royalblue'/><circle cx='200' cy='50' r='40' fill='tomato'/></svg>" alt="A blue square and a red circle" width="300" height="100" usemap="#shapes">
<map name="shapes">
  <area shape="rect" coords="0,0,100,100" href="#square" alt="Blue square">
  <area shape="circle" coords="200,50,40" href="#circle" alt="Red circle">
</map>
<p>Click the square or the circle. Each one is its own link.</p>''',
         tip="Image maps use fixed pixel coordinates, so they do not resize well on small screens. Use them for simple, fixed images.",
         exercise=[
             dict(q="Which attribute on an <img> connects it to an image map?", options=["map", "ismap", "usemap", "src"], answer=2),
             dict(q="Which element defines one clickable region inside a <map>?", options=["<region>", "<area>", "<zone>", "<spot>"], answer=1),
             dict(q="Which shape value describes a rectangle in an <area> element?", options=["square", "box", "rectangle", "rect"], answer=3),
         ]),
    dict(slug="picture", title="HTML Responsive Images", group="Links & Media",
         intro="Responsive images let the browser pick the best file for the screen size, so phones do not download huge pictures.",
         sections=[
             dict(h="The picture element", p="`<picture>` holds several `<source>` elements and one `<img>`. The browser uses the first source whose condition matches, and falls back to the <img>.",
                  code='<picture>\n  <source media="(min-width: 800px)" srcset="large.jpg">\n  <source media="(min-width: 400px)" srcset="medium.jpg">\n  <img src="small.jpg" alt="Mountain view">\n</picture>'),
             dict(h="srcset and sizes", p="On a plain <img>, `srcset` lists files with their widths, and `sizes` tells the browser how wide the image will be shown. The browser chooses a file for you.",
                  code='<img src="small.jpg"\n     srcset="small.jpg 480w, large.jpg 1000w"\n     sizes="(min-width: 800px) 800px, 100vw"\n     alt="Mountain view">'),
             dict(h="Modern formats", p="Use the `type` attribute to offer newer formats such as WebP or AVIF first, with JPEG as the fallback."),
         ],
         example='''<picture>
  <source media="(min-width: 500px)" srcset="data:image/svg+xml;utf8,<svg%20xmlns='http://www.w3.org/2000/svg'%20width='300'%20height='80'><rect%20width='300'%20height='80'%20fill='royalblue'/><text%20x='150'%20y='48'%20fill='white'%20font-size='20'%20text-anchor='middle'>Wide%20screen</text></svg>">
  <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='80'><rect width='200' height='80' fill='tomato'/><text x='100' y='48' fill='white' font-size='20' text-anchor='middle'>Small screen</text></svg>" alt="A banner that changes with the screen width">
</picture>
<p>Resize the result panel: the banner changes colour at 500 pixels.</p>''',
         tip="Always include a final <img> with an `alt`. It is the fallback and also where the picture is actually displayed.",
         exercise=[
             dict(q="Which element offers different image files for different screen conditions?", options=["<picture>", "<figure>", "<gallery>", "<imgset>"], answer=0),
             dict(q="Which element inside <picture> is always required as the fallback?", options=["<source>", "<img>", "<map>", "<track>"], answer=1),
             dict(q="What does the media attribute of a <source> element hold?", options=["A file name", "A media query", "An alt text", "A caption"], answer=1),
         ]),
    dict(slug="favicon", title="HTML Favicon and Page Title", group="Links & Media",
         intro="The tab of your page shows a small icon (the favicon) and a title. Both help visitors recognise your site.",
         sections=[
             dict(h="Add a favicon", p="Link an icon file from the <head>. PNG, ICO and SVG files all work.",
                  code='<head>\n  <title>My Site</title>\n  <link rel="icon" type="image/png" href="favicon.png">\n</head>'),
             dict(h="Choose a good title", p="The `<title>` appears on the browser tab, in bookmarks and in search results. Keep it clear and short, around 60 characters, and put the most important words first."),
             dict(h="Where it appears", p="Browsers show the favicon next to the title in tabs, history, bookmarks and the address bar suggestions."),
         ],
         example='''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TechHub - Learn to code</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><rect width='16' height='16' rx='3' fill='royalblue'/></svg>">
</head>
<body>
  <h1>Check the browser tab</h1>
  <p>On your own page, the title and icon appear on the tab.</p>
</body>
</html>''',
         tip="A sandboxed preview cannot show a tab. Save the code as a file and open it to see the title and favicon.",
         exercise=[
             dict(q="Which element adds a favicon to a page?", options=['<icon src="icon.png">', '<link rel="icon" href="icon.png">', '<meta icon="icon.png">', '<favicon href="icon.png">'], answer=1),
             dict(q="Where do you place the favicon link and the title?", options=["In the <body>", "In the <footer>", "In the <head>", "After </html>"], answer=2),
             dict(q="Which file types can be used for a favicon?", options=["Only .doc files", "Only .gif files", "PNG, ICO and SVG files", "Only .pdf files"], answer=2),
         ]),
    dict(slug="video", title="HTML Video", group="Links & Media",
         intro="The <video> element plays video directly in the page, with no extra plugin.",
         sections=[
             dict(h="Adding a video", p="Use `controls` to show play, pause and volume buttons. Put one or more `<source>` elements inside, and fallback text for very old browsers.",
                  code='<video controls width="400">\n  <source src="movie.mp4" type="video/mp4">\n  <source src="movie.webm" type="video/webm">\n  Your browser does not support the video tag.\n</video>'),
             dict(h="Useful attributes", p="`autoplay` starts playback, but browsers usually only allow it when the video is also `muted`. `loop` repeats it. `poster` shows an image before playing. `preload` hints how much to load in advance.",
                  code='<video controls muted loop poster="cover.jpg" width="400">\n  <source src="movie.mp4" type="video/mp4">\n</video>'),
             dict(h="Formats", p="MP4 (H.264), WebM and Ogg are the common formats. MP4 and WebM together cover practically all browsers."),
         ],
         example='''<video controls width="320" poster="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='320' height='180'><rect width='320' height='180' fill='navy'/><text x='160' y='98' fill='white' font-size='20' text-anchor='middle'>Video poster</text></svg>">
  <source src="movie.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p>No video file is attached in this example, but the player and the poster image show how the element looks.</p>''',
         tip="Do not autoplay videos with sound. It annoys visitors, and browsers block it anyway.",
         exercise=[
             dict(q="Which attribute adds play and pause buttons to a video?", options=["buttons", "controls", "player", "play"], answer=1),
             dict(q="Which attribute is usually needed together with autoplay so the browser allows it?", options=["loop", "poster", "muted", "preload"], answer=2),
             dict(q="Which attribute shows an image before the video starts playing?", options=["poster", "thumb", "cover", "preview"], answer=0),
         ]),
    dict(slug="audio", title="HTML Audio", group="Links & Media",
         intro="The <audio> element plays sound, such as music, podcasts or effects, directly in the page.",
         sections=[
             dict(h="Adding audio", p="It works like <video>. Add `controls` and list the files with <source>.",
                  code='<audio controls>\n  <source src="song.mp3" type="audio/mpeg">\n  <source src="song.ogg" type="audio/ogg">\n  Your browser does not support the audio element.\n</audio>'),
             dict(h="Attributes", p="`controls` shows the player. `loop` repeats. `muted` starts silent. `autoplay` tries to start at once, but browsers often block it. `preload` controls how much loads in advance."),
             dict(h="Formats", p="MP3 (`audio/mpeg`), Ogg (`audio/ogg`) and WAV (`audio/wav`) are supported by modern browsers. MP3 is the safest single choice."),
         ],
         example='''<p>An audio player with controls:</p>
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
<p>Add your own .mp3 file name in src to hear it.</p>''',
         tip="Give visitors a way to pause or mute audio. The `controls` attribute does that for you.",
         exercise=[
             dict(q="Which element plays sound files in a web page?", options=["<sound>", "<music>", "<audio>", "<mp3>"], answer=2),
             dict(q="Which attribute makes audio play again from the start when it ends?", options=["repeat", "loop", "again", "restart"], answer=1),
             dict(q="Which audio format is the safest single choice for most browsers?", options=["MP3", "AAC-LC raw", "MIDI", "FLAC only"], answer=0),
         ]),
    dict(slug="iframes", title="HTML Iframes", group="Links & Media",
         intro="An <iframe> shows another HTML page inside your page, like a window onto another document.",
         sections=[
             dict(h="Basic iframe", p="`src` is the page to show. Give it `width`, `height` and a `title` that describes the content.",
                  code='<iframe src="page.html" width="400" height="200" title="Example page"></iframe>'),
             dict(h="Inline content and safety", p="`srcdoc` lets you write the HTML directly in the attribute. `sandbox` limits what the embedded page can do. `loading=\"lazy\"` delays loading until the iframe is near the screen.",
                  code='<iframe srcdoc="<p>Hello from inside</p>" sandbox loading="lazy" title="Inline demo"></iframe>'),
             dict(h="Links that open in an iframe", p="Give the iframe a `name`, then use that name as the `target` of a link.",
                  code='<iframe name="demo" title="Demo"></iframe>\n<a href="page.html" target="demo">Show page</a>'),
         ],
         example='''<iframe srcdoc="<h3 style='font-family:sans-serif;color:royalblue'>I am inside an iframe</h3><p style='font-family:sans-serif'>This is a separate document.</p>" width="100%" height="120" title="An iframe with its own content" style="border: 2px solid royalblue;"></iframe>
<p>The box above is a separate HTML document embedded in this page.</p>''',
         tip="Always add a `title` to an iframe. Screen readers announce it so people know what the frame contains.",
         exercise=[
             dict(q="Which attribute gives an iframe an accessible description?", options=["alt", "title", "name", "label"], answer=1),
             dict(q="Which iframe attribute lets you write HTML inline instead of loading a URL?", options=["srcdoc", "html", "inline", "content"], answer=0),
             dict(q="Which iframe attribute restricts what the embedded page can do?", options=["limit", "secure", "block", "sandbox"], answer=3),
         ]),
    dict(slug="embedding", title="HTML YouTube and Embedding", group="Links & Media",
         intro="You can place videos, maps and other services in your page by embedding them with an <iframe>.",
         sections=[
             dict(h="Embed a YouTube video", p="On a video page choose Share, then Embed, and copy the code. It is an iframe whose `src` points to an embed address.",
                  code='<iframe width="560" height="315"\n  src="https://www.youtube.com/embed/VIDEO_ID"\n  title="Video title"\n  allowfullscreen></iframe>'),
             dict(h="Replace VIDEO_ID", p="The part of the address after `v=` in a normal video link is the video ID. Use it in place of `VIDEO_ID` in the embed address."),
             dict(h="Other embeds", p="Maps, slide decks and many other services give you the same kind of iframe code. Use their embed code and keep the `title` descriptive. Use `loading=\"lazy\"` so embeds below the fold load later."),
         ],
         example='''<iframe srcdoc="<body style='margin:0;font-family:sans-serif;background:navy;color:white;display:flex;align-items:center;justify-content:center;height:100vh'><div>Embedded video would play here</div></body>" width="100%" height="160" title="Placeholder for an embedded video" allowfullscreen style="border:0;"></iframe>
<p>On a real page the iframe src would be the embed address of the video.</p>''',
         tip="This tutorial does not load a real video, to keep the example self-contained. The code in the lesson is what you would paste into your own page.",
         exercise=[
             dict(q="Which element is normally used to embed a YouTube video in a page?", options=["<video>", "<embed-yt>", "<iframe>", "<object-video>"], answer=2),
             dict(q="Which iframe attribute allows an embedded video to go full screen?", options=["bigscreen", "allowfullscreen", "fullview", "maximize"], answer=1),
             dict(q="What should the title attribute of an embed iframe contain?", options=["A short description of the content", "The video address", "The page width", "Nothing, it is ignored"], answer=0),
         ]),

    # ============================================================ Lists & Tables
    dict(slug="nested-lists", title="HTML Nested and Styled Lists", group="Lists & Tables",
         intro="Lists can sit inside other lists, and CSS lets you change the bullets or numbers.",
         sections=[
             dict(h="Nesting", p="Put the inner `<ul>` or `<ol>` inside an `<li>` of the outer list.",
                  code='<ul>\n  <li>Fruit\n    <ul>\n      <li>Apple</li>\n      <li>Mango</li>\n    </ul>\n  </li>\n  <li>Vegetables</li>\n</ul>'),
             dict(h="Ordered list attributes", p="`type` changes the numbering style (`1`, `A`, `a`, `I`, `i`). `start` sets the first number. `reversed` counts down.",
                  code='<ol type="A" start="3">\n  <li>Third letter</li>\n  <li>Fourth letter</li>\n</ol>'),
             dict(h="Style with CSS", p="`list-style-type` changes the marker, for example `circle`, `square`, `decimal`, `lower-alpha`, `upper-roman` or `none`. Setting `display: inline` on items makes a horizontal menu.",
                  code='ul { list-style-type: square; }\nul.menu { list-style-type: none; padding: 0; }\nul.menu li { display: inline; margin-right: 12px; }'),
         ],
         example='''<style>
  ul.sq { list-style-type: square; }
  ul.menu { list-style-type: none; padding: 0; }
  ul.menu li { display: inline; margin-right: 14px; }
</style>
<ul class="sq">
  <li>Fruit
    <ul>
      <li>Apple</li>
      <li>Mango</li>
    </ul>
  </li>
  <li>Vegetables</li>
</ul>
<ol type="A" start="3"><li>Third</li><li>Fourth</li></ol>
<ul class="menu"><li>Home</li><li>About</li><li>Contact</li></ul>''',
         tip="Navigation menus are really lists of links, so mark them up as a list and style them with CSS.",
         exercise=[
             dict(q="Where does a nested list go inside its parent list?", options=["After the closing </ul>", "Inside an <li> of the parent", "Inside the <head>", "Inside a <p>"], answer=1),
             dict(q="Which ordered-list attribute makes the numbers begin at 5?", options=["begin", "first", "from", "start"], answer=3),
             dict(q="Which CSS property changes the bullet style of a list?", options=["bullet-style", "list-style-type", "marker-type", "list-bullet"], answer=1),
         ]),
    dict(slug="table-spans", title="HTML Table Headers and Spans", group="Lists & Tables",
         intro="Real tables often need cells that stretch across several columns or rows, and headings that work well with screen readers.",
         sections=[
             dict(h="Column and row spans", p="`colspan` makes a cell cover several columns. `rowspan` makes it cover several rows.",
                  code='<tr><th colspan="2">Name</th></tr>\n<tr><td rowspan="2">Team A</td><td>Asha</td></tr>\n<tr><td>Ravi</td></tr>'),
             dict(h="Header scope", p="Add `scope=\"col\"` to a heading cell that labels a column and `scope=\"row\"` to one that labels a row. Screen readers use this to read cells in context."),
             dict(h="Table sections", p="`<thead>`, `<tbody>` and `<tfoot>` group the header, body and footer rows. They make large tables easier to style and to read."),
         ],
         example='''<table border="1" cellpadding="6" style="border-collapse: collapse;">
  <thead>
    <tr><th scope="col">Team</th><th scope="col" colspan="2">Members</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row" rowspan="2">Team A</th><td>Asha</td><td>Ravi</td></tr>
    <tr><td>Meena</td><td>Kiran</td></tr>
  </tbody>
  <tfoot>
    <tr><td colspan="3">4 members in total</td></tr>
  </tfoot>
</table>''',
         tip="Count carefully. A cell with `colspan=\"2\"` replaces two normal cells in that row.",
         exercise=[
             dict(q="Which attribute makes a table cell stretch across two columns?", options=["colspan=\"2\"", "rowspan=\"2\"", "span=\"2\"", "merge=\"2\""], answer=0),
             dict(q="Which attribute makes a table cell stretch across several rows?", options=["colspan", "height", "rowspan", "rows"], answer=2),
             dict(q="Which attribute tells a screen reader whether a heading cell labels a column or a row?", options=["scope", "role", "label", "axis"], answer=0),
         ]),
    dict(slug="table-styling", title="HTML Table Styling", group="Lists & Tables",
         intro="CSS turns a plain table into a clear, readable one with borders, spacing, stripes and hover effects.",
         sections=[
             dict(h="Borders and spacing", p="Add `border` to cells and `padding` for space inside them. By default each cell has its own border, which makes double lines. `border-collapse: collapse` merges them.",
                  code='table { border-collapse: collapse; width: 100%; }\nth, td { border: 1px solid #ccc; padding: 8px; text-align: left; }'),
             dict(h="Stripes and hover", p="`tr:nth-child(even)` styles every second row. `tr:hover` highlights the row under the mouse.",
                  code='tr:nth-child(even) { background: #f2f6ff; }\ntr:hover { background: #dce8ff; }'),
             dict(h="Caption and width", p="`<caption>` gives the table a title. Set `width` on the table, and add an `overflow-x: auto` wrapper so wide tables scroll on small screens."),
         ],
         example='''<style>
  table { border-collapse: collapse; width: 100%; }
  caption { font-weight: bold; padding: 6px; }
  th { background: royalblue; color: white; }
  th, td { border: 1px solid #c9d6f2; padding: 8px; text-align: left; }
  tr:nth-child(even) td { background: #f2f6ff; }
  tr:hover td { background: #dce8ff; }
</style>
<table>
  <caption>Course list</caption>
  <tr><th>Course</th><th>Lessons</th></tr>
  <tr><td>HTML</td><td>54</td></tr>
  <tr><td>CSS</td><td>40</td></tr>
  <tr><td>JavaScript</td><td>35</td></tr>
</table>''',
         tip="Hover over the rows in the result to see the hover colour.",
         exercise=[
             dict(q="Which CSS property merges the double borders of table cells into one?", options=["border-merge", "border-collapse", "border-join", "table-border"], answer=1),
             dict(q="Which selector styles every second table row?", options=["tr:nth-child(even)", "tr:second", "tr.even-only", "tr:every(2)"], answer=0),
             dict(q="Which CSS property adds space inside table cells?", options=["margin", "spacing", "gap", "padding"], answer=3),
         ]),

    # ============================================================ Forms
    dict(slug="form-attributes", title="HTML Form Attributes", group="Forms",
         intro="The attributes on the <form> element decide where the data goes and how it is sent.",
         sections=[
             dict(h="action and method", p="`action` is the address that receives the data. `method` is either `get` or `post`. GET adds the data to the web address, so it is visible and suitable for searches. POST sends it in the body of the request, which is better for private or large data.",
                  code='<form action="/search" method="get">\n  <input type="search" name="q">\n  <button>Search</button>\n</form>'),
             dict(h="Other attributes", p="`target` says where to show the response. `autocomplete` turns browser suggestions on or off. `novalidate` switches off the built-in checks. `enctype=\"multipart/form-data\"` is required when the form uploads a file.",
                  code='<form action="/upload" method="post" enctype="multipart/form-data">\n  <input type="file" name="photo">\n</form>'),
             dict(h="The name attribute", p="Each control needs a `name`. The name is the key under which its value is sent. Controls without a name are not submitted."),
         ],
         example='''<form action="#" method="get" autocomplete="on">
  <p><label for="q">Search</label><br>
  <input type="search" id="q" name="q" placeholder="Type a word"></p>
  <button type="button">Search</button>
</form>
<p>Method <code>get</code> would place <code>?q=word</code> after the address.</p>''',
         tip="Never use GET for passwords. Anything sent with GET can appear in the address bar and browser history.",
         exercise=[
             dict(q="Which form method appends the submitted data to the web address?", options=["POST", "GET", "PUT", "SEND"], answer=1),
             dict(q="Which enctype is required for a form that uploads a file?", options=["text/plain", "application/json", "multipart/form-data", "image/jpeg"], answer=2),
             dict(q="Which form attribute turns off the browser's built-in validation?", options=["novalidate", "nocheck", "skipvalidation", "autocomplete"], answer=0),
         ]),
    dict(slug="form-elements", title="HTML Form Elements", group="Forms",
         intro="A form is built from several controls. Here are the main ones and when to use each.",
         sections=[
             dict(h="Text controls", p="`<input>` is a one-line field. `<textarea>` is for several lines. `<label>` describes a control and makes it easier to click.",
                  code='<label for="msg">Message</label>\n<textarea id="msg" name="msg" rows="4" cols="30"></textarea>'),
             dict(h="Choice controls", p="`<select>` with `<option>` makes a drop-down. `<optgroup>` groups options. `<datalist>` adds suggestions to an input.",
                  code='<select name="city">\n  <optgroup label="India">\n    <option>Chennai</option>\n    <option>Delhi</option>\n  </optgroup>\n</select>\n<input list="browsers" name="b">\n<datalist id="browsers">\n  <option value="Chrome">\n  <option value="Firefox">\n</datalist>'),
             dict(h="Grouping and buttons", p="`<fieldset>` groups related controls and `<legend>` gives the group a caption. `<button>` creates a clickable button, and `<output>` shows a calculated result."),
         ],
         example='''<form>
  <fieldset>
    <legend>Contact details</legend>
    <p><label for="nm">Name</label><br><input id="nm" name="nm"></p>
    <p><label for="ct">City</label><br>
    <select id="ct" name="ct">
      <optgroup label="India"><option>Chennai</option><option>Delhi</option></optgroup>
    </select></p>
    <p><label for="br">Favourite browser</label><br>
    <input id="br" list="bl" name="br"><datalist id="bl"><option value="Chrome"><option value="Firefox"></datalist></p>
    <p><label for="ms">Message</label><br><textarea id="ms" rows="3" cols="30"></textarea></p>
  </fieldset>
  <button type="button">Send</button>
</form>''',
         tip="Click a label in the result. The matching field gets focus, because the label's `for` matches the field's `id`.",
         exercise=[
             dict(q="Which element groups related form controls and shows a caption with <legend>?", options=["<group>", "<fieldset>", "<section>", "<form-box>"], answer=1),
             dict(q="Which element gives an input a list of suggested values?", options=["<options>", "<suggest>", "<select>", "<datalist>"], answer=3),
             dict(q="Which element holds multi-line text input?", options=["<input type=\"multiline\">", "<textfield>", "<textarea>", "<text>"], answer=2),
         ]),
    dict(slug="input-types", title="HTML Input Types", group="Forms",
         intro="The `type` attribute of <input> decides what kind of control appears and what the browser checks.",
         sections=[
             dict(h="Text-like types", p="`text`, `password` (hides characters), `email`, `url`, `tel`, `number` and `search`. On phones, the keyboard changes to suit the type.",
                  code='<input type="email" name="mail">\n<input type="password" name="pw">\n<input type="number" min="1" max="10">'),
             dict(h="Choices", p="`checkbox` allows many selections. `radio` allows one choice from a group that shares the same `name`.",
                  code='<input type="radio" name="size" value="s"> Small\n<input type="radio" name="size" value="l"> Large'),
             dict(h="Dates and special pickers", p="`date`, `time`, `datetime-local`, `month` and `week` open a date or time picker. `color` shows a colour picker. `range` shows a slider. `file` lets the user choose a file.",
                  code='<input type="date" name="d">\n<input type="color" value="#1d5bd8">\n<input type="range" min="0" max="100">'),
             dict(h="Buttons and hidden data", p="`submit`, `reset` and `button` create buttons. `hidden` stores a value that is sent but not shown."),
         ],
         example='''<form>
  <p><label>Email <input type="email" placeholder="you@example.com"></label></p>
  <p><label>Password <input type="password"></label></p>
  <p><label>Age <input type="number" min="1" max="120" value="18"></label></p>
  <p><label>Date <input type="date"></label></p>
  <p><label>Colour <input type="color" value="#1d5bd8"></label></p>
  <p><label>Volume <input type="range" min="0" max="100" value="40"></label></p>
  <p>Size: <label><input type="radio" name="size"> Small</label> <label><input type="radio" name="size"> Large</label></p>
  <p><label><input type="checkbox"> Subscribe</label></p>
</form>''',
         tip="Choose the most specific type. `type=\"email\"` gives you free validation and a better mobile keyboard.",
         exercise=[
             dict(q="Which input type shows a slider?", options=["slider", "range", "scale", "number"], answer=1),
             dict(q="Which input type lets the user pick only one option out of a group sharing a name?", options=["checkbox", "select", "radio", "toggle"], answer=2),
             dict(q="Which input type hides the characters while the user types?", options=["secret", "hidden", "mask", "password"], answer=3),
             ]),
    dict(slug="input-attributes", title="HTML Input Attributes", group="Forms",
         intro="Attributes add rules, hints and behaviour to input fields.",
         sections=[
             dict(h="Hints and defaults", p="`value` sets the starting value. `placeholder` shows hint text that disappears when you type. `autofocus` puts the cursor in the field on page load.",
                  code='<input type="text" name="user" value="Asha">\n<input type="text" placeholder="Your name">'),
             dict(h="Rules", p="`required` blocks submitting an empty field. `maxlength` limits the characters. `min`, `max` and `step` limit numbers and dates. `pattern` takes a regular expression the value must match.",
                  code='<input type="text" name="pin" pattern="[0-9]{4}" maxlength="4" required title="Four digits">'),
             dict(h="Read only and disabled", p="`readonly` stops editing, but the value is still submitted. `disabled` greys the field out and it is not submitted. `multiple` lets a file or email field accept several values. `checked` pre-selects a checkbox or radio."),
         ],
         example='''<form>
  <p><label>Name <input type="text" placeholder="Your name" required></label></p>
  <p><label>PIN <input type="text" pattern="[0-9]{4}" maxlength="4" title="Four digits" placeholder="4 digits"></label></p>
  <p><label>Quantity <input type="number" min="1" max="5" step="1" value="1"></label></p>
  <p><label>Locked <input type="text" value="Read only" readonly></label></p>
  <p><label>Off <input type="text" value="Disabled" disabled></label></p>
  <p><label><input type="checkbox" checked> Pre-ticked</label></p>
  <button>Submit</button>
</form>''',
         tip="Press Submit with the Name field empty. The browser stops you because of the `required` attribute.",
         exercise=[
             dict(q="Which attribute shows hint text that vanishes as soon as the user types?", options=["hint", "value", "placeholder", "title"], answer=2),
             dict(q="Which attribute stops the form from being submitted while a field is empty?", options=["required", "mandatory", "notempty", "check"], answer=0),
             dict(q="Which attribute makes a field uneditable but still submits its value?", options=["disabled", "locked", "readonly", "frozen"], answer=2),
             ]),

    # ============================================================ Layout & Semantics
    dict(slug="block-inline", title="HTML Block and Inline Elements", group="Layout & Semantics",
         intro="Every element is either block-level or inline by default. This decides how it fits into the page.",
         sections=[
             dict(h="Block elements", p="A block element starts on a new line and stretches across the full width available. Examples are `<div>`, `<p>`, `<h1>`, `<ul>`, `<table>`, `<form>` and `<section>`."),
             dict(h="Inline elements", p="An inline element stays inside the line of text and takes only as much width as its content. Examples are `<span>`, `<a>`, `<strong>`, `<em>`, `<img>` and `<code>`.",
                  code='<p>This is a <strong>bold</strong> word and a <a href="#">link</a> inside a paragraph.</p>'),
             dict(h="Changing the behaviour", p="CSS can change it. `display: block` makes an element block-level, `display: inline` makes it inline, and `display: inline-block` allows width and height while staying in the line."),
         ],
         example='''<style>
  .b { border: 2px solid royalblue; margin: 4px 0; }
  .i { border: 2px solid tomato; }
</style>
<div class="b">A div is a block. It takes the whole line.</div>
<p class="b">A paragraph is also a block.</p>
<p>These <span class="i">spans</span> and <em class="i">emphasis</em> are inline: <a class="i" href="#x">they stay</a> in the line.</p>''',
         tip="Width and height do not work on a plain inline element. Use `inline-block` or `block` when you need to size it.",
         exercise=[
             dict(q="Which of these elements is block-level by default?", options=["<span>", "<a>", "<div>", "<strong>"], answer=2),
             dict(q="Which of these elements is inline by default?", options=["<h2>", "<em>", "<ul>", "<section>"], answer=1),
             dict(q="Which CSS property changes whether an element behaves as block or inline?", options=["position", "display", "float-type", "flow"], answer=1),
         ]),
    dict(slug="div-span", title="HTML div and span", group="Layout & Semantics",
         intro="<div> and <span> are generic containers. They have no meaning of their own, so they are used to group content for styling or scripting.",
         sections=[
             dict(h="The div element", p="`<div>` is a block-level container. Use it to group several elements so one style or one layout rule applies to all of them.",
                  code='<div style="background: aliceblue; padding: 12px;">\n  <h3>Card title</h3>\n  <p>Card text.</p>\n</div>'),
             dict(h="The span element", p="`<span>` is an inline container. Use it to style a small piece of text inside a line.",
                  code='<p>My favourite colour is <span style="color: royalblue;">blue</span>.</p>'),
             dict(h="Prefer meaning first", p="If a semantic element such as `<nav>`, `<article>` or `<button>` fits, use it instead of a <div> or <span>."),
         ],
         example='''<div style="background: aliceblue; border: 1px solid #b9d0f5; padding: 12px; border-radius: 8px;">
  <h3 style="margin-top: 0;">Card title</h3>
  <p>Everything in this box is grouped by one div.</p>
  <p>Only <span style="color: tomato; font-weight: bold;">this part</span> is wrapped in a span.</p>
</div>''',
         tip="Too many nested divs make a page hard to read. Add them only when you need a group.",
         exercise=[
             dict(q="Which element suits colouring a single word inside a sentence?", options=["<div>", "<span>", "<section>", "<p>"], answer=1),
             dict(q="Which element groups several block elements so one style can cover them all?", options=["<div>", "<span>", "<em>", "<br>"], answer=0),
             dict(q="Do <div> and <span> carry any built-in meaning?", options=["Yes, they mark important text", "Yes, they mark headings", "No, they are generic containers", "Yes, they mark lists"], answer=2),
         ]),
    dict(slug="classes", title="HTML Classes", group="Layout & Semantics",
         intro="The `class` attribute names a group of elements so CSS and JavaScript can pick them all at once.",
         sections=[
             dict(h="Using a class", p="Give elements the same class name, then style it with a dot in CSS.",
                  code='<style>\n  .note { background: lightyellow; padding: 8px; }\n</style>\n<p class="note">First note</p>\n<p class="note">Second note</p>'),
             dict(h="More than one class", p="An element can have several classes separated by spaces, and each class can be used by many elements.",
                  code='<p class="note big">A big note</p>'),
             dict(h="Tag plus class and JavaScript", p="`p.note` styles only paragraphs with that class. In JavaScript, `document.getElementsByClassName(\"note\")` or `querySelectorAll(\".note\")` finds them."),
         ],
         example='''<style>
  .note { background: lightyellow; border-left: 4px solid orange; padding: 8px; margin: 6px 0; }
  .big { font-size: 22px; }
  p.warn { color: crimson; }
</style>
<p class="note">A normal note.</p>
<p class="note big">A big note: it has two classes.</p>
<p class="warn">Only paragraphs with the class warn are red.</p>''',
         tip="Choose class names by purpose, such as `warning`, not by looks, such as `red-text`.",
         exercise=[
             dict(q="How do you select all elements with the class \"note\" in CSS?", options=["#note", "*note", ".note", "note:class"], answer=2),
             dict(q="Can one element have more than one class?", options=["No, only one", "Yes, separated by spaces", "Yes, separated by commas", "Only inside a <div>"], answer=1),
             dict(q="Which CSS selector styles only paragraphs that have the class warn?", options=["warn.p", "p.warn", "p > warn", "p#warn"], answer=1),
         ]),
    dict(slug="id", title="HTML Id Attribute", group="Layout & Semantics",
         intro="The `id` attribute gives one element a unique name. It is used for styling, for links that jump to a spot, and for scripts.",
         sections=[
             dict(h="Unique names", p="An id must be unique in the page. In CSS it is selected with a hash sign.",
                  code='<style>\n  #intro { color: royalblue; }\n</style>\n<h1 id="intro">Welcome</h1>'),
             dict(h="Bookmarks", p="A link to `#intro` jumps to the element with `id=\"intro\"`. Together with a heading, this builds a table of contents.",
                  code='<a href="#chapter2">Go to chapter 2</a>\n...\n<h2 id="chapter2">Chapter 2</h2>'),
             dict(h="Class or id?", p="Use a class when many elements share a style. Use an id when exactly one element needs a name. In JavaScript, `document.getElementById(\"intro\")` finds one element by its id."),
         ],
         example='''<style>
  #title { color: royalblue; }
</style>
<p><a href="#end">Jump to the end</a></p>
<h2 id="title">This heading has the id title</h2>
<div style="height: 220px;"></div>
<h3 id="end">You jumped here using an id</h3>''',
         tip="Ids are case sensitive and should not contain spaces. Use names like `contact-form`.",
         exercise=[
             dict(q="Which CSS selector targets the element with id=\"top\"?", options=[".top", "#top", "top", "*top"], answer=1),
             dict(q="How many elements in one page may share the same id?", options=["Any number", "Up to ten", "Only one", "Two"], answer=2),
             dict(q="Which attribute does a link such as href=\"#contact\" jump to?", options=["class=\"contact\"", "name=\"contact\" only", "id=\"contact\"", "title=\"contact\""], answer=2),
         ]),
    dict(slug="layout", title="HTML Layout", group="Layout & Semantics",
         intro="Layout means arranging a page into areas such as a header, a menu, content and a footer. Semantic elements provide the structure and CSS provides the arrangement.",
         sections=[
             dict(h="Typical layout", p="Most pages have a `<header>`, a `<nav>`, a `<main>` area with content and maybe an `<aside>`, and a `<footer>`.",
                  code='<header>...</header>\n<nav>...</nav>\n<main>\n  <section>...</section>\n  <aside>...</aside>\n</main>\n<footer>...</footer>'),
             dict(h="Flexbox", p="`display: flex` puts children in a row and lets them share space. It is ideal for menus and for simple sidebars.",
                  code='.page { display: flex; gap: 16px; }\n.content { flex: 1; }\n.side { width: 200px; }'),
             dict(h="Grid", p="`display: grid` creates rows and columns together. Use `grid-template-columns` to describe the columns.",
                  code='.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }'),
         ],
         example='''<style>
  * { box-sizing: border-box; }
  header, footer { background: royalblue; color: white; padding: 10px; text-align: center; }
  .page { display: flex; gap: 10px; margin: 10px 0; }
  main { flex: 1; background: aliceblue; padding: 10px; }
  aside { width: 130px; background: #e3ecfb; padding: 10px; }
</style>
<header>Header</header>
<div class="page">
  <main>Main content takes the free space.</main>
  <aside>Sidebar</aside>
</div>
<footer>Footer</footer>''',
         tip="Old sites used tables or floats for layout. Today use flexbox for one direction and grid for two.",
         exercise=[
             dict(q="Which display value arranges child elements in a flexible row?", options=["flex", "row", "inline-row", "stack"], answer=0),
             dict(q="Which display value creates a layout of rows and columns together?", options=["table-layout", "grid", "columns", "matrix"], answer=1),
             dict(q="Which element is placed inside <main> for a group of side content?", options=["<footer>", "<head>", "<aside>", "<nav-side>"], answer=2),
         ]),
    dict(slug="responsive", title="HTML Responsive Web Design", group="Layout & Semantics",
         intro="A responsive page adapts to every screen, from small phones to large monitors.",
         sections=[
             dict(h="The viewport meta tag", p="Add this tag to the head so phones show the page at its real width instead of zooming out.",
                  code='<meta name="viewport" content="width=device-width, initial-scale=1">'),
             dict(h="Flexible images", p="`max-width: 100%` stops an image from being wider than its container, and `height: auto` keeps its proportions.",
                  code='img { max-width: 100%; height: auto; }'),
             dict(h="Media queries", p="A media query applies CSS only when a condition is true, such as a minimum or maximum screen width.",
                  code='.cards { display: grid; grid-template-columns: 1fr; }\n@media (min-width: 700px) {\n  .cards { grid-template-columns: 1fr 1fr; }\n}'),
         ],
         example='''<style>
  .box { padding: 12px; color: white; background: tomato; text-align: center; }
  .box::after { content: " (narrow: red)"; }
  @media (min-width: 500px) {
    .box { background: royalblue; }
    .box::after { content: " (wide: blue)"; }
  }
</style>
<div class="box">Resize the result panel</div>
<p>The box changes colour when the panel is at least 500 pixels wide.</p>''',
         tip="Design for the smallest screen first, then add media queries for larger screens (mobile first).",
         exercise=[
             dict(q="Which meta tag makes a page scale correctly on phones?", options=['<meta name="viewport" content="width=device-width, initial-scale=1">', '<meta name="phone" content="yes">', '<meta charset="mobile">', '<meta name="scale" content="auto">'], answer=0),
             dict(q="Which CSS rule keeps an image from becoming wider than its container?", options=["width: auto", "max-width: 100%", "overflow: image", "image-fit: stay"], answer=1),
             dict(q="Which CSS feature applies styles only at certain screen widths?", options=["Pseudo-elements", "Keyframes", "Media queries", "Variables"], answer=2),
         ]),

    # ============================================================ Advanced
    dict(slug="charset", title="HTML Character Sets", group="Advanced",
         intro="A character set tells the browser how to turn the bytes of a file into letters and symbols.",
         sections=[
             dict(h="Use UTF-8", p="UTF-8 can represent practically every character in every language, plus emojis. It is the standard for the web, so use it for every page.",
                  code='<meta charset="UTF-8">'),
             dict(h="Older sets", p="ASCII covers 128 English characters. ISO-8859-1 and Windows-1252 cover Western European letters. UTF-8 includes ASCII, so plain English text is the same in both."),
             dict(h="Where to place it", p="Put the `<meta charset>` tag first in the head, before anything with text in it, within the first 1024 bytes of the file. Also save the file itself as UTF-8."),
             dict(h="Garbled text", p="If you see strange sequences such as `Ã©` instead of é, the file was saved in one encoding but read in another."),
         ],
         example='''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Characters</title></head>
<body>
  <p>English, español: ñ é ü</p>
  <p>தமிழ் | हिन्दी | 日本語 | العربية</p>
  <p>Symbols: &copy; &euro; &#9731;</p>
</body>
</html>''',
         tip="Declare UTF-8 even for English pages. Names, quotes and symbols often contain non-ASCII characters.",
         exercise=[
             dict(q="Which character set is recommended for all new web pages?", options=["ASCII", "ISO-8859-1", "UTF-8", "Windows-1252"], answer=2),
             dict(q="Where should the meta charset tag appear?", options=["At the end of the body", "Early in the head", "After </html>", "Inside <title>"], answer=1),
             dict(q="What usually causes strange symbols such as Ã© to appear in a page?", options=["A missing alt attribute", "A wrong or missing character set", "Too much CSS", "An unclosed <p> tag"], answer=1),
         ]),
    dict(slug="url-encoding", title="HTML URL Encoding", group="Advanced",
         intro="A web address can only contain a limited set of safe characters. Other characters must be encoded so they travel safely.",
         sections=[
             dict(h="What a URL looks like", p="A URL (Uniform Resource Locator) has the form `scheme://host:port/path?query`. For example `https://example.com/search?q=html`."),
             dict(h="Percent encoding", p="An unsafe character is replaced by `%` followed by two hexadecimal digits. A space becomes `%20`, `é` becomes `%C3%A9` and `&` becomes `%26`. In query strings of forms, a space may also be written as `+`.",
                  code='https://example.com/search?q=hello%20world\nhttps://example.com/caf%C3%A9'),
             dict(h="Encoding in JavaScript", p="`encodeURIComponent(\"a & b\")` returns `a%20%26%20b`. Browsers also encode form data for you when a form is sent."),
         ],
         example='''<table border="1" cellpadding="6" style="border-collapse: collapse;">
  <tr><th>Character</th><th>Encoded</th></tr>
  <tr><td>space</td><td>%20</td></tr>
  <tr><td>&amp;</td><td>%26</td></tr>
  <tr><td>#</td><td>%23</td></tr>
  <tr><td>?</td><td>%3F</td></tr>
  <tr><td>&eacute;</td><td>%C3%A9</td></tr>
</table>''',
         tip="Use `encodeURIComponent()` when you build a query string by hand. Never paste raw user text into a URL.",
         exercise=[
             dict(q="What is a space encoded as in a URL?", options=["%20", "%00", "&sp;", "_"], answer=0),
             dict(q="What does the abbreviation URL stand for?", options=["Universal Resource Link", "Uniform Resource Locator", "Unified Reference Language", "User Request Line"], answer=1),
             dict(q="Which JavaScript function encodes a value for safe use in a URL query?", options=["escapeHtml()", "urlSafe()", "encodeURIComponent()", "toUrl()"], answer=2),
         ]),
    dict(slug="canvas", title="HTML Canvas", group="Advanced",
         intro="The <canvas> element creates a blank drawing area. You draw on it with JavaScript, which makes it good for charts, games and animation.",
         sections=[
             dict(h="Create a canvas", p="Give it a `width` and `height` in pixels and an `id`. Text between the tags is shown if the browser does not support canvas.",
                  code='<canvas id="myCanvas" width="300" height="120">\n  Your browser does not support the canvas element.\n</canvas>'),
             dict(h="Draw with JavaScript", p="Get the 2D drawing tools with `getContext(\"2d\")`, then draw shapes.",
                  code='<script>\n  const c = document.getElementById("myCanvas");\n  const ctx = c.getContext("2d");\n  ctx.fillStyle = "royalblue";\n  ctx.fillRect(20, 20, 120, 60);\n  ctx.beginPath();\n  ctx.arc(220, 50, 30, 0, 2 * Math.PI);\n  ctx.fill();\n</script>'),
             dict(h="Canvas or SVG?", p="Canvas draws pixels and is fast for many moving objects. SVG keeps shapes as elements and stays sharp at any size."),
         ],
         example='''<canvas id="myCanvas" width="300" height="120" style="border: 2px solid royalblue;">
  Your browser does not support the canvas element.
</canvas>
<p>The canvas above is empty because scripts are switched off in this editor. Copy the drawing code from the lesson into your own file to see the shapes.</p>''',
         tip="Set the size with the `width` and `height` attributes. Sizing a canvas with CSS only stretches the picture.",
         exercise=[
             dict(q="Which element creates a drawing area controlled by JavaScript?", options=["<draw>", "<canvas>", "<svg-area>", "<paint>"], answer=1),
             dict(q="Which method gives you the tools for 2D drawing on a canvas?", options=["getContext(\"2d\")", "getDrawing()", "startPaint()", "createBrush()"], answer=0),
             dict(q="What is shown between the <canvas> tags?", options=["The drawing", "Fallback text for unsupported browsers", "Nothing, it is ignored", "The page title"], answer=1),
         ]),
    dict(slug="svg", title="HTML SVG", group="Advanced",
         intro="SVG (Scalable Vector Graphics) draws shapes with markup. SVG images stay sharp at any size, and you can write them straight into HTML.",
         sections=[
             dict(h="Inline SVG", p="Put an `<svg>` element in your page and draw with shape elements such as `<rect>`, `<circle>`, `<ellipse>`, `<line>`, `<polygon>` and `<text>`.",
                  code='<svg width="200" height="100">\n  <circle cx="50" cy="50" r="40" fill="royalblue" />\n  <rect x="110" y="10" width="80" height="80" fill="tomato" />\n</svg>'),
             dict(h="Scaling with viewBox", p="`viewBox=\"0 0 200 100\"` defines the drawing's own coordinate system. With it, the graphic scales to fit any size you give it with CSS."),
             dict(h="Why use SVG", p="It never gets blurry, files are small for simple shapes, it can be styled with CSS, and its text can be read by search engines and screen readers."),
         ],
         example='''<svg viewBox="0 0 300 120" width="300" height="120" role="img" aria-label="A blue circle, a red square and a green line">
  <rect width="300" height="120" fill="aliceblue" />
  <circle cx="60" cy="60" r="40" fill="royalblue" />
  <rect x="120" y="20" width="80" height="80" fill="tomato" />
  <line x1="220" y1="20" x2="280" y2="100" stroke="seagreen" stroke-width="6" />
  <text x="150" y="112" font-size="12" text-anchor="middle" fill="navy">Shapes</text>
</svg>''',
         tip="Add `role=\"img\"` and an `aria-label` to an informative SVG so screen readers can describe it.",
         exercise=[
             dict(q="What does the abbreviation SVG stand for?", options=["Simple Vector Graph", "Scalable Vector Graphics", "Standard Visual Grid", "Styled Vector Group"], answer=1),
             dict(q="Which SVG element draws a circle?", options=["<round>", "<ellipse-r>", "<circle>", "<arc>"], answer=2),
             dict(q="Which SVG attribute lets a graphic scale to fit any container?", options=["viewBox", "scale", "zoom", "fit"], answer=0),
         ]),
    dict(slug="accessibility", title="HTML Accessibility", group="Advanced",
         intro="Accessible pages can be used by everyone, including people who use screen readers, keyboards or magnifiers.",
         sections=[
             dict(h="Use the right elements", p="Use `<button>` for actions, `<a>` for links, real headings for structure and landmarks such as `<nav>` and `<main>`. They work with the keyboard and screen readers with no extra effort."),
             dict(h="Text alternatives and labels", p="Give every informative image an `alt`. Give every form control a `<label>`. Icon-only buttons need an `aria-label` that describes the action.",
                  code='<button aria-label="Close dialog">&times;</button>\n<img src="chart.png" alt="Sales grew 20 percent in 2025">'),
             dict(h="Contrast and language", p="WCAG level AA asks for a contrast ratio of at least 4.5:1 for normal text. Set `lang` on <html> so speech software uses the right voice."),
             dict(h="Keyboard", p="Everything that can be clicked must also work with the Tab and Enter keys. Never remove the focus outline without a replacement."),
         ],
         example='''<style>
  button { font: inherit; padding: 8px 14px; border: 0; border-radius: 6px; background: navy; color: white; cursor: pointer; }
  button:focus-visible { outline: 3px solid orange; outline-offset: 2px; }
</style>
<p>Press the Tab key to move focus to the buttons:</p>
<button type="button">Save</button>
<button type="button" aria-label="Close dialog">&times;</button>
<p><label for="e">Email address</label><br><input id="e" type="email"></p>''',
         tip="Try using the page with only your keyboard. If you cannot reach or use something, it is not accessible yet.",
         exercise=[
             dict(q="Which attribute gives an icon-only button a name that a screen reader can announce?", options=["aria-label", "alt-text", "tooltip", "name-for"], answer=0),
             dict(q="Which element should you use for a clickable action so it works with the keyboard?", options=["<div>", "<span>", "<button>", "<p>"], answer=2),
             dict(q="What minimum contrast ratio does WCAG level AA require for normal text?", options=["2:1", "3:1", "4.5:1", "10:1"], answer=2),
         ]),
    dict(slug="seo", title="HTML and SEO", group="Advanced",
         intro="Search engine optimisation (SEO) helps search engines understand your page so the right people find it. Good HTML is the foundation.",
         sections=[
             dict(h="Title and description", p="Write a unique `<title>` for every page. Add `<meta name=\"description\">` with a summary of about 150 to 160 characters. Search engines often show it under the title.",
                  code='<title>Learn HTML | TechHub</title>\n<meta name="description" content="Free HTML lessons with live examples and quizzes.">'),
             dict(h="Structure", p="Use one `<h1>` and logical headings, semantic elements, descriptive link text and `alt` text on images. This helps both search engines and people."),
             dict(h="Robots and sharing", p="`<meta name=\"robots\" content=\"noindex\">` asks search engines not to list a page. `<link rel=\"canonical\" href=\"...\">` names the preferred address when a page has duplicates. Open Graph tags such as `og:title` control how a link looks when shared.",
                  code='<meta name="robots" content="noindex">\n<link rel="canonical" href="https://example.com/html">\n<meta property="og:title" content="Learn HTML">'),
         ],
         example='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Learn HTML | TechHub</title>
  <meta name="description" content="Free HTML lessons with live examples and quizzes.">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h1>Learn HTML</h1>
  <p>A good title, description and heading help search engines understand this page.</p>
</body>
</html>''',
         tip="Write for people first. Stuffing a page with repeated keywords hurts more than it helps.",
         exercise=[
             dict(q="Roughly how long should a meta description be?", options=["5 characters", "About 150 to 160 characters", "1000 characters", "As long as the page"], answer=1),
             dict(q="Which meta tag asks search engines not to list a page?", options=['<meta name="robots" content="noindex">', '<meta name="hide" content="true">', '<meta name="search" content="off">', '<meta name="private">'], answer=0),
             dict(q="How many <h1> elements should a typical page have?", options=["None", "One", "Six", "As many as possible"], answer=1),
         ]),
    dict(slug="best-practices", title="HTML Style Guide and Best Practices", group="Advanced",
         intro="Consistent, clean HTML is easier to read, maintain and fix. These habits will serve you on every project.",
         sections=[
             dict(h="Always declare the basics", p="Start with `<!DOCTYPE html>`, set `lang` on <html>, declare `<meta charset=\"UTF-8\">`, add a viewport tag and give every page a `<title>`."),
             dict(h="Write tidy code", p="Use lowercase tag and attribute names, quote attribute values, close your elements, indent nested elements with two spaces and keep lines readable.",
                  code='<!-- Good -->\n<ul>\n  <li>One</li>\n  <li>Two</li>\n</ul>'),
             dict(h="Content rules", p="Add `alt` to images, use headings in order, use semantic elements and avoid deprecated tags such as `<font>` and `<center>`. Move styles to CSS."),
             dict(h="Check your work", p="The W3C Markup Validation Service finds mistakes such as unclosed tags. Name files in lowercase with hyphens and no spaces, for example `about-us.html`."),
         ],
         example='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Clean page</title>
</head>
<body>
  <main>
    <h1>A clean page</h1>
    <p>Lowercase tags, quoted values, closed elements and two-space indents.</p>
    <ul>
      <li>Readable</li>
      <li>Valid</li>
    </ul>
  </main>
</body>
</html>''',
         tip="Run your pages through a validator before you publish them. It is quick and catches mistakes that are hard to spot.",
         exercise=[
             dict(q="Which doctype declaration is correct for HTML5?", options=["<!DOCTYPE html5>", "<!DOCTYPE html>", "<!HTML version=\"5\">", "<doctype html5>"], answer=1),
             dict(q="Which free tool checks whether your HTML is valid?", options=["The W3C Markup Validation Service", "A spell checker", "A file compressor", "The browser's address bar"], answer=0),
             dict(q="Which style of file name is recommended for web pages?", options=["Capital letters and spaces", "Lowercase with hyphens and no spaces", "Spaces and underscores mixed", "Only numbers"], answer=1),
         ]),
]


# Teaching order inside each group (lessons are sorted by group, then by this list).
ORDER = [
    "intro", "editors", "basic", "structure", "head-elements", "elements", "attributes",
    "headings", "paragraphs", "styles", "formatting", "quotations", "code-elements", "comments",
    "colors", "css", "entities", "symbols", "emojis",
    "links", "link-targets", "file-paths", "images", "image-maps", "picture", "favicon",
    "video", "audio", "iframes", "embedding",
    "lists", "nested-lists", "tables", "table-spans", "table-styling",
    "forms", "form-attributes", "form-elements", "input-types", "input-attributes",
    "block-inline", "div-span", "classes", "id", "semantic", "layout", "responsive",
    "charset", "url-encoding", "canvas", "svg", "accessibility", "seo", "best-practices",
]
LESSONS.sort(key=lambda l: (GROUPS.index(l["group"]), ORDER.index(l["slug"])))
BY_SLUG = {l["slug"]: l for l in LESSONS}


def _balance_answers():
    """Spread the correct answer evenly over positions A-D (swap, so other options keep their order)."""
    n = 0
    for lesson in LESSONS:
        for q in lesson["exercise"]:
            target = n % 4
            opts, a = q["options"], q["answer"]
            opts[a], opts[target] = opts[target], opts[a]
            q["answer"] = target
            n += 1


_balance_answers()
