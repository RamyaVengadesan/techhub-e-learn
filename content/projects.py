"""Guided build projects for TechHub.

Each project: slug, title, level, minutes, skills, summary, goal, steps[{title, text, code?}], final, tips.
`final` is assembled from the very same code snippets the steps show, so the steps always add up to the
finished project. In text fields, backtick spans and <tag> mentions render as inline code.
"""
import textwrap


def _indent(text, n):
    pad = " " * n
    return "\n".join((pad + line) if line.strip() else "" for line in text.strip("\n").splitlines())


def step(title, text, html=None, css=None, js=None, show=None, html_show=None):
    """One build step. html/css/js are appended to the finished page; `show` overrides the displayed code."""
    if show is None:
        parts = []
        if html_show or html:
            parts.append("<!-- Add inside the page (in <body>) -->\n" + (html_show or html).strip("\n"))
        if css:
            parts.append("/* Add inside <style> */\n" + css.strip("\n"))
        if js:
            parts.append("// Add inside <script>\n" + js.strip("\n"))
        show = "\n\n".join(parts)
    out = dict(title=title, text=text, _html=html, _css=css, _js=js)
    if show:
        out["code"] = show
    return out


def skeleton(title, note="base styles go here"):
    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{title}</title>
          <style>
            /* {note} */
          </style>
        </head>
        <body>
          <!-- page content goes here -->
        </body>
        </html>""")


def project(slug, title, level, minutes, skills, summary, goal, steps, tips, wrap=("<main>", "</main>")):
    htmls = [s["_html"].strip("\n") for s in steps if s["_html"]]
    csss = [s["_css"].strip("\n") for s in steps if s["_css"]]
    jss = [s["_js"].strip("\n") for s in steps if s["_js"]]
    body = "\n\n".join(htmls)
    if wrap:
        body = f"{wrap[0]}\n{_indent(body, 2)}\n{wrap[1]}"
    final = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{title}</title>\n  <style>\n{_indent(chr(10).join(['', *csss]).replace(chr(10) + chr(10), chr(10) + chr(10)), 4)}\n  </style>\n</head>\n<body>\n"
        f"{_indent(body, 2)}\n"
    )
    if jss:
        final += f"  <script>\n{_indent(chr(10).join(jss), 4)}\n  </script>\n"
    final += "</body>\n</html>\n"
    clean = [{k: v for k, v in s.items() if not k.startswith("_")} for s in steps]
    return dict(slug=slug, title=title, level=level, minutes=minutes, skills=skills, summary=summary,
                goal=goal, steps=clean, final=final, tips=tips)


BASE_BLUE = """
* { box-sizing: border-box; }
body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 24px;
  background: #eaf1fd;
  color: #17233d;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}
"""

PROJECTS = []

# ============================================================================ 1. Profile page
PROJECTS.append(project(
    "proj-profile-page", "Personal Profile Page", "beginner", 30, ["HTML", "CSS", "Centering", "Flexbox"],
    "Build a clean, centred profile card with an avatar, bio, skill tags and buttons.",
    "You will build a single profile card page. Along the way you practise the document structure, text elements, a list, links styled as buttons, and centring with CSS.",
    [
        step("Create the page and base styles",
             "Every page starts with the same skeleton. The `viewport` meta tag makes the page scale correctly on phones. Then add a few base styles: `box-sizing: border-box` makes widths include padding (far easier to reason about), and a grid on `<body>` with `place-items: center` centres the card in the window.",
             show=skeleton("Profile Page") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Add the card container",
             "Everything lives inside one `<main>` element. It is a landmark, so screen readers can jump straight to the content. The `max-width` keeps the card readable on big screens, and `width: 100%` lets it shrink on small ones.",
             html_show='<main class="card">\n  <!-- everything else goes here -->\n</main>',
             css="""
.card {
  width: 100%;
  max-width: 440px;
  padding: 32px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(11, 46, 122, .12);
  text-align: center;
}"""),
        step("Add an avatar",
             "No image files are needed: a circle made with `border-radius: 50%` and the person's initials works well. `aria-hidden=\"true\"` stops screen readers from reading the initials twice, because the name comes right after.",
             html='<div class="avatar" aria-hidden="true">AR</div>',
             css="""
.avatar {
  width: 96px;
  height: 96px;
  margin: 0 auto 16px;
  border-radius: 50%;
  background: #1d4ed8;
  color: #fff;
  display: grid;
  place-items: center;
  font-size: 2rem;
  font-weight: 700;
}"""),
        step("Add the name and role",
             "Use one `<h1>` for the name: it is the main heading of the page. Style the role with a class so you can change it without touching the heading. Resetting the heading margin gives you full control of the spacing.",
             html='<h1>Asha Rao</h1>\n<p class="role">Front-end developer in training</p>',
             css="""
h1 {
  margin: 0;
  font-size: 1.6rem;
  color: #0b2e7a;
}
.role {
  margin: 4px 0 16px;
  color: #1d4ed8;
  font-weight: 600;
}"""),
        step("Write a short bio",
             "Keep the bio to a sentence or two. Muted text colour creates a visual hierarchy: name first, role second, details third.",
             html='<p class="bio">I am learning HTML, CSS and JavaScript by building small projects. My next goal is my first responsive website.</p>',
             css="""
.bio {
  margin: 0;
  color: #4a5a78;
}"""),
        step("List your skills as tags",
             "A list of skills is a real list, so use `<ul>` and `<li>`. Flexbox with `flex-wrap` and `gap` lays the items out in a row that wraps on small screens, and `border-radius: 999px` turns each item into a pill.",
             html="""<ul class="skills">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Git</li>
  <li>Responsive design</li>
</ul>""",
             css="""
.skills {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin: 20px 0;
  padding: 0;
  list-style: none;
}
.skills li {
  padding: 4px 12px;
  border-radius: 999px;
  background: #e8f0ff;
  color: #1740b0;
  font-size: .9rem;
  font-weight: 600;
}"""),
        step("Add link buttons",
             "Links that go somewhere should be `<a>` elements, not `<button>`s. Style them to look like buttons with padding, a background and rounded corners. `.ghost` is a second style for the less important action.",
             html="""<div class="links">
  <a class="btn" href="#">View projects</a>
  <a class="btn ghost" href="#">Contact me</a>
</div>""",
             css="""
