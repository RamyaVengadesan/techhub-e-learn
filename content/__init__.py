"""Course content. Each module lives in its own file and exports GROUPS and LESSONS."""
from . import css as _css
from . import html as _html
from . import js as _js

MODULES = [
    dict(slug="html", title="HTML", subtitle="Structure the web", color="#E34F26",
         tagline="Learn to build the structure of every web page: text, links, images, lists, tables, forms and semantic layout.",
         groups=_html.GROUPS, lessons=_html.LESSONS),
    dict(slug="css", title="CSS", subtitle="Style the web", color="#1572B6",
         tagline="Make pages look professional: colours, the box model, typography, flexbox, grid, animation and responsive design.",
         groups=_css.GROUPS, lessons=_css.LESSONS),
    dict(slug="js", title="JavaScript", subtitle="Make the web interactive", color="#F7DF1E",
         tagline="Bring pages to life: variables, functions, arrays, objects, the DOM, events, async code and modern ES6+ features. Every example runs live.",
         groups=_js.GROUPS, lessons=_js.LESSONS),
]

MODULE_BY_SLUG = {m["slug"]: m for m in MODULES}
for m in MODULES:
    for l in m["lessons"]:
        l["module"] = m["slug"]

LEVELS = [("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")]
LEVEL_NAME = dict(LEVELS)
# which lesson groups belong to which quiz level, per module
LEVEL_GROUPS = {
    "html": {"beginner": ["Getting Started", "Text & Style"],
             "intermediate": ["Links & Media", "Lists & Tables", "Forms"],
             "advanced": ["Layout & Semantics", "Advanced", "Advanced HTML"]},
    "css": {"beginner": ["Getting Started", "Colors & Backgrounds", "Box Model", "Text & Fonts"],
            "intermediate": ["Layout", "Components", "Selectors"],
            "advanced": ["Effects & Animation", "Responsive Design", "Advanced", "Advanced CSS"]},
    "js": {"beginner": ["Getting Started", "Control Flow", "Functions"],
           "intermediate": ["Strings & Numbers", "Arrays & Objects", "The DOM", "Events & Timers"],
           "advanced": ["Asynchronous JavaScript", "Modern JavaScript", "Best Practices"]},
}
for m in MODULES:
    where = {g: lvl for lvl, gs in LEVEL_GROUPS[m["slug"]].items() for g in gs}
    assert set(where) == set(m["groups"]), f"level map out of date for {m['slug']}"
    for l in m["lessons"]:
        l["level"] = where[l["group"]]

LESSON_BY_SLUG = {l["slug"]: l for m in MODULES for l in m["lessons"]}
QUESTIONS = {f"{l['slug']}:{i}": dict(q, module=l["module"], level=l["level"]) for l in LESSON_BY_SLUG.values() for i, q in enumerate(l["exercise"])}

# questions are shown as plain text, so drop backtick markup from them
for l in LESSON_BY_SLUG.values():
    for q in l["exercise"]:
        q["q"] = q["q"].replace("`", "")
        q["options"] = [o.replace("`", "") for o in q["options"]]

assert len(LESSON_BY_SLUG) == sum(len(m["lessons"]) for m in MODULES), "duplicate lesson slug"

from .reference import REFS  # noqa: E402  (reference tables, W3Schools style)

REF_BY_SLUG = {r["slug"]: r for r in REFS}

from .challenges import CHALLENGES  # noqa: E402
from .cheatsheets import CHEATSHEETS  # noqa: E402
from .glossary import GLOSSARY  # noqa: E402
from .projects import PROJECTS  # noqa: E402
from .roadmap import ROADMAP  # noqa: E402

CHALLENGE_BY_SLUG = {c["slug"]: c for c in CHALLENGES}
PROJECT_BY_SLUG = {p["slug"]: p for p in PROJECTS}
SHEET_BY_SLUG = {s["slug"]: s for s in CHEATSHEETS}
assert len(CHALLENGE_BY_SLUG) == len(CHALLENGES) and len(PROJECT_BY_SLUG) == len(PROJECTS), "duplicate slug"
for _stage in ROADMAP:
    for _s in _stage["lessons"]:
        assert _s in LESSON_BY_SLUG, f"roadmap lesson missing: {_s}"
