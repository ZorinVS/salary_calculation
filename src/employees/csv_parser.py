import os
from pathlib import Path
from typing import Iterator


class CSVParser:
    """Класс для парсинга CSV файла с данными о сотрудниках.

    Константы:
        POSSIBLE_RATE_FIELDS (tuple): Возможные названия полей ставки
        SEP (str): Разделитель в CSV
        DATA_DIR (Path): Директория, где по умолчанию хранятся CSV файлы
    """

    POSSIBLE_RATE_FIELDS: tuple = ("rate", "hourly_rate", "salary",)
    SEP: str = ","
    DATA_DIR: Path = Path("data")

    def __init__(self) -> None:
        """Конструктор класса `CSVParser`."""
        self.files_dir = self.DATA_DIR

    def parse(self, filename: str) -> Iterator[dict]:
        """Парсинг CSV файла."""
        file_path = self._make_file_path(filename)
        self._check_filepath(file_path)

        with open(file_path, encoding="utf-8") as file:
            headers = self._get_headers_list(file.readline())
            for line in file:
                yield self._get_employee_dict(line, headers)

    def _get_headers_list(self, headers_line: str) -> list[str]:
        """Получение списка заголовков с нормализацией полей."""
        headers = headers_line.rstrip().split(self.SEP)
        return [self._normalize_header(header) for header in headers]

    def _normalize_header(self, header: str) -> str:
        """Нормализация названий заголовков."""
        if header == "id":
            return "employee_id"
        elif header in self.POSSIBLE_RATE_FIELDS:
            return "rate"
        return header

    def _get_employee_dict(self, values_line: str, headers: list[str]) -> dict:
        """Получение словаря из одной строки данных о сотруднике."""
        values = values_line.rstrip().split(self.SEP)
        return dict(zip(headers, values))

    def _make_file_path(self, filename: str) -> str:
        """Формирование пути к файлу, если передан не путь, а имя файла."""
        if os.path.sep not in filename:
            return str(self.files_dir / filename)
        return filename

    @staticmethod
    def _check_filepath(file_path: str) -> None:
        """Проверка существования файла."""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
