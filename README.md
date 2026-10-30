# TechHub

A online learning platform with two modules: **HTML** (54 lessons) and **CSS** (66 lessons).
Each lesson has a clear explanation, highlighted code, a live "Try it yourself" editor and exercises. Each module has its own 10-question quiz, and there is a mixed quiz. Progress is saved in the browser.

## Run it
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Put it online
Any Python host works (Render, Railway, PythonAnywhere). Build: `pip install -r requirements.txt`. Start: `gunicorn app:app`.

## Structure
- `app.py` Flask routes, code highlighter (HTML and CSS), JSON API (answer checking, quizzes, lesson search). Quiz answers stay on the server.
- `content/html.py`, `content/css.py` one file per module: lessons, examples and exercises.
- `content/__init__.py` registers the modules. To add a third module, create a file with `GROUPS` and `LESSONS` and add it to `MODULES`.
- `templates/` Jinja pages. `static/css/style.css` theme. `static/js/app.js` editor, search, exercises, quiz, progress.
- `tests.py` run `python -m unittest tests` (loads all 120 lessons and checks quiz logic).

## Add a lesson
Append a dict to `LESSONS` in the module file: slug, title, group, intro, sections, example, tip (optional), exercise (2+ questions, 4 unique options each). Use `<tag>` or `backtick` spans for inline code.
