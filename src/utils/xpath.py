from bs4 import Tag


def element_xpath(element: Tag) -> str:
    components = []
    try:
        current = element if element.name else element.parent
        for parent in element.parents:
            siblings = parent.find_all(current.name, recursive=False)
            if len(siblings) == 1:
                components.append(current.name)
            else:
                position = next(i for i, s in enumerate(siblings, 1) if s is current)
                components.append(f"{current.name}[{position}]")
            current = parent
        components.reverse()
        path = "/".join(components)
        return f"/{path}"
    except Exception:
        return "unable to calculate xpath"
