import csv
import logging


class CSVWorker:
    """
    A class for working with CSV files
    """

    def __init__(self, file_paths: list):
        self.file_paths = file_paths

    def read_files(self) -> list:
        """
        Read csv files and return rows
        :return: list of rows with data
        """
        rows = []

        for path in self.file_paths:
            try:
                with open(path, encoding="utf-8") as f:
                    reader_files = csv.DictReader(f)
                    for row in reader_files:
                        rows.append(row)
            except FileNotFoundError:
                logging.info(f"{path} is not found")
            except Exception as exc:
                logging.info(f"{path} is not read. Exception: {exc}")

        return rows
