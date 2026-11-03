"""Run: python -m unittest tests"""
import unittest
from app import app
from content import CHALLENGES, CHEATSHEETS, LESSON_BY_SLUG, MODULES, PROJECTS, QUESTIONS


class TechHub(unittest.TestCase):
    def setUp(self):
        self.c = app.test_client()

    def test_all_pages_load(self):
        urls = ["/", "/try", "/quiz", "/quiz/html", "/quiz/css", "/quiz/js/beginner", "/quiz/html/advanced", "/reference"]
        for m in MODULES:
            urls.append(f"/{m['slug']}/")
            for l in m["lessons"]:
                urls += [f"/{m['slug']}/{l['slug']}", f"/try/{l['slug']}"]
        for u in urls:
            self.assertEqual(self.c.get(u).status_code, 200, u)

    def test_new_pages_load(self):
        urls = ["/roadmap", "/challenges", "/projects", "/tools", "/tools/flexbox", "/tools/grid", "/tools/box-model", "/cheatsheets",
                "/glossary", "/privacy", "/terms", "/login", "/signup", "/sitemap.xml", "/robots.txt"]
        urls += [f"/challenges/{c['slug']}" for c in CHALLENGES] + [f"/projects/{p['slug']}" for p in PROJECTS] + [f"/projects/{p['slug']}/edit" for p in PROJECTS]
        urls += [f"/cheatsheets/{s['slug']}" for s in CHEATSHEETS]
        for u in urls:
            self.assertEqual(self.c.get(u).status_code, 200, u)
        self.assertIn("<urlset", self.c.get("/sitemap.xml").get_data(as_text=True))

    def test_feedback_api(self):
        import os, tempfile
        import app as appmod
        appmod.DB_PATH = os.path.join(tempfile.mkdtemp(), "t.db")
        ok = self.c.post("/api/feedback", json={"lesson": "intro", "helpful": True})
        self.assertEqual(ok.status_code, 200)
        self.assertEqual(self.c.post("/api/feedback", json={"lesson": "nope", "helpful": True}).status_code, 400)
        self.assertEqual(self.c.post("/api/feedback", json={"lesson": "intro", "helpful": "yes"}).status_code, 400)
        self.assertEqual(self.c.get("/admin/feedback").status_code, 404)

    def _fresh_db(self):
        import os, tempfile
        import app as appmod
        appmod.DB_PATH = os.path.join(tempfile.mkdtemp(), "t.db")

    def _csrf(self, c, path):
        import re
        html = c.get(path).get_data(as_text=True)
        return re.search(r'name="csrf" value="([0-9a-f]+)"', html).group(1)

    def test_accounts_and_progress(self):
        self._fresh_db()
        c = self.c
        self.assertEqual(c.get("/my-learning").status_code, 302)                      # needs login
        self.assertEqual(c.post("/api/progress", json={"lesson": "intro"}).status_code, 401)
        tok = self._csrf(c, "/signup")
        self.assertEqual(c.post("/signup", data={"csrf": "bad", "name": "A", "email": "a@b.co", "password": "longenough"}).status_code, 400)
        r = c.post("/signup", data={"csrf": tok, "name": "Asha", "email": "Asha@Example.com", "password": "short"})
        self.assertEqual(r.status_code, 400)
        r = c.post("/signup", data={"csrf": tok, "name": "Asha", "email": "Asha@Example.com", "password": "longenough"})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(c.get("/my-learning").status_code, 200)
        self.assertEqual(c.post("/api/progress", json={"lesson": "intro"}).get_json()["done"], ["intro"])
        self.assertEqual(c.post("/api/progress", json={"lessons": ["basic", "nope", 5]}).get_json()["done"], ["basic", "intro"])
        self.assertEqual(c.post("/api/pace", json={"pace": 99}).status_code, 400)
        self.assertEqual(c.post("/api/pace", json={"pace": 2}).status_code, 200)
        page = c.get("/my-learning").get_data(as_text=True)
        self.assertIn("Welcome back, Asha", page)
        tok = self._csrf(c, "/my-learning")
        self.assertEqual(c.post("/logout", data={"csrf": tok}).status_code, 302)
        self.assertEqual(c.get("/my-learning").status_code, 302)
        tok = self._csrf(c, "/login")
        self.assertEqual(c.post("/login", data={"csrf": tok, "email": "asha@example.com", "password": "wrong-pass"}).status_code, 400)
        r = c.post("/login?next=//evil.com", data={"csrf": tok, "email": "asha@example.com", "password": "longenough"})
        self.assertEqual(r.status_code, 302)
        self.assertNotIn("evil.com", r.headers["Location"])                            # open redirect blocked
        self.assertEqual(c.post("/api/progress", json={"lesson": "intro"}).get_json()["done"], ["basic", "intro"])

    def test_404s(self):
        for u in ["/html/nope", "/nope/", "/css/html-intro", "/quiz/zzz", "/quiz/html/zzz", "/reference/zzz", "/challenges/zzz", "/projects/zzz", "/tools/zzz", "/cheatsheets/zzz", "/try/zzz"]:
            self.assertEqual(self.c.get(u).status_code, 404, u)

    def test_content_valid(self):
        for m in MODULES:
            for l in m["lessons"]:
                self.assertIn(l["group"], m["groups"], l["slug"])
                self.assertGreaterEqual(len(l["exercise"]), 2, l["slug"])
        texts = [q["q"] for q in QUESTIONS.values()]
        self.assertEqual(len(texts), len(set(texts)))
        for q in QUESTIONS.values():
            self.assertEqual(len(q["options"]), 4)
            self.assertEqual(len(set(q["options"])), 4, q["q"])
            self.assertLess(q["answer"], 4)

    def test_answers_hidden_and_checked(self):
        slug = next(iter(LESSON_BY_SLUG))
        mod = LESSON_BY_SLUG[slug]["module"]
        self.assertNotIn('"answer"', self.c.get(f"/{mod}/{slug}").get_data(as_text=True))
        q = QUESTIONS[f"{slug}:0"]
        ok = self.c.post("/api/check", json={"id": f"{slug}:0", "choice": q["options"][q["answer"]]}).get_json()
        bad = self.c.post("/api/check", json={"id": f"{slug}:0", "choice": "zzz"}).get_json()
        self.assertTrue(ok["correct"]); self.assertFalse(bad["correct"])

    def test_quiz_by_module_and_level(self):
        for m in MODULES:
            for level in ("beginner", "intermediate", "advanced"):
                qs = self.c.get(f"/api/quiz?n=10&module={m['slug']}&level={level}").get_json()["questions"]
                self.assertEqual(len(qs), 10, (m["slug"], level))
                self.assertTrue(all("answer" not in q for q in qs))
                self.assertTrue(all(QUESTIONS[q["id"]]["module"] == m["slug"] and QUESTIONS[q["id"]]["level"] == level for q in qs))
        res = self.c.post("/api/quiz/check", json={"answers": {q["id"]: q["options"][0] for q in qs}}).get_json()
        self.assertEqual(res["total"], 10)
        self.assertEqual(self.c.get("/api/quiz?module=html&level=zzz").status_code, 404)

    def test_reference_pages(self):
        from content import REFS
        for r in REFS:
            self.assertEqual(self.c.get(f"/reference/{r['slug']}").status_code, 200, r["slug"])

    def test_search(self):
        r = self.c.get("/api/search?q=flexbox").get_json()["results"]
        self.assertTrue(any("flex" in x["title"].lower() for x in r))


if __name__ == "__main__":
    unittest.main()
