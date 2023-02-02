from urllib.parse import uses_netloc

schemes = [scheme for scheme in uses_netloc if scheme]

all_tags = {"a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio", "b", "base", "basefont", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", "frameset", "h1", "head", "header", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noframes", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strike", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt", "u", "ul", "var", "video", "wbr"}

text_inline_tags = {"abbr", "acronym", "b", "bdo", "big", "cite", "code", "del", "dfn", "em", "i", "ins", "kbd", "mark", "q", "samp", "small", "span", "strong", "sub", "sup", "tt", "var"}

text_block_tags = {"div", "p", "pre", "dt", "dd", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "title", "legend", "label", "textarea", "option", "fieldset", "button", "blockquote", "object", "caption"}

anchor_tags = {"a"}

text_context_tags = {"p", "pre", "dt", "dd", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6"}