.links {
  display: flex;
  justify-content: center;
  gap: 10px;
}
.btn {
  padding: 10px 18px;
  border: 2px solid #1d4ed8;
  border-radius: 8px;
  background: #1d4ed8;
  color: #fff;
  font-weight: 600;
  text-decoration: none;
}
.btn.ghost {
  background: #fff;
  color: #1d4ed8;
}"""),
        step("Polish: hover, focus and small screens",
             "Interactive things need visible states. `:hover` is for mouse users and `:focus-visible` is for keyboard users, so never remove the focus outline without replacing it. The media query tightens the padding on narrow phones.",
             css="""
.btn:hover {
  background: #1740b0;
  border-color: #1740b0;
  color: #fff;
}
.btn:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 2px;
}
@media (max-width: 480px) {
  .card { padding: 24px 20px; }
}"""),
    ],
    ["Replace the initials with a real photo using `<img>` and `border-radius: 50%`, and add `alt` text.",
     "Add a second section with your three favourite projects as a list of links.",
     "Change the colour scheme by editing just the blues, then try dark colours with a light card."],
    wrap=("<main class=\"card\">", "</main>")))

# ============================================================================ 2. Landing page
PROJECTS.append(project(
    "proj-landing-page", "Responsive Landing Page", "beginner", 45, ["HTML", "CSS", "Grid", "Responsive design"],
    "Create a landing page with a header, hero, three feature cards, a call-to-action band and a footer.",
    "You will build the layout most websites start with. You practise semantic elements, a centred container, CSS Grid with `auto-fit`, and a small media query so it also works on phones.",
    [
        step("Create the page and a centred container",
             "Start with the skeleton and base styles. The `.page` wrapper has a `max-width` and `margin: 0 auto`, which keeps line lengths readable on wide screens while staying fluid on small ones.",
             show=skeleton("Flowly") + """

/* Add inside <style> */
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f4f8ff;
  color: #17233d;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}
.page {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 20px 24px;
}""",
             css="""
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f4f8ff;
  color: #17233d;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}
.page {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 20px 24px;
}"""),
        step("Add the header",
             "A `<header>` holds the brand and navigation. Flexbox with `justify-content: space-between` pushes the brand to one side and the links to the other.",
             html="""<header class="site-header">
  <a class="brand" href="#">Flowly</a>
  <nav aria-label="Main">
    <a href="#features">Features</a>
    <a href="#start">Get started</a>
  </nav>
</header>""",
             css="""
.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 0;
}
.brand {
  font-size: 1.4rem;
  font-weight: 800;
  color: #0b2e7a;
  text-decoration: none;
}
.site-header nav a {
  margin-left: 18px;
  color: #2a3a5c;
  font-weight: 600;
  text-decoration: none;
}
.site-header nav a:hover { color: #1d4ed8; }"""),
        step("Add the hero section",
             "The hero is the first thing visitors see, so it needs one clear message and one clear action. `clamp()` makes the heading scale smoothly with the screen width, so no media query is needed for the font size.",
             html="""<section class="hero">
  <h1>Plan your work without the chaos</h1>
  <p>Flowly keeps tasks, notes and deadlines in one calm place, so your team always knows what is next.</p>
  <a class="btn" href="#start">Start for free</a>
</section>""",
             css="""
.hero {
  padding: 56px 0 48px;
  text-align: center;
}
.hero h1 {
  max-width: 18ch;
  margin: 0 auto 12px;
  font-size: clamp(2rem, 6vw, 3rem);
  line-height: 1.15;
  color: #0b2e7a;
}
.hero p {
  max-width: 52ch;
  margin: 0 auto 24px;
  color: #4a5a78;
  font-size: 1.1rem;
}
.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 8px;
  background: #1d4ed8;
  color: #fff;
  font-weight: 700;
  text-decoration: none;
}
.btn:hover { background: #1740b0; }"""),
        step("Add three feature cards",
             "Features are a repeating pattern, which is exactly what CSS Grid is for. `repeat(auto-fit, minmax(200px, 1fr))` means: make as many columns as fit, each at least 200px wide. The layout becomes responsive with a single line.",
             html="""<section id="features" class="features">
  <h2>Why teams choose Flowly</h2>
  <div class="grid">
    <article class="feature">
      <h3>Everything in one place</h3>
      <p>Tasks, notes and files live together, so nothing gets lost.</p>
    </article>
    <article class="feature">
      <h3>Clear priorities</h3>
      <p>See what matters today and what can wait until later.</p>
    </article>
    <article class="feature">
      <h3>Works for teams</h3>
      <p>Share a board and let everyone see progress at a glance.</p>
    </article>
  </div>
</section>""",
             css="""
.features h2 {
  margin: 0 0 16px;
  text-align: center;
  color: #0b2e7a;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}"""),
        step("Style the cards",
             "A white background, a thin border and a soft hover lift make the cards feel like separate pieces. A `transition` makes the hover movement smooth instead of abrupt.",
             css="""
.feature {
  padding: 20px;
  border: 1px solid #d3def2;
  border-top: 4px solid #1d4ed8;
  border-radius: 10px;
  background: #fff;
  transition: transform .2s, box-shadow .2s;
}
.feature h3 { margin: 0 0 6px; color: #0b2e7a; }
.feature p { margin: 0; color: #4a5a78; }
.feature:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 24px rgba(11, 46, 122, .14);
}"""),
        step("Add a call-to-action band",
             "End the page with one more clear action. A full-width coloured band stands out from the white cards, and white text on a dark blue keeps good contrast.",
             html="""<section id="start" class="cta">
  <h2>Ready to get organised?</h2>
  <p>Create a free account in under a minute. No card needed.</p>
  <a class="btn btn-light" href="#">Create free account</a>
</section>""",
             css="""
.cta {
  margin-top: 40px;
  padding: 36px 20px;
  border-radius: 14px;
  background: #0b2e7a;
  color: #fff;
  text-align: center;
}
.cta h2 { margin: 0 0 6px; }
.cta p { margin: 0 0 18px; color: #cfe0ff; }
.btn-light {
  background: #fff;
  color: #0b2e7a;
}
.btn-light:hover { background: #e8f0ff; }"""),
        step("Add a footer",
             "A `<footer>` closes the page. Small, muted text keeps it from competing with the content above.",
             html='<footer class="site-footer">\n  <p>&copy; 2026 Flowly. Built while learning HTML and CSS.</p>\n</footer>',
             css="""
.site-footer {
  padding-top: 24px;
  text-align: center;
  color: #5b6b86;
  font-size: .9rem;
}"""),
        step("Make it work on small screens and with a keyboard",
             "Stack the header on narrow phones so the links never crowd the brand. Add `:focus-visible` outlines so keyboard users can see where they are. Then resize the preview to test it.",
             css="""
a:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 3px;
}
@media (max-width: 560px) {
  .site-header {
    flex-direction: column;
    gap: 6px;
  }
  .site-header nav a { margin: 0 9px; }
}"""),
    ],
    ["Add a fourth feature card and watch the grid reflow by itself.",
     "Add a testimonial section with a quote and a name using `<blockquote>`.",
     "Move the colours into CSS variables (`--blue: #1d4ed8`) so you can re-theme the page in one place."],
    wrap=("<div class=\"page\">", "</div>")))

