# TechHub

A blue and white online learning platform with three modules: **HTML** (71 lessons), **CSS** (88 lessons) and **JavaScript** (66 lessons).
Each lesson has a clear explanation, highlighted code, a live "Try it yourself" editor and exercises. Each module has its own 10-question quiz, and there is a mixed quiz. Progress is saved in the browser.

## Run it
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Put it online
Any Python host works (Render, Railway, PythonAnywhere). Build: `pip install -r requirements.txt`. Start: `gunicorn app:app`.

## Structure
- `app.py` Flask routes, code highlighter (HTML and CSS), JSON API (answer checking, quizzes, lesson search). Quiz answers stay on the server.
- `content/html.py`, `content/css.py`, `content/js.py` one file per module: lessons, examples and exercises.
- `content/__init__.py` registers the modules. To add another module, create a file with `GROUPS` and `LESSONS` and add it to `MODULES`.
- `templates/` Jinja pages. `static/css/style.css` theme. `static/js/app.js` editor, search, exercises, quiz, progress.
- `tests.py` run `python -m unittest tests` (loads all 225 lessons and checks quiz logic).

## Add a lesson
Append a dict to `LESSONS` in the module file: slug, title, group, intro, sections, example, tip (optional), exercise (2+ questions, 4 unique options each). Use `<tag>` or `backtick` spans for inline code.

## Live code
Examples run in a sandboxed iframe (scripts allowed, no access to this site's cookies or storage). `console.log` output and errors appear under the result. Avoid `alert`, `prompt` and `localStorage` in examples; they are blocked in the sandbox.

## Reference and quizzes
- `/reference` has eight W3Schools-style tables (HTML tags, attributes, events; CSS properties, selectors, functions; JavaScript and DOM). Data lives in `content/reference.py`, one entry per line: `name :: description :: extra :: lesson-slug`.
- Quizzes are split by module and level (Beginner, Intermediate, Advanced). The level of each lesson group is set in `LEVEL_GROUPS` in `content/__init__.py`. Best scores are saved in the browser.


## New in this version

- **Roadmap** (`/roadmap`) - an 8-stage path from zero to job-ready.
- **Coding challenges** (`/challenges`) - 45 tasks, auto-checked in the browser.
- **Guided projects** (`/projects`) - 8 step-by-step builds that open in the live editor.
- **CSS tools** (`/tools`) - flexbox, grid and box-model playgrounds.
- **Cheat sheets** (`/cheatsheets`, printable), **glossary** (`/glossary`), lesson feedback, dark mode, sitemap and robots.txt, rate limiting.

## Configuration (environment variables)

| Variable | Purpose |
|---|---|
| `SITE_NAME`, `OWNER_NAME`, `CONTACT_EMAIL` | Shown in the footer and legal pages |
| `SITE_URL` | Public URL used for canonical links and the sitemap |
| `ADMIN_TOKEN` | Enables `/admin/feedback?token=...` (disabled when unset) |
| `DB_PATH` | SQLite file for lesson feedback |
| `TRUST_PROXY` | Set to `1` behind a reverse proxy so rate limiting sees real IPs |
| `PORT`, `FLASK_DEBUG` | Server options |

Run in production with `gunicorn app:app` (see `Procfile`).

**Note:** the Privacy and Terms pages are templates. Please review them (including the licence you want for the code examples) before launching publicly.

## Optional accounts and daily plan

- Learning needs no account. Visitors who log in get their progress saved on the server, a day streak, a weekly view, per-tutorial progress and a day-by-day plan at **/my-learning** (pace: 1, 2, 3, 5 or 8 lessons a day).
- Progress finished before logging in is merged into the account on the first page load after login.
- Storage: SQLite (`DB_PATH`). Passwords are hashed. Forms use CSRF tokens; session cookies are HttpOnly and SameSite=Lax.
- Set **SECRET_KEY** in production. If it is not set, a key is generated once into `.secret_key` next to the database (keep that file private and out of version control).
- Not included yet: password reset by email, email verification, account deletion page. Add these before a large public launch (privacy law may require a way to delete accounts).
