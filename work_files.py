import csv
import logging


def read_files(file_paths: list) -> list:
    rows = []

    for path in file_paths:
        try:
            with open(path, encoding="utf-8") as f:
                reader_files = csv.DictReader(f)
                for row in reader_files:
                    rows.append(row)
        except FileNotFoundError:
            logging.info(f"{path} is not found")
        except Exception as e:
            logging.info(f"{path} is not read. Exception: {e}")

    return rows