# ============================================================================ 3. Pricing cards
PROJECTS.append(project(
    "proj-pricing-cards", "Pricing Cards", "intermediate", 40, ["CSS", "Grid", "Flexbox", "Hover effects", "Pseudo-elements"],
    "Design three pricing cards with a highlighted plan, check-mark lists and smooth hover effects.",
    "You will build a pricing section with CSS Grid, align the buttons at the bottom of equal-height cards with Flexbox, add check marks with `::before`, and highlight the featured plan with a badge and a lift.",
    [
        step("Create the page and base styles",
             "Start from the usual skeleton and add base styles. Using a grid on `<body>` centres everything and gives you a simple way to keep the section away from the screen edges.",
             show=skeleton("Pricing Cards") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Make the grid container and heading",
             "The `<main>` becomes a grid. `auto-fit` with `minmax(220px, 1fr)` gives one, two or three columns depending on the available width. The intro spans every column with `grid-column: 1 / -1`.",
             html='<header class="intro">\n  <h1>Simple pricing</h1>\n  <p>Pick a plan. Change it any time.</p>\n</header>',
             html_show='<main class="plans">\n  <header class="intro">\n    <h1>Simple pricing</h1>\n    <p>Pick a plan. Change it any time.</p>\n  </header>\n  <!-- plan cards go here -->\n</main>',
             css="""
.plans {
  width: 100%;
  max-width: 900px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}
.intro {
  grid-column: 1 / -1;
  text-align: center;
}
.intro h1 { margin: 0; color: #0b2e7a; }
.intro p { margin: 4px 0 8px; color: #4a5a78; }"""),
        step("Build the first plan card",
             "Each plan is an `<article>` with a heading, a price, a feature list and a button. Putting the `/month` inside a `<span>` lets you style it smaller than the number.",
             html="""<article class="plan">
  <h2>Starter</h2>
  <p class="price">$0<span>/month</span></p>
  <ul>
    <li>1 project</li>
    <li>Community support</li>
    <li>Basic analytics</li>
  </ul>
  <a class="btn" href="#">Start free</a>
</article>""",
             css="""
.plan {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 28px 24px;
  border: 2px solid #d3def2;
  border-radius: 14px;
  background: #fff;
}
.plan h2 {
  margin: 0 0 8px;
  font-size: 1.1rem;
  color: #1d4ed8;
}"""),
        step("Style the price, list and button",
             "`flex: 1` on the list makes it absorb the spare height, so the buttons of all cards line up at the bottom even when the lists have different lengths. The check marks are drawn with `::before`, so they need no extra HTML.",
             css="""
.price {
  margin: 0 0 16px;
  font-size: 2.4rem;
  font-weight: 800;
  color: #0b2e7a;
}
.price span {
  font-size: 1rem;
  font-weight: 500;
  color: #5b6b86;
}
.plan ul {
  flex: 1;
  margin: 0 0 24px;
  padding: 0;
  list-style: none;
}
.plan li {
  padding: 5px 0 5px 26px;
  position: relative;
}
.plan li::before {
  content: "\\2713";
  position: absolute;
  left: 0;
  color: #0e7a4f;
  font-weight: 700;
}
.btn {
  display: block;
  padding: 11px 16px;
  border: 2px solid #1d4ed8;
  border-radius: 8px;
  background: #fff;
  color: #1d4ed8;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
}
.btn:hover {
  background: #1d4ed8;
  color: #fff;
}"""),
        step("Add the Pro and Team plans",
             "Copy the card twice and change the content. The Pro card gets an extra class, `featured`, which is the hook for the next step. Reusing one class for all cards keeps the CSS short.",
             html="""<article class="plan featured">
  <h2>Pro</h2>
  <p class="price">$12<span>/month</span></p>
  <ul>
    <li>Unlimited projects</li>
    <li>Priority support</li>
    <li>Advanced analytics</li>
    <li>Custom domain</li>
  </ul>
  <a class="btn" href="#">Choose Pro</a>
</article>

<article class="plan">
  <h2>Team</h2>
  <p class="price">$29<span>/month</span></p>
  <ul>
    <li>Everything in Pro</li>
    <li>5 team members</li>
    <li>Shared workspaces</li>
  </ul>
  <a class="btn" href="#">Choose Team</a>
</article>"""),
        step("Highlight the featured plan",
             "A filled background, a lifted position and a badge make the featured plan stand out. The badge is another `::before`, positioned over the top edge of the card.",
             css="""
.plan.featured {
  border-color: #1d4ed8;
  background: #1d4ed8;
  color: #fff;
  transform: translateY(-8px);
}
.plan.featured h2,
.plan.featured .price,
.plan.featured .price span { color: #fff; }
.plan.featured li::before { color: #9be5b8; }
.plan.featured .btn {
  border-color: #fff;
  background: #fff;
  color: #1740b0;
}
.plan.featured::before {
  content: "Most popular";
  position: absolute;
  top: -13px;
  left: 50%;
  transform: translateX(-50%);
  padding: 2px 14px;
  border-radius: 999px;
  background: #0b2e7a;
  color: #fff;
  font-size: .78rem;
  font-weight: 700;
  white-space: nowrap;
}"""),
        step("Add hover effects",
             "A `transition` on `transform` and `box-shadow` animates the hover. The featured card already uses `transform`, so give it its own hover rule that lifts it a little further.",
             css="""
.plan {
  transition: transform .2s, box-shadow .2s;
}
.plan:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 30px rgba(11, 46, 122, .16);
}
.plan.featured:hover {
  transform: translateY(-12px);
}"""),
        step("Respect accessibility and small screens",
             "Some people ask their system to reduce motion, and CSS can respect that with `prefers-reduced-motion`. On phones the cards stack, so the lift on the featured card is no longer needed.",
             css="""
a:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 3px;
}
@media (prefers-reduced-motion: reduce) {
  .plan { transition: none; }
}
@media (max-width: 640px) {
  .plan.featured,
  .plan.featured:hover { transform: none; }
  .plans { gap: 28px; }
}"""),
    ],
    ["Add a monthly/yearly toggle with a CSS-only checkbox and the `:has()` selector.",
     "Add a comparison table below the cards with `<table>`.",
     "Turn the colours into CSS custom properties and try a dark version."],
    wrap=("<main class=\"plans\">", "</main>")))

