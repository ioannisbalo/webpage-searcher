from typing import List

from src.outputs.ouput import Output
from src.finders import Result


class PrintOutput(Output):
    def write(self, results: List[Result]) -> None:
        if not results:
            print("No results found for provided input")
            return

        print("Results:")
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
