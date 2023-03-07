# © 2023 - Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, _


class HrTimesheetDailyTime(models.TransientModel):
    _name = "hr.timesheet.daily.time"
    _description = "Daily Time"

    employee_id = fields.Many2one('hr.employee', 'Employee', required=1)
    date = fields.Datetime('Date')

    def generate_report(self):
        self.ensure_one()
        if self.employee_id:
            action = self.env.ref('hr_timesheet_attendance_report.'
                                  'timesheet_attendance_report_action'
                                  ).read()[0]
            # We pass `Employee` and `Date` in the domain so that view
            # will be filtered
            domain = [
                ('employee_id', '=', self.employee_id.id),
            ]
            if self.date:
                date_from = self.date.replace(
                    hour=0, minute=0, second=0)
                date_to = self.date.replace(
                    hour=23, minute=59, second=59)
                domain += [('date_time', '>=', date_from),
                           ('date_time', '<=', date_to)]
            action['domain'] = domain
            return action
