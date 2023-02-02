from unittest import TestCase
from typing import List

from webpage_searcher.finders.url.url_finder import UrlFinder
from webpage_searcher.finders.result import Result, Link


class TestUrlFinder(TestCase):
    html: str

    @classmethod
    def setUpClass(cls):
        with open("tests/files/veza_domain.txt") as f:
            cls.html = f.read()

    def test_find_url(self):
        cases = [
            {"url": "twitter.com", "results": [Result(tag="a", xpath="/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]", string="Twitter", link=Link(href="https://twitter.com/vezadigital"), context=None)]},
            {"url": "http://twitter.com", "results": [Result(tag="a", xpath="/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]", string="Twitter", link=Link(href="https://twitter.com/vezadigital"), context=None)]},
            {"url": "https://twitter.com", "results": [Result(tag="a", xpath="/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]", string="Twitter", link=Link(href="https://twitter.com/vezadigital"), context=None)]},
            {"url": "facebook.com", "results": [Result(tag="a", xpath="/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[5]", string="Facebook", link=Link(href="https://www.facebook.com/VezaDigital/"), context=None)]},
            {"url": "vezadigital.com", "results": [
                Result(tag="a", xpath="/html/body/div/div/section[6]/div/div[2]/div[2]/div[3]/div[2]/div/a", string="Show more", link=Link(href="https://www.vezadigital.com/case-study/chili-piper"), context=None),
                Result(tag="a", xpath="/html/body/div/div/section[6]/div/div[3]/div[2]/div[1]/div[2]/div/a", string="Show more", link=Link(href="https://www.vezadigital.com/case-study/instabug"), context=None),
                Result(tag="a", xpath="/html/body/div/div/section[6]/div/div[4]/div[2]/div[2]/div[1]/div[2]/div/a", string="Show more", link=Link(href="https://www.vezadigital.com/case-study/spatial"), context=None),
                Result(tag="a", xpath="/html/body/div/div/section[6]/div/div[5]/div[2]/div[2]/div[2]/div/a", string="Show more", link=Link(href="https://www.vezadigital.com/case-study/regfox"), context=None)
            ]},
        ]
        for case in cases:
            with self.subTest(case["url"]):
                self._assert_case(self.html, case["url"], case["results"])

    def test_find_url_invalid_input(self):
        finder = UrlFinder(self.html)
        cases = ["", " ", "/", "/hello.com"]
        for case in cases:
            with self.subTest(case):
                with self.assertRaises(ValueError):
                    finder.find(case)

    def test_find_no_follow(self):
        html = "<html><body><p>this is <a href=\"https://google.com\" rel=\"nofollow\">google</a>!</p></body></html>"
        expected = [Result(tag="a", xpath="/html/body/p/a", string="google", link=Link(href="https://google.com", nofollow=True), context='this is google!')]
        self._assert_case(html, "www.google.com", expected)

    def test_find_with_www(self):
        html = "<html><body><a href=\"https://google.com\">google</a></body></html>"
        expected = [Result(tag="a", xpath="/html/body/a", string="google", link=Link(href="https://google.com", nofollow=False))]
        self._assert_case(html, "www.google.com", expected)

    def test_exclude_internal_links(self):
        html = "<html><body><a href=\"/products\">products</a></body></html>"
        self._assert_case(html, "products", [])

    def test_find_context_image(self):
        html = "<html><body><a href=\"https://google.com\"><img src=\"google.png\"></img></a></body></html>"
        expected = [Result(context="google.png", tag="a", xpath="/html/body/a", string="", link=Link(href="https://google.com", nofollow=False))]
        self._assert_case(html, "www.google.com", expected)

    def test_find_context_parent(self):
        html = "<html><body><p>This is <a href=\"https://google.com\">google</a>!</p></body></html>"
        expected = [Result(context="This is google!", tag="a", xpath="/html/body/p/a", string="google", link=Link(href="https://google.com", nofollow=False))]
        self._assert_case(html, "www.google.com", expected)

    def _assert_case(self, html: str, url: str, expected: List[Result]) -> None:
        finder = UrlFinder(html)
        results = finder.find(url)
        self.assertEqual(results, expected)
