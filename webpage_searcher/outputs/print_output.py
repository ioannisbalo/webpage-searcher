from webpage_searcher import Result
from webpage_searcher.outputs.ouput import Output


class PrintOutput(Output):
    def write(self, results: list[Result], item_type: str, item: str) -> None:
        if not results:
            print(f"No results found for provided {item_type}: {item}")
            return

        print(f"Results for {item_type} {item}:")
        print("-----------------------------------------------")
        for result in results:
            print(f"Tag:        {result.tag}")
            if result.link:
                print(f"Found link: {result.link.href}, nofollow: {result.link.nofollow}")
            print(f"XPath:      {result.xpath}")
            if result.string:
                print(f"Full text:  {result.string}")
            if result.context:
                print(f"In context: {result.context}")
            print("-----------------------------------------------")
