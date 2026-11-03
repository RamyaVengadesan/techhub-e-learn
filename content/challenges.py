"""Auto-checked coding challenges for TechHub.

Each challenge: slug, module, level, title, lesson (optional related lesson slug), instructions, starter,
tests [{label, js}], hint, solution.

Tests run in the learner's sandboxed page, about 600 ms after load. Every `js` is one JavaScript expression,
evaluated with indirect eval; a truthy (or resolved truthy) result passes, a thrown error fails.
Helpers available inside tests: $(sel), $$(sel), css(sel, prop[, pseudo]), rgb(color), text(sel), logs
(array of console.log lines), plus the learner's own top-level functions and variables.
"""


def T(label, js):
    return dict(label=label, js=js.strip())


def C(slug, module, level, title, lesson, instructions, starter, tests, hint, solution):
    return dict(slug=slug, module=module, level=level, title=title, lesson=lesson,
                instructions=instructions, starter=starter.strip("\n"), tests=tests,
                hint=hint, solution=solution.strip("\n"))


CHALLENGES = []
add = CHALLENGES.append

# ===================================================================================== HTML
# ----------------------------------------------------------------- beginner
add(C("ch-html-heading-paragraph", "html", "beginner", "Add a heading and a paragraph", "headings",
      "Add an `<h1>` heading that says Welcome, then a `<p>` paragraph below it that introduces yourself in one sentence.",
      r'''<!-- Write your h1 and your paragraph below -->
''',
      [T("Has an <h1> heading", r'''!!$('h1')'''),
       T("The heading says Welcome", r'''text('h1').toLowerCase().includes('welcome')'''),
       T("Has a <p> paragraph with some text", r'''text('p').length > 3'''),
       T("The paragraph comes after the heading", r'''!!$('h1') && !!$('p') && !!($('h1').compareDocumentPosition($('p')) & Node.DOCUMENT_POSITION_FOLLOWING)''')],
      "Headings use `<h1>text</h1>` and paragraphs use `<p>text</p>`.",
      r'''<h1>Welcome</h1>
<p>Hi, I am Asha and I am learning to build websites.</p>'''))

add(C("ch-html-link", "html", "beginner", "Create a link that opens in a new tab", "links",
      "Turn the sentence into a real link. Add an `<a>` that points to `https://example.com`, with the link text Visit Example, and make it open in a new tab with `target=\"_blank\"`.",
      r'''<p>Click here to visit the site: </p>''',
      [T("Has an <a> element", r'''!!$('a')'''),
       T("The href points to example.com", r'''($('a').getAttribute('href') || '').includes('example.com')'''),
       T("The link text says Visit Example", r'''text('a').toLowerCase().includes('visit example')'''),
       T("The link opens in a new tab", r'''$('a').getAttribute('target') === '_blank' ''')],
      "The address goes in the href attribute: `<a href=\"...\">text</a>`.",
      r'''<p>Click here to visit the site: <a href="https://example.com" target="_blank" rel="noopener">Visit Example</a></p>'''))

add(C("ch-html-image-alt", "html", "beginner", "Make an image accessible", "images",
      "This image has no description. Add an `alt` attribute that describes it (for example a blue banner) and set its `width` attribute to 200.",
      r'''<img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect width='300' height='200' fill='%231d4ed8'/></svg>">''',
      [T("Has an <img>", r'''!!$('img')'''),
       T("The image has alt text", r'''($('img').getAttribute('alt') || '').trim().length > 2'''),
       T("The width attribute is 200", r'''$('img').getAttribute('width') === '200' ''')],
      "Add `alt=\"...\"` and `width=\"200\"` inside the opening `<img>` tag.",
      r'''<img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><rect width='300' height='200' fill='%231d4ed8'/></svg>" alt="A plain blue banner" width="200">'''))

add(C("ch-html-lists", "html", "beginner", "Build a bulleted and a numbered list", "lists",
      "Under the first heading add a bulleted list (`<ul>`) with three items. Under the second heading add a numbered list (`<ol>`) with three steps. Use `<li>` for every item.",
      r'''<h2>Shopping</h2>
<!-- bulleted list here -->

<h2>Steps</h2>
<!-- numbered list here -->''',
      [T("Has a <ul> with at least 3 items", r'''$$('ul > li').length >= 3'''),
       T("Has an <ol> with at least 3 items", r'''$$('ol > li').length >= 3'''),
       T("The list items are not empty", r'''$$('li').length >= 6 && $$('li').every(li => li.textContent.trim().length > 0)'''),
       T("The <ul> comes before the <ol>", r'''!!$('ul') && !!$('ol') && !!($('ul').compareDocumentPosition($('ol')) & Node.DOCUMENT_POSITION_FOLLOWING)''')],
      "Each item is `<li>text</li>` and the `<li>` elements go inside `<ul>` or `<ol>`.",
      r'''<h2>Shopping</h2>
<ul>
  <li>Milk</li>
  <li>Bread</li>
  <li>Eggs</li>
</ul>

<h2>Steps</h2>
<ol>
  <li>Open the editor</li>
  <li>Write some HTML</li>
  <li>Run it</li>
</ol>'''))

add(C("ch-html-formatting", "html", "beginner", "Mark up important and emphasised text", "formatting",
      "Wrap the words very important in `<strong>` and the words slightly emphasised in `<em>`. Leave the rest of the sentence as plain text.",
      r'''<p>This text is very important and this is slightly emphasised.</p>''',
      [T("Has a <strong> element", r'''!!$('strong')'''),
       T("<strong> wraps the words very important", r'''text('strong').toLowerCase() === 'very important' '''),
       T("<em> wraps the words slightly emphasised", r'''text('em').toLowerCase() === 'slightly emphasised' '''),
       T("Both are still inside the paragraph", r'''!!$('p strong') && !!$('p em')''')],
      "Put `<strong>` and `</strong>` around only those two words.",
      r'''<p>This text is <strong>very important</strong> and this is <em>slightly emphasised</em>.</p>'''))

# ----------------------------------------------------------------- intermediate
add(C("ch-html-table", "html", "intermediate", "Build a data table", "tables",
      "Create a table with three header cells (`<th>`): Name, Age and City. Add two data rows below the header, each with three `<td>` cells.",
      r'''<!-- Build your table here -->''',
      [T("Has a <table>", r'''!!$('table')'''),
       T("Has at least 3 header cells", r'''$$('table th').length >= 3'''),
       T("Has at least 3 rows (header and 2 data rows)", r'''$$('table tr').length >= 3'''),
       T("Has at least 6 data cells", r'''$$('table td').length >= 6'''),
       T("Header cells say Name, Age and City", r'''['name', 'age', 'city'].every(w => $$('th').some(th => th.textContent.trim().toLowerCase() === w))''')],
      "A row is `<tr>`; header cells are `<th>` and data cells are `<td>`.",
      r'''<table border="1" cellpadding="6">
  <thead>
    <tr><th>Name</th><th>Age</th><th>City</th></tr>
  </thead>
  <tbody>
    <tr><td>Asha</td><td>21</td><td>Chennai</td></tr>
    <tr><td>Ravi</td><td>24</td><td>Pune</td></tr>
  </tbody>
</table>'''))

