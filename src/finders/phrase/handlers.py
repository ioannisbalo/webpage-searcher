from bs4 import Tag
from abc import ABC, abstractmethod

from src.utils.constants import as_child_tags, as_parent_tags, anchor_tags
from src.utils.xpath import element_xpath
from src.finders.result import Result


class TagHandler(ABC):
    @abstractmethod
    def result(self) -> Result:
        pass

    def __init__(self, tag: Tag):
        self._tag = tag

class ParentHandler(TagHandler):
    tags = as_parent_tags

    def result(self) -> Result:
        return Result(
            tag=self._tag.name,
            xpath=element_xpath(self._tag),
            string=self._tag.get_text(),
        )

class ChildHandler(TagHandler):
    tags = as_child_tags

    def result(self) -> Result:
        string = self._tag.get_text()
        context = self._get_context()
        return Result(
            tag=self._tag.name,
            xpath=element_xpath(self._tag),
            string=string,
            context=context if context != string else None,
        )

    def _get_context(self) -> str:
        parent = self._tag.parent
        while parent.name in self.tags:
            parent = parent.parent
        return parent.get_text()

class AnchorHandler(TagHandler):
    tags = anchor_tags

    def result(self) -> Result:
        return Result(
            tag=self._tag.name,
            xpath=element_xpath(self._tag),
            string=self._tag.get_text(),
            href=self._tag.attrs.get("href"),
        )
