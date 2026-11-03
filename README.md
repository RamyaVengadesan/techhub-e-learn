# TechHub

**A free, hands-on learning platform for HTML, CSS and JavaScript.**
Read a lesson, edit the code in a live editor, test yourself, then practise with auto-checked challenges and guided projects.

Built with Python (Flask), Jinja templates, plain CSS and vanilla JavaScript. No front-end build step, no database server.

---

## Features

| | |
|---|---|
| **225 lessons** | HTML (71), CSS (88) and JavaScript (66), each with explanations, highlighted code and exercises |
| **Live editor** | "Try it yourself" on every lesson, in a sandboxed iframe, with Run, Reset, Ctrl+Enter and full-screen mode |
| **45 coding challenges** | Write code in the browser and see each check pass or fail straight away |
| **8 guided projects** | Step-by-step builds (profile page, landing page, navbar, to-do list, calculator, memory game) |
| **Quizzes** | 3 levels per language, with best scores saved in the browser |
| **Reference** | 8 lookup tables (HTML tags, attributes, events; CSS properties, selectors, functions; JavaScript and DOM) with filter and jump links |
| **CSS playgrounds** | Flexbox, Grid and Box Model tools that generate copy-ready CSS |
| **Study aids** | 5 printable cheat sheets and a 114-term glossary |
| **Learning path** | An 8-stage roadmap from zero to job-ready |
| **Accounts (optional)** | Progress, streaks and a daily plan saved on the server; everything also works without logging in |
| **Dark mode** | Follows the system setting, with a manual toggle |
| **Responsive** | Works from phone to desktop, with a collapsible lesson menu |

## Quick start

Requires Python 3.9 or newer.

```bash
git clone https://github.com/<your-username>/techhub.git
cd techhub

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

Run the tests:

```bash
python -m unittest tests
```

## Project structure

```
techhub/
├── app.py                  Flask routes, code highlighter, JSON API (quizzes, answer checking, search)
├── content/                All learning content as Python data
│   ├── html.py  css.py  js.py        lessons, examples and exercises (one file per language)
│   ├── reference.py                  reference tables
│   ├── challenges.py  projects.py    practice content
│   ├── cheatsheets.py  glossary.py  roadmap.py
│   └── __init__.py                   registers modules and quiz levels
├── templates/              Jinja pages
│   ├── base.html                     header, lesson sidebar, footer
│   ├── _ui.html                      shared banner, page shell and icons
│   └── ...                           one template per page
├── static/
│   ├── css/style.css                 base theme
│   ├── css/pro.css                   professional layer (loaded last, overrides style.css)
│   └── js/app.js  tools.js           editor, search, quizzes, progress, CSS playgrounds
├── tests.py                loads all lessons and checks the quiz logic
├── requirements.txt
└── Procfile                gunicorn entry for hosts like Render or Railway
```

## Adding content

**A lesson:** append a dict to `LESSONS` in `content/html.py`, `css.py` or `js.py` with `slug`, `title`, `group`, `intro`, `sections`, `example`, an optional `tip`, and `exercise` (2 or more questions, 4 unique options each). Use `<tag>` or backtick spans for inline code.

**A reference entry:** add one line to `content/reference.py` in the form `name :: description :: extra :: lesson-slug`.

**A new language module:** create a file with `GROUPS` and `LESSONS`, then add it to `MODULES` in `content/__init__.py`.

The quiz level of each lesson group is set in `LEVEL_GROUPS` in `content/__init__.py`.

## Configuration

Set these environment variables as needed. All are optional for local use.

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | **Set this in production.** If unset, a key is generated once into `.secret_key` next to the database |
| `SITE_NAME`, `OWNER_NAME`, `CONTACT_EMAIL` | Shown in the footer and legal pages |
| `SITE_URL` | Public URL, used for canonical links and the sitemap (for example `https://www.yoursite.com`) |
| `ADMIN_TOKEN` | Enables `/admin/feedback?token=...` (disabled when unset) |
| `DB_PATH` | SQLite file for accounts and lesson feedback (default: `techhub.db` next to `app.py`) |
| `TRUST_PROXY` | Set to `1` behind a reverse proxy so rate limiting sees real IP addresses |
| `PORT`, `FLASK_DEBUG` | Server options |

## Deployment

Any Python host works (Render, Railway, PythonAnywhere, a VPS).

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app` (also in the `Procfile`)
- Set `SECRET_KEY`, `SITE_URL` and `TRUST_PROXY=1` on the host.
- SQLite lives on local disk. On hosts with an ephemeral filesystem, mount a persistent volume and point `DB_PATH` at it, or accounts and feedback are lost on each deploy.

## Security notes

- Lesson examples run in a sandboxed iframe (scripts allowed, no access to this site's cookies or storage). `alert`, `prompt` and `localStorage` are blocked inside it.
- Quiz answers are kept on the server and never sent to the browser.
- Passwords are hashed; forms use CSRF tokens; session cookies are HttpOnly and SameSite=Lax; API endpoints are rate limited.
- Never commit `.secret_key` or `techhub.db` (both are in `.gitignore`).

## Before a public launch

- The **Privacy** and **Terms** pages are templates. Review them, and choose a licence for the code examples.
- Not included yet: password reset by email, email verification and an account deletion page. Privacy law in some regions requires a way to delete accounts.

## Contributing

Issues and pull requests are welcome. Please run `python -m unittest tests` before submitting, and keep new lessons in the same format as the existing ones.

## License

Add a `LICENSE` file before publishing. [MIT](https://choosealicense.com/licenses/mit/) is a common choice for code like this.
