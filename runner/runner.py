import tabulate

from report.work_reports import ReportFactory
from work_files.work_files import CSVWorker


class ReportRunner:
    """
    Class for generating reports
    """
    def __init__(self, file_paths, report_name):
        self.reader = CSVWorker(file_paths)
        self.report = ReportFactory.create_report(report_name)


    def run(self):
        """
        Starts the report generation.
        """
        headers = self.report.parameters
        rows = self.reader.read_files()
        result = self.report.generate_report(rows)
        self.render(result, headers)


    @staticmethod
    def render(data: list, headers: list):
        """
        Generates a table
        :param data: Data to display in the table
        :param headers: Headings for the table
        """
        print(tabulate.tabulate(data, headers=headers))
