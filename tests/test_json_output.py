from pathlib import Path

from src.output import JSONOutput


def test_json_output_format(json_output: JSONOutput, prepared_data: dict, tmp_path: Path) -> None:
    """Тест создания отчета."""
    filename = "test_report.json"
    filepath = tmp_path / filename
    json_output.format(prepared_data, filename)
    assert filepath.exists() is True