add(C("ch-html-table-span", "html", "intermediate", "Add a caption and span a column", "table-spans",
      "Add a `<caption>` with the text Team to the table. Then make the Contact header cell stretch across two columns with `colspan`.",
      r'''<table border="1" cellpadding="6">
  <tr><th>Name</th><th>Contact</th></tr>
  <tr><td>Asha</td><td>asha@example.com</td><td>555-0101</td></tr>
</table>''',
      [T("Has a <caption>", r'''!!$('caption')'''),
       T("The caption says Team", r'''text('caption').toLowerCase().includes('team')'''),
       T("The Contact header spans 2 columns", r'''(() => { const th = $$('th').find(t => t.textContent.trim().toLowerCase() === 'contact'); return !!th && th.colSpan === 2; })()'''),
       T("The Name header is still there", r'''$$('th').some(t => t.textContent.trim().toLowerCase() === 'name')''')],
      "Use `colspan=\"2\"` on the `<th>`; the caption goes right after the opening `<table>` tag.",
      r'''<table border="1" cellpadding="6">
  <caption>Team</caption>
  <tr><th>Name</th><th colspan="2">Contact</th></tr>
  <tr><td>Asha</td><td>asha@example.com</td><td>555-0101</td></tr>
</table>'''))

add(C("ch-html-form-labels", "html", "intermediate", "Create a form with labelled inputs", "forms",
      "Inside the form add a text input for the name and an email input (`type=\"email\"`), each connected to a `<label>` with matching `for` and `id` values. Finish with a submit button.",
      r'''<form>
  <!-- Add the labelled inputs and the submit button -->
</form>''',
      [T("Has a <form>", r'''!!$('form')'''),
       T("Has a text input and an email input", r'''!!$('input[type="text"], input:not([type])') && !!$('input[type="email"]')'''),
       T("Every input is connected to a label (for and id match)", r'''$$('form input').filter(i => i.type !== 'submit').length >= 2 && $$('form input').filter(i => i.type !== 'submit').every(i => i.id && !!$('label[for="' + i.id + '"]'))'''),
       T("Has a submit button", r'''!!$('form button[type="submit"], form button:not([type]), form input[type="submit"]')''')],
      "A label looks like `<label for=\"name\">Name</label>` and its input needs `id=\"name\"`.",
      r'''<form>
  <p>
    <label for="name">Name</label><br>
    <input type="text" id="name" name="name">
  </p>
  <p>
    <label for="email">Email</label><br>
    <input type="email" id="email" name="email">
  </p>
  <button type="submit">Send</button>
</form>'''))

add(C("ch-html-semantic", "html", "intermediate", "Replace divs with semantic elements", "semantic",
      "These generic `<div>` elements work, but they say nothing about their purpose. Rewrite them using `<header>`, `<nav>`, `<main>` and `<footer>`.",
      r'''<div class="header"><h1>My Blog</h1></div>
<div class="nav"><a href="#">Home</a> <a href="#">About</a></div>
<div class="main"><h2>First post</h2><p>Hello!</p></div>
<div class="footer"><p>&copy; 2026</p></div>''',
      [T("Uses a <header> containing the <h1>", r'''!!$('header h1')'''),
       T("Uses a <nav> containing at least 2 links", r'''$$('nav a').length >= 2'''),
       T("Uses a <main> containing the post", r'''!!$('main h2') && !!$('main p')'''),
       T("Uses a <footer> containing the copyright text", r'''!!$('footer p') && text('footer').includes('2026')''')],
      "Swap each `<div class=\"...\">` for the element with that purpose, for example `<header>`.",
      r'''<header><h1>My Blog</h1></header>
<nav><a href="#">Home</a> <a href="#">About</a></nav>
<main><h2>First post</h2><p>Hello!</p></main>
<footer><p>&copy; 2026</p></footer>'''))

add(C("ch-html-select-textarea", "html", "intermediate", "Add a drop-down and a text area", "form-elements",
      "Add a labelled drop-down (`<select>`) called Course with three `<option>` choices, and a `<textarea>` with `name=\"message\"` and `rows=\"4\"`.",
      r'''<form>
  <!-- Add the select (with a label) and the textarea -->
</form>''',
      [T("Has a <select> with at least 3 options", r'''$$('select option').length >= 3'''),
       T("The select has a label", r'''!!$('select').id && !!$('label[for="' + $('select').id + '"]')'''),
       T("Has a <textarea> named message", r'''!!$('textarea[name="message"]')'''),
       T("The textarea has 4 rows", r'''!!$('textarea') && $('textarea').rows === 4''')],
      "Options go inside the select: `<select id=\"course\"><option>HTML</option></select>`.",
      r'''<form>
  <p>
    <label for="course">Course</label>
    <select id="course" name="course">
      <option>HTML</option>
      <option>CSS</option>
      <option>JavaScript</option>
    </select>
  </p>
  <p>
    <label for="msg">Message</label><br>
    <textarea id="msg" name="message" rows="4"></textarea>
  </p>
</form>'''))

# ----------------------------------------------------------------- advanced
add(C("ch-html-accessible-form", "html", "advanced", "Make a form accessible and validated", "form-validation",
      "Turn the email field into a real email input that is required and has `autocomplete=\"email\"`. Then group the two radio buttons in a `<fieldset>` with a `<legend>` that says Contact method.",
      r'''<form>
  <label for="email">Email</label>
  <input type="text" id="email" name="email">

  <p>Contact method</p>
  <label><input type="radio" name="method" value="email"> Email</label>
  <label><input type="radio" name="method" value="phone"> Phone</label>
</form>''',
      [T("The email input uses type=\"email\"", r'''!!$('#email') && $('#email').type === 'email' '''),
       T("The email input is required", r'''!!$('#email') && $('#email').required === true'''),
       T("The email input has autocomplete=\"email\"", r'''!!$('#email') && $('#email').getAttribute('autocomplete') === 'email' '''),
       T("Both radio buttons sit inside a fieldset", r'''$$('fieldset input[type="radio"]').length === 2'''),
       T("The fieldset has a legend about the contact method", r'''text('fieldset legend').toLowerCase().includes('contact')''')],
      "Change `type=\"text\"` to `type=\"email\"`, add `required`, and wrap the radios in `<fieldset><legend>...</legend>`.",
      r'''<form>
  <label for="email">Email</label>
  <input type="email" id="email" name="email" required autocomplete="email">

  <fieldset>
    <legend>Contact method</legend>
    <label><input type="radio" name="method" value="email"> Email</label>
    <label><input type="radio" name="method" value="phone"> Phone</label>
  </fieldset>
</form>'''))

add(C("ch-html-details", "html", "advanced", "Build an FAQ with details and summary", "details-summary",
      "Create two questions using `<details>` with a `<summary>` for the question and a paragraph for the answer. The first one should be open when the page loads (use the `open` attribute).",
      r'''<h2>FAQ</h2>
<!-- Add two details elements -->''',
      [T("Has at least 2 <details> elements", r'''$$('details').length >= 2'''),
       T("Each has a <summary> with text", r'''$$('details').length >= 2 && $$('details').every(d => d.querySelector('summary') && d.querySelector('summary').textContent.trim().length > 0)'''),
       T("Each has an answer paragraph", r'''$$('details').length >= 2 && $$('details').every(d => !!d.querySelector('p'))'''),
       T("The first one is open", r'''!!$('details') && $('details').open === true'''),
       T("The second one is closed", r'''$$('details').length >= 2 && $$('details')[1].open === false''')],
      "The question goes in `<summary>`, and the first `<details>` needs the `open` attribute.",
      r'''<h2>FAQ</h2>
<details open>
  <summary>What is HTML?</summary>
  <p>HTML is the language that structures web pages.</p>
</details>
<details>
  <summary>Is it free to learn?</summary>
  <p>Yes, all you need is a browser.</p>
</details>'''))

