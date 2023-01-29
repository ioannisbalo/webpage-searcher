from dataclasses import dataclass
from typing import Optional


@dataclass
class Result:
    tag: str
    xpath: str
    string: str
    context: Optional[str] = None
    href: Optional[str] = None
