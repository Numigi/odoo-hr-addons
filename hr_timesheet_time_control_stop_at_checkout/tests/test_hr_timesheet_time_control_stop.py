# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common
from datetime import timedelta, datetime


class TestHrTimesheetTimeControlStop(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.employee = self.env["hr.employee"].create({
            "name": "Somebody else",
            "pin": 12345,
            "user_id": 2,
        })
        self.attendance = self.env["hr.attendance"].create({
            "employee_id": self.employee.id,
            "check_in":  datetime.now() - timedelta(hours=2),
        })
        self.project = self.env['project.project'].create({
            'name': 'Test project',
            "allow_timesheets": True,
        })
        self.analytic_account = self.project.analytic_account_id
        self.task = self.env['project.task'].create({
            'name': 'Test task',
            'project_id': self.project.id,
        })
        self.line = self.env['account.analytic.line'].create({
            'date_time': datetime.now() - timedelta(hours=1),
            'task_id': self.task.id,
            'project_id': self.project.id,
            'account_id': self.analytic_account.id,
            'name': 'Test line',
            'employee_id': self.employee.id,
        })

    def test_stop_timer_at_checkout(self):
        """At checkout test if the timer is stopped"""
        self.assertEqual(self.employee.attendance_state, 'checked_in')
        self.employee.attendance_action_change()
        self.assertNotEqual(self.line.unit_amount, 0.0)
