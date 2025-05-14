import json

from src.output.base import OutputFormatter


class JSONOutput(OutputFormatter):
    """Сохраняет отчет в формате JSON."""

    FILE_EXTENSION: str = "json"

    def format(self, data: dict, filename: str) -> None:
        """Сохраняет данные в Json файл."""
        file_path = self.REPORTS_DIR / filename
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
