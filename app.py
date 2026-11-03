"""TechHub: an online learning site with an HTML module and a CSS module.

Run:  python app.py   then open http://127.0.0.1:5000
"""
import datetime as dt
import os
import random
import re
import secrets
import sqlite3
import time
from collections import defaultdict, deque
from functools import wraps
from html import escape

from flask import Flask, Response, abort, g, jsonify, redirect, render_template, request, session, url_for
from markupsafe import Markup
from werkzeug.security import check_password_hash, generate_password_hash

from content import (CHALLENGE_BY_SLUG, CHALLENGES, CHEATSHEETS, GLOSSARY, LESSON_BY_SLUG, LEVEL_NAME, LEVELS, MODULE_BY_SLUG,
                     MODULES, PROJECT_BY_SLUG, PROJECTS, QUESTIONS, REF_BY_SLUG, REFS, ROADMAP, SHEET_BY_SLUG)

app = Flask(__name__)

# ----------------------------------------------------------------- site settings (override with environment variables)
SITE_NAME = os.environ.get("SITE_NAME", "TechHub")
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")          # e.g. https://www.yoursite.com (used for canonical links and the sitemap)
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "contact@example.com")
OWNER_NAME = os.environ.get("OWNER_NAME", SITE_NAME)
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")                 # set it to enable /admin/feedback?token=...
DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "techhub.db"))
if os.environ.get("TRUST_PROXY") == "1":                        # set when running behind a reverse proxy / PaaS
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)


def _secret_key() -> str:
    key = os.environ.get("SECRET_KEY")
    if key:
        return key
    path = os.path.join(os.path.dirname(os.path.abspath(DB_PATH)), ".secret_key")   # generated once, kept next to the database
    try:
        with open(path) as f:
            return f.read().strip()
    except OSError:
        key = secrets.token_hex(32)
        try:
            with open(path, "w") as f:
                f.write(key)
            os.chmod(path, 0o600)
        except OSError:
            pass                                                                      # read-only disk: sessions last until restart
        return key


app.secret_key = _secret_key()
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", SESSION_COOKIE_SECURE=SITE_URL.startswith("https://"),
                  PERMANENT_SESSION_LIFETIME=dt.timedelta(days=60), MAX_CONTENT_LENGTH=64 * 1024)


def absolute(path: str) -> str:
    return (SITE_URL or request.url_root.rstrip("/")) + path


@app.after_request
def security_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    return resp


# ----------------------------------------------------------------- tiny in-memory rate limiter (per IP)
_hits = defaultdict(deque)


def rate_limit(limit=60, window=60):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            key = (request.remote_addr or "?", fn.__name__)
            now, q = time.time(), _hits[key]
            while q and now - q[0] > window:
                q.popleft()
            if len(q) >= limit:
                return jsonify(error="Too many requests. Please slow down."), 429
            q.append(now)
            return fn(*args, **kwargs)
        return wrapper
    return deco


# ----------------------------------------------------------------- feedback storage (SQLite)
def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, lesson TEXT NOT NULL, helpful INTEGER NOT NULL, created REAL NOT NULL)")
        g.db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, pw TEXT NOT NULL, pace INTEGER NOT NULL DEFAULT 3, created REAL NOT NULL)")
        g.db.execute("CREATE TABLE IF NOT EXISTS progress (user_id INTEGER NOT NULL, lesson TEXT NOT NULL, done_at REAL NOT NULL, PRIMARY KEY (user_id, lesson))")
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()

# ----------------------------------------------------------------- code highlighting
TOKEN = re.compile(
    r'(?P<comment><!--.*?-->)'
    r'|(?P<style>(?P<sopen><style[^>]*>)(?P<scss>.*?)(?P<sclose></style>))'
    r'|(?P<tag><\/?[a-zA-Z][\w-]*)(?P<attrs>(?:\s+[^\s"\'<>\/=]+(?:\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s"\'>]+))?)*)\s*(?P<end>\/?>)'
    r'|(?P<text>[^<]+|<)', re.S)
