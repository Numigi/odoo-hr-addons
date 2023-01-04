# © 2022 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api, exceptions, _, SUPERUSER_ID
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def stop_running_timer(self, employee, stop_dt):
        employee = employee or self.env.user.employee_ids
        # Find running work
        running = self.env["account.analytic.line"].search([
            ("date_time", "!=", False),
            ("employee_id", "in", employee.ids),
            ("id", "not in", self.env.context.get("resuming_lines", [])),
            ("project_id", "!=", False),
            ("unit_amount", "=", 0),
        ])
        for running_timer in running:
            running_timer.with_context(stop_dt=stop_dt).button_end_work()

    @api.multi
    def attendance_action_change(self):
        """Override methode to Stop task running timer after checkout
        """
        attendance = super(HrEmployee, self).attendance_action_change()
        if attendance.check_out:
            self.stop_running_timer(attendance.employee_id,
                                    attendance.check_out)
        return attendance
