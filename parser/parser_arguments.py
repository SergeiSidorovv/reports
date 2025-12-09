from argparse import ArgumentParser, Namespace


class CLI:
    """
    Class for parsing command line arguments
    """
    def __init__(self):
        self.parser = ArgumentParser(description="Report generatorr")

        self.parser.add_argument(
            "--files",
            required=True,
            nargs="+",
            help="Path to the reports"
        )
        self.parser.add_argument(
            "--report",
            required=True,
            help="Name report"
        )


    def parse(self) -> Namespace:
        """
        Selects the names of the arguments from the received command
        :return: The name of the command and the paths to search for files
        """
        parser_namespace = self.parser.parse_args()
        return parser_namespace
