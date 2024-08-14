# Copyright 2024 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestHrPayslipEmployees(TransactionCase):
    def setUp(self):
        super(TestHrPayslipEmployees, self).setUp()

        self.department1 = self.env['hr.department'].create({'name': 'Department 1'})
        self.department2 = self.env['hr.department'].create({'name': 'Department 2'})

        self.employee1 = self.env['hr.employee'].create(
            {
                'name': 'Employee 1',
                'department_id': self.department1.id,
            }
        )
        self.employee2 = self.env['hr.employee'].create(
            {
                'name': 'Employee 2',
                'department_id': self.department1.id,
            }
        )
        self.employee3 = self.env['hr.employee'].create(
            {
                'name': 'Employee 3',
                'department_id': self.department2.id,
            }
        )
        self.payslip_run = self.env['hr.payslip.run'].create(
            {
                'name': 'Test Payslip Run',
                'date_start': '2023-01-01',
                'date_end': '2023-01-31',
                'department_ids': [(6, 0, [self.department1.id, self.department2.id])],
            }
        )

    def test_default_employees_with_non_empty_payslip_batch_department(self):
        context = {
            'department_ids': [(6, 0, [self.department1.id, self.department2.id])]
        }
        payslip_employees = (
            self.env['hr.payslip.employees'].with_context(context).create({})
        )
        default_employees = payslip_employees.employee_ids.ids
        self.assertIn(
            self.employee1.id,
            default_employees,
            "Employee 1 should be in the default employees",
        )
        self.assertIn(
            self.employee2.id,
            default_employees,
            "Employee 2 should be in the default employees",
        )
        self.assertIn(
            self.employee3.id,
            default_employees,
            "Employee 3 should be in the default employees",
        )

    def test_employee_list_with_empty_payslip_batch_department(self):
        context = {'department_ids': [(6, 0, [])]}
        payslip_employees = (
            self.env['hr.payslip.employees'].with_context(context).create({})
        )
        self.assertEqual(
            payslip_employees.employee_ids.ids,
            [],
            "No employees should be returned when department_ids is empty",
        )
