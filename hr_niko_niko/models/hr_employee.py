# -*- coding: utf-8 -*-
# © 2021 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    time_in = fields.Boolean(
        string="Time in",
        compute='_compute_attendance_time_in'
    )

    def _Float_To_Time(self, Myfloat):
        hour, minute = divmod(Myfloat, 1)
        minute *= 60

        return "%02d:%02d" % (hour, minute)

    @api.depends('last_attendance_id.check_in',
                 'last_attendance_id.check_out',
                 'last_attendance_id'
                 )
    def _compute_attendance_time_in(self):

        for employee in self:
            resource_calendar_id = employee.resource_calendar_id
            att = employee.last_attendance_id.sudo()
            employee.time_in = False

            if att and not att.check_out:
                timezone = self._context.get('tz') or self.env.user.partner_id.tz or 'UTC'
                self_tz = self.with_context(tz=timezone)

                date = fields.Datetime.context_timestamp(
                    self_tz, fields.Datetime.from_string(fields.Datetime.now())
                )

                """
                    compare if the checkout date is between 
                    the configured dates (ResourceCalendar)
                """
                TimeNow = date.strftime("%H:%M")
                ToCompare1 = self._Float_To_Time(resource_calendar_id.start_time)
                ToCompare2 = self._Float_To_Time(resource_calendar_id.end_time)

                if ToCompare1 < TimeNow < ToCompare2:
                    employee.time_in = True
