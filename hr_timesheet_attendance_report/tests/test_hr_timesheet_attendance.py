# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests.common import SavepointCase


class TestAccountAnalytic(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env['hr.employee'].create({'name': 'Employee'})
        cls.presence = cls.env["hr.attendance"].create(
            {
                'employee_id': cls.employee.id,
                'check_in': '2023-02-16 08:05:45',
                'check_out': '2023-02-16 12:13:55',
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Customer Task",
                "email": "customer@task.com",
                "customer": True,
            }
        )

        cls.analytic_account = cls.env["account.analytic.account"].create(
            {
                "name": "My Analytic Account",
                "partner_id": cls.partner.id,
                "code": "TEST",
                "active": True,
            }
        )

        cls.analytic_account_2 = cls.env["account.analytic.account"].create(
            {
                "name": "My Analytic Account 2",
                "partner_id": cls.partner.id,
                "code": "TEST2",
                "active": True,
            }
        )

        cls.project = cls.env["project.project"].create(
            {
                "name": "My Project",
                "analytic_account_id": cls.analytic_account.id
            }
        )

        cls.task = cls.env["project.task"].create(
            {
                "name": "My Task",
                "project_id": cls.project.id,
            }
        )

        cls.analytic_line = cls.env["account.analytic.line"].create(
            {
                "name": "My Analytic line",
                "employee_id": cls.employee.id,
                "task_id": cls.task.id,
                "date_time": '2023-02-16 08:10:20',
                "project_id": cls.project.id,
                "account_id": cls.analytic_account.id,
                "unit_amount": 4,
            }
        )

    def test_compute_attendance(self):
        assert self.analytic_line.attendance
        assert self.analytic_line.attendance == \
               'Attendance: 2023-02-16 from 08:05 to 12:13 - 4:08'
