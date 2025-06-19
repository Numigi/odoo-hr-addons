# Copyright 2024 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.tests.common import TransactionCase


class TestHrPayslipRunDepartmentFilter(TransactionCase):

    def setUp(self):
        super(TestHrPayslipRunDepartmentFilter, self).setUp()
        self.company = self.env['res.company'].search([], limit=1)

        self.department1 = self.env['hr.department'].create({'name': 'Dept A'})
        self.department2 = self.env['hr.department'].create({'name': 'Dept B'})

        self.employee1 = self.env['hr.employee'].create({
            'name': 'Employee A',
            'department_id': self.department1.id,
            'company_id': self.company.id,
        })
        self.employee2 = self.env['hr.employee'].create({
            'name': 'Employee B',
            'department_id': self.department2.id,
            'company_id': self.company.id,
        })

        self.super_result = {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.payslip.employees',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_employee_ids': [(6, 0, [self.employee1.id, self.employee2.id])],
            }
        }

    def test_department_filter_applied(self):
        payslip_run = self.env['hr.payslip.run'].create({
            'name': 'Run',
            'date_start': '2024-01-01',
            'date_end': '2024-01-31',
            'company_id': self.company.id,
            'schedule_pay': 'monthly',
            'department_ids': [(6, 0, [self.department1.id])],
        })

        res = self.super_result.copy()

        if payslip_run.department_ids:
            employee_ids = self.env['hr.employee'].browse(
                res['context']['default_employee_ids'][0][2]
            )
            employee_filtered_ids = employee_ids.filtered(
                lambda e: e.department_id in payslip_run.department_ids
            ).ids
            res['context']['default_employee_ids'] = [(6, 0, employee_filtered_ids)]

        self.assertEqual(
            res['context']['default_employee_ids'][0][2],
            [self.employee1.id]
        )
