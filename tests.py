"""Run: python -m unittest tests"""
import unittest
from app import app
from content import LESSON_BY_SLUG, MODULES, QUESTIONS


class TechHub(unittest.TestCase):
    def setUp(self):
        self.c = app.test_client()

    def test_all_pages_load(self):
        urls = ["/", "/try", "/quiz", "/quiz/html", "/quiz/css", "/quiz/all"]
        for m in MODULES:
            urls.append(f"/{m['slug']}/")
            for l in m["lessons"]:
                urls += [f"/{m['slug']}/{l['slug']}", f"/try/{l['slug']}"]
        for u in urls:
            self.assertEqual(self.c.get(u).status_code, 200, u)

    def test_404s(self):
        for u in ["/html/nope", "/nope/", "/css/html-intro", "/quiz/zzz", "/try/zzz"]:
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

    def test_quiz_by_module(self):
        for mod in ("html", "css", "all"):
            qs = self.c.get(f"/api/quiz?n=10&module={mod}").get_json()["questions"]
            self.assertEqual(len(qs), 10)
            self.assertTrue(all("answer" not in q for q in qs))
            if mod != "all":
                self.assertTrue(all(QUESTIONS[q["id"]]["module"] == mod for q in qs))
            res = self.c.post("/api/quiz/check", json={"answers": {q["id"]: q["options"][0] for q in qs}}).get_json()
            self.assertEqual(res["total"], 10)

    def test_search(self):
        r = self.c.get("/api/search?q=flexbox").get_json()["results"]
        self.assertTrue(any("flex" in x["title"].lower() for x in r))


if __name__ == "__main__":
    unittest.main()