ATTR = re.compile(r'([^\s"\'<>\/=]+)(?:(\s*=\s*)("[^"]*"|\'[^\']*\'|[^\s"\'>]+))?')
CSS_TOKEN = re.compile(r'(?P<c>/\*.*?\*/)|(?P<sel>[^{}]+?)(?P<ob>\{)(?P<body>[^{}]*)(?P<cb>\})|(?P<rest>[^{}]+|[{}])', re.S)
CSS_DECL = re.compile(r'([\w-]+)(\s*:\s*)([^;]*)(;?)')


def _css(code: str) -> str:
    out = []
    for m in CSS_TOKEN.finditer(code):
        if m.group("c"):
            out.append(f'<span class="c">{escape(m.group("c"))}</span>')
        elif m.group("sel") is not None and m.group("ob"):
            inner = m.group("body")
            decls = []
            pos = 0
            for d in CSS_DECL.finditer(inner):
                decls.append(escape(inner[pos:d.start()]))
                decls.append(f'<span class="p">{escape(d.group(1))}</span>{escape(d.group(2))}'
                             f'<span class="v">{escape(d.group(3))}</span>{escape(d.group(4))}')
                pos = d.end()
            decls.append(escape(inner[pos:]))
            out.append(f'<span class="sel">{escape(m.group("sel"))}</span>{{{"".join(decls)}}}')
        else:
            out.append(escape(m.group("rest") or ""))
    return "".join(out)


def highlight(code: str) -> Markup:
    """Colour HTML (and CSS inside <style>) for display."""
    def attrs(m):
        out = f'<span class="a">{escape(m.group(1))}</span>'
        if m.group(2):
            out += f'{escape(m.group(2))}<span class="s">{escape(m.group(3))}</span>'
        return out

    parts = []
    for m in TOKEN.finditer(code):
        if m.group("comment"):
            parts.append(f'<span class="c">{escape(m.group("comment"))}</span>')
        elif m.group("style"):
            parts.append(f'<span class="t">&lt;style</span>' + escape(m.group("sopen")[len("<style"):-1]) + '<span class="t">&gt;</span>'
                         + _css(m.group("scss")) + '<span class="t">&lt;/style&gt;</span>')
        elif m.group("tag"):
            parts.append(f'<span class="t">{escape(m.group("tag"))}</span>'
                         + ATTR.sub(attrs, m.group("attrs"))
                         + f'<span class="t">{escape(m.group("end"))}</span>')
        else:
            parts.append(escape(m.group("text")))
    return Markup("".join(parts))


def rich(text: str) -> Markup:
    """Escape text; show `backtick spans` and <tag> mentions as inline code."""
    safe = str(escape(text))
    return Markup(re.sub(r"`([^`]+)`|(&lt;.+?&gt;)",
                         lambda m: f'<code class="i">{m.group(1) or m.group(2)}</code>', safe))


app.jinja_env.filters["highlight"] = highlight
app.jinja_env.filters["rich"] = rich


# ----------------------------------------------------------------- helpers
def neighbours(lesson):
    items = MODULE_BY_SLUG[lesson["module"]]["lessons"]
    i = items.index(lesson)
    return (items[i - 1] if i else None, items[i + 1] if i + 1 < len(items) else None, i + 1, len(items))


def current_user():
    if "user" not in g:
        g.user = None
        uid = session.get("uid")
        if uid:
            row = db().execute("SELECT id, name, email, pace FROM users WHERE id = ?", (uid,)).fetchone()
            if row:
                g.user = dict(id=row[0], name=row[1], email=row[2], pace=row[3])
            else:
                session.pop("uid", None)
    return g.user


def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_hex(16)
    return session["csrf"]


def user_done():
    u = current_user()
    if not u:
        return {}
    return {r[0]: r[1] for r in db().execute("SELECT lesson, done_at FROM progress WHERE user_id = ?", (u["id"],))}


@app.context_processor
def inject():
    u = current_user()
    return dict(modules=MODULES, site_name=SITE_NAME, contact_email=CONTACT_EMAIL, owner_name=OWNER_NAME, absolute=absolute,
                user=u, csrf_token=csrf_token, user_done_list=(sorted(user_done()) if u else []))


