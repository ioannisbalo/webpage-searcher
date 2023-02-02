from bs4 import Tag
from abc import ABC, abstractmethod

from webpage_searcher.utils.constants import text_block_tags, anchor_tags
from webpage_searcher.utils.xpath import element_xpath
from webpage_searcher.finders.result import Result, Link


class TagHandler(ABC):
    @abstractmethod
    def result(self) -> Result:
        pass

    def __init__(self, tag: Tag):
        self._tag = tag

class ParentHandler(TagHandler):
    tags = text_block_tags

    def result(self) -> Result:
        return Result(
            tag=self._tag.name,
            xpath=element_xpath(self._tag),
            string=self._tag.get_text(),
        )

class AnchorHandler(TagHandler):
    tags = anchor_tags

    def result(self) -> Result:
        return Result(
            tag=self._tag.name,
            xpath=element_xpath(self._tag),
            string=self._tag.get_text(),
            link=Link(
                href=self._tag.attrs.get("href"),
                nofollow="nofollow" in self._tag.attrs.get("rel", [])
            ),
        )
