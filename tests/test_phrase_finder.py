from unittest import TestCase

from src.finders.phrase.phrase_finder import PhraseFinder
from src.finders.result import Result


class TestPhraseFinder(TestCase):
    phrase_finder: PhraseFinder

    @classmethod
    def setUpClass(cls):
        with open("tests/files/veza_domain.txt") as f:
            html = f.read()
        cls.phrase_finder = PhraseFinder(html)

    def test_find_phrase(self):
        cases = [
            {"phrase": "Chili Piper", "results": [
                Result(tag="p", xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/p", string="Check how Veza helped Chili Piper get anew look for their website in a record amount of time."),
                Result(tag="h2", xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/h2", string="Chili Piper")
            ]},
            {"phrase": "chili piper", "results": [
                Result(tag="p", xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/p", string="Check how Veza helped Chili Piper get anew look for their website in a record amount of time."),
                Result(tag="h2", xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/h2", string="Chili Piper")
            ]},
            {"phrase": "veza digital is", "results": [
                Result(tag="div", xpath="/html/body/div/div/section[1]/div[1]/div[6]/div[2]/div[3]/div[2]/div[4]", string="Veza Digital is a full-service growth marketing agency that helps SaaS and B2B brands reach their marketing goals and beyond."),
                Result(tag="p", xpath="/html/body/div/div/section[1]/div[1]/div[6]/div[2]/div[3]/div[2]/div[1]/p", string="Veza Digital is a full-service growth marketing ")
            ]},
        ]
        for case in cases:
            with self.subTest(case["phrase"]):
                results = self.phrase_finder.find(case["phrase"])
                self.assertEqual(results, case["results"])

    def test_find_phrase_invalid_input(self):
        cases = ["", " ", "                       "]
        for case in cases:
            with self.subTest(case):
                with self.assertRaises(ValueError):
                    self.phrase_finder.find(case)
