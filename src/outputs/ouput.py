from abc import ABC, abstractmethod
from typing import List

from src.finders import Result


class Output(ABC):
    @abstractmethod
    def write(self, results: List[Result], item_type: str, item: str):
        pass