# ============================================================================ 4. Responsive navbar
PROJECTS.append(project(
    "proj-responsive-navbar", "Responsive Navbar with Menu Toggle", "intermediate", 45, ["HTML", "CSS", "JavaScript", "Media queries", "ARIA"],
    "Build a navigation bar that collapses into a hamburger-style menu on small screens.",
    "You will build a header that shows a row of links on wide screens and a Menu button on narrow ones. JavaScript toggles the menu, keeps `aria-expanded` in sync for screen readers, and closes it with the Escape key.",
    [
        step("Create the page and base styles",
             "Set up the skeleton with base styles. The page has a normal block layout this time, because the header should stretch across the full width.",
             show=skeleton("Responsive Navbar") + """

/* Add inside <style> */
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f4f8ff;
  color: #17233d;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}""",
             css="""
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f4f8ff;
  color: #17233d;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}"""),
        step("Write the header markup",
             "The structure matters here. The `<button>` is the control that opens the menu: it has `aria-expanded` to say whether the menu is open, and `aria-controls` to point at the menu's `id`. The links are a normal list inside `<nav>`, so the page works even before any JavaScript runs.",
             html="""<header class="site-header">
  <a class="brand" href="#">Orbit</a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" class="site-nav" aria-label="Main">
    <ul>
      <li><a href="#" aria-current="page">Home</a></li>
      <li><a href="#">Courses</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</header>"""),
        step("Style the desktop layout",
             "Build the wide-screen design first. Flexbox puts the brand and the links on one row, and a second flex row inside the list spaces out the links. The Menu button is hidden for now: it only appears on small screens.",
             css="""
.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 12px 24px;
  background: #0b2e7a;
}
.brand {
  color: #fff;
  font-size: 1.3rem;
  font-weight: 800;
  text-decoration: none;
}
.site-nav ul {
  display: flex;
  gap: 4px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.site-nav a {
  display: block;
  padding: 8px 14px;
  border-radius: 6px;
  color: #cfe0ff;
  font-weight: 600;
  text-decoration: none;
}
.site-nav a:hover { background: rgba(255, 255, 255, .12); color: #fff; }
.site-nav a[aria-current="page"] { background: #1d4ed8; color: #fff; }
.menu-toggle {
  display: none;
  padding: 8px 16px;
  border: 1px solid rgba(255, 255, 255, .5);
  border-radius: 6px;
  background: transparent;
  color: #fff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}"""),
        step("Add some page content",
             "A navbar on an empty page is hard to judge, so add a heading and a paragraph. This also tells the visitor how to test the responsive part.",
             html="""<main class="content">
  <h1>Welcome to Orbit</h1>
  <p>Make this preview narrower than 760px and the links collapse behind the Menu button.</p>
</main>""",
             css="""
.content {
  max-width: 640px;
  margin: 0 auto;
  padding: 40px 24px;
}
.content h1 { margin: 0 0 8px; color: #0b2e7a; }"""),
        step("Add the mobile layout with a media query",
             "Below 760px the Menu button appears and the nav is hidden by default. The nav gets `order: 3` and `width: 100%` so it drops onto its own row under the brand and the button. The `.open` class (which JavaScript will add) shows it again.",
             css="""
@media (max-width: 760px) {
  .menu-toggle { display: block; }
  .site-nav {
    display: none;
    order: 3;
    width: 100%;
    margin-top: 8px;
  }
  .site-nav.open { display: block; }
  .site-nav ul { flex-direction: column; }
}"""),
        step("Toggle the menu with JavaScript",
             "Select the button and the nav, then listen for clicks. `classList.toggle()` adds the class if it is missing and removes it if it is there, and it returns `true` when the class is now on. Use that result to keep `aria-expanded` correct.",
             js="""
const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("#site-nav");

toggle.addEventListener("click", () => {
  const isOpen = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", String(isOpen));
});"""),
        step("Close the menu with Escape and after a link click",
             "Good menus are easy to leave. Pressing Escape should close the menu and move focus back to the button, and clicking a link should close it too. One listener on the nav handles every link thanks to event delegation (`closest(\"a\")`).",
             js="""
function closeMenu() {
  nav.classList.remove("open");
  toggle.setAttribute("aria-expanded", "false");
}

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && nav.classList.contains("open")) {
    closeMenu();
    toggle.focus();
  }
});

nav.addEventListener("click", (event) => {
  if (event.target.closest("a")) closeMenu();
});"""),
        step("Add focus styles",
             "Everything is reachable with the Tab key, so make the focus ring clear. Keyboard users rely on it just as mouse users rely on the pointer.",
             css="""
.menu-toggle:hover { background: rgba(255, 255, 255, .12); }
a:focus-visible,
.menu-toggle:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 2px;
}"""),
    ],
    ["Rotate a three-line icon into an X when the menu is open, using a CSS transition.",
     "Add a dropdown submenu under Courses that opens with `:focus-within`.",
     "Make the header `position: sticky; top: 0` so it stays visible while scrolling."],
    wrap=("<div class=\"app\">", "</div>")))

