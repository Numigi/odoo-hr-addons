# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from odoo.exceptions import ValidationError
from odoo.tests.common import SavepointCase


class TestContract(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env["hr.employee"].create(
            {
                "name": "E1",
            }
        )

        cls.calendar = cls.env.ref("resource.resource_calendar_std")
        cls.contract = cls.env["hr.contract"].create(
            {
                "name": "/",
                "employee_id": cls.employee.id,
                "wage": 0,
                "resource_calendar_id": cls.calendar.id,
            }
        )

    def test_hourly_equivalent_wage(self):
        self.contract.wage_type = "hour"
        self.contract.wage = 10
        assert self.contract.equivalent_wage == 20800  # 10 * 40 * 52
        assert self.contract.equivalent_wage_type == "year"

    def test_yearly_equivalent_wage(self):
        self.contract.wage_type = "year"
        self.contract.wage = 20800
        assert self.contract.equivalent_wage == 10  # 20800 / (40 * 52)
        assert self.contract.equivalent_wage_type == "hour"

    def test_monthly_equivalent_wage(self):
        self.contract.wage_type = "month"
        self.contract.wage = 1800
        assert round(self.contract.equivalent_wage, 2) == 10.38  # 1800 * 12 / (40 * 52)
        assert self.contract.equivalent_wage_type == "hour"
