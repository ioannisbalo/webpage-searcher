import sys

from src.http import get_html
from src.outputs.print_output import PrintOutput
from src.finders import UrlFinder, PhraseFinder


class App:
    def __init__(self, webpage: str) -> None:
        html = get_html(webpage)
        if not html:
            sys.exit(1)
        self._url_finder = UrlFinder(html)
        self._phrase_finder = PhraseFinder(html)
        self._output = PrintOutput()

    def find_url(self, url: str) -> None:
        results = self._url_finder.find(url)
        self._output.write(results)

    def find_phrase(self, phrase: str) -> None:
        results = self._phrase_finder.find(phrase)
        self._output.write(results)
