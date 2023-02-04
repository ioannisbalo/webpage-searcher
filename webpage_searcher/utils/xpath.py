from bs4 import Tag


def element_xpath(element: Tag) -> str:
    components = []
    try:
        current = element if element.name else element.parent
        for parent in element.parents:
            if isinstance(current, Tag):
                siblings = parent.find_all(current.name, recursive=False)
                if len(siblings) == 1:
                    components.append(current.name)
                else:
                    position = next(i for i, s in enumerate(siblings, 1) if s is current)
                    components.append(f"{current.name}[{position}]")
            else:
                return _build_xpath(components)
            current = parent
        return _build_xpath(components)
    except Exception:
        return "unable to calculate xpath"


def _build_xpath(components: list[str]) -> str:
    components.reverse()
    path = "/".join(components)
    return f"/{path}"
