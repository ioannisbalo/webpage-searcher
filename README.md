# Webpage Searcher

### Description
A library that search for a phrase or a url in an html document

### Usage
To search for a url:
```
from webpage_searcher import UrlFinder

html = "<html><a href="https://google.com">google</a></html>"
finder = UrlFinder(html)
results = finder.find("google.com")
```

To search for a phrase:
```
from webpage_searcher import PhraseFinder

html = "<html>hello</html>"
finder = PhraseFinder(html)
results = finder.find("hello")
```

### Contributing
To run the tests:
1. Install dev dependencies: `poetry install --all-extras`
2. Run the tests: `pytest -v`
