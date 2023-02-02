from dataclasses import dataclass
from typing import Optional


@dataclass
class Link:
    href: Optional[str] = None
    nofollow: bool = False

@dataclass
class Result:
    tag: str
    xpath: str
    string: str
    link: Optional[Link] = None
    context: Optional[str] = None
