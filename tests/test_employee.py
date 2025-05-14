import pytest

from src.employees.employee import Employee


def test_create_employee_successful(employee_data: dict, employee: Employee) -> None:
    """Тест успешного создания сотрудника."""
    assert employee.employee_id == employee_data["employee_id"]
    assert employee.email == employee_data["email"]
    assert employee.name == employee_data["name"]
    assert employee.department == employee_data["department"]
    assert employee.hours_worked == employee_data["hours_worked"]
    assert employee.rate == employee_data["rate"]


def test_create_employee_failure(employee_data: dict) -> None:
    """Тест провального создания сотрудника."""
    data_for_creating = employee_data.copy()
    data_for_creating.pop("department")
    with pytest.raises(TypeError) as exc_info:
        Employee(**data_for_creating)
    expected_msg = "Employee.__init__() missing 1 required positional argument: 'department'"
    assert str(exc_info.value) == expected_msg


def test_str_instance(employee: Employee) -> None:
    """Тест строкового представления объекта."""
    expected = employee.name
    result = str(employee)
    assert expected == result
