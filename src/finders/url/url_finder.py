from bs4 import Tag
from typing import List, Optional
from urllib.parse import urlparse

from src.finders.finder import Finder
from src.finders.result import Result
from src.utils.constants import text_context_tags, schemes
from src.utils.xpath import element_xpath


class UrlFinder(Finder):
    def __init__(self, html: str) -> None:
        super().__init__(html)
        self._tags = self._soup.find_all("a", recursive=True)

    def find(self, url: str) -> List[Result]:
        filled_url = self._fill_scheme(url)
        domain = self._extract_domain(filled_url)
        if not domain:
            raise ValueError("please provide an appropriate url, for example: https://google.com/search")
        return [self._create_result(tag) for tag in self._tags if self._check_tag(domain, tag)]

    def _create_result(self, tag: Tag) -> Result:
        return Result(
            tag=tag.name,
            xpath=element_xpath(tag),
            href=tag.attrs["href"],
            string=tag.getText(),
            context=self._find_context(tag),
        )

    def _find_context(self, tag: Tag) -> Optional[str]:
        for child in tag.children:
            if child.name == "img":
                return child.attrs["src"]
        for parent in tag.parents:
            if parent.name in text_context_tags:
                return parent.get_text()
        return None

    def _check_tag(self, domain: str, tag: Tag) -> bool:
        tag_url = tag.attrs["href"]
        if tag_url.startswith("/"):
            return False
        tag_domain = self._extract_domain(tag_url)
        return tag_domain and tag_domain == domain

    def _extract_domain(self, url: str) -> str:
        parsed = urlparse(url)
        domain = parsed.netloc
        return domain.strip("www.").strip()

    def _fill_scheme(self, url: str) -> str:
        if any(url.startswith(scheme) for scheme in schemes):
            return url
        return "https://" + url