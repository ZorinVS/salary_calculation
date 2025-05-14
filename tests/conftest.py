import pytest

from src.employees.employee import Employee


@pytest.fixture
def employee_data():
    """Фикстура, содержащая данные для создания одного пользователя"""
    return {
        "employee_id": 1,
        "email": "test1@test.test",
        "name": "Test Test",
        "department": "department1",
        "hours_worked": 150,
        "rate": 60,
    }


@pytest.fixture
def employee(employee_data):
    return Employee(**employee_data)