add(C("ch-html-dialog", "html", "advanced", "Create a dialog with a close button", "dialog",
      "Add a `<dialog>` that is already open. Inside it put an `<h2>` heading and a `<form>` with `method=\"dialog\"` that contains a button labelled Close.",
      r'''<!-- Add your dialog here -->''',
      [T("Has a <dialog>", r'''!!$('dialog')'''),
       T("The dialog is open", r'''!!$('dialog') && $('dialog').open === true'''),
       T("The dialog has an <h2> heading", r'''!!$('dialog h2') && text('dialog h2').length > 0'''),
       T("The dialog has a form with method=\"dialog\"", r'''!!$('dialog form') && $('dialog form').getAttribute('method') === 'dialog' '''),
       T("The form has a button labelled Close", r'''!!$('dialog form button') && text('dialog form button').toLowerCase().includes('close')''')],
      "Write `<dialog open>` and put `<form method=\"dialog\"><button>Close</button></form>` inside.",
      r'''<dialog open>
  <h2>Welcome</h2>
  <p>This is a native dialog.</p>
  <form method="dialog">
    <button>Close</button>
  </form>
</dialog>'''))

add(C("ch-html-picture", "html", "advanced", "Serve a responsive picture", "picture",
      "Wrap the image in a `<picture>`. Add a `<source>` that uses `photo-large.jpg` when the screen is at least 600px wide (`media=\"(min-width: 600px)\"`). Give the `<img>` meaningful alt text and `loading=\"lazy\"`.",
      r'''<img src="photo-small.jpg">''',
      [T("The image is inside a <picture>", r'''!!$('picture img')'''),
       T("There is a <source> with a min-width media query", r'''!!$('picture source[media]') && $('picture source').getAttribute('media').includes('min-width')'''),
       T("The <source> uses photo-large.jpg", r'''!!$('picture source') && ($('picture source').getAttribute('srcset') || '').includes('photo-large.jpg')'''),
       T("The <img> has alt text", r'''!!$('img') && ($('img').getAttribute('alt') || '').trim().length > 2'''),
       T("The <img> loads lazily", r'''!!$('img') && $('img').getAttribute('loading') === 'lazy' ''')],
      "Order matters: `<picture>` holds the `<source>` first and the fallback `<img>` last.",
      r'''<picture>
  <source media="(min-width: 600px)" srcset="photo-large.jpg">
  <img src="photo-small.jpg" alt="A mountain lake at sunrise" loading="lazy">
</picture>'''))

add(C("ch-html-video", "html", "advanced", "Embed a video the right way", "video",
      "Create a `<video>` with playback controls (`controls`), a `poster` image, `preload=\"metadata\"` and a `<source>` of type `video/mp4`. Put a short fallback sentence inside the video for browsers that cannot play it.",
      r'''<!-- Add your video here -->''',
      [T("Has a <video> with controls", r'''!!$('video[controls]')'''),
       T("Has a poster attribute", r'''!!$('video') && ($('video').getAttribute('poster') || '').length > 0'''),
       T("Uses preload=\"metadata\"", r'''!!$('video') && $('video').getAttribute('preload') === 'metadata' '''),
       T("Has a <source> of type video/mp4", r'''!!$('video source[type="video/mp4"]')'''),
       T("Has fallback text inside the video", r'''!!$('video') && $('video').textContent.trim().length > 5''')],
      "The `<source src=\"clip.mp4\" type=\"video/mp4\">` goes inside `<video>`, followed by your fallback text.",
      r'''<video controls width="320" poster="poster.jpg" preload="metadata">
  <source src="clip.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>'''))

# ===================================================================================== CSS
# ----------------------------------------------------------------- beginner
add(C("ch-css-colors", "css", "beginner", "Colour a heading and a paragraph", "css-colors",
      "Write two rules: make every `h1` the colour `tomato`, and give every `p` a `lightyellow` background (use `background-color`).",
      r'''<style>
  /* write your CSS here */
</style>

<h1>Colour me</h1>
<p>I need a pale yellow background.</p>''',
      [T("The h1 text is tomato", r'''css('h1', 'color') === rgb('tomato')'''),
       T("The paragraph background is lightyellow", r'''css('p', 'backgroundColor') === rgb('lightyellow')'''),
       T("The heading has no background colour", r'''css('h1', 'backgroundColor') === 'rgba(0, 0, 0, 0)' ''')],
      "A rule looks like `h1 { color: tomato; }`.",
      r'''<style>
  h1 { color: tomato; }
  p { background-color: lightyellow; }
</style>

<h1>Colour me</h1>
<p>I need a pale yellow background.</p>'''))

add(C("ch-css-class-selector", "css", "beginner", "Style with a class", "css-selectors-basic",
      "Write a `.highlight` rule with a `gold` background and bold text, then apply the class to the second paragraph only.",
      r'''<style>
  /* write the .highlight rule */
</style>

<p>First paragraph.</p>
<p>Second paragraph.</p>''',
      [T("The second paragraph has the highlight class", r'''$$('p').length >= 2 && $$('p')[1].classList.contains('highlight')'''),
       T("The second paragraph has a gold background", r'''css('p:nth-of-type(2)', 'backgroundColor') === rgb('gold')'''),
       T("The second paragraph is bold", r'''parseInt(css('p:nth-of-type(2)', 'fontWeight')) >= 600'''),
       T("The first paragraph is not highlighted", r'''$$('p')[0].classList.contains('highlight') === false && css('p', 'backgroundColor') === 'rgba(0, 0, 0, 0)' ''')],
      "Class selectors start with a dot: `.highlight { ... }`, and the HTML needs `class=\"highlight\"`.",
      r'''<style>
  .highlight { background-color: gold; font-weight: bold; }
</style>

<p>First paragraph.</p>
<p class="highlight">Second paragraph.</p>'''))

add(C("ch-css-box-model", "css", "beginner", "Control the box model", "css-box-sizing",
      "Style `.box` so it is exactly 200px wide in total, even with padding and a border. Give it `padding: 20px`, a `4px solid` border, `margin-top: 30px` and `box-sizing: border-box`.",
      r'''<style>
  .box {
    width: 200px;
    background: #e8f0ff;
  }
</style>

<div class="box">Hello box</div>''',
      [T("The total box width is 200px", r'''Math.round($('.box').getBoundingClientRect().width) === 200'''),
       T("The padding is 20px", r'''css('.box', 'paddingTop') === '20px' && css('.box', 'paddingLeft') === '20px' '''),
       T("The border is 4px wide", r'''css('.box', 'borderTopWidth') === '4px' && css('.box', 'borderTopStyle') === 'solid' '''),
       T("The top margin is 30px", r'''css('.box', 'marginTop') === '30px' '''),
       T("It uses box-sizing: border-box", r'''css('.box', 'boxSizing') === 'border-box' ''')],
      "With `box-sizing: border-box`, padding and border are counted inside the width.",
      r'''<style>
  .box {
    width: 200px;
    background: #e8f0ff;
    padding: 20px;
    border: 4px solid #1d4ed8;
    margin-top: 30px;
    box-sizing: border-box;
  }
</style>

<div class="box">Hello box</div>'''))

