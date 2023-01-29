# Webpage Searcher

### Description
A command line application that searches a webpage for a link or a phrase provided.

### Usage
To use the cli:
1. Clone the repository and navigate inside the root folder: `git clone ` and `cd webpage-searcher`
2. Make sure you have python3 (version 3.7+ preferrably) installed in your system: `python3 -V`
3. You can optionally create a virtual environment:
    * `python3 -m venv ./venv`
    * `source ./venv/bin/activate`
4. Install the package manager (Poetry): `pip install -U pip setuptools` and `pip install poetry`
5. Install the dependencies: `poetry install`
6. You can now use the cli: `python main.py -w https://example.com -u example.com -p "Example phrase"`

### Contributing
To run the tests:
1. Install dev dependencies: `poetry install --all-extras`
2. Run the tests: `pytest -v`
