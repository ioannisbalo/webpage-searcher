from typing import List

from src.outputs.ouput import Output
from src.finders import Result


class PrintOutput(Output):
    def write(self, results: List[Result], item_type: str, item: str) -> None:
        if not results:
            print(f"No results found for provided {item_type}: {item}")
            return

        print(f"Results for {item_type} {item}:")
        print("-----------------------------------------------")
        for result in results:
            print(f"Tag:        {result.tag}")
            if result.href:
                print(f"Found link: {result.href}")
            print(f"XPath:      {result.xpath}")
            if result.string:
                print(f"Full text:  {result.string}")
            if result.context:
                print(f"In context: {result.context}")
            print("-----------------------------------------------")
