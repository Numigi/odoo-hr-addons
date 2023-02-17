# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import api, fields, models, _


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    attendance = fields.Char("Attendance",
                             compute='_get_attendance',
                             store=True,
                             help="Get attendance check_in, check_out "
                                  "and hours of each timesheet line")

    @api.multi
    @api.depends('date_time', 'employee_id', 'unit_amount')
    def _get_attendance(self):
        for record in self:
            domain = [
                ('employee_id', '=', record.employee_id.id),
                ('check_out', '!=', False),
                ('check_in', '<=', record.date_time),
                ('check_out', '>=', record.date_time),
            ]
            attendance = self.env['hr.attendance'].search(domain, limit=1)
            if attendance:
                day = attendance.check_in.date()
                from_time = attendance.check_in.strftime('%H:%M')
                to_time = attendance.check_out.strftime('%H:%M')
                duration = _('{}').format(
                    attendance.check_out - attendance.check_in
                )[0:-3]
                record.attendance = _('Attendance: %s from %s to %s - %s'
                                      % (day, from_time, to_time,
                                         duration))
