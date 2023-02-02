from bs4 import BeautifulSoup
from unittest import TestCase

from webpage_searcher.utils.xpath import element_xpath


class TestXpath(TestCase):
    def test_element_xpath(self):
        cases = [
            {"html": "<html id=\"this\"></html>", "xpath": "/html"},
            {"html": "<html id=\"this\"><body><p></p></body></html>", "xpath": "/html"},
            {"html": (
                "<html><body>"
                "<p id=\"this\"></p>"
                "</body></html>"
            ), "xpath": "/html/body/p"},
            {"html": (
                "<html><body>"
                "<p></p>"
                "<p></p>"
                "<p id=\"this\"></p>"
                "</body></html>"
            ), "xpath": "/html/body/p[3]"},
            {"html": (
                "<html><body>"
                "<p></p>"
                "<p id=\"this\"></p>"
                "<p></p>"
                "</body></html>"
            ), "xpath": "/html/body/p[2]"},
        ]

        for case in cases:
            soup = BeautifulSoup(case["html"], "html.parser")
            tag = soup.find(attrs={"id": "this"})
            self.assertEqual(element_xpath(tag), case["xpath"])

    def test_element_xpath_error(self):
        self.assertEqual(element_xpath("no tag"), "unable to calculate xpath")
