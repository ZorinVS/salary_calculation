import datetime
from typing import Callable

from src.output import OUTPUT_FORMATTERS


def validate_formatter_type(formatter_type: str) -> None:
    """Валидация типа форматтера."""
    if formatter_type not in OUTPUT_FORMATTERS:
        existing_types = ", ".join(t for t in OUTPUT_FORMATTERS.keys())
        raise ValueError(
            f"'{formatter_type}' is not a supported formatter type. Supported types are: '{existing_types}'."
        )


def create_filename(report_type: str, file_extension: str) -> str:
    """Генерация названия отчета по текущей дате."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'{report_type}_{timestamp}.{file_extension}'


def print_payout_report(report_data: dict) -> None:
    """Печать отчета по зарплатам в консоль."""
    for dept_name, data in report_data.items():
        print(dept_name)  # вывод информации по отделам
        print("-" * 16 + "  " + f"{'name':<20} {'hours':>5} {'rate':>5} {'payout':>8}")
        for emp in data["employees"]:
            # Вывод информации о каждом сотруднике
            print(f"{'':<16}  {emp['name']:<20} {int(emp['hours']):>5} {int(emp['rate']):>5} {int(emp['payout']):>8}")
        # Общий отчет по отделу
        print(f"{'':<16}  {'':<20} {int(data['total_hours']):>5} {'':>5} {int(data['total_payout']):>8}")
        print()


REPORT_PRINTERS: dict[str, Callable[[dict], None]] = {
    "payout": print_payout_report,
}
