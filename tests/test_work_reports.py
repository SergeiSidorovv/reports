import pytest

from report.work_reports import ReportFactory
from report.models_report import PerformanceReport


class TestReportFactory:
    def setup_class(self):
        report_factory = ReportFactory()
        self.report_factory = report_factory

    def test_parameters(self, paremeters_report_factory):
        type_self_parameters = isinstance(
            self.report_factory.reports["performance"], PerformanceReport
        )
        type_paremeters_report_factory = isinstance(
            paremeters_report_factory["performance"], PerformanceReport
        )
        assert self.report_factory.reports.keys() == paremeters_report_factory.keys()
        assert type_self_parameters == type_paremeters_report_factory

    def test_create_report(self):
        assert isinstance(
            self.report_factory.create_report("performance"), PerformanceReport
        )

    def test_create_report_without_report_name(self):
        with pytest.raises(ValueError) as exc_info:
            self.report_factory.create_report("")
        assert "Unknown report: " == str(exc_info.value)
