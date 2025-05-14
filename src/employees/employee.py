class Employee:
    """Класс для хранения данных о сотруднике."""

    __slots__ = ("employee_id", "email", "name", "department", "hours_worked", "rate")

    def __init__(self, employee_id: str, email: str, name: str, department: str, hours_worked: str, rate: str) -> None:
        """Конструктор класса `Employee`"""
        self.employee_id = int(employee_id)
        self.email = email
        self.name = name
        self.department = department
        self.hours_worked = float(hours_worked)
        self.rate = float(rate)

    def __str__(self):
        """Строковое представление сотрудника."""
        return self.name
