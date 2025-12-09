from argparse import ArgumentParser, Namespace


def parser_arguments() -> Namespace:
    parser = ArgumentParser(description="Report generator")

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Path to the reports"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Name report"
    )

    parser_namespace = parser.parse_args()
    return parser_namespace
