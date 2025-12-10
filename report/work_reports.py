from report.models_report import PerformanceReport


class ReportFactory:
    """
    Factory for creating reports
    """

    reports = {
        "performance": PerformanceReport(),
    }

    @classmethod
    def create_report(cls, report_name: str) -> object:
        """
        Creates a report
        :param name_report: The name of the report
        :return: The report object
        """
        if report_name not in cls.reports:
            raise ValueError(f"Unknown report: {report_name}")
        return cls.reports[report_name]
