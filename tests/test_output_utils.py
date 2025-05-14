import datetime

import pytest

from src.output import utils


def test_validate_formatter_type_successful() -> None:
    """Тест успешной валидации типа форматера."""
    utils.validate_formatter_type("json")


def test_validate_formatter_type_failure() -> None:
    """Тест провальной валидации типа форматера."""
    with pytest.raises(ValueError) as exc_info:
        utils.validate_formatter_type("txt")
    expected_msg = "'txt' is not a supported formatter type. Supported types are: 'json'."
    assert str(exc_info.value) == expected_msg


def test_create_filename() -> None:
    """Тест создания имени файла."""
    report_type, file_extension = "payout", "json"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    expected = f"{report_type}_{timestamp}.{file_extension}"
    result = utils.create_filename(report_type, file_extension)
    assert result == expected
