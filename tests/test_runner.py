import tabulate

from runner.runner import ReportRunner
from report.models_report import PerformanceReport
from work_files.work_files import CSVWorker


class TestReportRunner:

    def test_attributes(self, file_paths, report_name):
        runner = ReportRunner(file_paths, report_name)
        assert isinstance(runner.reader, CSVWorker)
        assert isinstance(runner.report, PerformanceReport)

    def test_run(self, monkeypatch):
        monkeypatch.setattr(tabulate, "tabulate", lambda data, headers: "TABLE_OUTPUT")

        printed = []

        monkeypatch.setattr("builtins.print", lambda msg: printed.append(msg))

        ReportRunner.render(data=[["a", 1], ["b", 2]], headers=["name", "value"])

        assert printed == ["TABLE_OUTPUT"]
