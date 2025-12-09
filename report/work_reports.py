from report.models_report import PerformanceReport


def get_report(name_report: str) -> dict:
    reports = {
        "performance": PerformanceReport(),
    }

    if name_report not in reports:
        raise ValueError(f"Unknown report: {name_report}")

    return reports[name_report]
