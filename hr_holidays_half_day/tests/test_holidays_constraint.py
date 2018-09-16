# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from datetime import datetime
from ddt import data, ddt
from odoo.exceptions import ValidationError
from odoo.tests import common


@ddt
class TestHolidaysConstraint(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env['hr.employee'].create({
            'name': 'Test',
        })

    def _create_leave(self, number_of_days):
        return self.env['hr.holidays'].create({
            'name': '/',
            'employee_id': self.employee.id,
            'number_of_days_temp': number_of_days,
            'holiday_status_id': self.env.ref('hr_holidays.holiday_status_sl').id,
            'date_from': datetime.now(),
            'date_to': datetime.now(),
            'type': 'remove',
        })

    @data(0.1, 0.2, 0.01, 0.05, 1.1, 1.05)
    def test_ifInvalidNumberOfDays_thenRaiseConstraint(self, number_of_days):
        with pytest.raises(ValidationError):
            self._create_leave(number_of_days)

    @data(0, 0.5, 1, 1.5)
    def test_ifValidNumberOfDays_thenConstraintNotRaised(self, number_of_days):
        self._create_leave(number_of_days)
