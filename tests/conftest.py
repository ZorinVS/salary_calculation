import pytest

from src.employees.csv_parser import CSVParser
from src.employees.employee import Employee


@pytest.fixture
def employee_data() -> dict:
    """Фикстура, содержащая данные для создания одного пользователя."""
    return {
        "employee_id": 1,
        "email": "test1@test.test",
        "name": "Test Test",
        "department": "department1",
        "hours_worked": 150,
        "rate": 60,
    }


@pytest.fixture
def employee(employee_data) -> Employee:
    """Фикстура, содержащая экземпляр класса `Employee`."""
    return Employee(**employee_data)


@pytest.fixture
def csv_parser() -> CSVParser:
    """Фикстура, содержащая экземпляр класса `CSVParser`."""
    return CSVParser()


@pytest.fixture
def csv_data() -> str:
    """Фикстура, содержащая данные CSV-файла."""
    return """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60"""


@pytest.fixture
def parsed_data() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Фикстура, содержащая спарсенные данные."""
    return (
        {
            "employee_id": "1", "email": "alice@example.com", "name": "Alice Johnson",
            "department": "Marketing", "hours_worked": "160", "rate": "50",
        },
        {
            "employee_id": "2", "email": "bob@example.com", "name": "Bob Smith",
            "department": "Design", "hours_worked": "150", 'rate': "40",
        },
        {
            "employee_id": "3", "email": "carol@example.com", "name": "Carol Williams",
            "department": "Design", "hours_worked": "170", "rate": "60",
        },
    )


@pytest.fixture
def csv_file(csv_data, tmp_path) -> str:
    """Фикстура, ссоздающая CSV-файл."""
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_data, encoding="utf-8")
    return str(file_path)
