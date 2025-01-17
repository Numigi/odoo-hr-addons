# Copyright 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class HREmployeeWorkingSpace(models.Model):
    """Add the management of the working space at the attendance."""

    _inherit = "hr.employee"

    def attendance_manual_working_space(
        self, next_action, working_space_id=None, entered_pin=None
    ):
        res = self.attendance_manual(next_action, entered_pin=entered_pin)
        if working_space_id:
            attendance = self.env["hr.attendance"].search(
                [("id", "=", res["action"]["attendance"]["id"])], limit=1
            )
            attendance.working_space_id = int(working_space_id)
        return res
