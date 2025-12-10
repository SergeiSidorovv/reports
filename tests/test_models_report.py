from report.models_report import PerformanceReport


class TestPerformanceReport:

    def setup_class(self):
        perfomance_report = PerformanceReport()
        self.perfomance_report = perfomance_report

    def test_parameters(self, paremeters_performance_report):
        assert self.perfomance_report.parameters == paremeters_performance_report

    def test_generate_report(self, employess2_data, rows_employess2):
        assert (
            self.perfomance_report.generate_report(rows_employess2) == employess2_data
        )

    def test_generate_report_without_data(self):
        rows = []
        assert self.perfomance_report.generate_report(rows) == rows
