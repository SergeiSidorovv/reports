import csv
import logging
import pytest
from unittest.mock import mock_open, patch
from work_files.work_files import CSVWorker


class TestCSVWorker:
    def test_csvworker_read_files_mock(self):

        csv_content = "name,age\nAlice,30\nBob,25\n"

        m = mock_open(read_data=csv_content)

        with patch("builtins.open", m):
            worker = CSVWorker(["dummy.csv"])
            rows = worker.read_files()

        assert rows == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]

    def test_csvworker_file_not_found(self, caplog):
        with caplog.at_level(logging.INFO):
            worker = CSVWorker(["nonexistent.csv"])
            rows = worker.read_files()

        assert rows == []
        assert "nonexistent.csv is not found" in caplog.text

    def test_csvworker_general_exception(self, caplog):
        with caplog.at_level(logging.INFO):
            m = mock_open()
            m.side_effect = ValueError("bad file")

            with patch("builtins.open", m):
                worker = CSVWorker(["dummy.csv"])
                rows = worker.read_files()

        assert rows == []
        assert "dummy.csv is not read. Exception: bad file" in caplog.text
