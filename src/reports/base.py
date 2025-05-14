from abc import ABC, abstractmethod
from typing import Iterable

from src.employees.employee import Employee
from src.output.base import OutputFormatter
from src.output.utils import REPORT_PRINTERS, create_filename


class Report(ABC):
    """Базовый класс для генерации отчетов."""

    REPORT_TYPE: str

    def __init__(self, formatter: OutputFormatter):
        self.formatter = formatter

    @abstractmethod
    def _prepare_data(self, employees: Iterable[Employee]) -> dict:
        """Абстрактный класс для подготовки данных."""
        pass

    def generate(self, employees: Iterable[Employee], do_print: bool = False) -> None:
        """Метод генерации отчета."""
        report_data = self._prepare_data(employees)
        filename = create_filename(report_type=self.REPORT_TYPE, file_extension=self.formatter.FILE_EXTENSION)
        self.formatter.format(report_data, filename)

        if do_print:
            REPORT_PRINTERS[self.REPORT_TYPE](report_data)