# ============================================================================ 5. Contact form
PROJECTS.append(project(
    "proj-contact-form", "Contact Form with Live Validation", "intermediate", 50, ["HTML forms", "JavaScript", "Validation", "Accessibility"],
    "Make a contact form that checks each field as the user types and only enables Send when everything is valid.",
    "You will build a form with name, email and message fields. JavaScript validates them live, shows friendly error messages next to the fields, counts the message characters and handles the submit without reloading the page.",
    [
        step("Create the page and base styles",
             "Start with the skeleton and the same centred base layout as the other card projects.",
             show=skeleton("Contact Form") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Add the card and heading",
             "Put everything in a `<main>` card. The form goes inside it in the next step.",
             html='<h1>Contact us</h1>\n<p class="sub">We reply within two working days.</p>',
             html_show='<main class="card">\n  <h1>Contact us</h1>\n  <p class="sub">We reply within two working days.</p>\n  <!-- the form goes here -->\n</main>',
             css="""
.card {
  width: 100%;
  max-width: 460px;
  padding: 32px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(11, 46, 122, .12);
}
h1 { margin: 0; color: #0b2e7a; font-size: 1.6rem; }
.sub { margin: 4px 0 20px; color: #4a5a78; }"""),
        step("Write the form",
             "Every input has a `<label>` linked with `for` and `id`, which makes the click area bigger and lets screen readers announce the field. `novalidate` turns off the browser's own pop-up messages so you can show your own. The empty `.error` paragraphs are where those messages will appear, and `aria-live=\"polite\"` makes screen readers announce them.",
             html="""<form id="contact" novalidate>
  <div class="field">
    <label for="name">Name</label>
    <input id="name" name="name" type="text" autocomplete="name">
    <p class="error" id="name-error" aria-live="polite"></p>
  </div>
  <div class="field">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email">
    <p class="error" id="email-error" aria-live="polite"></p>
  </div>
  <div class="field">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4" maxlength="200"></textarea>
    <p class="hint"><span id="count">0</span>/200</p>
    <p class="error" id="message-error" aria-live="polite"></p>
  </div>
  <button class="btn" id="send" type="submit" disabled>Send message</button>
  <p class="success" id="success" role="status" hidden></p>
</form>""",
             css="""
.field { margin-bottom: 14px; }
label {
  display: block;
  margin-bottom: 4px;
  font-weight: 600;
}
input, textarea {
  width: 100%;
  padding: 10px 12px;
  border: 2px solid #c5d6f6;
  border-radius: 8px;
  background: #fff;
  color: inherit;
  font: inherit;
}
textarea { resize: vertical; }
input:focus-visible, textarea:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 1px;
}
.hint {
  margin: 2px 0 0;
  text-align: right;
  color: #5b6b86;
  font-size: .85rem;
}
.error {
  min-height: 1.3em;
  margin: 2px 0 0;
  color: #b42318;
  font-size: .9rem;
}"""),
        step("Style the valid, invalid and disabled states",
             "Give each state its own look. Never rely on colour alone: the red border is backed up by the error text, and the button is disabled with `disabled`, so it cannot be activated by keyboard either.",
             css="""
input.invalid, textarea.invalid { border-color: #b42318; }
input.valid, textarea.valid { border-color: #0e7a4f; }
.btn {
  width: 100%;
  padding: 12px;
  border: 0;
  border-radius: 8px;
  background: #1d4ed8;
  color: #fff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.btn:hover:not(:disabled) { background: #1740b0; }
.btn:disabled {
  background: #a9bde8;
  cursor: not-allowed;
}
.success {
  margin: 14px 0 0;
  padding: 10px 14px;
  border-radius: 8px;
  background: #e6f5ec;
  color: #0e7a4f;
  font-weight: 600;
}"""),
        step("Describe the rules as data",
             "Instead of writing one big `if` chain, describe each field once: the element and a `check` function that returns `true` when the value is fine, or an error message when it is not. Adding a new rule later just means adding a line.",
             js="""
const form = document.querySelector("#contact");

const fields = {
  name: {
    el: form.elements.name,
    check: (v) => v.trim().length >= 2 || "Please enter your name (at least 2 characters).",
  },
  email: {
    el: form.elements.email,
    check: (v) => /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v) || "Enter a valid email like name@example.com.",
  },
  message: {
    el: form.elements.message,
    check: (v) => v.trim().length >= 10 || "The message needs at least 10 characters.",
  },
};"""),
        step("Show the state of each field",
             "`isValid()` only answers yes or no and has no side effects. `showState()` updates the look and the message, but only for fields the user has already visited (`touched`), so nobody gets an error before they have typed anything. `refresh()` redraws every field and updates the Send button.",
             js="""
const sendBtn = document.querySelector("#send");
const touched = {};

const isValid = (key) => fields[key].check(fields[key].el.value) === true;

function showState(key) {
  const { el, check } = fields[key];
  const result = check(el.value);
  const show = Boolean(touched[key]);
  el.classList.toggle("invalid", show && result !== true);
  el.classList.toggle("valid", show && result === true);
  el.setAttribute("aria-invalid", String(show && result !== true));
  document.querySelector("#" + key + "-error").textContent = show && result !== true ? result : "";
}

function refresh() {
  Object.keys(fields).forEach(showState);
  sendBtn.disabled = !Object.keys(fields).every(isValid);
}"""),
        step("Validate while the user types",
             "Listen to `input` to re-check on every keystroke and to `blur` to mark a field as visited when the user leaves it. The character counter is updated from the same `input` event.",
             js="""
Object.keys(fields).forEach((key) => {
  const el = fields[key].el;
  el.addEventListener("input", refresh);
  el.addEventListener("blur", () => {
    touched[key] = true;
    refresh();
  });
});

form.elements.message.addEventListener("input", (event) => {
  document.querySelector("#count").textContent = event.target.value.length;
});"""),
        step("Handle the submit",
             "Call `preventDefault()` so the browser does not reload the page. A real site would send the data to a server here with `fetch()`; this project just confirms and resets the form. Read the name before `reset()` clears it.",
             js="""
form.addEventListener("submit", (event) => {
  event.preventDefault();
  Object.keys(fields).forEach((key) => (touched[key] = true));
  if (!Object.keys(fields).every(isValid)) {
    refresh();
    return;
  }
  const who = fields.name.el.value.trim();
  form.reset();
  Object.keys(touched).forEach((key) => delete touched[key]);
  document.querySelector("#count").textContent = "0";
  refresh();
  const success = document.querySelector("#success");
  success.textContent = "Thanks, " + who + "! Your message is ready to send.";
  success.hidden = false;
});

refresh();"""),
    ],
    ["Add a phone field with the `pattern` attribute and a matching error message.",
     "Hide the success message again as soon as the user starts typing a new one.",
     "Send the form data with `fetch()` and a `FormData` object when you have a real endpoint."],
    wrap=("<main class=\"card\">", "</main>")))

