import pytest

from src.reports.utils import validate_report_type


def test_validate_report_type_successful() -> None:
    """Тест успешной валидации типа отчета."""
    validate_report_type("payout")


def test_validate_report_type_failure() -> None:
    """Тест провальной валидации типа отчета."""
    with pytest.raises(ValueError) as exc_info:
        validate_report_type("average_rate")
    expected_msg = "'average_rate' is not a supported report type. Supported types are: 'payout'."
    assert str(exc_info.value) == expected_msg
