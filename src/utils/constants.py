from urllib.parse import uses_netloc

schemes = [scheme for scheme in uses_netloc if scheme]

as_child_tags = ["tt", "i", "b", "q", "ins", "del", "big", "small", "em", "strong", "dfn", "code", "samp", "kbd", "var", "cite", "abbr", "acronym", "sub", "sup", "span", "bdo", "address"]

as_parent_tags = ["div", "p", "pre", "dt", "dd", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "title", "legend", "label", "textarea", "option", "fieldset", "button", "blockquote", "object", "caption"]

anchor_tags = ["a"]

text_context_tags = ["p", "pre", "dt", "dd", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6"]
