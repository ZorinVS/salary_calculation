from src.reports import REPORTS


def validate_report_type(report_type: str) -> None:
    """Валидация типа отчета."""
    if report_type not in REPORTS:
        existing_types = ", ".join(t for t in REPORTS.keys())
        raise ValueError(f"'{report_type}' is not a supported report type. Supported types are: '{existing_types}'.")
