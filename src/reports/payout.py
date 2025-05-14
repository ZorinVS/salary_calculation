from typing import Iterable

from src.employees.employee import Employee
from src.reports.base import Report


class PayoutReport(Report):
    """Класс для генерации отчета по заработной плате сотрудников, сгруппированный по отделам."""

    def _prepare_data(self, employees: Iterable[Employee]) -> dict:
        """Подготовка данных для генерации отчета по ЗП"""
        departments = {}
        for employee in employees:
            dept = employee.department
            payout = employee.hours_worked * employee.rate
            if dept not in departments:
                departments[dept] = {
                    "total_hours": 0.0,
                    "total_payout": 0.0,
                    "employees": []
                }
            departments[dept]["total_hours"] += employee.hours_worked
            departments[dept]["total_payout"] += payout
            departments[dept]["employees"].append({
                "name": employee.name,
                "hours": employee.hours_worked,
                "rate": employee.rate,
                "payout": payout
            })
        return departments
