from abc import ABC, abstractmethod

from webpage_searcher import Result


class Output(ABC):
    @abstractmethod
    def write(self, results: list[Result], item_type: str, item: str) -> None:
        pass
