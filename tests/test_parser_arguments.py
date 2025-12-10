import sys
from argparse import Namespace
from typing import ByteString
from parser.parser_arguments import CLI


class TestCLI:
    def setup_class(self):
        cli = CLI()
        self.cli = cli

    def test_cli_parse(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["prog", "--files", "a.txt", "b.txt", "--report", "monthly"]
        )
        arguments = self.cli.parse()
        assert arguments.files == [
            "a.txt",
            "b.txt",
        ]
        assert arguments.report == "monthly"

    
