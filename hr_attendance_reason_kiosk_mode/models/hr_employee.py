# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def attendance_action_change(self):
        """ Check In: Add employee attendance reasons
        """
        attendance = super(HrEmployee, self).attendance_action_change()
        if self._context.get('attendance_reasons') and \
                self._context['attendance_reasons']:
            attendance.write({
                'attendance_reason_ids': [
                    (6, 0, self._context['attendance_reasons'])
                ]
            })
        return attendance