# ----------------------------------------------------------------- pages
@app.get("/")
def home():
    total = sum(len(m["lessons"]) for m in MODULES)
    return render_template("home.html", page="home", total=total, questions=len(QUESTIONS), n_challenges=len(CHALLENGES), n_projects=len(PROJECTS),
                           n_refs=len(REFS), n_sheets=len(CHEATSHEETS), n_terms=len(GLOSSARY))


def quiz_counts():
    out = {}
    for m in MODULES:
        out[m["slug"]] = {lvl: sum(1 for q in QUESTIONS.values() if q["module"] == m["slug"] and q["level"] == lvl) for lvl, _ in LEVELS}
    return out


@app.get("/quiz")
def quiz_pick():
    return render_template("quiz_pick.html", page="quiz", counts=quiz_counts(), levels=LEVELS)


@app.get("/quiz/<mod>")
def quiz_module(mod):
    m = MODULE_BY_SLUG.get(mod) or abort(404)
    return render_template("quiz_module.html", page="quiz", m=m, counts=quiz_counts()[mod], levels=LEVELS)


@app.get("/quiz/<mod>/<level>")
def quiz(mod, level):
    m = MODULE_BY_SLUG.get(mod) or abort(404)
    if level not in LEVEL_NAME:
        abort(404)
    keys = [k for k, _ in LEVELS]
    nxt = keys[keys.index(level) + 1] if keys.index(level) + 1 < len(keys) else None
    return render_template("quiz.html", page="quiz", m=m, level=level, level_name=LEVEL_NAME[level], next_level=nxt,
                           next_name=LEVEL_NAME.get(nxt))


@app.get("/reference")
def reference_index():
    return render_template("reference_index.html", page="ref", refs=REFS)


@app.get("/reference/<slug>")
def reference(slug):
    r = REF_BY_SLUG.get(slug) or abort(404)
    return render_template("reference.html", page="ref", ref=r, refs=REFS, lessons=LESSON_BY_SLUG)


@app.get("/try")
def playground():
    return render_template("try.html", page="try", code="<h1>Hello, TechHub!</h1>\n<p>Edit this code and press Run.</p>\n<style>\n  h1 { color: royalblue; }\n</style>", back=None)


@app.get("/try/<slug>")
def try_lesson(slug):
    item = LESSON_BY_SLUG.get(slug) or abort(404)
    return render_template("try.html", page="try", code=item["example"], back=item, module=MODULE_BY_SLUG[item["module"]])


@app.get("/<mod>/")
def module(mod):
    m = MODULE_BY_SLUG.get(mod) or abort(404)
    return render_template("module.html", page="module", module=m, refs=REFS)


@app.get("/<mod>/<slug>")
def lesson(mod, slug):
    item = LESSON_BY_SLUG.get(slug)
    if not item or item["module"] != mod:
        abort(404)
    prev, nxt, num, total = neighbours(item)
    exercise = [dict(id=f"{slug}:{i}", q=q["q"], options=q["options"]) for i, q in enumerate(item["exercise"])]  # answers stay on the server
    return render_template("lesson.html", page="lesson", module=MODULE_BY_SLUG[mod], lesson=item,
                           prev=prev, next=nxt, num=num, total=total, exercise=exercise)


# ----------------------------------------------------------------- JSON API
@app.post("/api/check")
@rate_limit(120, 60)
def api_check():
    data = request.get_json(silent=True) or {}
    q = QUESTIONS.get(data.get("id"))
    if not q:
        return jsonify(error="unknown question"), 404
    answer = q["options"][q["answer"]]
    return jsonify(correct=data.get("choice") == answer, answer=answer)


@app.get("/api/quiz")
@rate_limit(120, 60)
def api_quiz():
    mod, level = request.args.get("module", ""), request.args.get("level", "")
    pool = [(k, v) for k, v in QUESTIONS.items() if v["module"] == mod and v["level"] == level]
    if not pool:
        return jsonify(error="unknown module or level"), 404
    n = min(max(request.args.get("n", 10, type=int), 1), len(pool))
    out = []
    for qid, q in random.sample(pool, n):
        opts = q["options"][:]
        random.shuffle(opts)
        out.append(dict(id=qid, q=q["q"], options=opts))
    return jsonify(questions=out)