# ============================================================================ 6. To-do list
PROJECTS.append(project(
    "proj-todo-list", "To-Do List", "intermediate", 50, ["JavaScript", "DOM", "Events", "Arrays"],
    "Build a to-do list where you can add, complete, delete and clear tasks.",
    "You will keep your tasks in a JavaScript array and write one `render()` function that draws the whole list from that data. This is the core idea behind almost every modern front-end framework.",
    [
        step("Create the page and base styles",
             "Start with the skeleton and the centred base layout.",
             show=skeleton("To-Do List") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Add the card and the form",
             "A form with one input and a button lets users add a task by pressing Enter, with no extra code. The `<label>` is visually hidden but still read by screen readers.",
             html="""<h1>My tasks</h1>
<form id="add-form" class="add">
  <label class="sr-only" for="new-task">New task</label>
  <input id="new-task" type="text" placeholder="What needs doing?" autocomplete="off">
  <button class="btn" type="submit">Add</button>
</form>""",
             html_show='<main class="card">\n  <h1>My tasks</h1>\n  <form id="add-form" class="add">\n    <label class="sr-only" for="new-task">New task</label>\n    <input id="new-task" type="text" placeholder="What needs doing?" autocomplete="off">\n    <button class="btn" type="submit">Add</button>\n  </form>\n  <!-- the list goes here -->\n</main>',
             css="""
.card {
  width: 100%;
  max-width: 460px;
  padding: 28px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(11, 46, 122, .12);
}
h1 { margin: 0 0 16px; color: #0b2e7a; font-size: 1.6rem; }
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}
.add { display: flex; gap: 8px; }
.add input {
  flex: 1;
  min-width: 0;
  padding: 10px 12px;
  border: 2px solid #c5d6f6;
  border-radius: 8px;
  font: inherit;
}
.btn {
  padding: 10px 18px;
  border: 0;
  border-radius: 8px;
  background: #1d4ed8;
  color: #fff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.btn:hover { background: #1740b0; }
input:focus-visible, button:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 2px;
}"""),
        step("Add the list, the summary and the clear button",
             "Leave the `<ul>` empty. JavaScript will fill it. The summary line tells the user how many tasks are left, and the clear button starts hidden because there is nothing to clear yet.",
             html="""<p id="summary" class="summary" aria-live="polite"></p>
<ul id="list" class="list"></ul>
<button id="clear" class="clear" type="button" hidden>Clear completed</button>""",
             css="""
.summary {
  margin: 16px 0 8px;
  color: #5b6b86;
  font-size: .95rem;
}
.list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 8px 0;
  border-bottom: 1px solid #e1e9f7;
}
.list label {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  cursor: pointer;
}
.list input[type="checkbox"] { width: 18px; height: 18px; accent-color: #1d4ed8; }
.list li.done span { color: #8a97ad; text-decoration: line-through; }
.delete {
  padding: 4px 10px;
  border: 1px solid #f0c4c0;
  border-radius: 6px;
  background: #fff;
  color: #b42318;
  font: inherit;
  font-size: .85rem;
  cursor: pointer;
}
.delete:hover { background: #fcebe9; }
.clear {
  margin-top: 14px;
  padding: 0;
  border: 0;
  background: none;
  color: #1d4ed8;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  text-decoration: underline;
}"""),
        step("Keep the data in an array",
             "The array is the single source of truth. Each task is an object with an `id`, the `text` and a `done` flag. The page is just a picture of this data: change the data, then redraw. Starting with two sample tasks makes the page look alive.",
             js="""
const form = document.querySelector("#add-form");
const input = document.querySelector("#new-task");
const list = document.querySelector("#list");
const summary = document.querySelector("#summary");
const clearBtn = document.querySelector("#clear");

let tasks = [
  { id: 1, text: "Read the HTML lesson", done: true },
  { id: 2, text: "Build the to-do list", done: false },
];
let nextId = 3;"""),
        step("Write render()",
             "`render()` empties the list and rebuilds it from `tasks`. Using `textContent` (not `innerHTML`) means a task like `<b>hi</b>` is shown as plain text, which keeps you safe from injected HTML. It also updates the summary and decides whether the clear button is visible.",
             js="""
function render() {
  list.textContent = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.dataset.id = task.id;
    li.className = task.done ? "done" : "";

    const label = document.createElement("label");
    const box = document.createElement("input");
    box.type = "checkbox";
    box.checked = task.done;
    const text = document.createElement("span");
    text.textContent = task.text;
    label.append(box, text);

    const del = document.createElement("button");
    del.type = "button";
    del.className = "delete";
    del.textContent = "Delete";
    del.setAttribute("aria-label", "Delete task: " + task.text);

    li.append(label, del);
    list.append(li);
  });

  const left = tasks.filter((t) => !t.done).length;
  summary.textContent = tasks.length
    ? left + (left === 1 ? " task left" : " tasks left")
    : "No tasks yet. Add your first one above.";
  clearBtn.hidden = !tasks.some((t) => t.done);
}

render();"""),
        step("Add new tasks",
             "On submit, stop the page reload, trim the text, ignore empty input, push a new object onto the array and call `render()`. Moving focus back to the input lets the user keep typing.",
             js="""
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  tasks.push({ id: nextId++, text, done: false });
  input.value = "";
  render();
  input.focus();
});"""),
        step("Complete and delete with event delegation",
             "Items are created and destroyed all the time, so attaching a listener to each one would be messy. Instead, listen once on the `<ul>` and look at `event.target` to see what was clicked. `li.dataset.id` tells you which task it belongs to.",
             js="""
list.addEventListener("change", (event) => {
  if (!event.target.matches("input[type=checkbox]")) return;
  const id = Number(event.target.closest("li").dataset.id);
  const task = tasks.find((t) => t.id === id);
  task.done = event.target.checked;
  render();
});

list.addEventListener("click", (event) => {
  if (!event.target.matches(".delete")) return;
  const id = Number(event.target.closest("li").dataset.id);
  tasks = tasks.filter((t) => t.id !== id);
  render();
});"""),
        step("Clear completed tasks",
             "`filter()` keeps only the tasks that are not done. Because the whole list is rebuilt by `render()`, the clear button also hides itself again when nothing is left to clear.",
             js="""
clearBtn.addEventListener("click", () => {
  tasks = tasks.filter((t) => !t.done);
  render();
});"""),
    ],
    ["Save the tasks with `localStorage` so they survive a page refresh (this works on your own site, not in the sandbox preview).",
     "Add All / Active / Completed filter buttons.",
     "Let users double-click a task to edit its text."],
    wrap=("<main class=\"card\">", "</main>")))

