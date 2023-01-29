from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from typing import List

from src.finders.result import Result


class Finder(ABC):
    _soup: BeautifulSoup

    @abstractmethod
    def find(self, item: str) -> List[Result]:
        pass

    def __init__(self, html: str) -> None:
        soup = BeautifulSoup(html, "html.parser")
        self._soup = self._clean_html(soup)

    def _clean_html(self, soup: BeautifulSoup) -> BeautifulSoup:
        to_remove = ["script", "style"]
        for tag in to_remove:
            for item in soup.find_all(tag, recursive=True):
                item.decompose()
        return soup