@app.post("/api/quiz/check")
@rate_limit(120, 60)
def api_quiz_check():
    answers = (request.get_json(silent=True) or {}).get("answers", {})
    results, score = [], 0
    for qid, choice in answers.items():
        q = QUESTIONS.get(qid)
        if q:
            right = q["options"][q["answer"]]
            ok = choice == right
            score += ok
            results.append(dict(id=qid, correct=ok, answer=right))
    return jsonify(score=score, total=len(results), results=results)


@app.get("/api/search")
@rate_limit(120, 60)
def api_search():
    q = request.args.get("q", "").strip().lower()
    if len(q) < 2:
        return jsonify(results=[])
    hits = []
    for l in LESSON_BY_SLUG.values():
        title = l["title"].lower()
        score = 3 if q in title else 1 if q in l["intro"].lower() else 0
        if score:
            hits.append((-score, title, l))
    hits.sort(key=lambda h: h[:2])
    return jsonify(results=[dict(title=l["title"], module=l["module"].upper(), url=f"/{l['module']}/{l['slug']}") for _, _, l in hits[:8]])


# ----------------------------------------------------------------- learning pages
@app.get("/roadmap")
def roadmap():
    return render_template("roadmap.html", page="roadmap", stages=ROADMAP, lessons=LESSON_BY_SLUG)


@app.get("/challenges")
def challenges():
    return render_template("challenges.html", page="practice", challenges=CHALLENGES, levels=LEVELS)


@app.get("/challenges/<slug>")
def challenge(slug):
    c = CHALLENGE_BY_SLUG.get(slug) or abort(404)
    same = [x for x in CHALLENGES if x["module"] == c["module"]]
    i = same.index(c)
    return render_template("challenge.html", page="practice", c=c, module=MODULE_BY_SLUG[c["module"]], lessons=LESSON_BY_SLUG,
                           prev=same[i - 1] if i else None, next=same[i + 1] if i + 1 < len(same) else None, level_name=LEVEL_NAME[c["level"]])


@app.get("/projects")
def projects():
    return render_template("projects.html", page="practice", projects=PROJECTS, levels=LEVELS)


@app.get("/projects/<slug>")
def project(slug):
    p = PROJECT_BY_SLUG.get(slug) or abort(404)
    return render_template("project.html", page="practice", p=p, level_name=LEVEL_NAME[p["level"]])


@app.get("/projects/<slug>/edit")
def project_edit(slug):
    p = PROJECT_BY_SLUG.get(slug) or abort(404)
    return render_template("try.html", page="practice", code=p["final"], back=None, back_project=p)


@app.get("/tools")
def tools():
    return render_template("tools.html", page="tools")


@app.get("/tools/<tool>")
def tool(tool):
    if tool not in ("flexbox", "grid", "box-model"):
        abort(404)
    return render_template(f"tool_{tool.replace('-', '_')}.html", page="tools")


@app.get("/cheatsheets")
def cheatsheets():
    return render_template("cheatsheets.html", page="tools", sheets=CHEATSHEETS)


@app.get("/cheatsheets/<slug>")
def cheatsheet(slug):
    s = SHEET_BY_SLUG.get(slug) or abort(404)
    return render_template("cheatsheet.html", page="tools", s=s, sheets=CHEATSHEETS)


@app.get("/glossary")
def glossary():
    letters = sorted({t["term"][0].upper() for t in GLOSSARY})
    return render_template("glossary.html", page="tools", terms=GLOSSARY, letters=letters, lessons=LESSON_BY_SLUG)


@app.get("/privacy")
def privacy():
    return render_template("privacy.html", page="legal")


@app.get("/terms")
def terms():
    return render_template("terms.html", page="legal")


