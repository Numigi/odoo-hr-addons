# © 2021 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResourceCalendar(models.Model):

    _inherit = "resource.calendar"

    hours_per_week = fields.Float(compute="_compute_hours_per_week")

    @api.depends(
        "attendance_ids.hour_from",
        "attendance_ids.hour_to",
    )
    def _compute_hours_per_week(self):
        for calendar in self:
            calendar.hours_per_week = calendar._get_hours_per_week()

    def _get_hours_per_week(self):
        return sum(l.hour_to - l.hour_from for l in self.attendance_ids)