add(C("ch-css-fonts-text", "css", "beginner", "Style text and fonts", "css-fonts",
      "Style the paragraph: font family `Georgia, serif`, font size `24px`, centred text (`text-align`) and a `line-height` of `1.6`.",
      r'''<style>
  p {
    /* your declarations here */
  }
</style>

<p>Good typography makes text easy to read.</p>''',
      [T("The font family is Georgia with a serif fallback", r'''css('p', 'fontFamily').toLowerCase().includes('georgia') && css('p', 'fontFamily').toLowerCase().includes('serif')'''),
       T("The font size is 24px", r'''css('p', 'fontSize') === '24px' '''),
       T("The text is centred", r'''css('p', 'textAlign') === 'center' '''),
       T("The line height is 1.6 times the font size", r'''Math.abs(parseFloat(css('p', 'lineHeight')) - 38.4) < 0.2''')],
      "A unitless `line-height: 1.6` is multiplied by the font size.",
      r'''<style>
  p {
    font-family: Georgia, serif;
    font-size: 24px;
    text-align: center;
    line-height: 1.6;
  }
</style>

<p>Good typography makes text easy to read.</p>'''))

add(C("ch-css-avatar", "css", "beginner", "Make a round avatar with a shadow", "css-border-radius",
      "Turn the square into a circle. Give `.avatar` a width and height of `100px`, `border-radius: 50%`, and a `box-shadow` so it looks lifted.",
      r'''<style>
  .avatar {
    background: #1d4ed8;
  }
</style>

<div class="avatar"></div>''',
      [T("The avatar is 100px wide and 100px tall", r'''(() => { const r = $('.avatar').getBoundingClientRect(); return Math.round(r.width) === 100 && Math.round(r.height) === 100; })()'''),
       T("The corners are fully rounded (a circle)", r'''['50%', '50px'].includes(css('.avatar', 'borderTopLeftRadius')) && ['50%', '50px'].includes(css('.avatar', 'borderBottomRightRadius'))'''),
       T("It has a box shadow", r'''css('.avatar', 'boxShadow') !== 'none' ''')],
      "A 50% radius on a square makes a circle: `border-radius: 50%`.",
      r'''<style>
  .avatar {
    background: #1d4ed8;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
  }
</style>

<div class="avatar"></div>'''))

# ----------------------------------------------------------------- intermediate
add(C("ch-css-flex-center", "css", "intermediate", "Centre a box with flexbox", "css-flexbox",
      "Use flexbox on `.parent` to centre `.child` both horizontally and vertically.",
      r'''<style>
  .parent {
    width: 400px;
    height: 300px;
    border: 2px solid #1d4ed8;
  }
  .child {
    width: 80px;
    height: 80px;
    background: #1d4ed8;
  }
</style>

<div class="parent"><div class="child"></div></div>''',
      [T("The parent is a flex container", r'''css('.parent', 'display') === 'flex' '''),
       T("The child is centred horizontally", r'''(() => { const p = $('.parent').getBoundingClientRect(), c = $('.child').getBoundingClientRect(); return Math.abs((p.left + p.width / 2) - (c.left + c.width / 2)) < 2; })()'''),
       T("The child is centred vertically", r'''(() => { const p = $('.parent').getBoundingClientRect(), c = $('.child').getBoundingClientRect(); return Math.abs((p.top + p.height / 2) - (c.top + c.height / 2)) < 2; })()'''),
       T("The child keeps its 80px size", r'''Math.round($('.child').getBoundingClientRect().width) === 80 && Math.round($('.child').getBoundingClientRect().height) === 80''')],
      "You need `display: flex` plus two alignment properties: `justify-content` and `align-items`.",
      r'''<style>
  .parent {
    width: 400px;
    height: 300px;
    border: 2px solid #1d4ed8;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .child {
    width: 80px;
    height: 80px;
    background: #1d4ed8;
  }
</style>

<div class="parent"><div class="child"></div></div>'''))

add(C("ch-css-grid-columns", "css", "intermediate", "Lay out three equal grid columns", "css-grid",
      "Turn `.grid` into a grid with three equal columns and a `16px` gap between items.",
      r'''<style>
  .grid {
    /* make this a 3-column grid */
  }
  .grid div {
    background: #e8f0ff;
    padding: 20px;
  }
</style>

<div class="grid">
  <div>1</div><div>2</div><div>3</div>
  <div>4</div><div>5</div><div>6</div>
</div>''',
      [T("The container is a grid", r'''css('.grid', 'display') === 'grid' '''),
       T("There are exactly 3 columns", r'''css('.grid', 'gridTemplateColumns').trim().split(/\s+/).length === 3'''),
       T("The columns have equal widths", r'''(() => { const w = css('.grid', 'gridTemplateColumns').trim().split(/\s+/).map(parseFloat); return w.length === 3 && Math.max(...w) - Math.min(...w) < 1; })()'''),
       T("The gap is 16px", r'''css('.grid', 'columnGap') === '16px' && css('.grid', 'rowGap') === '16px' ''')],
      "Try `grid-template-columns: repeat(3, 1fr)` and `gap: 16px`.",
      r'''<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }
  .grid div {
    background: #e8f0ff;
    padding: 20px;
  }
</style>

<div class="grid">
  <div>1</div><div>2</div><div>3</div>
  <div>4</div><div>5</div><div>6</div>
</div>'''))