# ============================================================================ 7. Tip calculator
PROJECTS.append(project(
    "proj-tip-calculator", "Tip Calculator", "beginner", 40, ["JavaScript", "DOM", "Math", "Events"],
    "Calculate the tip and the total per person from a bill, a tip percentage and the number of people.",
    "You will read numbers from inputs, do the maths, format the result as currency and update the page live. It is a great first project for connecting HTML inputs to JavaScript.",
    [
        step("Create the page and base styles",
             "Start with the skeleton and the same centred base layout.",
             show=skeleton("Tip Calculator") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Add the card and the bill field",
             "Use `type=\"number\"` so phones show a number keyboard. `min=\"0\"` and `step=\"0.01\"` describe the valid values, and `inputmode=\"decimal\"` helps mobile keyboards show a decimal point.",
             html="""<h1>Tip calculator</h1>
<div class="field">
  <label for="bill">Bill amount</label>
  <input id="bill" type="number" min="0" step="0.01" inputmode="decimal" placeholder="0.00" value="48.50">
</div>""",
             html_show='<main class="card">\n  <h1>Tip calculator</h1>\n  <div class="field">\n    <label for="bill">Bill amount</label>\n    <input id="bill" type="number" min="0" step="0.01" inputmode="decimal" placeholder="0.00" value="48.50">\n  </div>\n  <!-- more fields go here -->\n</main>',
             css="""
.card {
  width: 100%;
  max-width: 420px;
  padding: 28px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(11, 46, 122, .12);
}
h1 { margin: 0 0 18px; color: #0b2e7a; font-size: 1.6rem; }
.field { margin-bottom: 16px; }
label, .label {
  display: block;
  margin-bottom: 6px;
  font-weight: 600;
}
input[type="number"] {
  width: 100%;
  padding: 10px 12px;
  border: 2px solid #c5d6f6;
  border-radius: 8px;
  font: inherit;
}
input:focus-visible, button:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 2px;
}"""),
        step("Add the tip buttons",
             "Buttons are quicker than typing for common values. A `role=\"group\"` with a label tells screen readers they belong together, and `aria-pressed` announces which one is selected. The custom field lets people choose any percentage.",
             html="""<div class="field">
  <span class="label" id="tip-label">Tip</span>
  <div class="tips" role="group" aria-labelledby="tip-label">
    <button type="button" class="tip" data-tip="10" aria-pressed="false">10%</button>
    <button type="button" class="tip" data-tip="15" aria-pressed="true">15%</button>
    <button type="button" class="tip" data-tip="20" aria-pressed="false">20%</button>
    <input id="custom" type="number" min="0" max="100" placeholder="Custom %" aria-label="Custom tip percentage">
  </div>
</div>""",
             css="""
.tips {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
.tip {
  padding: 10px 0;
  border: 2px solid #c5d6f6;
  border-radius: 8px;
  background: #fff;
  color: #0b2e7a;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.tip:hover { background: #e8f0ff; }
.tip[aria-pressed="true"] {
  border-color: #1d4ed8;
  background: #1d4ed8;
  color: #fff;
}
#custom { grid-column: 1 / -1; }"""),
        step("Add the number of people",
             "Splitting the bill is a small extra that makes the calculator genuinely useful. `min=\"1\"` and `step=\"1\"` keep it a whole number of people.",
             html="""<div class="field">
  <label for="people">Number of people</label>
  <input id="people" type="number" min="1" step="1" value="2">
</div>""",
             css=None),
        step("Show the results",
             "An `<output>`-style result area shows the answers. `aria-live=\"polite\"` makes screen readers announce the new values when they change. The Reset button gets its own style so it looks secondary.",
             html="""<div class="results" aria-live="polite">
  <p>Tip per person <strong id="tip-each">$0.00</strong></p>
  <p>Total per person <strong id="total-each">$0.00</strong></p>
</div>
<button type="button" id="reset" class="reset">Reset</button>""",
             css="""
.results {
  margin: 20px 0 14px;
  padding: 16px 18px;
  border-radius: 12px;
  background: #0b2e7a;
  color: #cfe0ff;
}
.results p {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0;
  padding: 4px 0;
}
.results strong {
  color: #fff;
  font-size: 1.5rem;
}
.reset {
  width: 100%;
  padding: 10px;
  border: 2px solid #1d4ed8;
  border-radius: 8px;
  background: #fff;
  color: #1d4ed8;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.reset:hover { background: #e8f0ff; }"""),
        step("Read the inputs and do the maths",
             "`Number()` converts the text from the inputs into numbers. If the user clears a field you get `NaN` or `0`, so fall back to safe values with `|| 0` and `Math.max(1, ...)`. Never divide by zero people.",
             js="""
const bill = document.querySelector("#bill");
const people = document.querySelector("#people");
const custom = document.querySelector("#custom");
const tipButtons = document.querySelectorAll(".tip");
const tipEach = document.querySelector("#tip-each");
const totalEach = document.querySelector("#total-each");

let tipPercent = 15;

const money = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });

function calculate() {
  const amount = Math.max(0, Number(bill.value) || 0);
  const count = Math.max(1, Math.floor(Number(people.value) || 1));
  const tip = amount * (tipPercent / 100);
  tipEach.textContent = money.format(tip / count);
  totalEach.textContent = money.format((amount + tip) / count);
}"""),
        step("Connect the tip buttons and inputs",
             "Selecting a button updates `tipPercent`, clears the custom field and moves the pressed state with `aria-pressed`. Typing in the custom field un-presses every button. Finally, recalculate whenever any input changes.",
             js="""
tipButtons.forEach((button) => {
  button.addEventListener("click", () => {
    tipPercent = Number(button.dataset.tip);
    custom.value = "";
    tipButtons.forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
    calculate();
  });
});

custom.addEventListener("input", () => {
  tipPercent = Math.min(100, Math.max(0, Number(custom.value) || 0));
  tipButtons.forEach((b) => b.setAttribute("aria-pressed", "false"));
  calculate();
});

bill.addEventListener("input", calculate);
people.addEventListener("input", calculate);"""),
        step("Add Reset and calculate once on load",
             "Reset puts every value back to its default. Calling `calculate()` at the end shows the results for the starting values straight away instead of showing zero.",
             js="""
document.querySelector("#reset").addEventListener("click", () => {
  bill.value = "";
  people.value = "1";
  custom.value = "";
  tipPercent = 15;
  tipButtons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.tip === "15")));
  calculate();
  bill.focus();
});

calculate();"""),
    ],
    ["Add a round-up button that rounds the total per person up to the next whole currency unit.",
     "Let the user pick a currency and use `Intl.NumberFormat` with that currency code.",
     "Show the total bill including the tip as well as the per-person amounts."],
    wrap=("<main class=\"card\">", "</main>")))

