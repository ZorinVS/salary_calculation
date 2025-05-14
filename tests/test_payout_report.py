import datetime
from pathlib import Path

from src.employees.employee import Employee
from src.reports import PayoutReport


def test_report_generate(payout_report: PayoutReport, employee: Employee, tmp_path: Path) -> None:
    """Тест генерации Json-отчета."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{payout_report.REPORT_TYPE}_{timestamp}.{payout_report.formatter.FILE_EXTENSION}"
    filepath = tmp_path / filename
    payout_report.generate([employee])
    filepath.exists()