add(C("ch-css-hover-button", "css", "intermediate", "Add a hover effect with a transition", "css-transitions",
      "Give `.btn` a `royalblue` background and rounded corners (at least `6px`). Add a `.btn:hover` rule that changes the background colour, and a `transition` so the change is smooth.",
      r'''<style>
  .btn {
    color: white;
    border: 0;
    padding: 10px 20px;
    cursor: pointer;
  }
</style>

<button class="btn">Hover me</button>''',
      [T("The button background is royalblue", r'''css('.btn', 'backgroundColor') === rgb('royalblue')'''),
       T("The corners are rounded (6px or more)", r'''parseFloat(css('.btn', 'borderTopLeftRadius')) >= 6'''),
       T("A :hover rule changes the background to a different colour", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => r.selectorText && r.selectorText.includes('.btn:hover') && (r.style.backgroundColor || r.style.background) && rgb(r.style.backgroundColor || r.style.background) !== css('.btn', 'backgroundColor')))'''),
       T("The button has a transition", r'''parseFloat(css('.btn', 'transitionDuration')) > 0''')],
      "Add `transition: background-color 0.3s;` to `.btn`, and write `.btn:hover { background-color: navy; }`.",
      r'''<style>
  .btn {
    color: white;
    border: 0;
    padding: 10px 20px;
    cursor: pointer;
    background-color: royalblue;
    border-radius: 8px;
    transition: background-color 0.3s;
  }
  .btn:hover {
    background-color: navy;
  }
</style>

<button class="btn">Hover me</button>'''))

add(C("ch-css-position-badge", "css", "intermediate", "Pin a badge to the corner of a card", "css-position",
      "Make `.card` the positioning context with `position: relative`. Then use `position: absolute` on `.badge` to place it in the top-right corner of the card.",
      r'''<style>
  .card {
    width: 260px;
    padding: 24px;
    border: 1px solid #c5d6f6;
  }
  .badge {
    background: tomato;
    color: white;
    padding: 2px 8px;
    border-radius: 10px;
  }
</style>

<div class="card">
  <span class="badge">New</span>
  <h3>Course card</h3>
</div>''',
      [T("The card is position: relative", r'''css('.card', 'position') === 'relative' '''),
       T("The badge is position: absolute", r'''css('.badge', 'position') === 'absolute' '''),
       T("The badge sits at the top edge of the card", r'''(() => { const c = $('.card').getBoundingClientRect(), b = $('.badge').getBoundingClientRect(); return Math.abs(b.top - c.top) <= 20; })()'''),
       T("The badge sits at the right edge of the card", r'''(() => { const c = $('.card').getBoundingClientRect(), b = $('.badge').getBoundingClientRect(); return Math.abs(c.right - b.right) <= 20; })()''')],
      "Absolute positioning is measured from the nearest positioned ancestor. Try `top: 10px; right: 10px;`.",
      r'''<style>
  .card {
    width: 260px;
    padding: 24px;
    border: 1px solid #c5d6f6;
    position: relative;
  }
  .badge {
    background: tomato;
    color: white;
    padding: 2px 8px;
    border-radius: 10px;
    position: absolute;
    top: 10px;
    right: 10px;
  }
</style>

<div class="card">
  <span class="badge">New</span>
  <h3>Course card</h3>
</div>'''))

add(C("ch-css-pseudo-list", "css", "intermediate", "Decorate a list with pseudo-elements", "css-pseudo-elements",
      "Use `li::before` to put an arrow (the text `→ `) in front of every list item. Then use `li:nth-child(even)` to give every even item a light grey background.",
      r'''<style>
  ul { list-style: none; padding: 0; }
  li { padding: 6px 10px; }
  /* add your rules here */
</style>

<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Python</li>
</ul>''',
      [T("Each list item gets a ::before arrow", r'''getComputedStyle($('li'), '::before').content.includes('→')'''),
       T("The second item has a background colour", r'''css('li:nth-child(2)', 'backgroundColor') !== 'rgba(0, 0, 0, 0)' '''),
       T("The fourth item has the same background as the second", r'''css('li:nth-child(4)', 'backgroundColor') === css('li:nth-child(2)', 'backgroundColor')'''),
       T("The first and third items stay transparent", r'''css('li:nth-child(1)', 'backgroundColor') === 'rgba(0, 0, 0, 0)' && css('li:nth-child(3)', 'backgroundColor') === 'rgba(0, 0, 0, 0)' ''')],
      "`li::before { content: \"→ \"; }` adds text before the content, and `li:nth-child(even)` picks every second item.",
      r'''<style>
  ul { list-style: none; padding: 0; }
  li { padding: 6px 10px; }
  li::before { content: "→ "; }
  li:nth-child(even) { background: #eeeeee; }
</style>

<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Python</li>
</ul>'''))

# ----------------------------------------------------------------- advanced
add(C("ch-css-custom-properties", "css", "advanced", "Theme a page with custom properties", "css-variables",
      "Declare a custom property `--brand` on `:root` (any colour you like). Then replace the hard-coded colours so the `h1` text colour and the `.btn` background both use `var(--brand)`.",
      r'''<style>
  h1 { color: #1d4ed8; }
  .btn { background: #1d4ed8; color: white; border: 0; padding: 8px 16px; }
</style>

<h1>Themed page</h1>
<button class="btn">Action</button>''',
      [T("--brand is defined on :root", r'''getComputedStyle(document.documentElement).getPropertyValue('--brand').trim().length > 0'''),
       T("The heading colour matches --brand", r'''css('h1', 'color') === rgb(getComputedStyle(document.documentElement).getPropertyValue('--brand').trim())'''),
       T("The button background matches --brand", r'''css('.btn', 'backgroundColor') === rgb(getComputedStyle(document.documentElement).getPropertyValue('--brand').trim())'''),
       T("The stylesheet uses var(--brand)", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => r.cssText.includes('var(--brand)')))''')],
      "Declare it as `:root { --brand: #0b8457; }` and read it with `color: var(--brand);`.",
      r'''<style>
  :root { --brand: #0b8457; }
  h1 { color: var(--brand); }
  .btn { background: var(--brand); color: white; border: 0; padding: 8px 16px; }
</style>

<h1>Themed page</h1>
<button class="btn">Action</button>'''))

add(C("ch-css-card-hover-lift", "css", "advanced", "Lift a card on hover with transform", "css-transforms",
      "Give `.card` a smooth `transition` on `transform` (at least 0.2s). Then add a `.card:hover` rule that lifts the card with a `transform` such as `translateY(-6px)` or `scale(1.05)`.",
      r'''<style>
  .card {
    width: 200px;
    padding: 20px;
    border: 1px solid #c5d6f6;
    border-radius: 10px;
    background: white;
  }
</style>

<div class="card">Hover over me</div>''',
      [T("The card transitions the transform property", r'''/transform|all/.test(css('.card', 'transitionProperty'))'''),
       T("The transition lasts at least 0.2 seconds", r'''parseFloat(css('.card', 'transitionDuration')) >= 0.2'''),
       T("A :hover rule sets a transform", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => r.selectorText && r.selectorText.includes('.card:hover') && r.style.transform && r.style.transform !== 'none'))''')],
      "Add `transition: transform 0.25s;` to `.card` and `.card:hover { transform: translateY(-6px); }`.",
      r'''<style>
  .card {
    width: 200px;
    padding: 20px;
    border: 1px solid #c5d6f6;
    border-radius: 10px;
    background: white;
    transition: transform 0.25s;
  }
  .card:hover {
    transform: translateY(-6px);
  }
</style>

<div class="card">Hover over me</div>'''))

add(C("ch-css-grid-areas", "css", "advanced", "Build a page layout with grid areas", "css-grid-areas",
      "Make `.layout` a grid using `grid-template-areas`: the header and footer span the full width, and the sidebar sits to the left of the main content. Assign each child to its area with `grid-area`.",
      r'''<style>
  .layout { gap: 10px; }
  .layout > * { padding: 14px; background: #e8f0ff; }
  .header { }
  .sidebar { }
  .main { }
  .footer { }
</style>

<div class="layout">
  <div class="header">Header</div>
  <div class="sidebar">Sidebar</div>
  <div class="main">Main</div>
  <div class="footer">Footer</div>
</div>''',
      [T("The layout is a grid", r'''css('.layout', 'display') === 'grid' '''),
       T("The header spans the full width", r'''(() => { const l = $('.layout').getBoundingClientRect(), h = $('.header').getBoundingClientRect(); return Math.abs(l.width - h.width) < 2; })()'''),
       T("The sidebar is to the left of the main area", r'''(() => { const s = $('.sidebar').getBoundingClientRect(), m = $('.main').getBoundingClientRect(); return s.right <= m.left + 1 && Math.abs(s.top - m.top) < 2; })()'''),
       T("The footer spans the full width below the main area", r'''(() => { const l = $('.layout').getBoundingClientRect(), f = $('.footer').getBoundingClientRect(), m = $('.main').getBoundingClientRect(); return Math.abs(l.width - f.width) < 2 && f.top >= m.bottom - 1; })()'''),
       T("grid-template-areas names all four areas", r'''(() => { const a = css('.layout', 'gridTemplateAreas'); return ['header', 'sidebar', 'main', 'footer'].every(n => a.includes(n)); })()''')],
      "Try `grid-template-areas: \"header header\" \"sidebar main\" \"footer footer\";` with `grid-template-columns: 200px 1fr;`.",
      r'''<style>
  .layout {
    display: grid;
    grid-template-columns: 200px 1fr;
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
    gap: 10px;
  }
  .layout > * { padding: 14px; background: #e8f0ff; }
  .header { grid-area: header; }
  .sidebar { grid-area: sidebar; }
  .main { grid-area: main; }
  .footer { grid-area: footer; }
</style>

<div class="layout">
  <div class="header">Header</div>
  <div class="sidebar">Sidebar</div>
  <div class="main">Main</div>
  <div class="footer">Footer</div>
</div>'''))

add(C("ch-css-fluid-type", "css", "advanced", "Use clamp() for fluid typography", "css-calc-min-max-clamp",
      "The heading uses a fixed size. Replace it with `clamp()` so it never goes below `1.5rem` or above `3rem`, and grows with the screen in between (for example `4vw` in the middle).",
      r'''<style>
  h1 {
    font-size: 32px;
  }
</style>

<h1>Fluid heading</h1>''',
      [T("The font size is set with clamp()", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => r.selectorText && r.selectorText.includes('h1') && /clamp\(/.test(r.cssText)))'''),
       T("The size is never below 24px", r'''parseFloat(css('h1', 'fontSize')) >= 24'''),
       T("The size is never above 48px", r'''parseFloat(css('h1', 'fontSize')) <= 48'''),
       T("clamp() uses a viewport unit for the preferred value", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => /clamp\([^)]*v[wi]/.test(r.cssText)))''')],
      "The format is `clamp(minimum, preferred, maximum)`, for example `clamp(1.5rem, 4vw, 3rem)`.",
      r'''<style>
  h1 {
    font-size: clamp(1.5rem, 4vw, 3rem);
  }
</style>

<h1>Fluid heading</h1>'''))

add(C("ch-css-has-selector", "css", "advanced", "Style a parent with :has()", "css-has-is-where",
      "Use the `:has()` selector so that a `.card` gets a `tomato` border colour whenever it contains a checked checkbox. Unchecked cards keep the default border.",
      r'''<style>
  .card {
    border: 3px solid #c5d6f6;
    padding: 14px;
    border-radius: 8px;
    width: 220px;
  }
  /* add a :has() rule here */
</style>

<div class="card">
  <label><input type="checkbox"> Select this card</label>
</div>''',
      [T("The unchecked card keeps its original border colour", r'''(() => { const i = $('input'); i.checked = false; return css('.card', 'borderTopColor') === rgb('#c5d6f6'); })()'''),
       T("The checked card gets a tomato border", r'''(() => { const i = $('input'); i.checked = true; const ok = css('.card', 'borderTopColor') === rgb('tomato'); i.checked = false; return ok; })()'''),
       T("Unchecking restores the original border", r'''(() => { const i = $('input'); i.checked = true; i.checked = false; return css('.card', 'borderTopColor') === rgb('#c5d6f6'); })()'''),
       T("The stylesheet uses :has()", r'''[...document.styleSheets].some(s => [...s.cssRules].some(r => r.cssText.includes(':has(')))''')],
      "Write `.card:has(input:checked) { border-color: tomato; }`.",
      r'''<style>
  .card {
    border: 3px solid #c5d6f6;
    padding: 14px;
    border-radius: 8px;
    width: 220px;
  }
  .card:has(input:checked) {
    border-color: tomato;
  }
</style>

<div class="card">
  <label><input type="checkbox"> Select this card</label>
</div>'''))

# ===================================================================================== JavaScript
# ----------------------------------------------------------------- beginner
add(C("ch-js-variables", "js", "beginner", "Declare variables and print them", "js-variables",
      "Declare a constant `city` with the value `\"Chennai\"` and a variable `count` with the number `5`. Then print them on one line with `console.log(city, count)`.",
      r'''<script>
  // declare city and count here

  // print them here
</script>''',
      [T("city is a constant string \"Chennai\"", r'''typeof city === 'string' && city === 'Chennai' '''),
       T("count is the number 5", r'''typeof count === 'number' && count === 5'''),
       T("The console shows: Chennai 5", r'''logs.some(l => l.trim() === 'Chennai 5')''')],
      "Use `const city = \"Chennai\";` and `let count = 5;`.",
      r'''<script>
  const city = "Chennai";
  let count = 5;

  console.log(city, count);
</script>'''))

add(C("ch-js-function-add", "js", "beginner", "Write a function that adds numbers", "js-functions",
      "Finish the function `add(a, b)` so it returns the sum of its two arguments.",
      r'''<script>
  function add(a, b) {
    // return the sum here
  }
</script>''',
      [T("add is a function", r'''typeof add === 'function' '''),
       T("add(2, 3) returns 5", r'''typeof add === 'function' && add(2, 3) === 5'''),
       T("add(-1, 1) returns 0", r'''typeof add === 'function' && add(-1, 1) === 0'''),
       T("add(0.5, 0.25) returns 0.75", r'''typeof add === 'function' && add(0.5, 0.25) === 0.75''')],
      "A function hands back a value with the `return` keyword.",
      r'''<script>
  function add(a, b) {
    return a + b;
  }
</script>'''))

add(C("ch-js-grade", "js", "beginner", "Choose a grade with if / else", "js-if-else",
      "Write `grade(score)`: return `\"A\"` for 90 or more, `\"B\"` for 80 to 89, `\"C\"` for 70 to 79, and `\"F\"` for anything lower.",
      r'''<script>
  function grade(score) {
    // use if / else if / else
  }
</script>''',
      [T("grade(95) returns A", r'''typeof grade === 'function' && grade(95) === 'A' '''),
       T("grade(85) returns B", r'''typeof grade === 'function' && grade(85) === 'B' '''),
       T("grade(70) returns C", r'''typeof grade === 'function' && grade(70) === 'C' '''),
       T("grade(40) returns F", r'''typeof grade === 'function' && grade(40) === 'F' '''),
       T("The boundaries are right (90 is A, 89 is B, 79 is C)", r'''typeof grade === 'function' && grade(90) === 'A' && grade(89) === 'B' && grade(79) === 'C' ''')],
      "Check the highest score first: `if (score >= 90) return \"A\";` then `else if (score >= 80)` and so on.",
      r'''<script>
  function grade(score) {
    if (score >= 90) return "A";
    else if (score >= 80) return "B";
    else if (score >= 70) return "C";
    else return "F";
  }
</script>'''))

add(C("ch-js-loop-total", "js", "beginner", "Count with a loop", "js-loops",
      "Use a loop to print the numbers 1 to 5, each with its own `console.log`. After the loop print the total of those numbers as `Total: 15`.",
      r'''<script>
  let total = 0;
  // loop here

  // print the total here
</script>''',
      [T("The first five lines are 1, 2, 3, 4 and 5", r'''logs.slice(0, 5).join(',') === '1,2,3,4,5' '''),
       T("The sixth line is Total: 15", r'''logs[5] === 'Total: 15' '''),
       T("The total variable ends up as 15", r'''typeof total !== 'undefined' && total === 15''')],
      "Start the loop with `for (let i = 1; i <= 5; i++)` and add `i` to `total` each time.",
      r'''<script>
  let total = 0;
  for (let i = 1; i <= 5; i++) {
    console.log(i);
    total += i;
  }
  console.log("Total: " + total);
</script>'''))

add(C("ch-js-arrays", "js", "beginner", "Change an array", "js-arrays",
      "The array `fruits` already has `apple` and `banana`. Add `cherry` to the end, add `mango` to the start, then print the whole array as one line with `fruits.join(\", \")`.",
      r'''<script>
  const fruits = ["apple", "banana"];
  // add cherry to the end
  // add mango to the start
  // print the array joined with ", "
</script>''',
      [T("The array is mango, apple, banana, cherry", r'''JSON.stringify(fruits) === JSON.stringify(['mango', 'apple', 'banana', 'cherry'])'''),
       T("The array has 4 items", r'''fruits.length === 4'''),
       T("The console shows: mango, apple, banana, cherry", r'''logs.some(l => l.trim() === 'mango, apple, banana, cherry')''')],
      "`push` adds to the end and `unshift` adds to the start.",
      r'''<script>
  const fruits = ["apple", "banana"];
  fruits.push("cherry");
  fruits.unshift("mango");
  console.log(fruits.join(", "));
</script>'''))

# ----------------------------------------------------------------- intermediate
add(C("ch-js-click-counter", "js", "intermediate", "Build a click counter", "js-event-listener",
      "Make the button count clicks. Every time `#btn` is clicked, increase the number shown in `#count` by 1.",
      r'''<button id="btn">Click me</button>
<p>Clicks: <span id="count">0</span></p>

<script>
  // add your click handler here
</script>''',
      [T("One click adds 1 to the counter", r'''(() => { const b = Number(text('#count')); $('#btn').click(); return Number(text('#count')) === b + 1; })()'''),
       T("Two more clicks add 2", r'''(() => { const b = Number(text('#count')); $('#btn').click(); $('#btn').click(); return Number(text('#count')) === b + 2; })()'''),
       T("The counter shows a number", r'''!Number.isNaN(Number(text('#count'))) && text('#count') !== '' '''),
       T("The button and counter are still on the page", r'''!!$('#btn') && !!$('#count')''')],
      "Use `btn.addEventListener(\"click\", ...)` and keep the number in a variable.",
      r'''<button id="btn">Click me</button>
<p>Clicks: <span id="count">0</span></p>

<script>
  let clicks = 0;
  document.querySelector("#btn").addEventListener("click", () => {
    clicks++;
    document.querySelector("#count").textContent = clicks;
  });
</script>'''))

add(C("ch-js-render-list", "js", "intermediate", "Render an array into the page", "js-dom-elements",
      "Loop over the `items` array and add one `<li>` for each item to the `<ul id=\"list\">`, using `document.createElement` or `innerHTML`.",
      r'''<ul id="list"></ul>

<script>
  const items = ["HTML", "CSS", "JavaScript"];
  // build the list items here
</script>''',
      [T("The list has 3 items", r'''$$('#list li').length === 3'''),
       T("The items show HTML, CSS and JavaScript in order", r'''$$('#list li').map(li => li.textContent.trim()).join(',') === 'HTML,CSS,JavaScript' '''),
       T("The items are real <li> elements inside the <ul>", r'''$$('#list > li').length === 3''')],
      "`items.forEach(item => { ... })` runs once per item; `list.appendChild(li)` adds an element.",
      r'''<ul id="list"></ul>

<script>
  const items = ["HTML", "CSS", "JavaScript"];
  const list = document.querySelector("#list");
  items.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
</script>'''))

add(C("ch-js-even-squares", "js", "intermediate", "Filter and map an array", "js-array-iteration",
      "Write `evenSquares(nums)`. It should return a new array with the square of every even number in `nums`, using `filter` and `map`. For example `evenSquares([1, 2, 3, 4])` returns `[4, 16]`.",
      r'''<script>
  function evenSquares(nums) {
    // filter the even numbers, then map each to its square
  }
</script>''',
      [T("evenSquares([1, 2, 3, 4]) returns [4, 16]", r'''typeof evenSquares === 'function' && JSON.stringify(evenSquares([1, 2, 3, 4])) === '[4,16]' '''),
       T("An empty array returns an empty array", r'''typeof evenSquares === 'function' && JSON.stringify(evenSquares([])) === '[]' '''),
       T("No even numbers returns an empty array", r'''typeof evenSquares === 'function' && JSON.stringify(evenSquares([5, 7])) === '[]' '''),
       T("It does not change the original array", r'''(() => { if (typeof evenSquares !== 'function') return false; const a = [2, 3, 6]; evenSquares(a); return JSON.stringify(a) === '[2,3,6]'; })()'''),
       T("evenSquares([6, 8]) returns [36, 64]", r'''typeof evenSquares === 'function' && JSON.stringify(evenSquares([6, 8])) === '[36,64]' ''')],
      "`nums.filter(n => n % 2 === 0).map(n => n * n)`.",
      r'''<script>
  function evenSquares(nums) {
    return nums.filter(n => n % 2 === 0).map(n => n * n);
  }
</script>'''))

add(C("ch-js-describe-person", "js", "intermediate", "Work with objects and template literals", "js-template-literals",
      "Finish `describe(person)` so it returns a sentence built with a template literal, such as `Asha is 21 years old and lives in Pune`. The `person` object is already defined for you.",
      r'''<script>
  const person = { name: "Asha", age: 21, city: "Pune" };

  function describe(p) {
    // return the sentence here
  }
</script>''',
      [T("describe(person) returns the correct sentence", r'''typeof describe === 'function' && describe(person) === 'Asha is 21 years old and lives in Pune' '''),
       T("It works for any object", r'''typeof describe === 'function' && describe({ name: 'Ravi', age: 30, city: 'Delhi' }) === 'Ravi is 30 years old and lives in Delhi' '''),
       T("The person object is unchanged", r'''person.name === 'Asha' && person.age === 21 && person.city === 'Pune' ''')],
      "Use backticks: `${p.name} is ${p.age} years old ...`.",
      r'''<script>
  const person = { name: "Asha", age: 21, city: "Pune" };

  function describe(p) {
    return `${p.name} is ${p.age} years old and lives in ${p.city}`;
  }
</script>'''))

add(C("ch-js-greeting", "js", "intermediate", "Read an input and update the page", "js-dom-forms",
      "When `#greet` is clicked, read the value of `#name`, trim extra spaces, and show `Hello, <name>!` inside `#out`. If the box is empty, show `Hello, stranger!`.",
      r'''<input id="name" placeholder="Your name">
<button id="greet">Greet</button>
<p id="out"></p>

<script>
  // write your click handler here
</script>''',
      [T("A name produces Hello, Ravi!", r'''(() => { $('#name').value = 'Ravi'; $('#greet').click(); return text('#out') === 'Hello, Ravi!'; })()'''),
       T("Extra spaces are trimmed", r'''(() => { $('#name').value = '  Asha  '; $('#greet').click(); return text('#out') === 'Hello, Asha!'; })()'''),
       T("An empty box produces Hello, stranger!", r'''(() => { $('#name').value = ''; $('#greet').click(); return text('#out') === 'Hello, stranger!'; })()'''),
       T("A box with only spaces also says stranger", r'''(() => { $('#name').value = '   '; $('#greet').click(); return text('#out') === 'Hello, stranger!'; })()''')],
      "`input.value.trim()` removes spaces; `out.textContent = ...` changes the text.",
      r'''<input id="name" placeholder="Your name">
<button id="greet">Greet</button>
<p id="out"></p>

<script>
  document.querySelector("#greet").addEventListener("click", () => {
    const name = document.querySelector("#name").value.trim();
    document.querySelector("#out").textContent = name ? `Hello, ${name}!` : "Hello, stranger!";
  });
</script>'''))

# ----------------------------------------------------------------- advanced
add(C("ch-js-closure-counter", "js", "advanced", "Create a private counter with a closure", "js-closures",
      "Write `makeCounter()`. It returns a function that adds 1 to a private count each time it is called and returns the new count. Two counters must not share their counts.",
      r'''<script>
  function makeCounter() {
    // keep a private variable and return a function
  }
</script>''',
      [T("The first call returns 1, then 2", r'''(() => { if (typeof makeCounter !== 'function') return false; const c = makeCounter(); return typeof c === 'function' && c() === 1 && c() === 2; })()'''),
       T("Two counters are independent", r'''(() => { if (typeof makeCounter !== 'function') return false; const a = makeCounter(), b = makeCounter(); return a() === 1 && a() === 2 && b() === 1 && a() === 3; })()'''),
       T("The count is not exposed as a global variable", r'''typeof window.count === 'undefined' && typeof window.counter === 'undefined' ''')],
      "Declare `let count = 0;` inside `makeCounter` and return `() => ++count`.",
      r'''<script>
  function makeCounter() {
    let count = 0;
    return function () {
      count++;
      return count;
    };
  }
</script>'''))

add(C("ch-js-promise-delay", "js", "advanced", "Return a promise that resolves after a delay", "js-promises",
      "Write `delay(ms, value)`. It must return a Promise that resolves with `value` after `ms` milliseconds.",
      r'''<script>
  function delay(ms, value) {
    // return a new Promise that uses setTimeout
  }
</script>''',
      [T("delay returns a Promise", r'''typeof delay === 'function' && delay(1, 'x') instanceof Promise'''),
       T("It resolves with the given value", r'''typeof delay === 'function' && delay(10, 'hello').then(v => v === 'hello')'''),
       T("It waits at least the requested time", r'''(async () => { if (typeof delay !== 'function') return false; const t = Date.now(); const v = await delay(60, 'ok'); return v === 'ok' && Date.now() - t >= 55; })()'''),
       T("It does not wait much longer than requested", r'''(async () => { if (typeof delay !== 'function') return false; const t = Date.now(); await delay(30, 1); return Date.now() - t < 200; })()''')],
      "`return new Promise(resolve => setTimeout(() => resolve(value), ms));`",
      r'''<script>
  function delay(ms, value) {
    return new Promise(resolve => setTimeout(() => resolve(value), ms));
  }
</script>'''))

add(C("ch-js-async-total", "js", "advanced", "Run async work in parallel", "js-async-await",
      "`fakePrice(id)` takes 100 ms and resolves with a price. Write the async function `getTotal()` that fetches the prices for ids 1 and 2 at the same time with `Promise.all` and resolves with their sum. It should finish in about 100 ms, not 200 ms.",
      r'''<script>
  const prices = { 1: 10, 2: 20 };
  function fakePrice(id) {
    return new Promise(resolve => setTimeout(() => resolve(prices[id]), 100));
  }

  async function getTotal() {
    // fetch both prices in parallel and return the sum
  }
</script>''',
      [T("getTotal returns a Promise", r'''typeof getTotal === 'function' && getTotal() instanceof Promise'''),
       T("It resolves with the total 30", r'''typeof getTotal === 'function' && getTotal().then(v => v === 30)'''),
       T("It runs the requests in parallel (faster than 170 ms)", r'''(async () => { if (typeof getTotal !== 'function') return false; const t = Date.now(); const v = await getTotal(); return v === 30 && Date.now() - t < 170; })()''')],
      "Start both calls before waiting: `const [a, b] = await Promise.all([fakePrice(1), fakePrice(2)]);`",
      r'''<script>
  const prices = { 1: 10, 2: 20 };
  function fakePrice(id) {
    return new Promise(resolve => setTimeout(() => resolve(prices[id]), 100));
  }

  async function getTotal() {
    const [a, b] = await Promise.all([fakePrice(1), fakePrice(2)]);
    return a + b;
  }
</script>'''))

add(C("ch-js-classes", "js", "advanced", "Model shapes with classes and inheritance", "js-inheritance",
      "Finish the `Rectangle` class: a constructor taking `width` and `height`, a getter `area`, and a method `perimeter()`. Then write `Square`, which extends `Rectangle` and takes a single side length.",
      r'''<script>
  class Rectangle {
    // constructor, get area, perimeter()
  }

  // class Square extends Rectangle
</script>''',
      [T("Rectangle(3, 4) has area 12", r'''typeof Rectangle === 'function' && new Rectangle(3, 4).area === 12'''),
       T("Rectangle(3, 4) has perimeter 14", r'''typeof Rectangle === 'function' && new Rectangle(3, 4).perimeter() === 14'''),
       T("Square(5) has area 25", r'''typeof Square === 'function' && new Square(5).area === 25'''),
       T("Square(5) has perimeter 20", r'''typeof Square === 'function' && new Square(5).perimeter() === 20'''),
       T("A Square is a Rectangle", r'''typeof Square === 'function' && new Square(2) instanceof Rectangle''')],
      "In `Square`, call `super(side, side)` inside the constructor.",
      r'''<script>
  class Rectangle {
    constructor(width, height) {
      this.width = width;
      this.height = height;
    }
    get area() {
      return this.width * this.height;
    }
    perimeter() {
      return 2 * (this.width + this.height);
    }
  }

  class Square extends Rectangle {
    constructor(side) {
      super(side, side);
    }
  }
</script>'''))

add(C("ch-js-spread-destructuring", "js", "advanced", "Use spread and destructuring", "js-destructuring",
      "Write three small functions. `mergeSettings(defaults, overrides)` returns a new object where `overrides` win and neither input changes. `swapPair([a, b])` returns `[b, a]` using destructuring. `splitFirst(list)` returns `{ first, rest }` using a rest element.",
      r'''<script>
  function mergeSettings(defaults, overrides) {
    // use the spread operator
  }

  function swapPair(pair) {
    // use array destructuring
  }

  function splitFirst(list) {
    // use [first, ...rest]
  }
</script>''',
      [T("mergeSettings lets overrides win", r'''typeof mergeSettings === 'function' && JSON.stringify(mergeSettings({ a: 1, b: 2 }, { b: 3, c: 4 })) === JSON.stringify({ a: 1, b: 3, c: 4 })'''),
       T("mergeSettings does not change its inputs", r'''(() => { if (typeof mergeSettings !== 'function') return false; const d = { a: 1 }, o = { b: 2 }; const r = mergeSettings(d, o); return r !== d && JSON.stringify(d) === '{"a":1}' && JSON.stringify(o) === '{"b":2}'; })()'''),
       T("swapPair([1, 2]) returns [2, 1]", r'''typeof swapPair === 'function' && JSON.stringify(swapPair([1, 2])) === '[2,1]' '''),
       T("splitFirst([1, 2, 3]) returns first 1 and rest [2, 3]", r'''typeof splitFirst === 'function' && JSON.stringify(splitFirst([1, 2, 3])) === JSON.stringify({ first: 1, rest: [2, 3] })'''),
       T("splitFirst of one item has an empty rest", r'''typeof splitFirst === 'function' && JSON.stringify(splitFirst([9])) === JSON.stringify({ first: 9, rest: [] })''')],
      "`{ ...defaults, ...overrides }` merges objects; `const [a, ...rest] = list;` splits arrays.",
      r'''<script>
  function mergeSettings(defaults, overrides) {
    return { ...defaults, ...overrides };
  }

  function swapPair(pair) {
    const [a, b] = pair;
    return [b, a];
  }

  function splitFirst(list) {
    const [first, ...rest] = list;
    return { first, rest };
  }
</script>'''))
