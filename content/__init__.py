"""Course content. Each module lives in its own file and exports GROUPS and LESSONS."""
from . import css as _css
from . import html as _html

MODULES = [
    dict(slug="html", title="HTML", subtitle="Structure the web", color="#E34F26",
         tagline="Learn to build the structure of every web page: text, links, images, lists, tables, forms and semantic layout.",
         groups=_html.GROUPS, lessons=_html.LESSONS),
    dict(slug="css", title="CSS", subtitle="Style the web", color="#1572B6",
         tagline="Make pages look professional: colours, the box model, typography, flexbox, grid, animation and responsive design.",
         groups=_css.GROUPS, lessons=_css.LESSONS),
]

MODULE_BY_SLUG = {m["slug"]: m for m in MODULES}
for m in MODULES:
    for l in m["lessons"]:
        l["module"] = m["slug"]

LESSON_BY_SLUG = {l["slug"]: l for m in MODULES for l in m["lessons"]}
QUESTIONS = {f"{l['slug']}:{i}": dict(q, module=l["module"]) for l in LESSON_BY_SLUG.values() for i, q in enumerate(l["exercise"])}

# questions are shown as plain text, so drop backtick markup from them
for l in LESSON_BY_SLUG.values():
    for q in l["exercise"]:
        q["q"] = q["q"].replace("`", "")
        q["options"] = [o.replace("`", "") for o in q["options"]]

assert len(LESSON_BY_SLUG) == sum(len(m["lessons"]) for m in MODULES), "duplicate lesson slug"
