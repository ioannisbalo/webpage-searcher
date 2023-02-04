from unittest import TestCase

from webpage_searcher.finders.phrase.phrase_finder import PhraseFinder
from webpage_searcher.finders.result import Link, Result


class TestPhraseFinder(TestCase):
    phrase_finder: PhraseFinder
    html: str

    @classmethod
    def setUpClass(cls):
        with open("tests/files/veza_domain.txt") as f:
            cls.html = f.read()

    def test_find_phrase(self):
        cases = [
            {
                "phrase": "Chili Piper Get",
                "results": [
                    Result(
                        tag="p",
                        xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/p",
                        string=(
                            "Check how Veza helped Chili Piper get anew look for "
                            "their website in a record amount of time."
                        ),
                    ),
                ],
            },
            {
                "phrase": "chili piper get",
                "results": [
                    Result(
                        tag="p",
                        xpath="/html/body/div/div/section[6]/div/div[2]/div[1]/div[1]/p",
                        string=(
                            "Check how Veza helped Chili Piper get anew look for "
                            "their website in a record amount of time."
                        ),
                    ),
                ],
            },
            {
                "phrase": "brands reach their marketing goals and beyond",
                "results": [
                    Result(
                        tag="div",
                        xpath="/html/body/div/div/section[1]/div[1]/div[6]/div[2]/div[3]/div[2]/div[4]",
                        string=(
                            "Veza Digital is a full-service growth marketing agency that "
                            "helps SaaS and B2B brands reach their marketing goals and beyond."
                        ),
                    )
                ],
            },
        ]
        for case in cases:
            with self.subTest(case["phrase"]):
                self._assert_case(self.html, case["phrase"], case["results"])

    def test_find_phrase_invalid_input(self):
        cases = ["", " ", "                       "]
        finder = PhraseFinder(self.html)
        for case in cases:
            with self.subTest(case):
                with self.assertRaises(ValueError):
                    finder.find(case)

    def test_find_phrase_split_inline(self):
        html = "<html><body><p>he<span>ll</span>o sir</p></body></html>"
        expected = [Result(tag="p", xpath="/html/body/p", string="hello sir")]
        self._assert_case(html, "hello", expected)

    def test_find_phrase_in_anchor(self):
        html = '<html><body><p>this is <a href="https://google.com">google</a>!</p></body></html>'
        expected = [
            Result(
                tag="a",
                xpath="/html/body/p/a",
                string="google",
                link=Link(href="https://google.com", nofollow=False),
            )
        ]
        self._assert_case(html, "google", expected)

        no_follow_html = (
            '<html><body><p>this is <a href="https://google.com" rel="nofollow">google</a>!</p></body></html>'
        )
        expected[0].link.nofollow = True
        self._assert_case(no_follow_html, "google", expected)

    def test_find_multiple(self):
        html = (
            '<html><body><div>one<p> two </p><a href="sample.com">'
            "one</a></div><p>one <span>two</span></p></body></html>"
        )
        expected = [
            Result(tag="div", xpath="/html/body/div", string="one two one"),
            Result(tag="p", xpath="/html/body/p", string="one two"),
            Result(
                tag="a",
                xpath="/html/body/div/a",
                string="one",
                link=Link(href="sample.com", nofollow=False),
            ),
        ]
        self._assert_case(html, "one", expected)

    def _assert_case(self, html: str, phrase: str, expected: list[Result]) -> None:
        finder = PhraseFinder(html)
        results = finder.find(phrase)
        if len(expected) == 1:
            self.assertEqual(results, expected)
        else:
            for result in expected:
                self.assertTrue(result in results)
