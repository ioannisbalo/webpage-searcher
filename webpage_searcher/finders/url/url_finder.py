from re import sub
from typing import Optional
from urllib.parse import urlparse

from bs4 import Tag

from webpage_searcher.finders.finder import Finder
from webpage_searcher.finders.result import Link, Result
from webpage_searcher.utils.constants import schemes, text_context_tags
from webpage_searcher.utils.xpath import element_xpath


class UrlFinder(Finder):
    def __init__(self, html: str) -> None:
        super().__init__(html)
        self._tags = [tag for tag in self._soup.find_all("a", recursive=True) if "href" in tag.attrs]

    def find(self, url: str) -> list[Result]:
        filled_url = self._fill_scheme(url)
        domain = self._extract_domain(filled_url)
        if not domain:
            raise ValueError("please provide an appropriate url, for example: https://google.com/search")
        return [self._create_result(tag) for tag in self._tags if self._check_tag(domain, tag)]

    def _create_result(self, tag: Tag) -> Result:
        return Result(
            tag=tag.name,
            xpath=element_xpath(tag),
            link=Link(href=tag.attrs["href"], nofollow="nofollow" in tag.attrs.get("rel", [])),
            string=tag.getText(),
            context=self._find_context(tag),
        )

    def _find_context(self, tag: Tag) -> Optional[str]:
        for child in tag.children:
            if not isinstance(child, Tag):
                continue
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
        return tag_domain is not None and tag_domain == domain

    def _extract_domain(self, url: str) -> Optional[str]:
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            return sub("www\\.", "", domain).strip()
        except (KeyError, ValueError, TypeError):
            return None

    def _fill_scheme(self, url: str) -> str:
        if any(url.startswith(scheme) for scheme in schemes):
            return url
        return "https://" + url
