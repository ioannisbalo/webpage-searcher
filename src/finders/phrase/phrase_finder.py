from typing import List, Type

from src.finders.finder import Finder
from src.finders.phrase.handlers import AnchorHandler, ChildHandler, ParentHandler, TagHandler
from src.finders.result import Result


class PhraseFinder(Finder):
    handlers: Type[TagHandler] = [
        ParentHandler,
        ChildHandler,
        AnchorHandler,
    ]

    def find(self, phrase: str) -> List[Result]:
        phrase = self._format_phrase(phrase)
        results = []
        for handler_class in self.handlers:
            for tag_name in handler_class.tags:
                tags = self._soup.find_all(tag_name, recursive=True)
                for tag in tags:
                    text = str(tag.string).lower()
                    if phrase in text:
                        handler = handler_class(tag)
                        results.append(handler.result())
        return results

    def _format_phrase(self, phrase: str) -> str:
        result = phrase.strip()
        if not result:
            raise ValueError("please provide an appropriate phrase, example: Chili Piper")
        return result.lower()
