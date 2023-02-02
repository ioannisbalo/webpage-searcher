from bs4 import NavigableString, Tag
from typing import List, Type

from webpage_searcher.finders.finder import Finder
from webpage_searcher.finders.phrase.handlers import AnchorHandler, ParentHandler, TagHandler
from webpage_searcher.finders.result import Result


class PhraseFinder(Finder):
    handlers: Type[TagHandler] = [
        ParentHandler,
        AnchorHandler,
    ]

    def find(self, phrase: str) -> List[Result]:
        phrase = self._format_phrase(phrase)
        results = []
        for handler_class in self.handlers:
            for tag_name in handler_class.tags:
                tags: List[Tag] = self._soup.find_all(tag_name, recursive=True)
                for tag in tags:
                    if phrase in self._get_text(tag):
                        handler = handler_class(tag)
                        results.append(handler.result())
        return results

    def _format_phrase(self, phrase: str) -> str:
        result = phrase.strip()
        if not result:
            raise ValueError("please provide an appropriate phrase, example: Chili Piper")
        return result.lower()

    def _get_text(self, tag: Tag) -> str:
        text = "".join([str(c) for c in tag.contents if isinstance(c, NavigableString)])
        return text.lower()
