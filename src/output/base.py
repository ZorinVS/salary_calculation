from abc import ABC, abstractmethod
from pathlib import Path


class OutputFormatter(ABC):
    """Базовый класс для форматов вывода отчета."""

    FILE_EXTENSION: str
    REPORTS_DIR: Path = Path("reports")

    @abstractmethod
    def format(self, data: dict, filename: str) -> str:
        """Сохраняет данные в файл."""
        pass
