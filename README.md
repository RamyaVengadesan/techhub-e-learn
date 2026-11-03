# TechHub

A website for learning HTML, CSS and JavaScript. I built it as a W3Schools-style tutorial site that I can run and host myself.

Each lesson has a short explanation, an example you can edit and run in the browser, and a couple of questions at the end. There are also coding challenges, small projects, quizzes, a reference section and a few CSS tools.

It's a Flask app. No Node, no build step and no separate database server, just Python and SQLite.

## Screenshots

Add a few screenshots here before you push. Put the images in a `screenshots/` folder and link them like this:

```
![Home page](screenshots/home.png)
![Lesson page](screenshots/lesson.png)
```

## What's in it

- 225 lessons: HTML (71), CSS (88), JavaScript (66)
- A "Try it yourself" editor on every lesson (runs in a sandboxed iframe)
- 45 coding challenges that check your code in the browser
- 8 guided projects (profile page, landing page, navbar, to-do list, calculator, memory game, and so on)
- Quizzes for each language at beginner, intermediate and advanced level
- Reference tables for HTML, CSS and JavaScript
- Flexbox, Grid and box model playgrounds
- Cheat sheets (printable) and a glossary
- A learning path for complete beginners
- Optional login to save progress and get a daily plan
- Dark mode, and it works on phones

## Running it locally

You need Python 3.9 or newer.

```bash
git clone https://github.com/<your-username>/techhub.git
cd techhub
python -m venv .venv
.venv\Scripts\activate          # on Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

To run the tests:

```bash
python -m unittest tests
```

## How it's organised

```
app.py            routes, code highlighting, quiz/search API
content/          all the lessons, challenges, projects and reference data (plain Python files)
templates/        Jinja pages
static/css/       style.css (base) and pro.css (the newer design, loaded last)
static/js/        app.js (editor, search, quizzes, progress) and tools.js (CSS playgrounds)
tests.py          checks that every lesson loads and the quiz logic works
```

## Adding a lesson

Lessons live in `content/html.py`, `content/css.py` and `content/js.py`. Add a new dict to the `LESSONS` list with these keys:

`slug`, `title`, `group`, `intro`, `sections`, `example`, `tip` (optional) and `exercise` (at least 2 questions with 4 different options each).

For inline code in text, use `<tag>` or backticks. Run the tests afterwards to make sure it loads.

Reference tables are in `content/reference.py`, one entry per line:
`name :: description :: extra :: lesson-slug`

## Settings

Everything is optional when running locally. These are environment variables:

| Name | What it does |
|---|---|
| `SECRET_KEY` | Session key. Set it when you deploy. If you don't, one is generated into `.secret_key` |
| `SITE_NAME`, `OWNER_NAME`, `CONTACT_EMAIL` | Shown in the footer and the legal pages |
| `SITE_URL` | Your public URL (used for canonical links and the sitemap) |
| `ADMIN_TOKEN` | Turns on `/admin/feedback?token=...`. Off if not set |
| `DB_PATH` | Where the SQLite file lives |
| `TRUST_PROXY` | Set to `1` if you're behind a proxy like Render or Railway |

## Deploying

Any host that runs Python will do (Render, Railway, PythonAnywhere).

- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`

SQLite is just a file, so on hosts where the disk resets on every deploy you'll lose accounts and feedback unless you attach a persistent disk and point `DB_PATH` at it.
