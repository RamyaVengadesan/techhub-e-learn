"""TechHub: an online learning site with an HTML module and a CSS module.

Run:  python app.py   then open http://127.0.0.1:5000
"""
import os
import random
import re
from html import escape

from flask import Flask, abort, jsonify, render_template, request
from markupsafe import Markup

from content import LESSON_BY_SLUG, MODULE_BY_SLUG, MODULES, QUESTIONS

app = Flask(__name__)

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


@app.context_processor
def inject():
    return dict(modules=MODULES)


# ----------------------------------------------------------------- pages
@app.get("/")
def home():
    total = sum(len(m["lessons"]) for m in MODULES)
    return render_template("home.html", page="home", total=total, questions=len(QUESTIONS))


@app.get("/quiz")
def quiz_pick():
    return render_template("quiz_pick.html", page="quiz", counts={m["slug"]: sum(1 for q in QUESTIONS.values() if q["module"] == m["slug"]) for m in MODULES})


@app.get("/quiz/<mod>")
def quiz(mod):
    if mod != "all" and mod not in MODULE_BY_SLUG:
        abort(404)
    return render_template("quiz.html", page="quiz", mod=mod, module=MODULE_BY_SLUG.get(mod))


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
    return render_template("module.html", page="module", module=m)


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
def api_check():
    data = request.get_json(silent=True) or {}
    q = QUESTIONS.get(data.get("id"))
    if not q:
        return jsonify(error="unknown question"), 404
    answer = q["options"][q["answer"]]
    return jsonify(correct=data.get("choice") == answer, answer=answer)


@app.get("/api/quiz")
def api_quiz():
    mod = request.args.get("module", "all")
    pool = [(k, v) for k, v in QUESTIONS.items() if mod == "all" or v["module"] == mod]
    n = min(max(request.args.get("n", 10, type=int), 1), len(pool))
    out = []
    for qid, q in random.sample(pool, n):
        opts = q["options"][:]
        random.shuffle(opts)
        out.append(dict(id=qid, q=q["q"], options=opts))
    return jsonify(questions=out)


@app.post("/api/quiz/check")
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


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html", page=""), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
