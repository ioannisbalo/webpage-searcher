import argparse

from src.app import App


def main() -> None:
    parser = argparse.ArgumentParser(description="A command line tool that finds a url or a phrase in a website's html")

    parser.add_argument("-w", "--webpage", type=str, help="Url of the website to be searched", required=True)
    parser.add_argument("-u", "--url", type=str, help="Url to be searched for in the website's links")
    parser.add_argument("-p", "--phrase", type=str, help="Phrase to be searched for in the website's text")

    args = parser.parse_args()

    if not args.url and not args.phrase:
        raise ValueError("Please provide either a url or a phrase to be searched for")

    app = App(args.webpage)

    if args.url:
        app.find_url(args.url)
    if args.phrase:
        app.find_phrase(args.phrase)

if __name__ == "__main__":
    main()