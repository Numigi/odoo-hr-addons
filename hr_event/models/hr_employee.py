# © 2022 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Employee(models.Model):

    _inherit = "hr.employee"

    event_count = fields.Integer("Number of Events", compute='_compute_event_count')

    def _compute_event_count(self):
        for employee in self:
            employee.event_count = self.env['hr.event'].search(
                [('employee_id', '=', employee.id)], count=True)
