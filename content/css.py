"""CSS module lessons for TechHub. Same schema as the HTML lessons:
slug, title, group, intro, sections[{h, p, code?}], example, tip (optional), exercise[{q, options, answer}].
"""

GROUPS = ["Getting Started", "Colors & Backgrounds", "Box Model", "Text & Fonts", "Layout",
          "Components", "Selectors", "Effects & Animation", "Responsive Design", "Advanced"]


def L(slug, title, group, intro, sections, example, tip=None, exercise=()):
    d = dict(slug=slug, title=title, group=group, intro=intro,
             sections=[dict(h=s[0], p=s[1], **({"code": s[2]} if len(s) > 2 else {})) for s in sections],
             example=example)
    if tip:
        d["tip"] = tip
    d["exercise"] = [dict(q=q, options=o, answer=a) for q, o, a in exercise]
    return d


LESSONS = [
# ============================================================ Getting Started
L("css-intro", "CSS Introduction", "Getting Started",
  "CSS controls how HTML looks: colours, spacing, fonts and layout. This chapter explains what it is and why it matters.",
  [("What is CSS?", "CSS stands for Cascading Style Sheets. HTML gives a page its structure, and CSS describes how that structure is presented on screen, on paper or on a phone."),
   ("Why use CSS?", "One stylesheet can restyle a whole website. You change a rule once and every page that uses it updates, which saves time and keeps the design consistent."),
   ("Before and after", "The same HTML can look plain or polished depending on the CSS applied to it.",
    "<style>\n  h1 { color: royalblue; }\n  p  { font-family: sans-serif; }\n</style>\n<h1>Styled heading</h1>\n<p>Styled paragraph.</p>")],
  '''<style>
  body { font-family: sans-serif; padding: 16px; }
  h1 { color: #1d5bd8; border-bottom: 3px solid #1d5bd8; padding-bottom: 6px; }
  p { background: #eaf2ff; padding: 10px; border-radius: 8px; }
</style>
<h1>My styled page</h1>
<p>This paragraph is styled with CSS. Delete the style block to see the plain HTML.</p>''',
  "Delete everything inside the `<style>` block and run again to see how plain HTML looks without CSS.",
  [("What does CSS stand for?", ["Cascading Style Sheets", "Creative Style System", "Computer Style Syntax", "Colourful Style Sheets"], 0),
   ("What is the main job of CSS?", ["Describe how HTML is presented", "Store data in a database", "Run server code", "Define the page structure"], 0)]),

L("css-syntax", "CSS Syntax", "Getting Started",
  "A CSS rule has a selector and a block of declarations. Once you can read one rule, you can read any stylesheet.",
  [("Anatomy of a rule", "The selector says which elements to style. Inside curly braces, each declaration is a `property: value;` pair ending with a semicolon.",
    "<style>\n  p {\n    color: red;\n    text-align: center;\n  }\n</style>"),
   ("Multiple selectors", "Separate selectors with commas to apply the same declarations to all of them.",
    "<style>\n  h1, h2, h3 { color: navy; }\n</style>"),
   ("Spaces and case", "Whitespace and line breaks are ignored, so format rules for readability. Property names and keywords are case-insensitive, but lowercase is the convention.")],
  '''<style>
  h1, h2 { color: #0e2a5c; text-align: center; }
  p { color: #1d5bd8; font-size: 20px; text-align: center; }
</style>
<h1>Heading one</h1>
<h2>Heading two</h2>
<p>One rule set for two headings, another for the paragraph.</p>''',
  "Forgetting a semicolon between declarations is the most common beginner mistake.",
  [("Which part of a rule chooses the elements to style?", ["The selector", "The value", "The semicolon", "The comment"], 0),
   ("How does each declaration end?", ["With a semicolon", "With a period", "With a colon", "With a slash"], 0),
   ("How do you apply one rule to h1 and h2 together?", ["Separate the selectors with a comma", "Join them with a plus sign", "Write them on one line without spaces", "Use two curly braces"], 0)]),

L("css-how-to-add", "CSS How To Add", "Getting Started",
  "There are three ways to add CSS to a page: inline, internal and external. Real sites use external stylesheets.",
  [("External CSS", "Put rules in a separate `.css` file and link it from the `<head>`. One file can style many pages, so this is the recommended way.",
    '<link rel="stylesheet" href="styles.css">'),
   ("Internal CSS", "Place rules inside a `<style>` element in the head. Good for a single page or a quick demo.",
    "<head>\n  <style>\n    body { background: #eaf2ff; }\n  </style>\n</head>"),
   ("Inline CSS", "Add a `style` attribute to one element. It affects only that element and is hard to maintain, so use it sparingly.",
    '<p style="color: blue;">Blue text</p>')],
  '''<style>
  p { color: seagreen; }
</style>
<p>Styled by the internal style block (green).</p>
<p style="color: crimson;">Inline style wins here (red).</p>''',
  "When two rules conflict, an inline style beats an internal or external one with the same specificity.",
  [("Which element links an external stylesheet?", ["<link>", "<style>", "<script>", "<css>"], 0),
   ("Which method styles only a single element through an attribute?", ["Inline CSS", "External CSS", "Internal CSS", "Imported CSS"], 0),
   ("Why are external stylesheets recommended?", ["One file can style many pages", "They run faster than JavaScript", "They need no HTML", "They cannot be cached"], 0)]),

L("css-comments", "CSS Comments", "Getting Started",
  "Comments are notes for people. The browser ignores them, so use them to explain or to switch rules off.",
  [("Writing a comment", "A CSS comment starts with `/*` and ends with `*/`. It can span several lines.",
    "<style>\n  /* Main heading colour */\n  h1 { color: navy; }\n</style>"),
   ("Disabling code", "Wrap a declaration in a comment to test the page without deleting it.",
    "<style>\n  p {\n    color: red;\n    /* font-size: 30px; */\n  }\n</style>"),
   ("Not like HTML comments", "CSS does not use `<!-- -->` and does not support `//` comments. Use `/* */` only.")],
  '''<style>
  /* This comment is ignored */
  p { color: #1d5bd8; }
  /* p { color: red; }  <- remove the comment marks to switch this rule on */
</style>
<p>The paragraph is blue because the red rule is commented out.</p>''',
  None,
  [("Which is the correct CSS comment?", ["/* comment */", "// comment", "<!-- comment -->", "# comment"], 0),
   ("What happens to a commented-out declaration?", ["The browser ignores it", "It runs twice", "It causes an error", "It is applied to children only"], 0)]),

L("css-selectors-basic", "CSS Selectors", "Getting Started",
  "Selectors pick which elements a rule applies to. The four basic kinds are element, class, id and universal.",
  [("Element selector", "Match every element with that tag name.", "<style>\n  p { color: navy; }\n</style>"),
   ("Class selector", "A dot followed by a class name matches every element with that class. A class can be reused anywhere.",
    '<style>\n  .note { background: #eaf2ff; }\n</style>\n<p class="note">Hello</p>'),
   ("ID selector", "A hash followed by an id matches the one element with that id. An id must be unique in a page.",
    '<style>\n  #title { color: crimson; }\n</style>\n<h1 id="title">Hi</h1>'),
   ("Universal and grouping", "`*` matches everything. Commas group selectors: `h1, h2, p`.")],
  '''<style>
  * { font-family: sans-serif; }
  p { color: #0e2a5c; }
  .note { background: #eaf2ff; padding: 8px; border-left: 4px solid #1d5bd8; }
  #title { color: #1d5bd8; }
</style>
<h1 id="title">Selectors</h1>
<p>Plain paragraph (element selector).</p>
<p class="note">Paragraph with a class.</p>''',
  "Prefer classes for styling. Ids are best kept for links and scripting.",
  [("Which symbol starts a class selector?", [". (dot)", "# (hash)", "* (star)", "& (ampersand)"], 0),
   ("Which symbol starts an id selector?", ["# (hash)", ". (dot)", "@ (at)", "~ (tilde)"], 0),
   ("What does the `*` selector match?", ["Every element", "Only headings", "Only the body", "Elements with a class"], 0)]),

# ============================================================ Colors & Backgrounds
L("css-colors", "CSS Colors", "Colors & Backgrounds",
  "CSS can describe colour in several ways. Names, HEX, RGB and HSL all do the same job, so pick the one you find clearest.",
  [("Colour names", "There are 140 named colours such as `tomato`, `royalblue` and `seagreen`."),
   ("HEX", "A hash followed by six hexadecimal digits for red, green and blue: `#1d5bd8`. A short form like `#fff` means `#ffffff`."),
   ("RGB and RGBA", "`rgb(29, 91, 216)` mixes red, green and blue from 0 to 255. Add a fourth value for transparency: `rgba(29, 91, 216, 0.5)`."),
   ("HSL", "`hsl(220, 76%, 48%)` sets hue (0-360), saturation and lightness. It makes it easy to create lighter or darker shades of one colour.")],
  '''<style>
  .box { display: inline-block; width: 90px; height: 70px; margin: 4px; color: #fff; font: 13px sans-serif; padding: 6px; border-radius: 8px; }
</style>
<div class="box" style="background: tomato;">name</div>
<div class="box" style="background: #1d5bd8;">HEX</div>
<div class="box" style="background: rgb(14, 122, 79);">RGB</div>
<div class="box" style="background: rgba(29, 91, 216, 0.5);">RGBA</div>
<div class="box" style="background: hsl(280, 60%, 45%);">HSL</div>''',
  "Use `color` for text and `background-color` for the area behind it.",
  [("Which value is a valid HEX colour?", ["#1d5bd8", "1d5bd8#", "hex(1d5bd8)", "#1d5bd8g"], 0),
   ("What does the fourth number in `rgba()` control?", ["Opacity (alpha)", "Brightness", "Saturation", "Hue"], 0),
   ("Which property sets the colour of text?", ["color", "text-color", "font-color", "foreground"], 0)]),

L("css-backgrounds", "CSS Backgrounds", "Colors & Backgrounds",
  "Background properties fill an element with a colour or image, and control how the image repeats and where it sits.",
  [("Background colour", "`background-color` fills the padding and content area, and extends under the border."),
   ("Background image", "`background-image: url(...)` adds an image. It repeats in both directions by default; `background-repeat: no-repeat` stops that."),
   ("Position and size", "`background-position` places the image and `background-size: cover` scales it to fill the box, cropping if needed."),
   ("Shorthand", "`background` combines the properties in one declaration.",
    "<style>\n  .hero {\n    background: #eaf2ff url(photo.jpg) no-repeat center / cover;\n  }\n</style>")],
  '''<style>
  .bg {
    height: 160px; border-radius: 12px; color: #fff; font: 700 22px sans-serif; padding: 16px;
    background-color: #1d5bd8;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24'><circle cx='12' cy='12' r='4' fill='white' fill-opacity='0.35'/></svg>");
    background-repeat: repeat;
  }
</style>
<div class="bg">Repeating dot pattern</div>''',
  "Always set a `background-color` as a fallback in case the image fails to load.",
  [("Which value stops a background image from repeating?", ["no-repeat", "repeat-none", "once", "single"], 0),
   ("What does `background-size: cover` do?", ["Scales the image to fill the box", "Hides the background", "Repeats it twice", "Shrinks it to fit inside"], 0)]),

L("css-gradients", "CSS Gradients", "Colors & Backgrounds",
  "Gradients blend two or more colours smoothly. They are images created by the browser, so they need no files.",
  [("Linear gradient", "`linear-gradient()` blends along a line. Give an angle or a direction, then the colour stops.",
    "<style>\n  .a { background: linear-gradient(to right, #1d5bd8, #7fb0ff); }\n</style>"),
   ("Radial gradient", "`radial-gradient()` spreads out from a centre point in a circle or ellipse."),
   ("Conic gradient", "`conic-gradient()` sweeps colours around a centre, like a colour wheel or pie chart."),
   ("Colour stops", "Add positions to control where each colour starts: `linear-gradient(#1d5bd8 0%, #fff 60%)`.")],
  '''<style>
  .g { height: 70px; margin: 8px 0; border-radius: 10px; }
  .g1 { background: linear-gradient(to right, #1d5bd8, #9cc3ff); }
  .g2 { background: linear-gradient(135deg, #0e2a5c 0%, #1d5bd8 55%, #eaf2ff 100%); }
  .g3 { background: radial-gradient(circle, #ffffff, #1d5bd8); }
  .pie { width: 90px; height: 90px; border-radius: 50%; background: conic-gradient(#1d5bd8 0 40%, #9cc3ff 0 70%, #0e2a5c 0); }
</style>
<div class="g g1"></div><div class="g g2"></div><div class="g g3"></div><div class="pie"></div>''',
  "Gradients go in `background` or `background-image`, never in `background-color`.",
  [("Which function blends colours along a straight line?", ["linear-gradient()", "radial-gradient()", "conic-gradient()", "line-blend()"], 0),
   ("Which gradient sweeps colours around a centre point?", ["conic-gradient()", "linear-gradient()", "radial-gradient()", "circle-gradient()"], 0),
   ("Where can a gradient be used?", ["background-image", "background-color", "font-color", "border-width"], 0)]),

L("css-opacity", "CSS Opacity", "Colors & Backgrounds",
  "Opacity controls how see-through an element is. It ranges from 0 (invisible) to 1 (fully solid).",
  [("The opacity property", "`opacity: 0.5` makes the element and everything inside it half transparent."),
   ("Opacity affects children", "Text and child elements inherit the transparency. To fade only the background, use `rgba()` or `hsla()` colour instead.",
    "<style>\n  .faded { opacity: 0.4; }          /* whole element */\n  .glass { background: rgba(255,255,255,.4); } /* only the background */\n</style>"),
   ("Hover effects", "Opacity is popular for hover states: `img:hover { opacity: 0.8; }`.")],
  '''<style>
  .row { background: #1d5bd8; padding: 12px; border-radius: 10px; }
  .row div { display: inline-block; width: 100px; padding: 18px 0; margin: 4px; text-align: center; background: #fff; color: #0e2a5c; font: 14px sans-serif; border-radius: 8px; }
</style>
<div class="row">
  <div style="opacity: 1;">1</div>
  <div style="opacity: 0.7;">0.7</div>
  <div style="opacity: 0.4;">0.4</div>
  <div style="opacity: 0.15;">0.15</div>
</div>''',
  None,
  [("What opacity value makes an element fully transparent?", ["0", "1", "100", "-1"], 0),
   ("What does `opacity` affect?", ["The element and its children", "Only the background", "Only the border", "Only the text"], 0),
   ("How can you make only the background see-through?", ["Use an rgba() background colour", "Set opacity on the body", "Use visibility: hidden", "Use display: none"], 0)]),

# ============================================================ Box Model
L("css-borders", "CSS Borders", "Box Model",
  "Borders draw a line around an element. You control the width, style and colour, on all sides or on each side.",
  [("Border shorthand", "`border: 2px solid #1d5bd8` sets width, style and colour together. The style is required or no border appears."),
   ("Border styles", "Common styles are `solid`, `dashed`, `dotted`, `double` and `none`."),
   ("Single sides", "Use `border-top`, `border-right`, `border-bottom` and `border-left`, for example `border-bottom: 3px solid navy`.",
    "<style>\n  h2 { border-bottom: 3px solid #1d5bd8; }\n</style>")],
  '''<style>
  div { margin: 8px 0; padding: 10px; font: 15px sans-serif; }
</style>
<div style="border: 2px solid #1d5bd8;">solid</div>
<div style="border: 3px dashed #0e7a4f;">dashed</div>
<div style="border: 3px dotted tomato;">dotted</div>
<div style="border: 6px double #0e2a5c;">double</div>
<div style="border-left: 8px solid #1d5bd8; background: #eaf2ff;">left border only</div>''',
  "If you set a border width and colour but forget the style, nothing is drawn because the default style is `none`.",
  [("Which border property value is required to make a border visible?", ["A border style such as solid", "A border radius", "A margin", "A background"], 0),
   ("Which declaration draws a line only under an element?", ["border-bottom: 2px solid", "border: bottom", "underline: 2px", "line-bottom: solid"], 0)]),

L("css-border-radius", "CSS Border Radius", "Box Model",
  "`border-radius` rounds the corners of an element. Large values turn boxes into pills and circles.",
  [("Rounded corners", "`border-radius: 12px` rounds all four corners equally."),
   ("Different corners", "Give up to four values, clockwise from the top-left: `border-radius: 20px 0 20px 0`."),
   ("Circles and pills", "A square with `border-radius: 50%` becomes a circle. A very large radius such as `999px` turns a wide box into a pill shape.")],
  '''<style>
  .s { display: inline-block; width: 90px; height: 90px; margin: 6px; background: #1d5bd8; color: #fff; font: 13px sans-serif; text-align: center; line-height: 90px; }
</style>
<div class="s" style="border-radius: 12px;">12px</div>
<div class="s" style="border-radius: 50%;">50%</div>
<div class="s" style="border-radius: 30px 0 30px 0;">mixed</div>
<div class="s" style="width: 160px; height: 44px; line-height: 44px; border-radius: 999px;">pill</div>''',
  None,
  [("What does `border-radius: 50%` do to a square?", ["Makes it a circle", "Makes it half as wide", "Adds a 50px border", "Hides the corners"], 0),
   ("In what order do four border-radius values apply?", ["Top-left, top-right, bottom-right, bottom-left", "Top, bottom, left, right", "Left, right, top, bottom", "Bottom-left first, then counter-clockwise"], 0)]),

L("css-margins", "CSS Margins", "Box Model",
  "Margins create space outside an element. They push other elements away and never have a background colour.",
  [("Margin properties", "Use `margin-top`, `margin-right`, `margin-bottom` and `margin-left`, or the `margin` shorthand."),
   ("Shorthand values", "One value sets all sides. Two values set top/bottom then left/right. Four values go top, right, bottom, left (clockwise).",
    "<style>\n  .a { margin: 20px; }\n  .b { margin: 10px 40px; }\n  .c { margin: 5px 10px 15px 20px; }\n</style>"),
   ("Centering with auto", "A block element with a set width and `margin: 0 auto` is centred horizontally."),
   ("Margin collapse", "Vertical margins of neighbouring blocks merge into one: the larger of the two wins, not the sum.")],
  '''<style>
  .wrap { background: #eaf2ff; padding: 6px; }
  .box { width: 200px; padding: 10px; background: #1d5bd8; color: #fff; font: 15px sans-serif; text-align: center; }
</style>
<div class="wrap">
  <div class="box" style="margin: 0 auto 20px;">centred, margin-bottom 20px</div>
  <div class="box" style="margin: 0 0 0 40px;">margin-left 40px</div>
</div>''',
  "Negative margins are allowed and pull an element towards its neighbour.",
  [("What does `margin: 0 auto` do to a block with a fixed width?", ["Centres it horizontally", "Removes its border", "Makes it full width", "Hides it"], 0),
   ("Margin shorthand with four values follows which order?", ["Top, right, bottom, left", "Left, right, top, bottom", "Top, bottom, left, right", "Right, top, left, bottom"], 0),
   ("Where is margin space located?", ["Outside the border", "Inside the border", "Inside the content", "Between content and padding"], 0)]),

L("css-padding", "CSS Padding", "Box Model",
  "Padding is the space between an element's content and its border. The background colour fills it.",
  [("Padding properties", "Use `padding-top`, `padding-right`, `padding-bottom`, `padding-left` or the `padding` shorthand. It follows the same value order as margin."),
   ("Padding vs margin", "Padding is inside the border and shows the background. Margin is outside the border and is always transparent."),
   ("Padding changes size", "By default, padding is added to the width and height. The `box-sizing` lesson shows how to avoid surprises.")],
  '''<style>
  .p { background: #1d5bd8; color: #fff; font: 15px sans-serif; display: inline-block; margin: 6px; }
</style>
<div class="p" style="padding: 4px;">padding 4px</div>
<div class="p" style="padding: 20px;">padding 20px</div>
<div class="p" style="padding: 8px 32px;">8px 32px</div>''',
  None,
  [("Where is padding located?", ["Between the content and the border", "Outside the border", "Between two siblings", "Inside the margin"], 0),
   ("Does padding show the element's background colour?", ["Yes", "No", "Only with opacity", "Only on inline elements"], 0)]),

L("css-height-width", "CSS Height and Width", "Box Model",
  "`width` and `height` set the size of an element's content box. Use `max-width` to keep layouts flexible.",
  [("Setting a size", "Values can be fixed (`300px`) or relative (`50%`, `100vw`). Block elements fill the available width by default, and height follows the content."),
   ("max-width and min-width", "`max-width` stops an element growing past a limit but lets it shrink on small screens. `min-width` sets a lower limit."),
   ("Responsive image", "`max-width: 100%; height: auto` keeps an image inside its container.",
    "<style>\n  img { max-width: 100%; height: auto; }\n</style>")],
  '''<style>
  .a { width: 300px; background: #1d5bd8; color: #fff; padding: 8px; font: 14px sans-serif; margin-bottom: 8px; }
  .b { max-width: 300px; background: #0e7a4f; color: #fff; padding: 8px; font: 14px sans-serif; }
</style>
<div class="a">width: 300px (never shrinks)</div>
<div class="b">max-width: 300px (shrinks on a narrow screen)</div>''',
  "Prefer `max-width` over `width` for containers so they never cause sideways scrolling on phones.",
  [("Which property lets an element shrink on small screens but never grow past a limit?", ["max-width", "min-width", "fixed-width", "limit-width"], 0),
   ("What does `height: auto` do?", ["Lets the height follow the content", "Sets height to zero", "Makes it full screen", "Locks the aspect ratio to 1"], 0)]),

L("css-box-model", "CSS Box Model", "Box Model",
  "Every element is a rectangular box made of four layers. Understanding them explains most spacing problems.",
  [("The four layers", "From inside to outside: content, padding, border and margin."),
   ("Total size", "With the default `content-box` sizing, total width = width + left and right padding + left and right border. Margin adds space around that.",
    "<style>\n  div {\n    width: 300px;\n    padding: 20px;\n    border: 5px solid navy;\n    margin: 10px;\n  }\n  /* total width = 300 + 40 + 10 = 350px */\n</style>"),
   ("Inspecting boxes", "Browser developer tools (F12) show a diagram of the box model for any selected element, which is the fastest way to debug spacing.")],
  '''<style>
  .m { background: #fde8c8; padding: 14px; display: inline-block; font: 12px sans-serif; }
  .b { background: #ffd479; padding: 8px; border: 6px solid #0e2a5c; }
  .p { background: #9bd0ff; padding: 18px; }
  .c { background: #1d5bd8; color: #fff; padding: 14px 22px; }
</style>
<div class="m">margin
  <div class="b">border
    <div class="p">padding
      <div class="c">content</div>
    </div>
  </div>
</div>''',
  None,
  [("Which is the correct order of box layers from inside to outside?", ["Content, padding, border, margin", "Content, margin, border, padding", "Padding, content, margin, border", "Border, padding, content, margin"], 0),
   ("With content-box sizing, a 300px wide box with 20px padding each side and no border is how wide in total?", ["340px", "300px", "320px", "360px"], 0)]),

L("css-box-sizing", "CSS Box Sizing", "Box Model",
  "`box-sizing` decides whether padding and border are counted inside the width you set. Nearly every modern project sets it to `border-box`.",
  [("content-box vs border-box", "`content-box` (default) adds padding and border to the width. `border-box` includes them, so a 300px box stays 300px."),
   ("The usual reset", "Apply `border-box` to every element with one rule. Layout maths becomes much simpler.",
    "<style>\n  *, *::before, *::after {\n    box-sizing: border-box;\n  }\n</style>")],
  '''<style>
  .t { width: 200px; padding: 20px; border: 5px solid #0e2a5c; background: #eaf2ff; margin-bottom: 8px; font: 14px sans-serif; }
  .bb { box-sizing: border-box; }
</style>
<div class="t">content-box: 250px wide</div>
<div class="t bb">border-box: 200px wide</div>''',
  None,
  [("Which `box-sizing` value includes padding and border in the declared width?", ["border-box", "content-box", "padding-box", "total-box"], 0),
   ("What is the default value of `box-sizing`?", ["content-box", "border-box", "inherit", "none"], 0)]),

L("css-outline", "CSS Outline", "Box Model",
  "An outline is a line drawn outside the border. Unlike a border, it takes up no space and does not change layout.",
  [("Outline properties", "`outline: 3px dashed #1d5bd8` works like a border shorthand. `outline-offset` moves it away from the edge."),
   ("Focus rings", "Browsers use outlines to show keyboard focus. Never remove them without providing a clear replacement, because keyboard users rely on them.",
    "<style>\n  button:focus-visible {\n    outline: 3px solid #1d5bd8;\n    outline-offset: 3px;\n  }\n</style>")],
  '''<style>
  .o { margin: 20px; padding: 14px; background: #eaf2ff; font: 15px sans-serif; }
</style>
<div class="o" style="outline: 3px solid #1d5bd8;">solid outline</div>
<div class="o" style="outline: 3px dashed #0e7a4f; outline-offset: 8px;">dashed, offset 8px</div>''',
  None,
  [("How does an outline differ from a border?", ["It takes up no space in the layout", "It is always rounded", "It can only be black", "It sits inside the padding"], 0),
   ("Why should focus outlines not be removed carelessly?", ["Keyboard users need to see where they are", "They slow the page down", "They break the box model", "Browsers ignore them anyway"], 0)]),

L("css-box-shadow", "CSS Box Shadow", "Box Model",
  "`box-shadow` adds depth by drawing a soft shadow around an element. It is the key to cards and raised buttons.",
  [("Syntax", "`box-shadow: x-offset y-offset blur spread colour`. The first two values are required.",
    "<style>\n  .card { box-shadow: 0 6px 18px rgba(14, 42, 92, .25); }\n</style>"),
   ("Inset and multiple shadows", "Add `inset` to draw the shadow inside. Separate several shadows with commas to build richer effects."),
   ("Keep it subtle", "Soft, low-opacity shadows look professional. Very dark, sharp shadows look dated.")],
  '''<style>
  body { background: #eaf2ff; padding: 16px; font: 15px sans-serif; }
  .c { display: inline-block; width: 120px; padding: 20px; margin: 10px; background: #fff; border-radius: 12px; text-align: center; }
</style>
<div class="c" style="box-shadow: 0 2px 6px rgba(14,42,92,.2);">small</div>
<div class="c" style="box-shadow: 0 12px 28px rgba(14,42,92,.3);">large</div>
<div class="c" style="box-shadow: inset 0 0 0 3px #1d5bd8;">inset</div>''',
  None,
  [("Which keyword draws a shadow inside the box?", ["inset", "inner", "inside", "within"], 0),
   ("Which two values are required in `box-shadow`?", ["Horizontal and vertical offset", "Blur and colour", "Spread and colour", "Opacity and blur"], 0)]),

# ============================================================ Text & Fonts
L("css-text", "CSS Text", "Text & Fonts",
  "Text properties control colour, alignment, spacing and decoration so that paragraphs are easy to read.",
  [("Colour and alignment", "`color` sets the text colour. `text-align` can be `left`, `right`, `center` or `justify`."),
   ("Decoration and transform", "`text-decoration` adds or removes underline, overline and line-through. `text-transform` changes case: `uppercase`, `lowercase`, `capitalize`."),
   ("Spacing", "`line-height` sets the space between lines (1.5 to 1.7 reads well). `letter-spacing` and `word-spacing` adjust gaps. `text-indent` indents the first line.")],
  '''<style>
  p { font-family: sans-serif; margin: 8px 0; }
</style>
<p style="text-align: center; color: #1d5bd8;">Centred blue text</p>
<p style="text-transform: uppercase; letter-spacing: 3px;">uppercase with spacing</p>
<p style="text-decoration: underline wavy #0e7a4f;">Wavy underline</p>
<p style="line-height: 1.8; width: 300px;">A line height of 1.8 gives wrapped lines more room to breathe, which helps readability.</p>''',
  "A unitless `line-height` such as `1.6` scales with the font size and is the safest choice.",
  [("Which property changes text to capital letters?", ["text-transform", "text-case", "font-variant-caps only", "text-style"], 0),
   ("Which `text-align` value stretches lines to fill the width?", ["justify", "stretch", "fill", "full"], 0),
   ("What does `text-decoration: none` commonly remove?", ["The underline from links", "The text colour", "The font", "The line height"], 0)]),

L("css-text-effects", "CSS Text Effects", "Text & Fonts",
  "Shadows, overflow handling and wrapping rules let you style text beyond simple colour.",
  [("Text shadow", "`text-shadow: 2px 2px 4px rgba(0,0,0,.3)` adds a shadow behind letters. Offsets come first, then blur and colour."),
   ("Truncating with an ellipsis", "Combine three declarations to cut a single line with three dots.",
    "<style>\n  .clip {\n    white-space: nowrap;\n    overflow: hidden;\n    text-overflow: ellipsis;\n  }\n</style>"),
   ("Wrapping long words", "`overflow-wrap: break-word` lets very long words break so they do not overflow their container.")],
  '''<style>
  h1 { font: 800 40px sans-serif; color: #1d5bd8; text-shadow: 3px 3px 0 #9cc3ff; margin: 0 0 12px; }
  .clip { width: 220px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; background: #eaf2ff; padding: 8px; font: 15px sans-serif; }
</style>
<h1>Shadow</h1>
<div class="clip">This long sentence is cut off with an ellipsis at the edge.</div>''',
  None,
  [("Which property adds a shadow to letters?", ["text-shadow", "font-shadow", "box-shadow", "letter-shadow"], 0),
   ("Which value of `text-overflow` shows three dots?", ["ellipsis", "dots", "clip-dots", "truncate"], 0)]),

L("css-fonts", "CSS Fonts", "Text & Fonts",
  "Font properties choose the typeface, size, weight and style of text.",
  [("font-family", "Lists fonts in priority order and ends with a generic family: `font-family: Arial, sans-serif`."),
   ("Size and weight", "`font-size` accepts `px`, `rem`, `em` or `%`. `font-weight` uses `400` (normal) to `700` (bold), or the words `normal` and `bold`."),
   ("Style and shorthand", "`font-style: italic` slants text. The `font` shorthand sets style, weight, size/line-height and family together.",
    "<style>\n  p { font: italic 600 18px/1.6 Georgia, serif; }\n</style>")],
  '''<style>
  p { margin: 6px 0; font-size: 20px; }
</style>
<p style="font-family: Georgia, serif;">Georgia, a serif font</p>
<p style="font-family: Arial, sans-serif; font-weight: 700;">Arial bold, a sans-serif font</p>
<p style="font-family: 'Courier New', monospace;">Courier New, monospace</p>
<p style="font-family: sans-serif; font-style: italic;">Italic text</p>''',
  "Use `rem` for font sizes so text respects the user's browser font setting.",
  [("Which declaration sets the typeface?", ["font-family", "font-type", "font-name", "typeface"], 0),
   ("Which `font-weight` number normally means bold?", ["700", "100", "400", "300"], 0)]),

L("css-font-stacks", "CSS Web Safe Fonts and Font Stacks", "Text & Fonts",
  "Not every computer has every font. A font stack lists fallbacks so text always renders sensibly.",
  [("Web safe fonts", "Fonts such as Arial, Verdana, Times New Roman, Georgia and Courier New exist on almost all systems."),
   ("Generic families", "End every stack with a generic family: `serif`, `sans-serif`, `monospace`, `cursive` or `fantasy`. The browser picks any installed font of that kind."),
   ("System font stack", "`system-ui` uses the operating system's interface font and loads instantly.",
    "<style>\n  body {\n    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;\n  }\n</style>")],
  '''<style>
  p { font-size: 18px; margin: 8px 0; }
</style>
<p style="font-family: 'NoSuchFont', Georgia, serif;">Unknown font falls back to Georgia.</p>
<p style="font-family: 'NoSuchFont', 'AlsoMissing', sans-serif;">Both missing, so the generic sans-serif is used.</p>
<p style="font-family: system-ui, sans-serif;">System UI font stack.</p>''',
  "Wrap font names that contain spaces in quotes, like `'Times New Roman'`.",
  [("Why end a font stack with a generic family?", ["It guarantees a sensible fallback", "It makes fonts load faster", "It is required for bold text", "It enables italics"], 0),
   ("Which of these is a generic font family?", ["monospace", "Arial", "Verdana", "Georgia"], 0)]),

L("css-icons", "CSS Icons and Symbols", "Text & Fonts",
  "You can add simple icons without images by using Unicode characters, HTML entities and CSS-drawn shapes.",
  [("Unicode symbols", "Characters like check marks, arrows and stars are ordinary text, so they scale and take `color` like any letter.",
    "<span>&#10003; Done  &#9733; Star  &rarr; Next</span>"),
   ("Icons with ::before", "Insert a symbol with the `content` property on a pseudo-element so the HTML stays clean.",
    "<style>\n  .done::before { content: '\\2713 '; color: green; }\n</style>"),
   ("Icon fonts and SVG", "Icon libraries (loaded as fonts or inline SVG) are common in real projects. Inline SVG is sharp at any size and can be coloured with CSS.")],
  '''<style>
  li { list-style: none; font: 18px sans-serif; margin: 6px 0; }
  .ok::before { content: "\\2713  "; color: #0e7a4f; font-weight: 700; }
  .star::before { content: "\\2605  "; color: #f5a623; }
  .go::before { content: "\\2192  "; color: #1d5bd8; }
</style>
<ul>
  <li class="ok">Completed</li>
  <li class="star">Favourite</li>
  <li class="go">Next step</li>
</ul>''',
  None,
  [("How can you add a symbol before an element without changing the HTML?", ["Use ::before with the content property", "Use the icon attribute", "Use margin-icon", "Use text-icon"], 0),
   ("Why are Unicode symbols useful as simple icons?", ["They are text, so they scale and take the text colour", "They need an image file", "They cannot be styled", "They only work in Chrome"], 0)]),

L("css-links", "CSS Links", "Text & Fonts",
  "Links can be styled differently depending on their state: unvisited, visited, hovered and pressed.",
  [("Link states", "Use pseudo-classes: `a:link`, `a:visited`, `a:hover` and `a:active`. If you write all four, follow the order link, visited, hover, active (LVHA)."),
   ("Removing underlines", "`text-decoration: none` removes the underline. Show it again on hover so links still look clickable."),
   ("Links as buttons", "Padding, a background and `display: inline-block` turn a link into a button.",
    "<style>\n  a.btn { display: inline-block; padding: 10px 20px; background: #1d5bd8; color: #fff; border-radius: 8px; text-decoration: none; }\n</style>")],
  '''<style>
  a { color: #1d5bd8; text-decoration: none; font: 18px sans-serif; }
  a:hover { text-decoration: underline; color: #0e2a5c; }
  a.btn { display: inline-block; padding: 10px 22px; background: #1d5bd8; color: #fff; border-radius: 8px; margin-top: 10px; }
  a.btn:hover { background: #0e2a5c; }
</style>
<a href="#">Hover this link</a><br>
<a class="btn" href="#">Button-style link</a>''',
  "Underlines help people recognise links, so keep some other clear visual cue if you remove them.",
  [("Which pseudo-class matches a link while the mouse is over it?", [":hover", ":active", ":link", ":focus-within"], 0),
   ("What is the correct order for link pseudo-classes?", ["link, visited, hover, active", "hover, active, link, visited", "active, hover, visited, link", "visited, link, active, hover"], 0)]),

L("css-lists", "CSS Lists", "Text & Fonts",
  "List properties change the bullet or number style, or remove markers entirely so a list can become a menu.",
  [("Marker style", "`list-style-type` accepts values such as `disc`, `circle`, `square`, `decimal`, `lower-alpha`, `upper-roman` and `none`."),
   ("Marker position", "`list-style-position: inside` puts the marker inside the content box. The default is `outside`."),
   ("Reset for menus", "Navigation lists usually start with a reset.",
    "<style>\n  ul { list-style: none; margin: 0; padding: 0; }\n</style>")],
  '''<style>
  ul { font: 16px sans-serif; display: inline-block; vertical-align: top; margin: 0 24px 0 0; }
</style>
<ul style="list-style-type: square; color: #1d5bd8;"><li>square</li><li>square</li></ul>
<ol style="list-style-type: upper-roman;"><li>Roman</li><li>Roman</li></ol>
<ul style="list-style: none; padding: 0;"><li>no marker</li><li>no marker</li></ul>''',
  None,
  [("Which value removes list markers?", ["list-style-type: none", "list-style: hidden", "marker: off", "display: bullets"], 0),
   ("Which `list-style-type` produces I, II, III?", ["upper-roman", "decimal", "lower-alpha", "roman-caps"], 0)]),

L("css-tables", "CSS Tables", "Text & Fonts",
  "Tables become readable with borders, padding, zebra stripes and hover highlights.",
  [("Collapsing borders", "`border-collapse: collapse` merges neighbouring cell borders into a single line."),
   ("Cell spacing and alignment", "Add `padding` to `th` and `td`, and use `text-align` to align numbers to the right."),
   ("Zebra stripes", "`tr:nth-child(even)` shades every second row so the eye can follow it across.",
    "<style>\n  tr:nth-child(even) { background: #eaf2ff; }\n</style>")],
  '''<style>
  table { border-collapse: collapse; width: 100%; font: 15px sans-serif; }
  th, td { padding: 10px 12px; text-align: left; border-bottom: 1px solid #d5e1f5; }
  th { background: #1d5bd8; color: #fff; }
  tr:nth-child(even) td { background: #eaf2ff; }
  tr:hover td { background: #d6e6ff; }
</style>
<table>
  <tr><th>Course</th><th>Lessons</th></tr>
  <tr><td>HTML</td><td>40</td></tr>
  <tr><td>CSS</td><td>65</td></tr>
  <tr><td>JavaScript</td><td>50</td></tr>
</table>''',
  None,
  [("Which property merges adjacent table borders?", ["border-collapse: collapse", "table-merge: on", "border-join: yes", "cell-spacing: 0 only"], 0),
   ("Which selector shades every second table row?", ["tr:nth-child(even)", "tr:second", "tr:alternate", "tr.even-only"], 0)]),

# ============================================================ Layout
L("css-display", "CSS Display", "Layout",
  "`display` decides how an element takes part in layout. It is the most important layout property.",
  [("Block and inline", "Block elements (`div`, `p`, `h1`) start on a new line and fill the width. Inline elements (`span`, `a`) flow within a line and ignore width and height."),
   ("Changing the type", "Set `display: inline` or `display: block` to switch behaviour, or `display: none` to remove an element from the page entirely."),
   ("Modern values", "`display: flex` and `display: grid` turn an element into a layout container for its children, covered in later lessons.")],
  '''<style>
  .item { background: #1d5bd8; color: #fff; padding: 8px 14px; margin: 4px; font: 14px sans-serif; }
</style>
<p style="font: 14px sans-serif;">Block (each on its own line):</p>
<div class="item" style="display: block;">one</div>
<div class="item" style="display: block;">two</div>
<p style="font: 14px sans-serif;">Same elements as inline:</p>
<div class="item" style="display: inline;">one</div>
<div class="item" style="display: inline;">two</div>
<div class="item" style="display: none;">hidden</div>''',
  None,
  [("Which `display` value removes an element from the layout entirely?", ["none", "hidden", "collapse", "off"], 0),
   ("Which elements start on a new line and fill the available width by default?", ["Block elements", "Inline elements", "Only images", "Only links"], 0),
   ("What happens to `width` on an inline element?", ["It is ignored", "It is doubled", "It is applied to children", "It sets the margin"], 0)]),

L("css-visibility", "CSS Visibility", "Layout",
  "`visibility: hidden` hides an element but keeps its space, unlike `display: none`.",
  [("hidden vs none", "`visibility: hidden` makes the element invisible while it still occupies its space. `display: none` removes it and the space disappears."),
   ("Showing again", "`visibility: visible` is the default. Both properties are often toggled with JavaScript or `:hover`."),
   ("Accessibility", "Elements hidden with either method are removed from the accessibility tree, so screen readers skip them.")],
  '''<style>
  .r { background: #eaf2ff; padding: 6px; font: 14px sans-serif; }
  .b { display: inline-block; background: #1d5bd8; color: #fff; padding: 8px 14px; margin: 4px; }
</style>
<div class="r"><span class="b">A</span><span class="b" style="visibility: hidden;">B (hidden, space kept)</span><span class="b">C</span></div>
<br>
<div class="r"><span class="b">A</span><span class="b" style="display: none;">B</span><span class="b">C</span></div>''',
  None,
  [("What is the difference between `visibility: hidden` and `display: none`?", ["Hidden keeps the empty space, none does not", "None keeps the empty space, hidden does not", "They are identical", "Hidden also deletes the element"], 0),
   ("Which value is the default for `visibility`?", ["visible", "hidden", "collapse", "auto"], 0)]),

L("css-position", "CSS Position", "Layout",
  "`position` controls how an element is placed. Combined with `top`, `right`, `bottom` and `left` it can offset or pin elements.",
  [("static and relative", "`static` is the default normal flow. `relative` keeps the element in flow but lets you shift it with offsets, and it becomes a reference for absolutely positioned children."),
   ("absolute", "`absolute` removes the element from the flow and positions it relative to the nearest positioned ancestor (any ancestor that is not `static`)."),
   ("fixed and sticky", "`fixed` pins the element to the viewport. `sticky` scrolls normally until it reaches an offset, then sticks like a header.")],
  '''<style>
  .parent { position: relative; height: 150px; background: #eaf2ff; border: 2px solid #1d5bd8; font: 14px sans-serif; }
  .badge { position: absolute; top: 10px; right: 10px; background: #1d5bd8; color: #fff; padding: 6px 12px; border-radius: 20px; }
  .shift { position: relative; top: 10px; left: 20px; display: inline-block; background: #0e7a4f; color: #fff; padding: 8px 14px; margin: 40px 0 0 10px; }
</style>
<div class="parent">
  <span class="badge">absolute: top-right</span>
  <div class="shift">relative: shifted</div>
</div>''',
  "Put `position: relative` on a parent when you want an absolute child to be placed inside it.",
  [("An absolutely positioned element is placed relative to what?", ["The nearest positioned ancestor", "The previous sibling", "The body always", "Its own margin"], 0),
   ("Which `position` value pins an element to the viewport while scrolling?", ["fixed", "relative", "static", "inline"], 0),
   ("What is the default `position` value?", ["static", "relative", "absolute", "sticky"], 0)]),

L("css-z-index", "CSS Z-index", "Layout",
  "`z-index` sets the stacking order of overlapping elements: higher numbers appear in front.",
  [("How it works", "`z-index` only applies to positioned elements (anything except `static`) and flex or grid items. An element with a higher value is drawn on top."),
   ("Negative values", "A negative `z-index` places an element behind its parent's content."),
   ("Stacking contexts", "Some properties such as `opacity` below 1, `transform` and `position: fixed` create a new stacking context. A child can never escape above a sibling of its context, no matter how high its value.")],
  '''<style>
  .stack { position: relative; height: 150px; font: 14px sans-serif; color: #fff; }
  .stack div { position: absolute; width: 120px; height: 90px; padding: 8px; border-radius: 10px; }
</style>
<div class="stack">
  <div style="background: #1d5bd8; left: 0; top: 0; z-index: 1;">z-index 1</div>
  <div style="background: #0e7a4f; left: 50px; top: 30px; z-index: 3;">z-index 3</div>
  <div style="background: #0e2a5c; left: 100px; top: 60px; z-index: 2;">z-index 2</div>
</div>''',
  None,
  [("Which element appears in front of the others?", ["The one with the highest z-index", "The one with the lowest z-index", "The first one in the HTML always", "The one with the largest width"], 0),
   ("Which elements does `z-index` normally apply to?", ["Positioned elements and flex or grid items", "Only inline text", "Only images", "Only the body"], 0)]),

L("css-overflow", "CSS Overflow", "Layout",
  "`overflow` decides what happens when content is larger than its box.",
  [("Values", "`visible` (default) lets content spill out. `hidden` clips it. `scroll` always shows scrollbars. `auto` shows them only when needed."),
   ("Single axis", "`overflow-x` and `overflow-y` control each direction separately."),
   ("Common uses", "`overflow: hidden` clips rounded images to a card, and `overflow: auto` makes a scrollable panel or a table that scrolls sideways on phones.")],
  '''<style>
  .box { width: 200px; height: 80px; border: 2px solid #1d5bd8; margin: 6px; display: inline-block; vertical-align: top; font: 14px sans-serif; }
</style>
<div class="box" style="overflow: visible;">visible: this long text spills right out of the box and keeps going</div>
<div class="box" style="overflow: hidden;">hidden: this long text gets clipped at the edge of the box and the rest is not shown</div>
<div class="box" style="overflow: auto;">auto: this long text gets a scrollbar because it is taller than the box. Scroll to read more of it here.</div>''',
  None,
  [("Which `overflow` value clips content that does not fit?", ["hidden", "visible", "clip-all", "cut"], 0),
   ("Which value adds scrollbars only when they are needed?", ["auto", "scroll", "hidden", "inherit"], 0)]),

L("css-float", "CSS Float and Clear", "Layout",
  "`float` pushes an element to the left or right so text wraps around it. It was once used for whole layouts, but today it is mainly for wrapping text around images.",
  [("float", "`float: left` or `float: right` takes the element out of normal flow and lets inline content wrap around it."),
   ("clear", "`clear: both` makes an element move below any floated elements."),
   ("Containing floats", "A parent of only floated children collapses to zero height. `display: flow-root` on the parent fixes it cleanly.",
    "<style>\n  .parent { display: flow-root; }\n</style>"),
   ("Use flexbox or grid", "For page layouts, use flexbox or grid instead of floats.")],
  '''<style>
  .pic { float: left; width: 90px; height: 90px; margin: 0 14px 6px 0; border-radius: 10px; background: #1d5bd8; color: #fff; font: 13px sans-serif; text-align: center; line-height: 90px; }
  p { font: 15px/1.6 sans-serif; }
  .after { clear: both; background: #eaf2ff; padding: 6px; font: 14px sans-serif; }
</style>
<div class="pic">float</div>
<p>Text wraps around a floated element. This is the classic use for floats: a picture on one side with the paragraph flowing beside it and underneath it once the text becomes longer than the picture is tall.</p>
<div class="after">clear: both starts below the float</div>''',
  None,
  [("What does `clear: both` do?", ["Moves the element below any floats", "Removes the element's float forever", "Clears all colours", "Hides floated elements"], 0),
   ("What is float mainly used for today?", ["Wrapping text around an image", "Building full page layouts", "Centring text", "Adding shadows"], 0)]),

L("css-inline-block", "CSS Inline-block", "Layout",
  "`display: inline-block` combines both worlds: the element flows in a line like text but accepts width, height, margin and padding like a block.",
  [("Comparing the three", "Inline ignores width and height. Block fills the line. Inline-block sits in the line and respects its dimensions."),
   ("Typical use", "Buttons, badges and simple navigation items. For a row of items with equal spacing, flexbox is usually cleaner."),
   ("Whitespace gaps", "Because inline-block items behave like words, the space between them in the HTML shows as a small gap on screen.")],
  '''<style>
  .tag { display: inline-block; width: 90px; padding: 10px 0; margin: 4px; text-align: center; background: #1d5bd8; color: #fff; border-radius: 8px; font: 14px sans-serif; }
</style>
<span class="tag">HTML</span><span class="tag">CSS</span><span class="tag">JS</span><span class="tag">Python</span>''',
  None,
  [("What does `display: inline-block` allow that plain inline does not?", ["Setting width and height", "Hiding the element", "Using flexbox children", "Removing the text"], 0),
   ("Why might gaps appear between inline-block items?", ["Whitespace in the HTML is treated like a space", "Browsers add random margin", "They always have a 10px border", "The z-index is too low"], 0)]),

L("css-align", "CSS Align", "Layout",
  "Centring is a common task with several techniques. Choose the one that suits the element type.",
  [("Horizontal centring", "Text: `text-align: center`. A block with a width: `margin: 0 auto`. Inline-block items: `text-align: center` on the parent."),
   ("Vertical centring", "The modern way is flexbox or grid. Both centre in two directions with just two or three lines.",
    "<style>\n  .parent {\n    display: grid;\n    place-items: center;\n    height: 200px;\n  }\n</style>"),
   ("Older techniques", "`line-height` equal to the height centres a single line of text, and `position: absolute` with `transform: translate(-50%, -50%)` centres a box in its parent.")],
  '''<style>
  .parent { display: grid; place-items: center; height: 180px; background: #eaf2ff; border: 2px solid #1d5bd8; }
  .child { background: #1d5bd8; color: #fff; padding: 14px 24px; border-radius: 10px; font: 16px sans-serif; }
</style>
<div class="parent"><div class="child">Centred both ways</div></div>''',
  None,
  [("Which pair of declarations centres a child in both directions with grid?", ["display: grid; place-items: center", "display: block; align: middle", "margin: center; display: grid-center", "text-align: center; vertical: middle"], 0),
   ("Which technique centres a fixed-width block horizontally?", ["margin: 0 auto", "text-align: auto", "float: center", "position: middle"], 0)]),

L("css-flexbox", "CSS Flexbox", "Layout",
  "Flexbox lays out items in one direction, either a row or a column, and distributes space between them.",
  [("Creating a flex container", "Set `display: flex` on the parent. Its direct children become flex items and line up in a row by default."),
   ("Direction and wrapping", "`flex-direction` can be `row`, `column`, `row-reverse` or `column-reverse`. `flex-wrap: wrap` lets items drop onto new lines."),
   ("Alignment", "`justify-content` aligns items along the main axis (`flex-start`, `center`, `space-between`, `space-around`, `space-evenly`). `align-items` aligns them across the cross axis. `gap` adds space between items.",
    "<style>\n  .row {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    gap: 12px;\n  }\n</style>")],
  '''<style>
  .row { display: flex; justify-content: space-between; align-items: center; gap: 10px; background: #eaf2ff; padding: 10px; height: 110px; border-radius: 10px; }
  .row div { background: #1d5bd8; color: #fff; padding: 14px 22px; border-radius: 8px; font: 15px sans-serif; }
</style>
<div class="row"><div>1</div><div style="padding: 30px 22px;">2</div><div>3</div></div>''',
  "Remember: `justify-content` follows the main axis, `align-items` follows the cross axis. They swap when the direction is `column`.",
  [("Which declaration turns an element into a flex container?", ["display: flex", "flex: container", "layout: flex", "position: flex"], 0),
   ("Which property spaces flex items along the main axis?", ["justify-content", "align-items", "flex-grow", "place-content only"], 0),
   ("What does `flex-wrap: wrap` do?", ["Lets items move onto new lines", "Wraps text in quotes", "Reverses the item order", "Shrinks items to zero"], 0)]),

L("css-flex-items", "CSS Flex Items", "Layout",
  "Flex item properties control how each child grows, shrinks and aligns inside the container.",
  [("flex-grow, flex-shrink, flex-basis", "`flex-grow` says how much spare space an item takes. `flex-shrink` says how much it gives up when space is short. `flex-basis` sets the starting size."),
   ("The flex shorthand", "`flex: 1` means grow 1, shrink 1, basis 0, so equal-weight items share the space evenly. `flex: 0 0 200px` makes a fixed-width item."),
   ("Single item control", "`align-self` overrides the container's `align-items` for one item. `order` changes the visual order. `margin-left: auto` pushes an item to the far end.")],
  '''<style>
  .row { display: flex; gap: 8px; background: #eaf2ff; padding: 8px; border-radius: 10px; }
  .row div { background: #1d5bd8; color: #fff; padding: 14px; border-radius: 8px; font: 14px sans-serif; text-align: center; }
</style>
<div class="row">
  <div style="flex: 0 0 90px;">fixed 90px</div>
  <div style="flex: 1;">flex: 1</div>
  <div style="flex: 2;">flex: 2 (twice as wide)</div>
</div>''',
  None,
  [("What does `flex: 1` on all items do?", ["Gives them equal shares of the space", "Makes them 1px wide", "Reverses their order", "Stops them wrapping"], 0),
   ("Which property overrides alignment for a single flex item?", ["align-self", "justify-self only", "flex-align", "item-align"], 0)]),

L("css-flex-patterns", "CSS Flexbox Patterns", "Layout",
  "A few flexbox patterns solve most everyday layouts: centring, navigation bars, equal columns and sticky footers.",
  [("Perfect centring", "Two lines centre anything: `display: flex; justify-content: center; align-items: center;`."),
   ("Navigation with a spacer", "Put the logo first and use `margin-left: auto` on the first link to push the links to the right."),
   ("Sticky footer", "Make the page wrapper a column with `min-height: 100vh` and give the main area `flex: 1`, so the footer stays at the bottom on short pages.",
    "<style>\n  body { min-height: 100vh; display: flex; flex-direction: column; }\n  main { flex: 1; }\n</style>"),
   ("Card rows", "`flex-wrap: wrap` with `flex: 1 1 220px` on each card makes a row of cards that wraps automatically.")],
  '''<style>
  .nav { display: flex; align-items: center; gap: 14px; background: #0e2a5c; padding: 10px 16px; border-radius: 10px; font: 15px sans-serif; color: #fff; }
  .nav .logo { font-weight: 700; margin-right: auto; }
  .cards { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
  .cards div { flex: 1 1 140px; background: #eaf2ff; border: 1px solid #1d5bd8; padding: 18px; border-radius: 10px; font: 14px sans-serif; text-align: center; }
</style>
<div class="nav"><span class="logo">TechHub</span><span>Home</span><span>Courses</span><span>About</span></div>
<div class="cards"><div>Card 1</div><div>Card 2</div><div>Card 3</div></div>''',
  None,
  [("How do you push a flex item to the far end of the row?", ["margin-left: auto", "float: right", "align-self: end only", "order: 99 only"], 0),
   ("Which flex value makes cards at least 220px wide that grow to fill space?", ["flex: 1 1 220px", "flex: 220px 0 0", "flex: 0 0 1", "flex: auto 220"], 0)]),

L("css-grid", "CSS Grid", "Layout",
  "Grid lays out items in rows and columns at the same time. It is the strongest tool for page-level layouts.",
  [("Creating a grid", "Set `display: grid` and describe the columns with `grid-template-columns`. Children flow into the cells automatically."),
   ("The fr unit", "`fr` means a fraction of the free space: `grid-template-columns: 1fr 2fr` gives the second column twice the width. `repeat(3, 1fr)` makes three equal columns.",
    "<style>\n  .grid {\n    display: grid;\n    grid-template-columns: repeat(3, 1fr);\n    gap: 12px;\n  }\n</style>"),
   ("Spanning", "`grid-column: span 2` makes an item cover two columns. `grid-row: span 2` covers two rows.")],
  '''<style>
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .grid div { background: #1d5bd8; color: #fff; padding: 20px; border-radius: 8px; text-align: center; font: 15px sans-serif; }
  .wide { grid-column: span 2; background: #0e2a5c !important; }
</style>
<div class="grid"><div>1</div><div class="wide">2 (spans two columns)</div><div>3</div><div>4</div><div>5</div></div>''',
  None,
  [("What does `1fr 2fr` produce?", ["Two columns, the second twice as wide", "Two columns of 1px and 2px", "One column split in half", "Two equal columns"], 0),
   ("Which declaration creates three equal columns?", ["grid-template-columns: repeat(3, 1fr)", "columns: 3 equal", "grid-columns: 3", "display: grid-3"], 0),
   ("How do you make a grid item cover two columns?", ["grid-column: span 2", "column-count: 2", "width: 2fr", "colspan: 2"], 0)]),

L("css-grid-areas", "CSS Grid Areas and Placement", "Layout",
  "Named grid areas let you draw a page layout almost like a diagram in your CSS.",
  [("grid-template-areas", "Describe the layout with strings, one per row. Each word names an area; repeat a name to span cells.",
    "<style>\n  .page {\n    display: grid;\n    grid-template-columns: 160px 1fr;\n    grid-template-areas:\n      'header header'\n      'side   main'\n      'footer footer';\n  }\n</style>"),
   ("Assigning items", "Give each child `grid-area: name` to place it in the matching area."),
   ("Line placement", "You can also place items by line numbers: `grid-column: 1 / 3` starts at line 1 and ends at line 3.")],
  '''<style>
  .page { display: grid; grid-template-columns: 100px 1fr; grid-template-areas: "header header" "side main" "footer footer"; gap: 8px; font: 14px sans-serif; color: #fff; }
  .page div { padding: 14px; border-radius: 8px; }
  .h { grid-area: header; background: #0e2a5c; }
  .s { grid-area: side; background: #1d5bd8; }
  .m { grid-area: main; background: #4a86f0; min-height: 70px; }
  .f { grid-area: footer; background: #0e2a5c; }
</style>
<div class="page"><div class="h">header</div><div class="s">side</div><div class="m">main</div><div class="f">footer</div></div>''',
  None,
  [("Which property assigns a child to a named area?", ["grid-area", "grid-name", "area-name", "grid-place"], 0),
   ("In `grid-template-areas`, what does repeating a name across cells do?", ["Makes that area span those cells", "Causes an error", "Duplicates the item", "Hides the area"], 0)]),

L("css-grid-responsive", "CSS Responsive Grid", "Layout",
  "With `auto-fit` and `minmax()`, a grid can change its number of columns by itself, with no media queries.",
  [("The magic line", "`repeat(auto-fit, minmax(180px, 1fr))` creates as many columns of at least 180px as will fit, then stretches them to fill the row.",
    "<style>\n  .cards {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));\n    gap: 16px;\n  }\n</style>"),
   ("auto-fit vs auto-fill", "`auto-fit` stretches items to fill leftover space. `auto-fill` keeps empty tracks, leaving gaps at the end."),
   ("Resize to see", "Drag the preview's width or open the page full screen and resize the window; the columns rearrange themselves.")],
  '''<style>
  .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; }
  .cards div { background: #eaf2ff; border: 2px solid #1d5bd8; border-radius: 10px; padding: 22px 8px; text-align: center; font: 15px sans-serif; color: #0e2a5c; }
</style>
<div class="cards"><div>One</div><div>Two</div><div>Three</div><div>Four</div><div>Five</div><div>Six</div></div>''',
  "This single declaration often replaces several media queries.",
  [("What does `minmax(180px, 1fr)` mean?", ["At least 180px, growing to share space", "Exactly 180px", "At most 180px", "Between 1px and 180px"], 0),
   ("Which keyword stretches grid items to fill the leftover row space?", ["auto-fit", "auto-fill", "auto-stretch", "fit-all"], 0)]),

# ============================================================ Components
L("css-navbar", "CSS Navigation Bar", "Components",
  "A navigation bar is just a styled list of links. Reset the list, lay it out with flexbox, then style the links.",
  [("Start with a list", "Use a `<nav>` containing a `<ul>` of links. Remove bullets and default spacing first."),
   ("Lay out and style", "Make the list a flex row, add padding to the links and a hover colour.",
    "<style>\n  nav ul { display: flex; list-style: none; margin: 0; padding: 0; }\n  nav a { display: block; padding: 14px 18px; color: #fff; text-decoration: none; }\n  nav a:hover { background: #1747ab; }\n</style>"),
   ("Show the current page", "Mark the active link with a class or `aria-current=\"page\"` and style it differently.")],
  '''<style>
  nav { background: #0e2a5c; border-radius: 10px; }
  nav ul { display: flex; list-style: none; margin: 0; padding: 0; }
  nav a { display: block; padding: 14px 20px; color: #fff; text-decoration: none; font: 600 15px sans-serif; }
  nav a:hover { background: #1747ab; }
  nav a[aria-current="page"] { background: #1d5bd8; }
  nav li:last-child { margin-left: auto; }
</style>
<nav><ul>
  <li><a href="#" aria-current="page">Home</a></li>
  <li><a href="#">Courses</a></li>
  <li><a href="#">Blog</a></li>
  <li><a href="#">Login</a></li>
</ul></nav>''',
  None,
  [("Which element is meant for main navigation links?", ["<nav>", "<menu-bar>", "<aside>", "<header-links>"], 0),
   ("What is the first step when turning a `ul` into a menu?", ["Remove the list markers and default padding", "Add a table", "Set it to float: none", "Wrap each item in a form"], 0)]),

L("css-dropdown", "CSS Dropdowns", "Components",
  "A dropdown menu can be built with CSS only, by hiding a submenu and revealing it on hover or focus.",
  [("Structure", "Put the hidden menu inside the item that opens it, and make that item `position: relative`."),
   ("Show on hover", "Hide the menu with `display: none`, then show it with `:hover` or `:focus-within`. Adding `:focus-within` keeps it usable with a keyboard.",
    "<style>\n  .dd { position: relative; display: inline-block; }\n  .menu { display: none; position: absolute; top: 100%; left: 0; }\n  .dd:hover .menu, .dd:focus-within .menu { display: block; }\n</style>"),
   ("Place it above others", "Give the menu a `z-index` so it overlaps the content below.")],
  '''<style>
  .dd { position: relative; display: inline-block; font: 15px sans-serif; }
  .dd > button { background: #1d5bd8; color: #fff; border: 0; padding: 10px 18px; border-radius: 8px; font: 600 15px sans-serif; cursor: pointer; }
  .menu { display: none; position: absolute; top: 100%; left: 0; min-width: 160px; background: #fff; border: 1px solid #d5e1f5; border-radius: 8px; box-shadow: 0 8px 20px rgba(14,42,92,.2); z-index: 10; }
  .menu a { display: block; padding: 10px 14px; color: #0e2a5c; text-decoration: none; }
  .menu a:hover { background: #eaf2ff; }
  .dd:hover .menu, .dd:focus-within .menu { display: block; }
</style>
<div class="dd"><button>Hover or focus me</button>
  <div class="menu"><a href="#">HTML</a><a href="#">CSS</a><a href="#">JavaScript</a></div>
</div>''',
  None,
  [("Which pseudo-class keeps a CSS dropdown open for keyboard users?", [":focus-within", ":visited", ":first-child", ":empty"], 0),
   ("Which positioning pair places a submenu under its parent?", ["relative on the parent, absolute on the menu", "fixed on the parent, static on the menu", "sticky on both", "float on both"], 0)]),

L("css-gallery", "CSS Image Gallery and object-fit", "Components",
  "A gallery combines grid layout with `object-fit` so images of different shapes fill equal tiles neatly.",
  [("object-fit", "`object-fit: cover` scales the image to fill its box and crops the overflow. `contain` fits the whole image inside, leaving empty space. `fill` stretches it."),
   ("object-position", "`object-position` chooses which part is kept when `cover` crops, for example `center top`."),
   ("Gallery recipe", "A responsive grid, equal-sized tiles and `object-fit: cover` on each `<img>`.",
    "<style>\n  .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 8px; }\n  .gallery img { width: 100%; height: 120px; object-fit: cover; }\n</style>")],
  '''<style>
  .gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
  .gallery img { width: 100%; height: 100px; border-radius: 8px; }
  .cover { object-fit: cover; } .contain { object-fit: contain; background: #eaf2ff; } .fill { object-fit: fill; }
  p { font: 13px sans-serif; text-align: center; margin: 4px 0; }
</style>
<div class="gallery">
  <div><img class="cover" alt="wide banner, cover" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='100'><rect width='300' height='100' fill='%231d5bd8'/><circle cx='150' cy='50' r='40' fill='%23ffd479'/></svg>"><p>cover</p></div>
  <div><img class="contain" alt="wide banner, contain" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='100'><rect width='300' height='100' fill='%231d5bd8'/><circle cx='150' cy='50' r='40' fill='%23ffd479'/></svg>"><p>contain</p></div>
  <div><img class="fill" alt="wide banner, fill" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='100'><rect width='300' height='100' fill='%231d5bd8'/><circle cx='150' cy='50' r='40' fill='%23ffd479'/></svg>"><p>fill (stretched)</p></div>
</div>''',
  None,
  [("Which `object-fit` value fills the box and crops any extra?", ["cover", "contain", "fill", "scale-down"], 0),
   ("Which `object-fit` value shows the whole image without cropping and keeps its proportions?", ["contain", "cover", "crop", "stretch"], 0)]),

L("css-forms", "CSS Forms", "Components",
  "Forms look better and are easier to use when inputs have consistent spacing, clear focus states and readable labels.",
  [("Style the controls", "Give inputs padding, a border and rounded corners. Use `width: 100%` with `box-sizing: border-box` so they fill their container."),
   ("Focus state", "`input:focus` highlights the field being edited. Use a visible outline or border colour change.",
    "<style>\n  input:focus { border-color: #1d5bd8; outline: 3px solid #cfe0ff; }\n</style>"),
   ("Validation states", "`:required`, `:valid` and `:invalid` let you style fields by their validity.")],
  '''<style>
  form { max-width: 320px; font: 15px sans-serif; }
  label { display: block; margin: 10px 0 4px; font-weight: 600; color: #0e2a5c; }
  input, select { width: 100%; box-sizing: border-box; padding: 10px 12px; border: 2px solid #d5e1f5; border-radius: 8px; font: inherit; }
  input:focus, select:focus { border-color: #1d5bd8; outline: 3px solid #cfe0ff; }
  input:invalid:not(:placeholder-shown) { border-color: #b42318; }
  button { margin-top: 14px; background: #1d5bd8; color: #fff; border: 0; padding: 10px 20px; border-radius: 8px; font: 600 15px sans-serif; }
</style>
<form>
  <label for="n">Name</label><input id="n" placeholder="Your name">
  <label for="e">Email (type something invalid)</label><input id="e" type="email" placeholder="you@example.com">
  <button type="button">Send</button>
</form>''',
  None,
  [("Which pseudo-class styles the input that currently has keyboard focus?", [":focus", ":hover only", ":checked", ":target"], 0),
   ("Which declaration pair makes an input fill its container neatly?", ["width: 100% with box-sizing: border-box", "width: auto with float: left", "height: 100% with margin: 100px", "display: none with width: 100%"], 0)]),

L("css-buttons-cards", "CSS Buttons and Cards", "Components",
  "Buttons and cards are the most common interface building blocks. Both rely on padding, radius, shadow and a hover state.",
  [("Buttons", "Give buttons generous padding, a clear colour, rounded corners and a hover or focus effect. Add `cursor: pointer`."),
   ("Cards", "A card is a box with a background, padding, border-radius and a soft shadow. Often a grid or flex container holds several cards."),
   ("Lift on hover", "Combine `transition` with `transform: translateY(-4px)` for a gentle lift.",
    "<style>\n  .card { transition: transform .2s, box-shadow .2s; }\n  .card:hover { transform: translateY(-4px); }\n</style>")],
  '''<style>
  body { background: #eaf2ff; padding: 12px; font-family: sans-serif; }
  .card { max-width: 240px; background: #fff; border-radius: 14px; padding: 20px; box-shadow: 0 4px 14px rgba(14,42,92,.15); transition: transform .2s, box-shadow .2s; }
  .card:hover { transform: translateY(-4px); box-shadow: 0 14px 28px rgba(14,42,92,.25); }
  .card h3 { margin: 0 0 6px; color: #0e2a5c; }
  .card p { margin: 0 0 14px; color: #5a6b8c; font-size: 14px; }
  .btn { background: #1d5bd8; color: #fff; border: 0; padding: 10px 20px; border-radius: 8px; font: 600 14px sans-serif; cursor: pointer; transition: background .2s; }
  .btn:hover { background: #0e2a5c; }
</style>
<div class="card"><h3>CSS Course</h3><p>Hover over this card.</p><button class="btn">Start</button></div>''',
  None,
  [("Which property makes the pointer a hand over a button?", ["cursor: pointer", "hover: hand", "pointer: on", "mouse: click"], 0),
   ("Which two properties give a card its raised look?", ["border-radius and box-shadow", "float and clear", "list-style and outline", "z-index and visibility"], 0)]),

L("css-tooltips", "CSS Tooltips", "Components",
  "A tooltip is a small box that appears when the user hovers over or focuses an element, built with a positioned child.",
  [("Structure", "Wrap the trigger in a relatively positioned container and place the tooltip text in a child that is hidden by default."),
   ("Show on hover", "Reveal the tooltip with `:hover` and `:focus-within`, and position it above the trigger with `bottom: 125%`.",
    "<style>\n  .tip { position: relative; display: inline-block; }\n  .tip span { visibility: hidden; position: absolute; bottom: 125%; left: 50%; transform: translateX(-50%); }\n  .tip:hover span { visibility: visible; }\n</style>"),
   ("An arrow", "A `::after` pseudo-element with a border trick draws the little pointer.")],
  '''<style>
  body { padding-top: 50px; font: 15px sans-serif; text-align: center; }
  .tip { position: relative; display: inline-block; border-bottom: 2px dotted #1d5bd8; cursor: help; color: #1d5bd8; }
  .tip span { visibility: hidden; opacity: 0; transition: opacity .2s; position: absolute; bottom: 130%; left: 50%; transform: translateX(-50%); width: 160px; background: #0e2a5c; color: #fff; padding: 8px; border-radius: 8px; font-size: 13px; }
  .tip span::after { content: ""; position: absolute; top: 100%; left: 50%; margin-left: -6px; border: 6px solid transparent; border-top-color: #0e2a5c; }
  .tip:hover span, .tip:focus-within span { visibility: visible; opacity: 1; }
</style>
<p>Hover over the <span class="tip" tabindex="0">dotted word<span>CSS tooltips need no JavaScript.</span></span> to see it.</p>''',
  None,
  [("Which property positions a tooltip relative to its trigger container?", ["position: absolute inside a position: relative parent", "float: tooltip", "display: popup", "z-index: tooltip"], 0),
   ("Which pseudo-element is handy for a tooltip arrow?", ["::after", "::marker", "::selection", "::placeholder"], 0)]),

# ============================================================ Selectors
L("css-combinators", "CSS Combinators", "Selectors",
  "Combinators select elements based on their relationship to other elements in the HTML tree.",
  [("Descendant (space)", "`div p` selects every `p` anywhere inside a `div`."),
   ("Child (>)", "`div > p` selects only `p` elements that are direct children of a `div`."),
   ("Adjacent sibling (+)", "`h2 + p` selects the first `p` immediately after an `h2`."),
   ("General sibling (~)", "`h2 ~ p` selects every `p` sibling that comes after an `h2` and shares the same parent.")],
  '''<style>
  div p { color: #0e2a5c; }
  div > p { font-weight: 700; }
  h2 + p { background: #cfe0ff; padding: 4px; }
  h2 ~ p.later { color: #b42318; }
  body { font: 16px sans-serif; }
</style>
<div>
  <h2>Heading</h2>
  <p>Directly after the h2 (adjacent sibling, also a child).</p>
  <p class="later">A later sibling (general sibling, red).</p>
  <section><p>Nested one level deeper: descendant only.</p></section>
</div>''',
  None,
  [("Which combinator selects only direct children?", [">", "+", "~", "(space)"], 0),
   ("What does `h2 + p` select?", ["The first p right after an h2", "Every p inside an h2", "All p siblings after an h2", "The p before an h2"], 0),
   ("What does the space combinator in `div p` select?", ["All p descendants of a div", "Only direct child p elements", "Only the first p", "Every div inside a p"], 0)]),

L("css-pseudo-classes", "CSS Pseudo-classes", "Selectors",
  "A pseudo-class selects an element in a particular state or position, such as hovered, focused or first in its list.",
  [("State classes", "`:hover`, `:focus`, `:active`, `:checked`, `:disabled` and `:focus-visible` respond to what the user is doing or the control's state."),
   ("Structural classes", "`:first-child`, `:last-child`, `:nth-child(2n)`, `:nth-of-type()` and `:only-child` select by position."),
   ("Logical classes", "`:not(.x)` excludes matches. `:is(h1, h2)` and `:where()` group selectors. `:has(img)` selects a parent that contains an image.",
    "<style>\n  li:not(:last-child) { border-bottom: 1px solid #ccc; }\n  .card:has(img) { padding: 0; }\n</style>")],
  '''<style>
  ul { list-style: none; padding: 0; width: 240px; font: 16px sans-serif; border: 1px solid #d5e1f5; border-radius: 10px; overflow: hidden; }
  li { padding: 10px 14px; }
  li:not(:last-child) { border-bottom: 1px solid #d5e1f5; }
  li:nth-child(odd) { background: #eaf2ff; }
  li:first-child { font-weight: 700; color: #1d5bd8; }
  li:hover { background: #cfe0ff; }
</style>
<ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li></ul>''',
  None,
  [("Which pseudo-class selects every other item starting with the first?", [":nth-child(odd)", ":nth-child(even)", ":every-other", ":first-of-all"], 0),
   ("What does `:not(.x)` do?", ["Selects elements without the class x", "Selects only elements with class x", "Deletes class x", "Selects the parent of x"], 0),
   ("Which pseudo-class matches a parent that contains a certain child?", [":has()", ":parent", ":contains()", ":inside()"], 0)]),

L("css-pseudo-elements", "CSS Pseudo-elements", "Selectors",
  "A pseudo-element styles a specific part of an element, or adds generated content before or after it.",
  [("Syntax", "Pseudo-elements use two colons: `::before`, `::after`, `::first-line`, `::first-letter`, `::selection`, `::marker` and `::placeholder`."),
   ("Generated content", "`::before` and `::after` need the `content` property, even if it is an empty string, or they will not appear.",
    "<style>\n  .req::after { content: ' *'; color: red; }\n</style>"),
   ("Styling parts of text", "`::first-letter` creates drop caps. `::selection` changes the colour of highlighted text.")],
  '''<style>
  p { font: 17px/1.6 sans-serif; max-width: 360px; }
  p::first-letter { font-size: 2.6em; float: left; line-height: 1; padding-right: 6px; color: #1d5bd8; font-weight: 700; }
  p::selection { background: #1d5bd8; color: #fff; }
  .req::after { content: " *"; color: #b42318; }
  blockquote::before { content: "\\201C"; font-size: 2em; color: #1d5bd8; }
</style>
<p>Pseudo-elements style a part of an element, here its first letter. Try selecting this text.</p>
<span class="req">Required field</span>
<blockquote>Generated quote mark</blockquote>''',
  None,
  [("Which property must be set for ::before to display?", ["content", "display-text", "insert", "text"], 0),
   ("Which pseudo-element styles the first letter of a paragraph?", ["::first-letter", "::first-char", ":first-letter-only", "::initial"], 0)]),

L("css-attribute-selectors", "CSS Attribute Selectors", "Selectors",
  "Attribute selectors match elements by their attributes or attribute values, with no extra classes needed.",
  [("Basic forms", "`[title]` has the attribute. `[type=\"email\"]` matches an exact value."),
   ("Partial matches", "`[href^=\"https\"]` starts with, `[href$=\".pdf\"]` ends with, `[href*=\"blog\"]` contains."),
   ("Case and lists", "`[lang|=\"en\"]` matches `en` or `en-US`. Add ` i` before the bracket to ignore case.",
    "<style>\n  a[href$='.pdf']::after { content: ' (PDF)'; }\n</style>")],
  '''<style>
  body { font: 17px/2 sans-serif; }
  a[href^="https"] { color: #0e7a4f; }
  a[href$=".pdf"]::after { content: " (PDF)"; font-size: 13px; color: #b42318; }
  input[type="email"] { border: 2px solid #1d5bd8; padding: 6px; border-radius: 6px; }
</style>
<a href="https://example.com">Secure link</a><br>
<a href="guide.pdf">Download guide</a><br>
<input type="email" placeholder="email field styled by attribute">''',
  None,
  [("What does `a[href$=\".pdf\"]` select?", ["Links whose href ends with .pdf", "Links whose href starts with .pdf", "Links containing pdf anywhere", "Links named pdf"], 0),
   ("Which operator means 'starts with' in an attribute selector?", ["^=", "$=", "*=", "|="], 0)]),

L("css-specificity", "CSS Specificity", "Selectors",
  "When several rules target the same element, specificity decides which one wins. It is calculated from the kinds of selectors used.",
  [("The ranking", "From weakest to strongest: element selectors (and pseudo-elements), then classes, attributes and pseudo-classes, then ids, then inline styles."),
   ("Counting", "Think of it as three numbers (ids, classes, elements). `#nav .link a` is 1-1-1. A higher number in an earlier column always beats any number of later ones."),
   ("Same specificity", "If specificity is equal, the rule that comes last in the CSS wins."),
   ("!important", "`!important` overrides normal specificity. Use it very rarely, because it makes later changes hard.")],
  '''<style>
  p { color: gray; }                 /* 0-0-1 */
  .note { color: #1d5bd8; }          /* 0-1-0 beats element */
  p.note { color: #0e7a4f; }         /* 0-1-1 beats .note */
  #special { color: #b42318; }       /* 1-0-0 beats any classes */
  body { font: 17px sans-serif; }
</style>
<p>Element rule: gray</p>
<p class="note">Class + element rule: green</p>
<p class="note" id="special">Id rule: red</p>''',
  "If a style does not apply, open dev tools: crossed-out declarations show which rule is overriding yours.",
  [("Which selector is the most specific?", ["#menu", ".menu", "div", "div p"], 0),
   ("If two rules have equal specificity, which one wins?", ["The one that appears later", "The one that appears earlier", "The shorter one", "Neither, it is an error"], 0),
   ("Which is generally best to avoid using?", ["!important", "class selectors", "comments", "variables"], 0)]),

L("css-inheritance-cascade", "CSS Inheritance and the Cascade", "Selectors",
  "Some properties pass down from parent to child automatically (inheritance), and the cascade decides between competing rules.",
  [("Inheritance", "Text-related properties such as `color`, `font-family`, `font-size`, `line-height` and `text-align` are inherited. Box properties such as `margin`, `padding` and `border` are not."),
   ("Control keywords", "`inherit` forces inheritance. `initial` resets to the default. `unset` inherits if the property normally inherits, otherwise resets. `revert` goes back to the browser stylesheet."),
   ("The cascade order", "The browser looks at origin and importance, then specificity, then source order. This is where the name 'Cascading' comes from.")],
  '''<style>
  .parent { color: #1d5bd8; border: 3px solid #0e2a5c; padding: 10px; font: 17px sans-serif; }
  .child  { margin-top: 8px; }
  .reset  { color: initial; }
  .force  { border: inherit; padding: 6px; }
</style>
<div class="parent">
  Parent text (blue, border).
  <p class="child">Child inherits the colour but not the border.</p>
  <p class="child reset">Child with color: initial (back to black).</p>
  <p class="child force">Child with border: inherit.</p>
</div>''',
  None,
  [("Which property is inherited by default?", ["color", "margin", "border", "padding"], 0),
   ("What does the `inherit` keyword do?", ["Takes the value from the parent", "Resets to the browser default", "Deletes the property", "Copies the value from the sibling"], 0)]),

# ============================================================ Effects & Animation
L("css-transforms", "CSS 2D Transforms", "Effects & Animation",
  "`transform` moves, rotates, scales and skews an element without disturbing the layout around it.",
  [("The functions", "`translate(x, y)` moves, `rotate(45deg)` turns, `scale(1.2)` resizes and `skew(10deg)` slants. Combine several in one declaration, separated by spaces."),
   ("transform-origin", "Transforms happen around the centre by default. `transform-origin: top left` changes the pivot point."),
   ("Layout is unaffected", "A transformed element keeps its original space in the layout, so neighbours do not move.",
    "<style>\n  .box:hover { transform: rotate(8deg) scale(1.1); }\n</style>")],
  '''<style>
  .row { padding: 30px 10px; }
  .t { display: inline-block; width: 80px; height: 80px; margin: 0 16px; background: #1d5bd8; color: #fff; font: 13px sans-serif; text-align: center; line-height: 80px; border-radius: 10px; }
</style>
<div class="row">
  <div class="t" style="transform: rotate(20deg);">rotate</div>
  <div class="t" style="transform: scale(1.3);">scale</div>
  <div class="t" style="transform: translate(0, -14px);">translate</div>
  <div class="t" style="transform: skew(15deg);">skew</div>
</div>''',
  None,
  [("Which function turns an element by an angle?", ["rotate()", "turn-around()", "spin()", "angle()"], 0),
   ("Around which point does a transform pivot by default?", ["The centre of the element", "The top-left corner", "The page origin", "The parent's centre"], 0)]),

L("css-transitions", "CSS Transitions", "Effects & Animation",
  "Transitions smooth a change between two states, such as a colour change on hover, instead of snapping instantly.",
  [("Syntax", "`transition: property duration timing-function delay`. For example `transition: background .3s ease`."),
   ("Timing functions", "`ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out` and `cubic-bezier()` shape the speed curve."),
   ("Put it on the base state", "Place `transition` on the normal rule, not only on `:hover`, so the animation runs both when entering and when leaving the state.",
    "<style>\n  .btn { background: #1d5bd8; transition: background .3s; }\n  .btn:hover { background: #0e2a5c; }\n</style>"),
   ("Animate cheap properties", "`transform` and `opacity` animate smoothly because browsers can handle them without recalculating layout.")],
  '''<style>
  .b { display: inline-block; padding: 14px 28px; margin: 10px; background: #1d5bd8; color: #fff; border-radius: 10px; font: 600 15px sans-serif; cursor: pointer; transition: all .35s ease; }
  .b:hover { background: #0e2a5c; transform: translateY(-4px) scale(1.05); box-shadow: 0 10px 20px rgba(14,42,92,.3); }
  .w { width: 120px; transition: width .6s; background: #0e7a4f; color: #fff; padding: 12px; font: 14px sans-serif; border-radius: 8px; }
  .w:hover { width: 300px; }
</style>
<div class="b">Hover me</div>
<div class="w">Hover: grows</div>''',
  None,
  [("Which property defines how long a transition lasts?", ["transition-duration", "transition-speed", "transition-time-limit", "animate-for"], 0),
   ("Which two properties are cheapest for browsers to animate?", ["transform and opacity", "width and height", "margin and padding", "top and left"], 0),
   ("Where should `transition` usually be written?", ["On the normal (non-hover) rule", "Only on :hover", "Inside a media query", "In the HTML"], 0)]),

L("css-animations", "CSS Animations", "Effects & Animation",
  "Animations run automatically through a series of steps called keyframes, with no hover or click needed.",
  [("Define keyframes", "`@keyframes` names the animation and describes what styles apply at `from` and `to`, or at percentages.",
    "<style>\n  @keyframes pulse {\n    0%   { transform: scale(1); }\n    50%  { transform: scale(1.2); }\n    100% { transform: scale(1); }\n  }\n</style>"),
   ("Apply it", "`animation: pulse 2s ease-in-out infinite` sets the name, duration, timing and repeat count in one line."),
   ("More controls", "`animation-delay`, `animation-direction: alternate`, `animation-fill-mode: forwards` and `animation-play-state: paused` fine-tune playback."),
   ("Respect motion preferences", "Wrap large movement in `@media (prefers-reduced-motion: no-preference)` or disable it for users who ask for less motion.")],
  '''<style>
  @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.25); } }
  @keyframes slide { from { left: 0; } to { left: calc(100% - 60px); } }
  .dot { width: 70px; height: 70px; margin: 14px; background: #1d5bd8; border-radius: 50%; animation: pulse 1.6s ease-in-out infinite; }
  .track { position: relative; height: 60px; background: #eaf2ff; border-radius: 10px; }
  .ball { position: absolute; top: 0; width: 60px; height: 60px; background: #0e7a4f; border-radius: 50%; animation: slide 2s ease-in-out infinite alternate; }
  @media (prefers-reduced-motion: reduce) { .dot, .ball { animation: none; } }
</style>
<div class="dot"></div>
<div class="track"><div class="ball"></div></div>''',
  None,
  [("Which at-rule defines the steps of an animation?", ["@keyframes", "@animate", "@steps", "@motion"], 0),
   ("What does `animation-iteration-count: infinite` do?", ["Repeats the animation forever", "Plays it once", "Pauses it", "Reverses the page"], 0),
   ("Why use `prefers-reduced-motion`?", ["To respect users who want less movement", "To make animations faster", "To enable GPU drawing", "To change fonts"], 0)]),

L("css-filters", "CSS Filters", "Effects & Animation",
  "`filter` applies visual effects such as blur, brightness and grayscale to an element, which is great for images and hover effects.",
  [("Filter functions", "`blur(4px)`, `brightness(120%)`, `contrast()`, `grayscale(100%)`, `sepia()`, `hue-rotate(90deg)`, `invert()`, `saturate()` and `drop-shadow()`."),
   ("Combine them", "Chain several filters with spaces, in the order you want them applied: `filter: grayscale(50%) blur(2px)`."),
   ("backdrop-filter", "`backdrop-filter: blur(8px)` blurs what is behind an element, giving a frosted-glass look on translucent panels.")],
  '''<style>
  .p { display: inline-block; width: 90px; height: 90px; margin: 6px; border-radius: 12px; background: linear-gradient(135deg, #1d5bd8, #ffd479); color: #fff; font: 12px sans-serif; text-align: center; line-height: 90px; }
</style>
<div class="p">normal</div>
<div class="p" style="filter: grayscale(100%);">grayscale</div>
<div class="p" style="filter: blur(2px);">blur</div>
<div class="p" style="filter: hue-rotate(120deg);">hue</div>
<div class="p" style="filter: invert(100%);">invert</div>''',
  None,
  [("Which filter function converts an element to black and white?", ["grayscale(100%)", "mono()", "bw()", "desaturate-all()"], 0),
   ("Which property blurs the content behind a translucent element?", ["backdrop-filter", "filter-behind", "background-blur", "blur-back"], 0)]),

L("css-cursor", "CSS Cursor and User Interaction", "Effects & Animation",
  "The `cursor` property changes the mouse pointer, and a few related properties control how users interact with elements.",
  [("Cursor values", "`pointer` (hand), `default`, `text`, `move`, `grab`, `not-allowed`, `wait`, `help` and `crosshair` tell users what an element does."),
   ("pointer-events and user-select", "`pointer-events: none` makes an element ignore the mouse. `user-select: none` stops text from being selected."),
   ("Smooth scrolling", "`scroll-behavior: smooth` animates jumps to anchor links.")],
  '''<style>
  .c { display: inline-block; margin: 6px; padding: 14px 18px; background: #eaf2ff; border: 2px solid #1d5bd8; border-radius: 10px; font: 14px sans-serif; }
</style>
<div class="c" style="cursor: pointer;">pointer</div>
<div class="c" style="cursor: not-allowed;">not-allowed</div>
<div class="c" style="cursor: help;">help</div>
<div class="c" style="cursor: move;">move</div>
<div class="c" style="cursor: crosshair;">crosshair</div>''',
  "Use `cursor: pointer` only on things that are clickable.",
  [("Which cursor value shows a hand over clickable elements?", ["pointer", "hand", "click", "link"], 0),
   ("What does `user-select: none` do?", ["Prevents text selection", "Hides the cursor", "Disables scrolling", "Blocks all clicks"], 0)]),

# ============================================================ Responsive Design
L("css-media-queries", "CSS Media Queries", "Responsive Design",
  "Media queries apply CSS only when conditions such as screen width are met. They are the core of responsive design.",
  [("Syntax", "`@media (condition) { rules }`. The most common condition is viewport width.",
    "<style>\n  @media (max-width: 600px) {\n    .sidebar { display: none; }\n  }\n</style>"),
   ("Breakpoints", "Pick breakpoints where your content starts to look wrong, not specific devices. Common values are around 600px, 900px and 1200px."),
   ("Other features", "`orientation: landscape`, `prefers-color-scheme: dark`, `prefers-reduced-motion`, `hover: hover` and `print` can all be queried. Combine with `and`, `,` (or) and `not`."),
   ("Do not forget the viewport", "Pages need `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">` so phones use their real width.")],
  '''<style>
  .box { padding: 20px; font: 600 18px sans-serif; color: #fff; text-align: center; background: #1d5bd8; }
  .box::after { content: " - wide layout (over 500px)"; }
  @media (max-width: 500px) {
    .box { background: #0e7a4f; }
    .box::after { content: " - narrow layout (500px or less)"; }
  }
</style>
<div class="box">Resize the preview</div>''',
  "Use the full-screen option and drag the browser window to watch queries switch on and off.",
  [("Which at-rule applies styles conditionally by screen size?", ["@media", "@screen-size", "@responsive", "@if"], 0),
   ("Which meta tag makes a page use the device width on phones?", ["viewport", "responsive", "device", "mobile-width"], 0),
   ("What does `max-width: 600px` in a media query mean?", ["The viewport is 600px wide or narrower", "The viewport is at least 600px wide", "Exactly 600px wide", "The element is 600px wide"], 0)]),

L("css-responsive-images", "CSS Responsive Images and Media", "Responsive Design",
  "Images and videos should shrink with their container instead of overflowing on a small screen.",
  [("Fluid images", "`max-width: 100%; height: auto;` stops an image from exceeding its container while keeping its proportions."),
   ("Aspect ratio", "`aspect-ratio: 16 / 9` reserves the right shape for a video or card before it loads, which avoids layout jumps."),
   ("Art direction", "In HTML, `<picture>` with `<source media>` or `srcset` and `sizes` let the browser pick a suitable image file. CSS handles the display size.",
    "<style>\n  img, video { max-width: 100%; height: auto; }\n  .video { aspect-ratio: 16 / 9; }\n</style>")],
  '''<style>
  .frame { width: 70%; min-width: 180px; border: 2px dashed #1d5bd8; padding: 6px; }
  img { max-width: 100%; height: auto; display: block; border-radius: 8px; }
  .ratio { aspect-ratio: 16 / 9; background: #0e2a5c; color: #fff; display: grid; place-items: center; border-radius: 8px; font: 15px sans-serif; margin-top: 8px; }
</style>
<div class="frame">
  <img alt="wide blue banner" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='200'><rect width='800' height='200' fill='%231d5bd8'/><text x='400' y='115' fill='white' font-size='48' text-anchor='middle'>800 x 200 image</text></svg>">
  <div class="ratio">aspect-ratio: 16 / 9</div>
</div>''',
  None,
  [("Which pair of declarations makes an image scale down inside its container?", ["max-width: 100%; height: auto", "width: 1000px; height: 100%", "float: left; clear: both", "display: none; width: auto"], 0),
   ("What does `aspect-ratio: 16 / 9` do?", ["Keeps the box at a 16 to 9 shape", "Sets the width to 16px", "Rotates the box", "Changes the font ratio"], 0)]),

L("css-mobile-first", "CSS Mobile-first Design", "Responsive Design",
  "Mobile-first means writing the small-screen styles first and adding enhancements for larger screens with `min-width` queries.",
  [("Why mobile first?", "Phones are the most common devices, and a simple single-column layout is the easiest starting point. Extra columns and spacing are added only when there is room."),
   ("min-width queries", "Base styles have no query. Each larger breakpoint adds to them with `@media (min-width: 700px)`.",
    "<style>\n  .cards { display: grid; gap: 12px; }              /* 1 column */\n  @media (min-width: 700px) {\n    .cards { grid-template-columns: repeat(3, 1fr); } /* 3 columns */\n  }\n</style>"),
   ("Benefits", "Smaller devices download less CSS to override, and the code is easier to reason about.")],
  '''<style>
  .cards { display: grid; gap: 10px; }
  .cards div { background: #eaf2ff; border: 2px solid #1d5bd8; padding: 18px; border-radius: 10px; font: 15px sans-serif; text-align: center; }
  @media (min-width: 520px) { .cards { grid-template-columns: repeat(3, 1fr); } }
</style>
<div class="cards"><div>Card 1</div><div>Card 2</div><div>Card 3</div></div>''',
  None,
  [("Which media feature is typical in a mobile-first stylesheet?", ["min-width", "max-width only", "orientation only", "print only"], 0),
   ("In mobile-first CSS, where are the small-screen styles written?", ["Outside any media query", "Inside max-width: 300px only", "In a separate HTML file", "After all other styles inside @print"], 0)]),

L("css-dark-mode", "CSS Dark Mode", "Responsive Design",
  "Websites can follow the visitor's system theme using the `prefers-color-scheme` media query, ideally together with CSS variables.",
  [("The media query", "`@media (prefers-color-scheme: dark)` applies rules when the user's operating system is in dark mode."),
   ("Use variables", "Define colours once as custom properties, then override them inside the query. The rest of the CSS stays unchanged.",
    "<style>\n  :root { --bg: #fff; --text: #0e2a5c; }\n  @media (prefers-color-scheme: dark) {\n    :root { --bg: #0b1220; --text: #e6eeff; }\n  }\n  body { background: var(--bg); color: var(--text); }\n</style>"),
   ("color-scheme", "`color-scheme: light dark` tells the browser to style built-in controls such as scrollbars and form fields to match.")],
  '''<style>
  :root { color-scheme: light dark; --bg: #ffffff; --text: #0e2a5c; --accent: #1d5bd8; }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #0b1220; --text: #e6eeff; --accent: #7fb0ff; }
  }
  body { background: var(--bg); color: var(--text); font: 17px sans-serif; padding: 16px; }
  h2 { color: var(--accent); margin-top: 0; }
</style>
<h2>Theme aware</h2>
<p>Switch your device between light and dark mode and this preview follows it.</p>''',
  None,
  [("Which media query detects a dark system theme?", ["prefers-color-scheme: dark", "dark-mode: on", "theme: night", "color: dark"], 0),
   ("Why combine dark mode with CSS variables?", ["You change colours in one place", "Variables make text bold", "Variables disable media queries", "It is required by the spec"], 0)]),

L("css-units", "CSS Units", "Responsive Design",
  "CSS has absolute and relative units. Choosing relative units makes designs adapt to screens and user settings.",
  [("Absolute units", "`px` is the everyday absolute unit. `cm`, `mm`, `in`, `pt` are mainly for print."),
   ("Relative to text", "`em` is relative to the element's font size. `rem` is relative to the root (`html`) font size, which makes it predictable. `ch` is the width of the digit 0."),
   ("Relative to the viewport", "`vw` and `vh` are 1% of the viewport width and height. `dvh` follows mobile browser bars correctly. `vmin` and `vmax` use the smaller or larger side."),
   ("Percentages", "`%` is relative to the parent for width, and to different references for other properties.")],
  '''<style>
  html { font-size: 16px; }
  .u { background: #1d5bd8; color: #fff; padding: 6px 10px; margin: 6px 0; font: 14px sans-serif; }
</style>
<div class="u" style="width: 200px;">200px</div>
<div class="u" style="width: 50%;">50% of parent</div>
<div class="u" style="width: 20rem; max-width: 100%;">20rem (320px)</div>
<div class="u" style="width: 40vw;">40vw</div>''',
  "Use `rem` for font sizes and spacing, `px` for thin borders, and `%` or `fr` for layout widths.",
  [("Which unit is relative to the root element's font size?", ["rem", "em", "px", "pt"], 0),
   ("What is `1vw`?", ["1% of the viewport width", "1px wide", "1% of the parent width", "One word width"], 0),
   ("Which unit is relative to the font size of the current element?", ["em", "rem", "vh", "cm"], 0)]),

# ============================================================ Advanced
L("css-variables", "CSS Variables (Custom Properties)", "Advanced",
  "Custom properties store a value once and reuse it everywhere. They are the foundation of themes and design systems.",
  [("Define and use", "Names start with two dashes. Define them on `:root` to make them global, and read them with `var()`.",
    "<style>\n  :root { --brand: #1d5bd8; --radius: 10px; }\n  .btn { background: var(--brand); border-radius: var(--radius); }\n</style>"),
   ("Fallbacks", "`var(--space, 16px)` uses 16px if `--space` is not defined."),
   ("Scoped and dynamic", "Variables follow the cascade, so you can override them for one component. Unlike preprocessor variables, they can change at runtime with JavaScript or media queries.")],
  '''<style>
  :root { --brand: #1d5bd8; --radius: 12px; --space: 14px; }
  .btn { background: var(--brand); color: #fff; padding: var(--space) calc(var(--space) * 2); border-radius: var(--radius); border: 0; font: 600 15px sans-serif; margin: 4px; }
  .alt { --brand: #0e7a4f; }
</style>
<button class="btn">Default brand</button>
<button class="btn alt">Overridden variable</button>''',
  None,
  [("How do variable names begin in CSS custom properties?", ["With two dashes (--)", "With a dollar sign", "With an at sign", "With a hash"], 0),
   ("Which function reads a custom property?", ["var()", "get()", "use()", "env-read()"], 0),
   ("Where are global CSS variables usually defined?", [":root", "body > p", "::after", "@import"], 0)]),

L("css-calc-min-max-clamp", "CSS calc(), min(), max() and clamp()", "Advanced",
  "CSS maths functions let you mix units and create fluid sizes without media queries.",
  [("calc()", "Does arithmetic with mixed units: `width: calc(100% - 40px)`. Put spaces around `+` and `-`."),
   ("min() and max()", "`min(90%, 600px)` picks the smaller value, so it works like `max-width`. `max(16px, 2vw)` picks the larger one."),
   ("clamp()", "`clamp(min, preferred, max)` keeps a value between two limits. It is perfect for fluid type.",
    "<style>\n  h1 { font-size: clamp(1.5rem, 4vw, 3rem); }\n</style>")],
  '''<style>
  .bar { background: #eaf2ff; padding: 6px; margin: 6px 0; font: 14px sans-serif; }
  .bar div { background: #1d5bd8; color: #fff; padding: 10px; }
  h2 { font-size: clamp(1.1rem, 4vw, 2rem); color: #0e2a5c; margin: 8px 0; font-family: sans-serif; }
</style>
<div class="bar"><div style="width: calc(100% - 60px);">calc(100% - 60px)</div></div>
<div class="bar"><div style="width: min(80%, 300px);">min(80%, 300px)</div></div>
<h2>Fluid heading with clamp()</h2>''',
  None,
  [("What does `clamp(1rem, 3vw, 2rem)` do?", ["Keeps the value between 1rem and 2rem", "Always returns 3vw", "Returns the smallest of three", "Rounds to whole rem"], 0),
   ("Which function picks the smaller of its values?", ["min()", "max()", "clamp() only", "least()"], 0),
   ("What is required inside `calc()` around plus and minus?", ["Spaces", "Quotes", "Semicolons", "Brackets of type []"], 0)]),

L("css-counters", "CSS Counters", "Advanced",
  "CSS counters number headings, steps or list items automatically, without changing the HTML.",
  [("Three steps", "Reset a counter on a parent with `counter-reset`, increase it on each item with `counter-increment`, and display it with `counter()` in `content`.",
    "<style>\n  ol.steps { counter-reset: step; list-style: none; }\n  ol.steps li::before { counter-increment: step; content: 'Step ' counter(step) ': '; }\n</style>"),
   ("Nested counters", "`counters(name, '.')` joins nested levels like 1.2.3, useful for outlines.")],
  '''<style>
  body { counter-reset: section; font: 17px sans-serif; }
  h3 { counter-reset: sub; color: #0e2a5c; margin: 12px 0 4px; }
  h3::before { counter-increment: section; content: "Section " counter(section) ". "; color: #1d5bd8; }
  p::before { counter-increment: sub; content: counter(section) "." counter(sub) "  "; color: #1d5bd8; font-weight: 700; }
  p { margin: 2px 0; }
</style>
<h3>Basics</h3><p>First point</p><p>Second point</p>
<h3>Layout</h3><p>First point</p><p>Second point</p>''',
  None,
  [("Which property increases a counter?", ["counter-increment", "counter-add", "counter-up", "increment"], 0),
   ("Which function shows a counter's value in generated content?", ["counter()", "number()", "count()", "value()"], 0)]),

L("css-best-practices", "CSS Best Practices", "Advanced",
  "Good habits keep a stylesheet small, predictable and easy to change. This chapter pulls the earlier lessons together.",
  [("Organise", "Group related rules, keep a consistent order (layout, box, text, visual), and comment sections. Use meaningful class names such as `.card-title`, not `.blue-text`."),
   ("Keep specificity low", "Style with classes, avoid ids and `!important`, and avoid long selector chains. Low specificity means easy overrides."),
   ("Use modern tools", "Use `box-sizing: border-box`, flexbox and grid for layout, variables for design tokens, and relative units for accessibility."),
   ("Accessibility and performance", "Keep a text contrast ratio of at least 4.5:1, never hide focus outlines, respect `prefers-reduced-motion`, and avoid huge unused CSS files."),
   ("Test", "Check in several browsers and screen sizes, validate your CSS, and use developer tools to inspect problems.")],
  '''<style>
  :root { --brand: #1d5bd8; --ink: #0e2a5c; --space: 16px; }
  *, *::before, *::after { box-sizing: border-box; }
  body { font: 1rem/1.6 system-ui, sans-serif; color: var(--ink); margin: 0; padding: var(--space); }
  .card { max-width: 340px; padding: var(--space); border: 1px solid #d5e1f5; border-radius: 12px; }
  .card__title { margin: 0 0 8px; color: var(--brand); }
  .card__link { color: var(--brand); }
  .card__link:focus-visible { outline: 3px solid #cfe0ff; outline-offset: 2px; }
</style>
<article class="card">
  <h3 class="card__title">Tidy CSS</h3>
  <p>Classes, variables, low specificity and a visible focus ring.</p>
  <a class="card__link" href="#">Read more</a>
</article>''',
  None,
  [("Which is a good approach to selectors?", ["Use classes and keep specificity low", "Use ids and !important everywhere", "Use long nested selector chains", "Style every element inline"], 0),
   ("What is the recommended minimum contrast ratio for normal text?", ["4.5:1", "1.5:1", "2:1", "10:1"], 0),
   ("Why name a class `.card-title` instead of `.blue-text`?", ["It describes purpose, so the colour can change freely", "Blue is not a valid word", "Class names must contain hyphens only", "It loads faster"], 0)]),
]

# ------------------------------------------------------------------------------------
# Shuffle each question's options once (fixed seed) so the right answer is not always first.
import random as _random

for _lesson in LESSONS:
    for _q in _lesson["exercise"]:
        _right = _q["options"][_q["answer"]]
        _rng = _random.Random(_lesson["slug"] + _q["q"])
        _rng.shuffle(_q["options"])
        _q["answer"] = _q["options"].index(_right)

BY_SLUG = {l["slug"]: l for l in LESSONS}
