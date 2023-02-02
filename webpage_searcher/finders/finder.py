from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from typing import List

from webpage_searcher.finders.result import Result
from webpage_searcher.utils.constants import all_tags, text_inline_tags


class Finder(ABC):
    _soup: BeautifulSoup

    @abstractmethod
    def find(self, item: str) -> List[Result]:
        pass

    def __init__(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")
        self._soup = self._clean_html(soup)

    def _clean_html(self, soup: BeautifulSoup) -> BeautifulSoup:
        for item in soup.find_all({"script", "style"}, recursive=True):
            item.decompose()
        for item in soup.find_all(text_inline_tags, recursive=True):
            item.unwrap()
        return soup
