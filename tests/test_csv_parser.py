import os

from src.employees.csv_parser import CSVParser


def test_create_csv_parser(csv_parser: CSVParser) -> None:
    """Тест инициализации экземпляра класса `CSVParser`."""
    assert str(csv_parser.files_dir) == "data"


def test_make_filepath_with_name(csv_parser: CSVParser) -> None:
    """Тест метода, создающего путь, при передаче имени файла."""
    filename, files_dir = "Test1.csv", csv_parser.files_dir
    result = csv_parser._make_file_path(filename)
    expected = os.path.join(files_dir, filename)
    assert result == expected


def test_make_filepath_with_path(csv_parser: CSVParser) -> None:
    """Тест метода, создающего путь, при передаче пути."""
    filepath = "/Users/vladislav/Downloads/drive-download-20250513T084446Z-1-001/data1.csv"
    result = csv_parser._make_file_path(filepath)
    assert result == filepath


def test_parse(
        csv_parser: CSVParser, csv_file: str, parsed_data: tuple[dict[str, str], dict[str, str], dict[str, str]]
) -> None:
    """Тест парсинга CSV-файла."""
    result = list(csv_parser.parse(filename=csv_file))
    for res, expected in zip(result, parsed_data):
        assert res, expected
