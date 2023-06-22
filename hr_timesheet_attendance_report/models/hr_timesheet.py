# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    attendance = fields.Char("Attendance",
                             compute='_get_attendance',
                             store=True,
                             help="Get attendance check_in, check_out "
                                  "and hours of each timesheet line")

    @api.multi
    @api.depends('date_time', 'employee_id', 'unit_amount',
                 'employee_id.attendance_ids',
                 'employee_id.attendance_ids.check_in',
                 'employee_id.attendance_ids.check_out')
    def _get_attendance(self):
        try:
            with self._cr.savepoint():
                self.env['hr.timesheet.switch']._transient_vacuum(force=True)
            self._cr.commit()
        except Exception as e:
            _logger.warning("Failed to clean transient model "
                            "'hr.timesheet.switch'\n%s", str(e))
        for record in self:
            domain = [
                ('employee_id', '=', record.employee_id.id),
                ('check_out', '!=', False),
                ('check_in', '<=', record.date_time),
                ('check_out', '>=', record.date_time),
            ]
            attendance = self.env['hr.attendance'].search(domain, limit=1)
            if attendance:
                check_in_tz = fields.Datetime.context_timestamp(
                    attendance,
                    fields.Datetime.from_string(attendance.check_in)
                )
                check_out_tz = fields.Datetime.context_timestamp(
                    attendance,
                    fields.Datetime.from_string(attendance.check_out)
                )
                day = check_in_tz.date()
                from_time = check_in_tz.strftime('%H:%M')
                to_time = check_out_tz.strftime('%H:%M')
                duration = _('{}').format(
                    check_out_tz - check_in_tz
                )[0:-3]
                record.attendance = _('Attendance: %s from %s to %s - %s'
                                      % (day, from_time, to_time,
                                         duration))
