import argparse

from src.employees.csv_parser import CSVParser
from src.employees.employee import Employee
from src.output import OUTPUT_FORMATTERS
from src.output.utils import validate_formatter_type
from src.reports import REPORTS
from src.reports.utils import validate_report_type


def main():
    # Парсер параметров в консоли
    parser = argparse.ArgumentParser(description="CSV to JSON report converter")
    parser.add_argument("files", nargs="+", help="List of CSV files to process")
    parser.add_argument("--report", required=True, help="Report type (e.g., payout)")
    parser.add_argument("--formatter", default="json", help="Report formatter (e.g., payout)")

    csv_parser = CSVParser()  # парсер CSV-файлов

    try:
        args = parser.parse_args()
        validate_report_type(args.report)
        validate_formatter_type(args.formatter)
    except ValueError as e:
        print(f"Validation error: {e}")
    else:
        formatter = OUTPUT_FORMATTERS[args.formatter]()  # форматер отчета
        report = REPORTS[args.report](formatter)         # генератор отчета
        employees = (                                    # парсинг данных сотрудников
            Employee(**data)
            for file in args.files
            for data in csv_parser.parse(file)
        )
        report.generate(employees, do_print=True)


if __name__ == '__main__':
    main()