# ----------------------------------------------------------------- SEO files
@app.get("/robots.txt")
def robots():
    return Response(f"User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /admin/\nSitemap: {absolute('/sitemap.xml')}\n", mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    paths = ["/", "/roadmap", "/challenges", "/projects", "/tools", "/tools/flexbox", "/tools/grid", "/tools/box-model", "/cheatsheets",
             "/glossary", "/reference", "/quiz", "/try", "/privacy", "/terms"]
    paths += [f"/{m['slug']}/" for m in MODULES]
    paths += [f"/{l['module']}/{l['slug']}" for l in LESSON_BY_SLUG.values()]
    paths += [f"/reference/{r['slug']}" for r in REFS]
    paths += [f"/challenges/{c['slug']}" for c in CHALLENGES]
    paths += [f"/projects/{p['slug']}" for p in PROJECTS]
    paths += [f"/cheatsheets/{s['slug']}" for s in CHEATSHEETS]
    paths += [f"/quiz/{m['slug']}" for m in MODULES]
    body = "".join(f"<url><loc>{escape(absolute(p))}</loc></url>" for p in paths)
    return Response(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>', mimetype="application/xml")


# ----------------------------------------------------------------- lesson feedback
@app.post("/api/feedback")
@rate_limit(20, 60)
def api_feedback():
    data = request.get_json(silent=True) or {}
    lesson, helpful = data.get("lesson"), data.get("helpful")
    if lesson not in LESSON_BY_SLUG or not isinstance(helpful, bool):
        return jsonify(error="invalid feedback"), 400
    db().execute("INSERT INTO feedback (lesson, helpful, created) VALUES (?, ?, ?)", (lesson, int(helpful), time.time()))
    db().commit()
    return jsonify(ok=True)


@app.get("/admin/feedback")
def admin_feedback():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(404)
    rows = db().execute("SELECT lesson, SUM(helpful), SUM(1 - helpful), COUNT(*) FROM feedback GROUP BY lesson ORDER BY SUM(1 - helpful) DESC, COUNT(*) DESC").fetchall()
    cells = "".join(f"<tr><td>{escape(r[0])}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in rows)
    return Response(f"<!doctype html><meta charset=utf-8><title>Feedback</title><body style='font-family:system-ui;margin:24px'><h1>Lesson feedback</h1>"
                    f"<table border=1 cellpadding=6 style='border-collapse:collapse'><tr><th>Lesson</th><th>Helpful</th><th>Not helpful</th><th>Total</th></tr>{cells}</table>"
                    f"<p>Lessons with the most 'not helpful' votes come first.</p>", mimetype="text/html")



# ----------------------------------------------------------------- optional accounts (learning works without one)
EMAIL_RE = re.compile(r"^[^@\s]{1,64}@[^@\s]{1,255}\.[^@\s]{2,}$")
ORDER = [l for m in MODULES for l in m["lessons"]]                 # the daily path follows this order


def safe_next(target):
    return target if target and target.startswith("/") and not target.startswith("//") and "\\" not in target else url_for("my_learning")


def check_csrf():
    if not secrets.compare_digest(request.form.get("csrf", ""), session.get("csrf", "x")):
        abort(400)


def start_session(uid):
    session.clear()
    session.permanent = True
    session["uid"] = uid
    csrf_token()


@app.route("/signup", methods=["GET", "POST"])
@rate_limit(20, 60)
def signup():
    if current_user():
        return redirect(url_for("my_learning"))
    error, name, email = "", "", ""
    if request.method == "POST":
        check_csrf()
        name, email = request.form.get("name", "").strip()[:60], request.form.get("email", "").strip().lower()
        pw = request.form.get("password", "")
        if not name:
            error = "Enter your name."
        elif not EMAIL_RE.match(email):
            error = "Enter a valid email address."
        elif len(pw) < 8:
            error = "Use a password with at least 8 characters."
        else:
            try:
                cur = db().execute("INSERT INTO users (name, email, pw, created) VALUES (?, ?, ?, ?)", (name, email, generate_password_hash(pw), time.time()))
                db().commit()
                start_session(cur.lastrowid)
                return redirect(safe_next(request.args.get("next")))
            except sqlite3.IntegrityError:
                error = "An account with this email already exists. Log in instead."
    return render_template("signup.html", page="account", error=error, name=name, email=email, next=request.args.get("next", "")), 400 if error else 200


@app.route("/login", methods=["GET", "POST"])
@rate_limit(20, 60)
def login():
    if current_user():
        return redirect(url_for("my_learning"))
    error, email = "", ""
    if request.method == "POST":
        check_csrf()
        email = request.form.get("email", "").strip().lower()
        row = db().execute("SELECT id, pw FROM users WHERE email = ?", (email,)).fetchone()
        if row and check_password_hash(row[1], request.form.get("password", "")):
            start_session(row[0])
            return redirect(safe_next(request.args.get("next")))
        error = "Wrong email or password."
    return render_template("login.html", page="account", error=error, email=email, next=request.args.get("next", "")), 400 if error else 200


@app.post("/logout")
def logout():
    check_csrf()
    session.clear()
    return redirect(url_for("home"))


def need_user():
    u = current_user()
    if not u or not request.is_json:
        abort(401)
    return u


@app.errorhandler(401)
def unauthorised(_):
    if request.path.startswith("/api/"):
        return jsonify(error="Log in to save progress."), 401
    return redirect(url_for("login", next=request.path))


@app.post("/api/progress")
@rate_limit(240, 60)
def api_progress():
    u = need_user()
    data = request.get_json(silent=True) or {}
    slugs = data.get("lessons") if isinstance(data.get("lessons"), list) else [data.get("lesson")]
    slugs = [s for s in slugs[:400] if isinstance(s, str) and s in LESSON_BY_SLUG]
    now = time.time()
    db().executemany("INSERT OR IGNORE INTO progress (user_id, lesson, done_at) VALUES (?, ?, ?)", [(u["id"], s, now) for s in slugs])
    db().commit()
    return jsonify(done=sorted(user_done()))


@app.post("/api/pace")
@rate_limit(60, 60)
def api_pace():
    u = need_user()
    pace = (request.get_json(silent=True) or {}).get("pace")
    if pace not in (1, 2, 3, 5, 8):
        return jsonify(error="Choose 1, 2, 3, 5 or 8 lessons a day."), 400
    db().execute("UPDATE users SET pace = ? WHERE id = ?", (pace, u["id"]))
    db().commit()
    return jsonify(ok=True)


def local_offset():
    try:
        return max(-840, min(840, int(request.cookies.get("th_tz", "0"))))   # minutes behind UTC, set by the browser
    except ValueError:
        return 0


@app.get("/my-learning")
def my_learning():
    u = current_user()
    if not u:
        return redirect(url_for("login", next=request.path))
    done = user_done()
    off = dt.timedelta(minutes=-local_offset())
    day = lambda ts: (dt.datetime.fromtimestamp(ts, dt.timezone.utc) + off).date()
    today = (dt.datetime.now(dt.timezone.utc) + off).date()
    active = {day(ts) for ts in done.values()}
    streak, d = 0, today if today in active else today - dt.timedelta(days=1)
    while d in active:
        streak, d = streak + 1, d - dt.timedelta(days=1)
    done_today = sum(1 for ts in done.values() if day(ts) == today)
    week = [dict(label=(today - dt.timedelta(days=i)).strftime("%a"), on=(today - dt.timedelta(days=i)) in active, today=i == 0) for i in range(6, -1, -1)]
    todo = [l for l in ORDER if l["slug"] not in done]
    pace = u["pace"]
    plan = [dict(day=i + 1, lessons=todo[i * pace:(i + 1) * pace]) for i in range(7) if todo[i * pace:(i + 1) * pace]]
    mods = [dict(m=m, done=sum(1 for l in m["lessons"] if l["slug"] in done), total=len(m["lessons"])) for m in MODULES]
    return render_template("my_learning.html", page="account", total=len(ORDER), done_n=len(done), streak=streak, done_today=done_today,
                           week=week, plan=plan, mods=mods, days_left=-(-len(todo) // pace), recent=[LESSON_BY_SLUG[s] for s, _ in sorted(done.items(), key=lambda kv: -kv[1])[:5]])

@app.errorhandler(404)
def not_found(_):
    return render_template("404.html", page=""), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
