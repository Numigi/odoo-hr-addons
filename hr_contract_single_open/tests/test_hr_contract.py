# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from odoo.exceptions import ValidationError
from odoo.tests.common import SavepointCase


class TestContract(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env['hr.employee'].create({
            'name': 'E1',
        })

        cls.contract = cls.env['hr.contract'].create({
            'name': '/',
            'employee_id': cls.employee.id,
            'state': 'open',
            'wage': 0,
        })

    def test_if_2_contract__raise_error(self):
        with pytest.raises(ValidationError):
            self.contract.copy({'state': 'open'})

    def test_if_other_contract_not_open__error_not_raised(self):
        self.contract.copy({'state': 'draft'})

    def test_if_contract_not_active__error_not_raised(self):
        self.contract.active = False
        self.contract.copy({'state': 'open', 'active': True})

    def test_if_other_contract_not_active__error_not_raised(self):
        self.contract.copy({'state': 'open', 'active': False})

    def test_if_other_contract_has_different_employee__error_not_raised(self):
        self.contract.copy({
            'state': 'open',
            'employee_id': self.employee.copy().id,
        })
