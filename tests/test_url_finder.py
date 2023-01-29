from unittest import TestCase

from src.finders.url.url_finder import UrlFinder
from src.finders.result import Result


class TestUrlFinder(TestCase):
    url_finder: UrlFinder

    @classmethod
    def setUpClass(cls):
        with open("tests/files/veza_domain.txt") as f:
            html = f.read()
        cls.url_finder = UrlFinder(html)

    def test_find_url(self):
        cases = [
            {"url": "twitter.com", "results": [Result(tag='a', xpath='/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]', string='Twitter', href='https://twitter.com/vezadigital', context=None)]},
            {"url": "http://twitter.com", "results": [Result(tag='a', xpath='/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]', string='Twitter', href='https://twitter.com/vezadigital', context=None)]},
            {"url": "https://twitter.com", "results": [Result(tag='a', xpath='/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[2]', string='Twitter', href='https://twitter.com/vezadigital', context=None)]},
            {"url": "facebook.com", "results": [Result(tag='a', xpath='/html/body/div/div/nav/div[1]/div/div[1]/div/div/div[2]/div[2]/div/a[5]', string='Facebook', href='https://www.facebook.com/VezaDigital/', context=None)]},
            {"url": "vezadigital.com", "results": [
                Result(tag='a', xpath='/html/body/div/div/section[6]/div/div[2]/div[2]/div[3]/div[2]/div/a', string='Show more', href='https://www.vezadigital.com/case-study/chili-piper', context=None),
                Result(tag='a', xpath='/html/body/div/div/section[6]/div/div[3]/div[2]/div[1]/div[2]/div/a', string='Show more', href='https://www.vezadigital.com/case-study/instabug', context=None),
                Result(tag='a', xpath='/html/body/div/div/section[6]/div/div[4]/div[2]/div[2]/div[1]/div[2]/div/a', string='Show more', href='https://www.vezadigital.com/case-study/spatial', context=None),
                Result(tag='a', xpath='/html/body/div/div/section[6]/div/div[5]/div[2]/div[2]/div[2]/div/a', string='Show more', href='https://www.vezadigital.com/case-study/regfox', context=None)
            ]},
        ]
        for case in cases:
            with self.subTest(case["url"]):
                results = self.url_finder.find(case["url"])
                self.assertEqual(results, case["results"])


    def test_find_url_invalid_input(self):
        cases = ["", " ", "/", "/hello.com"]
        for case in cases:
            with self.subTest(case):
                with self.assertRaises(ValueError):
                    self.url_finder.find(case)