# ============================================================================ 8. Memory game
PROJECTS.append(project(
    "proj-memory-game", "Memory Card Game", "advanced", 75, ["JavaScript", "DOM", "Game logic", "CSS Grid", "Accessibility"],
    "Build a card-matching game with shuffling, flip animations, a move counter and a win message.",
    "You will make a 4 by 4 board of face-down cards. Players flip two at a time to find matching pairs. You will practise arrays, the Fisher-Yates shuffle, game state, timeouts and keyboard-friendly buttons.",
    [
        step("Create the page and base styles",
             "Start with the skeleton and the base layout, then build the game one piece at a time.",
             show=skeleton("Memory Game") + "\n\n/* Add inside <style> */" + BASE_BLUE.rstrip("\n"), css=BASE_BLUE),
        step("Add the header and the board",
             "The page needs a title, a move counter, a restart button, the board itself and a message line. The board stays empty: JavaScript builds the cards, so you can reshuffle by rebuilding it.",
             html="""<header class="top">
  <h1>Memory</h1>
  <p class="moves">Moves: <strong id="moves">0</strong></p>
  <button class="btn" id="restart" type="button">Restart</button>
</header>
<div class="board" id="board"></div>
<p class="message" id="message" role="status"></p>""",
             html_show='<main class="game">\n  <header class="top">\n    <h1>Memory</h1>\n    <p class="moves">Moves: <strong id="moves">0</strong></p>\n    <button class="btn" id="restart" type="button">Restart</button>\n  </header>\n  <div class="board" id="board"></div>\n  <p class="message" id="message" role="status"></p>\n</main>',
             css="""
.game {
  width: 100%;
  max-width: 420px;
  padding: 22px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(11, 46, 122, .12);
}
.top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}
.top h1 { flex: 1; margin: 0; color: #0b2e7a; font-size: 1.5rem; }
.moves { margin: 0; color: #4a5a78; }
.btn {
  padding: 8px 16px;
  border: 0;
  border-radius: 8px;
  background: #1d4ed8;
  color: #fff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.btn:hover { background: #1740b0; }
.message {
  min-height: 1.6em;
  margin: 14px 0 0;
  text-align: center;
  color: #0e7a4f;
  font-weight: 700;
}"""),
        step("Lay out the board",
             "A CSS Grid with four equal columns is all the layout a card game needs. `aspect-ratio: 1` (on the cards, next step) keeps them square at any size.",
             css="""
.board {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}"""),
        step("Style the cards",
             "Each card is a real `<button>`, so it gets keyboard focus, Enter and Space for free. The `.front` (a question mark) shows by default and the `.back` (the symbol) shows once the card has the `flipped` class. A short `pop` animation makes the flip feel alive.",
             css="""
.card {
  display: grid;
  place-items: center;
  aspect-ratio: 1;
  border: 2px solid #1d4ed8;
  border-radius: 12px;
  background: #1d4ed8;
  color: #fff;
  font-size: 2rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s;
}
.card:hover:not(:disabled) { background: #1740b0; }
.card .back { display: none; }
.card.flipped {
  border-color: #c5d6f6;
  background: #f4f8ff;
  animation: pop .25s ease;
}
.card.flipped .front { display: none; }
.card.flipped .back { display: block; }
.card.matched {
  border-color: #0e7a4f;
  background: #e6f5ec;
}
.card:disabled { cursor: default; }
.card:focus-visible, .btn:focus-visible {
  outline: 3px solid #86aef7;
  outline-offset: 2px;
}
@keyframes pop {
  from { transform: scale(.85); }
  to { transform: scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  .card.flipped { animation: none; }
}"""),
        step("Prepare the data and shuffle",
             "Eight symbols doubled give sixteen cards. The Fisher-Yates shuffle walks backwards through the array and swaps each item with a random earlier one, which gives every ordering an equal chance. (Sorting with `Math.random()` looks tempting but is biased.) Names are kept for screen readers.",
             js="""
const SYMBOLS = ["\\u2605", "\\u25CF", "\\u25B2", "\\u25A0", "\\u25C6", "\\u2665", "\\u2663", "\\u2660"];
const NAMES = ["Star", "Circle", "Triangle", "Square", "Diamond", "Heart", "Club", "Spade"];
const COLORS = ["#b45309", "#0891b2", "#4f46e5", "#0e7a4f", "#7c3aed", "#be185d", "#0f766e", "#1d4ed8"];

const board = document.querySelector("#board");
const movesEl = document.querySelector("#moves");
const message = document.querySelector("#message");

let first = null;
let lock = false;
let moves = 0;
let found = 0;

function shuffle(items) {
  for (let i = items.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [items[i], items[j]] = [items[j], items[i]];
  }
  return items;
}"""),
        step("Build the board",
             "`setup()` resets all the state and creates sixteen buttons. Each button gets two `<span>`s, the question mark and the symbol, and remembers which symbol it holds in `data-index`. Building the DOM with `createElement` avoids `innerHTML` entirely.",
             js="""
function setup() {
  board.textContent = "";
  first = null;
  lock = false;
  moves = 0;
  found = 0;
  movesEl.textContent = "0";
  message.textContent = "";

  const deck = shuffle([...SYMBOLS.keys(), ...SYMBOLS.keys()]);
  deck.forEach((index) => {
    const card = document.createElement("button");
    card.type = "button";
    card.className = "card";
    card.dataset.index = index;
    card.setAttribute("aria-label", "Hidden card");

    const front = document.createElement("span");
    front.className = "front";
    front.textContent = "?";
    const back = document.createElement("span");
    back.className = "back";
    back.textContent = SYMBOLS[index];
    back.style.color = COLORS[index];

    card.append(front, back);
    board.append(card);
  });
}

setup();"""),
        step("Flip cards and check for a match",
             "One click handler on the board covers every card. The `lock` flag stops the player flipping a third card while a wrong pair is still showing. On a match the pair stays open and is disabled. On a miss, `setTimeout` waits 800 ms so the player can see both cards, then turns them back.",
             js="""
function flip(card) {
  card.classList.add("flipped");
  card.setAttribute("aria-label", NAMES[card.dataset.index]);
}

function unflip(card) {
  card.classList.remove("flipped");
  card.setAttribute("aria-label", "Hidden card");
}

board.addEventListener("click", (event) => {
  const card = event.target.closest(".card");
  if (!card || lock || card === first || card.disabled) return;

  flip(card);
  if (!first) {
    first = card;
    return;
  }

  moves++;
  movesEl.textContent = moves;

  if (first.dataset.index === card.dataset.index) {
    [first, card].forEach((c) => {
      c.classList.add("matched");
      c.disabled = true;
    });
    first = null;
    found++;
    if (found === SYMBOLS.length) {
      message.textContent = "You won in " + moves + " moves!";
    }
  } else {
    lock = true;
    const previous = first;
    setTimeout(() => {
      unflip(previous);
      unflip(card);
      first = null;
      lock = false;
    }, 800);
  }
});"""),
        step("Add the restart button",
             "Restart simply calls `setup()` again: because all state lives in a few variables and the board is rebuilt from scratch, there is nothing else to clean up.",
             js="""
document.querySelector("#restart").addEventListener("click", setup);"""),
    ],
    ["Add a timer that starts on the first flip and shows the elapsed seconds.",
     "Store the best (lowest) move count in a variable and show it next to the current moves.",
     "Add a difficulty selector that changes the grid to 3 by 4 or 5 by 4 cards."],
    wrap=("<main class=\"game\">", "</main>")))
