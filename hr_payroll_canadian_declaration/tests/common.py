# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import datetime, timedelta
from odoo.tests.common import SavepointCase


class PayrollPreparationToPayslipCase(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env["hr.employee"].create(
            {
                "name": "John Doe",

            }
        )
        cls.date_start = datetime.now().date()
        cls.date_end = cls.date_start + timedelta(30)
        cls.structure = cls.env['hr.payroll.structure'].create({
                'name': 'Salary Structure A',
                'code': 'SD',
                'rule_ids': [(6, 0, [
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_houserentallowance1').id,
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_convanceallowance1').id,
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_professionaltax1').id,
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_providentfund1').id,
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_meal_voucher').id,
                    cls.env.ref(
                        'hr_payroll.hr_salary_rule_sales_commission').id
                ])],
        })
        cls.contract = cls.env["hr.contract"].create(
            {
                "name": "Test",
                "employee_id": cls.employee.id,
                "date_start": cls.date_start,
                "wage": 50000,
                "state": "open",
                "struct_id": cls.structure.id,
            }
        )
