# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from odoo.exceptions import ValidationError
from odoo.tests import common
from ddt import ddt, data


@ddt
class TestHrExpenseSheet(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expense_pool = cls.env["hr.expense"]
        cls.sheet_pool = cls.env["hr.expense.sheet"]
        cls.employee = cls.env.ref("hr.employee_admin")
        cls.expense = cls.env.ref("hr_expense.travel_by_air_expense").copy()

    @data(
        ("2020-01-01",),
        ("2020-01-01", "2020-01-25"),
        ("2020-02-01", "2020-02-25"),
    )
    def test_create_successPaths(self, dates):
        expenses = self._create_expenses_from_date(dates)

        sheet = self.sheet_pool.create({
            "name": "tsheet",
            "employee_id": self.employee.id,
            "expense_line_ids": [(6, False, expenses)]
        })
        assert sheet

    @data(("2020-01-01", "2020-02-01"))
    def test_create_faillingPaths(self, dates):
        expenses = self._create_expenses_from_date(dates)

        with pytest.raises(ValidationError):
            self.sheet_pool.create({
                "name": "tsheet",
                "employee_id": self.employee.id,
                "expense_line_ids": [(6, False, expenses)]
            })

    @data(
        ("2020-01-01",),
        ("2020-01-01", "2020-01-25"),
        ("2020-02-01", "2020-02-25"),
    )
    def test_write_successPaths(self, dates):
        expenses = self._create_expenses_from_date(dates)
        sheet = self.sheet_pool.create({
            "name": "tsheet",
            "employee_id": self.employee.id,
        })
        sheet.write({"expense_line_ids": [(6, False, expenses)]})
        assert sheet

    @data(("2020-01-01", "2020-02-01"))
    def test_write_faillingPaths(self, dates):
        expenses = self._create_expenses_from_date(dates)
        sheet = self.sheet_pool.create({
            "name": "tsheet",
            "employee_id": self.employee.id,
        })

        with pytest.raises(ValidationError):
            sheet.write({"expense_line_ids": [(6, False, expenses)]})

    def _create_expenses_from_date(self, dates):
        expenses = []
        for date in dates:
            expense = self.expense.copy()
            expense.date = date
            expenses.append(expense.id)
        return expenses
